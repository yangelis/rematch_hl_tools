import xtrack as xt
import xtrack._temp.lhc_match as lm


def clean_expr2(expr):
    return (
        expr.replace("vars['", "")
        .replace("f.", "")
        .replace("']", "")
        .replace("None", "0")
    )


def clean_expr(expr):
    a = str(expr)
    return (
        a.replace("vars['", "").replace("f.", "").replace("']", "").replace("None", "0")
    )


def get_presqueeze(collider, line_name):
    bim = line_name[-2:]
    tw81_45_xt = lm.get_arc_periodic_solution(collider, arc_name=["81", "45"])

    beta0 = tw81_45_xt[line_name]["45"].get_twiss_init(f"s.ds.l5.{bim}")
    beta0.mux = 0
    beta0.muy = 0
    tw_ip5_pre = collider[line_name].twiss(
        start="s.ds.l5.b1", end=f"e.ds.r5.{bim}", init=beta0
    )

    beta0 = tw81_45_xt[line_name]["81"].get_twiss_init(f"s.ds.l1.{bim}")
    beta0.mux = 0
    beta0.muy = 0
    tw_ip1_pre = collider[line_name].twiss(
        start=f"s.ds.l1.{bim}", end=f"e.ds.r1.{bim}", init=beta0
    )

    res = {"ir1": tw_ip1_pre, "ir5": tw_ip5_pre}
    return res


def get_cellphases(collider):
    tw_arcs = lm.get_arc_periodic_solution(collider, arc_name=lm.ARC_NAMES)

    cell_phases = {}
    cell_phases.update(
        {"12": {}, "23": {}, "34": {}, "45": {}, "56": {}, "67": {}, "78": {}, "81": {}}
    )

    for arc_name in lm.ARC_NAMES:
        for bim in ["b1", "b2"]:
            for plane in ["x", "y"]:
                mu1 = tw_arcs[f"lhc{bim}"][arc_name][
                    f"mu{plane}", f"e.cell.{arc_name}.{bim}"
                ]
                mu2 = tw_arcs[f"lhc{bim}"][arc_name][
                    f"mu{plane}", f"s.cell.{arc_name}.{bim}"
                ]
                cell_phases[arc_name][f"mu{plane}cell{arc_name}{bim}"] = mu1 - mu2

    return cell_phases


def get_arcphase(collider):
    tw_arcs = lm.get_arc_periodic_solution(collider, arc_name=lm.ARC_NAMES)

    arc_phases = {}
    arc_phases.update(
        {"12": {}, "23": {}, "34": {}, "45": {}, "56": {}, "67": {}, "78": {}, "81": {}}
    )

    for arc_name in lm.ARC_NAMES:
        for bim in ["b1", "b2"]:
            for plane in ["x", "y"]:
                mu1 = tw_arcs[f"lhc{bim}"][arc_name][
                    f"mu{plane}", f"s.ds.l{arc_name[1]}.{bim}"
                ]
                mu2 = tw_arcs[f"lhc{bim}"][arc_name][
                    f"mu{plane}", f"e.ds.r{arc_name[0]}.{bim}"
                ]
                arc_phases[arc_name][f"mu{plane}{arc_name}{bim}"] = mu1 - mu2

    return arc_phases


def get_ip_params_to_save_(collider, tw_arcs_):
    ip_params = {}
    ip_params.update(
        {"1": {}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {}, "7": {}, "8": {}}
    )
    for arc in lm.ARC_NAMES:
        for bim in ["b1", "b2"]:
            tw_arcs = lm.get_arc_periodic_solution(collider, f"lhc{bim}", arc)
            beta0 = tw_arcs.get_twiss_init(f"s.ds.l{arc[1]}.{bim}")
            beta0.mux = 0
            beta0.muy = 0

            tw_pre = None
            if arc == "81":
                tw_pre = (
                    collider[f"lhc{bim}"]
                    .cycle("ip3")
                    .twiss(
                        start=f"s.ds.l{arc[1]}.{bim}",
                        end=f"e.ds.r{arc[1]}.{bim}",
                        init=beta0,
                        method="4d",
                        reverse={"b1": False, "b2": True}[bim],
                    )
                )
            else:
                tw_pre = collider[f"lhc{bim}"].twiss(
                    start=f"s.ds.l{arc[1]}.{bim}",
                    end=f"e.ds.r{arc[1]}.{bim}",
                    init=beta0,
                )

            mux = (
                tw_pre["mux", f"e.ds.r{arc[1]}.{bim}"]
                - tw_pre["mux", f"s.ds.l{arc[1]}.{bim}"]
            )
            muy = (
                tw_pre["muy", f"e.ds.r{arc[1]}.{bim}"]
                - tw_pre["muy", f"s.ds.l{arc[1]}.{bim}"]
            )

            muxip_l = (
                tw_pre["mux", f"ip{arc[1]}"] - tw_pre["mux", f"s.ds.l{arc[1]}.{bim}"]
            )
            muyip_l = (
                tw_pre["muy", f"ip{arc[1]}"] - tw_pre["muy", f"s.ds.l{arc[1]}.{bim}"]
            )
            muxip_r = (
                tw_pre["mux", f"e.ds.r{arc[1]}.{bim}"] - tw_pre["mux", f"ip{arc[1]}"]
            )
            muyip_r = (
                tw_pre["muy", f"e.ds.r{arc[1]}.{bim}"] - tw_pre["muy", f"ip{arc[1]}"]
            )

            ip_params[f"{arc[1]}"][f"betxip{arc[1]}{bim}"] = tw_pre[
                "betx", f"ip{arc[1]}"
            ]
            ip_params[f"{arc[1]}"][f"betyip{arc[1]}{bim}"] = tw_pre[
                "bety", f"ip{arc[1]}"
            ]
            ip_params[f"{arc[1]}"][f"alfxip{arc[1]}{bim}"] = tw_pre[
                "alfx", f"ip{arc[1]}"
            ]
            ip_params[f"{arc[1]}"][f"alfyip{arc[1]}{bim}"] = tw_pre[
                "alfy", f"ip{arc[1]}"
            ]
            ip_params[f"{arc[1]}"][f"dxip{arc[1]}{bim}"] = tw_pre["dx", f"ip{arc[1]}"]
            ip_params[f"{arc[1]}"][f"dpxip{arc[1]}{bim}"] = tw_pre["dpx", f"ip{arc[1]}"]
            ip_params[f"{arc[1]}"][f"muxip{arc[1]}{bim}"] = mux
            ip_params[f"{arc[1]}"][f"muyip{arc[1]}{bim}"] = muy
            ip_params[f"{arc[1]}"][f"muxip{arc[1]}{bim}_l"] = muxip_l
            ip_params[f"{arc[1]}"][f"muyip{arc[1]}{bim}_l"] = muyip_l
            ip_params[f"{arc[1]}"][f"muxip{arc[1]}{bim}_r"] = muxip_r
            ip_params[f"{arc[1]}"][f"muyip{arc[1]}{bim}_r"] = muyip_r

    return ip_params


def _save_optics_summary(collider, tw=None):
    if tw is None:
        tw = collider.twiss()

    tw_pre = get_presqueeze(collider, "lhcb1")

    lines = []
    lines.append("\n!*** Optics summary ***")

    lines.append(f"qxb1      = {tw.lhcb1.qx:9.5f} ; qyb1  = {tw.lhcb1.qy:9.5f} ;")
    lines.append(f"qxb2      = {tw.lhcb2.qx:9.5f} ; qyb2  = {tw.lhcb2.qy:9.5f} ;")
    lines.append(f"qpxb1     = {tw.lhcb1.dqx:9.5f} ; qpyb1 = {tw.lhcb1.dqy:9.5f} ;")
    lines.append(f"qpxb2     = {tw.lhcb2.dqx:9.5f} ; qpyb2 = {tw.lhcb2.dqy:9.5f} ;")
    lines.append(f"betx_IP1  = {tw.lhcb1['betx', 'ip1']:2.3f} ;")
    lines.append(f"bety_IP1  = {tw.lhcb1['bety', 'ip1']:2.3f} ;")
    lines.append(f"betx_IP5  = {tw.lhcb1['betx', 'ip5']:2.3f} ;")
    lines.append(f"bety_IP5  = {tw.lhcb1['bety', 'ip5']:2.3f} ;")
    lines.append(f"betx0_IP1 = {tw_pre['ir1']['betx', 'ip1']:2.3f} ;")
    lines.append(f"bety0_IP1 = {tw_pre['ir1']['bety', 'ip1']:2.3f} ;")
    lines.append(f"betx0_IP5 = {tw_pre['ir5']['betx', 'ip5']:2.3f} ;")
    lines.append(f"bety0_IP5 = {tw_pre['ir5']['bety', 'ip5']:2.3f} ;")
    lines.append(f"betx_IP2  = {tw.lhcb1['betx', 'ip2']:2.3f} ;")
    lines.append(f"bety_IP2  = {tw.lhcb1['bety', 'ip2']:2.3f} ;")
    lines.append(f"betx_IP8  = {tw.lhcb1['betx', 'ip8']:2.3f} ;")
    lines.append(f"bety_IP8  = {tw.lhcb1['bety', 'ip8']:2.3f} ;")

    params = "phi_irIRN on_xIRN on_sepIRN on_oIRN on_aIRN"

    for ip in ["1", "5", "8", "2"]:
        for param in params.split():
            pname = param.replace("IRN", ip)
            lines.append(f"{pname:13} = {collider.varval[pname]:28} ;")

    return lines


def _save_optics_orbconf15(collider, ip):
    lines = []
    params_ip15 = (
        "cphi_irIRN sphi_irIRN on_xIRNhs on_xIRNhl "
        "on_sepIRNh on_aIRNh on_oIRNh "
        "on_xIRNvs on_xIRNvl "
        "on_sepIRNv on_aIRNv on_oIRNv"
    )
    for param in params_ip15.split():
        pname = param.replace("IRN", str(ip))
        sexpr = str(collider.vars[pname]._expr)
        expr = clean_expr2(sexpr)
        lines.append(f"{pname:10} := {expr} ;")

    return lines


def _save_optics_orbconf28(collider, ip):
    lines = []
    params_ip28 = (
        "cphi_irIRN sphi_irIRN on_xIRNh "
        "on_sepIRNh on_aIRNh on_oIRNh "
        "on_xIRNv on_sepIRNv on_aIRNv on_oIRNv"
    )
    for param in params_ip28.split():
        pname = param.replace("IRN", ip)
        sexpr = str(collider.vars[pname]._expr)
        expr = clean_expr2(sexpr)
        lines.append(f"{pname:10} := {expr} ;")

    return lines


def _save_optics_disp(collider):
    lines = []
    disp_params = (
        "on_dx1hs on_dx1vs on_dx1hl on_dx1vl "
        "on_dx5hs on_dx5vs on_dx5hl on_dx5vl "
        "on_dsep1h on_dsep1v on_dsep5h on_dsep5v"
    )
    lines.append(f"{'on_disp':11} = {collider.varval['on_disp']} ;")
    for param in disp_params.split():
        expr = clean_expr(collider.vars[param]._expr)
        lines.append(f"{param:10} := {expr} ;")
    return lines


def _save_orbit_configuration(collider):
    lines = []
    lines.append("\n!***Orbit configuration ***")

    for ip in ["1", "5"]:
        lines += _save_optics_orbconf15(collider, ip)

    for ip in ["2", "8"]:
        lines += _save_optics_orbconf28(collider, ip)

    lines += _save_optics_disp(collider)

    return lines


def _save_dipoles(collider):
    lines = []
    lines.append("\n!*** Dipoles ***")

    dipoles = (
        "kd1.lr1 kd2.l1 kd2.r1 kd1.l2 kd1.r2 kd2.l2 kd2.r2 "
        "kd3.lr3 kd4.lr3 kd3.l4 kd3.r4 kd4.l4 kd4.r4 "
        "kd34.lr3 kd34.lr7 kd1.lr5 kd2.l5 kd2.r5 "
        "kd3.lr7 kd4.lr7 kd1.l8 kd1.r8 kd2.l8 kd2.r8 kbh.a67 kbh.a78 "
        "ksumd2.l1b2 ksumd2.l2b2 ksumd2.l5b2 ksumd2.l8b2 "
        "ksumd2.r1b2 ksumd2.r2b2 ksumd2.r5b2 ksumd2.r8b2 "
        "kb.a12 kb.a23 kb.a34 kb.a45 "
        "kb.a56 kb.a67 kb.a78 kb.a81"
    )

    for dipole in dipoles.split():
        expr = clean_expr(collider.vars[dipole]._expr)
        lines.append(f"{dipole:15} := {expr} ;")

    return lines


def _save_experimental_magnets(collider):
    lines = []
    lines.append("\n!***Experiment magnets***")

    knobs = "on_sol_atlas on_sol_alice on_sol_cms on_alice on_lhcb"
    for k in knobs.split():
        lines.append(f"{k:16} = {collider.varval[k]} ;")

    magnets = (
        "abas abls abcs "
        "abxwt.l2 abwmd.l2 abaw.r2 abxwt.r2 "
        "abxws.l8 abxwh.l8 ablw.r8 abxws.r8"
    )
    for m in magnets.split():
        expr = clean_expr(collider.vars[m]._expr)
        lines.append(f"{m:15} := {expr} ;")

    return lines


def _save_optics_arcs(collider):
    lines = []
    lines.append("\n!*** Arc Optics ***")

    arc_names = ["81", "12", "45", "56", "78", "23", "34", "67"]

    arc_group_ats = ["81", "12", "45", "56"]
    arc_group_non_ats = ["78", "23", "34", "67"]

    for kflag in ["f", "d"]:
        for arc in arc_group_ats:
            kname = "kq" + kflag + f".a{arc}"
            lines.append(f"{kname:21} = {collider.varval[kname]:28.16f} ;")

    for kflag in ["f", "d"]:
        for arc in arc_group_non_ats:
            kname = "kq" + kflag + f".a{arc}"
            lines.append(f"{kname:21} = {collider.varval[kname]:28.16f} ;")

    for bim in ["b1", "b2"]:
        for kflag in ["f", "d"]:
            for arc in arc_group_ats:
                kname = "kqt" + kflag + f".a{arc}{bim}"
                lines.append(f"{kname:21} = {collider.varval[kname]:28.16f} ;")

        for kflag in ["f", "d"]:
            for arc in arc_group_non_ats:
                kname = f"kqt{kflag}.a{arc}{bim}"
                expr = (
                    str(collider.vars[kname]._expr)
                    .replace("vars['", "")
                    .replace("']", "")
                )
                lines.append(f"{kname:20} := {expr} ;")

    for kn in ["1", "2"]:
        for bim in ["b1", "b2"]:
            for kflag in ["f", "d"]:
                for arc in arc_group_ats:
                    sname = f"ks{kflag}{kn}.a{arc}{bim}"
                    lines.append(f"{sname:21} = {collider.varval[sname]:28.16f} ;")

            for kflag in ["f", "d"]:
                for arc in arc_group_non_ats:
                    sname = f"ks{kflag}{kn}.a{arc}{bim}"
                    expr = (
                        str(collider.vars[sname]._expr)
                        .replace("vars['", "")
                        .replace("']", "")
                    )
                    lines.append(f"{sname:20} := {expr} ;")

    cellphases = get_cellphases(collider)
    for arc in lm.ARC_NAMES:
        for nmu, mu in cellphases[arc].items():
            lines.append(f"{nmu:21} = {mu:28.16f} ;")

    arcphases = get_arcphase(collider)
    for arc in lm.ARC_NAMES:
        for nmu, mu in arcphases[arc].items():
            lines.append(f"{nmu:21} = {mu:28.16f} ;")

    return lines


def _save_optics_triplet(collider, ip):
    lines = []
    names = "kqx.lip ktqx1.lip ktqx2.lip kqx.rip ktqx1.rip ktqx2.rip"

    for n in names.split():
        tn = n.replace("ip", str(ip))
        lines.append(f"{tn:21} = {collider.varval[tn]:28.16f} ;")
    return lines


def _save_optics_triplethl(collider, ip):
    lines = []
    names = (
        "kqx1.lip kqx2a.lip kqx2b.lip kqx3.lip kqx1.rip kqx2a.rip kqx2b.rip kqx3.rip"
    )

    for n in names.split():
        tn = n.replace("ip", str(ip))
        lines.append(f"{tn:21} = {collider.varval[tn]:28.16f} ;")
    return lines


def _save_optics_quad(collider, qtype, nquad, ip):
    lines = []
    names = "kQN.lipb1 kQN.ripb1 kQN.lipb2 kQN.ripb2"
    for n in names.split():
        tn = n.replace("Q", qtype).replace("N", str(nquad)).replace("ip", str(ip))
        lines.append(f"{tn:21} = {collider.varval[tn]:28.16f} ;")
    return lines


def _save_optics_ms(collider, ip):
    l4 = _save_optics_quad(collider, "q", 4, ip)
    l5 = _save_optics_quad(collider, "q", 5, ip)
    l6 = _save_optics_quad(collider, "q", 6, ip)
    return l4 + l5 + l6


def _save_optics_ds(collider, ip):
    lines = []
    if ip != 6:
        lines += _save_optics_quad(collider, "q", 7, ip)

    lines += _save_optics_quad(collider, "q", 8, ip)
    lines += _save_optics_quad(collider, "q", 9, ip)
    lines += _save_optics_quad(collider, "q", 10, ip)
    lines += _save_optics_quad(collider, "qtl", 11, ip)
    lines += _save_optics_quad(collider, "qt", 12, ip)
    lines += _save_optics_quad(collider, "qt", 13, ip)

    return lines


def _save_optics_coll(collider, ip):
    lines = []
    names = "kq4.lrirn kqt4.lirn kqt4.rirn kq5.lrirn kqt5.lirn kqt5.rirn"
    for n in names.split():
        tn = n.replace("irn", str(ip))
        lines.append(f"{tn:21} = {collider.varval[tn]:28.16f} ;")
    lines += _save_optics_quad(collider, "q", 6, ip)
    lines += _save_optics_quad(collider, "qtl", 7, ip)
    lines += _save_optics_quad(collider, "qtl", 8, ip)
    lines += _save_optics_quad(collider, "qtl", 9, ip)
    lines += _save_optics_quad(collider, "qtl", 10, ip)
    lines += _save_optics_quad(collider, "qtl", 11, ip)
    lines += _save_optics_quad(collider, "qt", 12, ip)
    lines += _save_optics_quad(collider, "qt", 13, ip)

    return lines


def _save_optics_mcbx(collider, ip):
    lines = []
    names = (
        "acbxhv1.lirn acbxhv1.rirn acbxhv2.lirn acbxhv2.rirn acbxhv3.lirn acbxhv3.rirn"
    )

    for hv in ["h", "v"]:
        for n in names.split():
            m = n.replace("irn", str(ip)).replace("hv", hv)
            expr = clean_expr(collider.vars[m]._expr)
            lines.append(f"{m:20} := {expr} ;")
    return lines


def _save_optics_orb15(collider, ip):
    lines = []
    names = (
        "acbrdh4.lirnb1 acbrdh4.rirnb1 acbrdh4.lirnb2 acbrdh4.rirnb2 "
        "acbrdv4.lirnb1 acbrdv4.rirnb1 acbrdv4.lirnb2 acbrdv4.rirnb2 "
        "acbyhs4.lirnb1 acbyhs4.lirnb2 acbyhs4.rirnb1 acbyhs4.rirnb2 "
        "acbyvs4.lirnb1 acbyvs4.lirnb2 acbyvs4.rirnb1 acbyvs4.rirnb2 "
        "acbyh4.lirnb2 acbyh4.rirnb1 acbyv4.lirnb1 acbyv4.rirnb2 "
        "acbch5.lirnb2 acbch5.rirnb1 acbcv5.lirnb1 acbcv5.rirnb2 "
        "acbch6.lirnb1 acbch6.rirnb2 acbcv6.lirnb2 acbcv6.rirnb1"
    )
    for n in names.split():
        m = n.replace("irn", str(ip))
        expr = clean_expr(collider.vars[m]._expr)
        lines.append(f"{m:20} := {expr} ;")
    return lines


def _save_optics_orb2(collider):
    lines = []

    names_hvs = (
        "acbyhs4.l2b1 acbyvs4.l2b1 acbyhs4.r2b1 acbyvs4.r2b1 "
        "acbyhs4.l2b2 acbyvs4.l2b2 acbyhs4.r2b2 acbyvs4.r2b2 "
        "acbyhs5.l2b1 acbyvs5.l2b1 acbcvs5.r2b1 acbchs5.r2b1 "
        "acbyhs5.l2b2 acbyvs5.l2b2 acbcvs5.r2b2 acbchs5.r2b2"
    )
    names_hv = (
        "acbyh4.l2b2 acbyv4.l2b1 acbyh4.r2b1 acbyv4.r2b2 "
        "acbyv5.l2b2 acbyh5.l2b1 acbcv5.r2b1 acbch5.r2b2 "
        "acbch6.l2b2 acbcv6.l2b1 acbch6.r2b1 acbcv6.r2b2"
    )

    for n in names_hvs.split() + names_hv.split():
        expr = clean_expr(collider.vars[n]._expr)
        lines.append(f"{n:20} := {expr} ;")
    return lines


def _save_optics_orb8(collider):
    lines = []
    names_hvs = (
        "acbyhs4.l8b1 acbyvs4.l8b1 acbyhs4.r8b1 acbyvs4.r8b1 "
        "acbyhs4.l8b2 acbyvs4.l8b2 acbyhs4.r8b2 acbyvs4.r8b2 "
        "acbchs5.l8b1 acbcvs5.l8b1 acbyvs5.r8b1 acbyhs5.r8b1 "
        "acbchs5.l8b2 acbcvs5.l8b2 acbyvs5.r8b2 acbyhs5.r8b2"
    )
    names = "acbyh4.l8b2 acbyv4.l8b1 acbyh4.r8b1 acbyv4.r8b2"
    for n in names_hvs.split() + names.split():
        expr = clean_expr(collider.vars[n]._expr)
        lines.append(f"{n:20} := {expr} ;")

    names_maybe = (
        "acbcv5.l8b2 acbch5.l8b1 acbyv5.r8b1 acbyh5.r8b2 "
        "acbch6.l8b2 acbcv6.l8b1 acbch6.r8b1 acbcv6.r8b2"
    )

    for n in names_maybe.split():
        try:
            expr = clean_expr(collider.vars[n]._expr)
            lines.append(f"{n:20} := {expr} ;")
        except:
            continue
    names_rest = (
        "acbcv5.l8b2 acbch5.l8b1 acbyv5.r8b1 acbyh5.r8b2 "
        "acbch6.l8b2 acbcv6.l8b1 acbch6.r8b1 acbcv6.r8b2"
    )
    for n in names_rest.split():
        expr = clean_expr(collider.vars[n]._expr)
        lines.append(f"{n:20} := {expr} ;")

    return lines


def _save_optics_orb28(collider, ip):
    lines = []
    if ip == 2:
        lines += _save_optics_orb2(collider)
    elif ip == 8:
        lines += _save_optics_orb8(collider)
    return lines


def _save_optics_crabs15(collider, ip):
    lines = []
    names = (
        "ahcrab_lirnb1 ahcrab_lirnb2 ahcrab_rirnb1 ahcrab_rirnb2 "
        "avcrab_lirnb1 avcrab_lirnb2 avcrab_rirnb1 avcrab_rirnb2 "
        "v_crabh.lirnb1 v_crabh.lirnb2 v_crabh.rirnb1 v_crabh.rirnb2 "
        "v_crabv.lirnb1 v_crabv.lirnb2 v_crabv.rirnb1 v_crabv.rirnb2"
    )

    for n in names.split():
        tn = n.replace("irn", str(ip))
        lines.append(f"{tn:21} = {collider.varval[tn]:28.16g} ;")

    return lines


def _save_optics_orblv(collider, acb, qq, ip, bb1, bb2):
    lines = []
    names = "acbhqq.lirnbim1 acbvqq.lirnbim2 acbhqq.rirnbim2 acbvqq.rirnbim1"
    for n in names.split():
        m = (
            n.replace("acb", acb)
            .replace("qq", str(qq))
            .replace("irn", str(ip))
            .replace("bim1", bb1)
            .replace("bim2", bb2)
        )
        try:
            expr = clean_expr(collider.vars[m]._expr)
            lines.append(f"{m:20} := {expr} ;")
        except:
            continue
    return lines


def _save_optics_orbarc1357(collider, ip):
    lines = []
    lines += _save_optics_orblv(collider, "acbc", 7, ip, "b2", "b1")
    lines += _save_optics_orblv(collider, "acbc", 8, ip, "b1", "b2")
    lines += _save_optics_orblv(collider, "acbc", 9, ip, "b2", "b1")
    lines += _save_optics_orblv(collider, "acbc", 10, ip, "b1", "b2")
    for i in range(11, 33):
        lines += _save_optics_orblv(collider, "acb", i, ip, "b2", "b1")
        lines += _save_optics_orblv(collider, "acb", i, ip, "b1", "b2")

    return lines


def _save_optics_orbarc2468(collider, ip):
    lines = []
    lines += _save_optics_orblv(collider, "acbc", 7, ip, "b1", "b2")
    lines += _save_optics_orblv(collider, "acbc", 8, ip, "b2", "b1")
    lines += _save_optics_orblv(collider, "acbc", 9, ip, "b1", "b2")
    lines += _save_optics_orblv(collider, "acbc", 10, ip, "b2", "b1")
    for i in range(11, 33):
        lines += _save_optics_orblv(collider, "acb", i, ip, "b1", "b2")
        lines += _save_optics_orblv(collider, "acb", i, ip, "b2", "b1")

    return lines


# TODO: update them during rematching
def _save_optics_summ(collider, ip):
    lines = []
    lines.append(
        f"betxIP{ip}b1  = {collider.varval[f'betxip{ip}b1']:11.6f}; "
        f"betyIP{ip}b1  = {collider.varval[f'betyip{ip}b1']:11.6f}; "
        f"alfxIP{ip}b1  = {collider.varval[f'alfxip{ip}b1']:11.6f}; "
        f"alfyIP{ip}b1  = {collider.varval[f'alfyip{ip}b1']:11.6f}; "
        f"dxIP{ip}b1    = {collider.varval[f'dxip{ip}b1']:11.6f}; "
        f"dpxIP{ip}b1   = {collider.varval[f'dpxip{ip}b1']:11.6f}; "
    )
    lines.append(
        f"betxIP{ip}b2  = {collider.varval[f'betxip{ip}b2']:11.6f}; "
        f"betyIP{ip}b2  = {collider.varval[f'betyip{ip}b2']:11.6f}; "
        f"alfxIP{ip}b2  = {collider.varval[f'alfxip{ip}b2']:11.6f}; "
        f"alfyIP{ip}b2  = {collider.varval[f'alfyip{ip}b2']:11.6f}; "
        f"dxIP{ip}b2    = {collider.varval[f'dxip{ip}b2']:11.6f}; "
        f"dpxIP{ip}b2   = {collider.varval[f'dpxip{ip}b2']:11.6f}; "
    )
    lines.append(
        f"muxIP{ip}b1   = {collider.varval[f'muxip{ip}b1']:11.6f}; "
        f"muyIP{ip}b1   = {collider.varval[f'muyip{ip}b1']:11.6f}; "
        f"muxIP{ip}b1_L = {collider.varval[f'muxip{ip}b1_l']:11.6f}; "
        f"muyIP{ip}b1_L = {collider.varval[f'muyip{ip}b1_l']:11.6f}; "
        f"muxIP{ip}b1_R = {collider.varval[f'muxip{ip}b1_r']:11.6f}; "
        f"muyIP{ip}b1_R = {collider.varval[f'muyip{ip}b1_r']:11.6f}; "
    )
    lines.append(
        f"muxIP{ip}b2   = {collider.varval[f'muxip{ip}b2']:11.6f}; "
        f"muyIP{ip}b2   = {collider.varval[f'muyip{ip}b2']:11.6f}; "
        f"muxIP{ip}b2_L = {collider.varval[f'muxip{ip}b2_l']:11.6f}; "
        f"muyIP{ip}b2_L = {collider.varval[f'muyip{ip}b2_l']:11.6f}; "
        f"muxIP{ip}b2_R = {collider.varval[f'muxip{ip}b2_r']:11.6f}; "
        f"muyIP{ip}b2_R = {collider.varval[f'muyip{ip}b2_r']:11.6f}; "
    )

    return lines


def _save_optics_summ_cross(collider, ip):
    lines = []
    names = "xipirnb1 yipirnb1 pxipirnb1 pyipirnb1"
    for bim in ["b1", "b2"]:
        for n in names.split():
            m = n.replace("irn", str(ip)).replace("b1", bim)
            expr = clean_expr(collider.vars[m]._expr)
            lines.append(f"{m:20} := {expr} ;")

    return lines


def _save_optics_ir15(collider, ip):
    lines = []
    lines.append(f"\n!*** IR{ip} Optics***")
    lines += _save_optics_triplethl(collider, ip)
    lines += _save_optics_ms(collider, ip)
    lines += _save_optics_ds(collider, ip)

    lines += _save_optics_mcbx(collider, ip)
    lines += _save_optics_orb15(collider, ip)
    lines += _save_optics_orbarc1357(collider, ip)

    lines += _save_optics_crabs15(collider, ip)

    lines += _save_optics_summ(collider, ip)
    lines += _save_optics_summ_cross(collider, ip)

    return lines


def _save_optics_ir28(collider, ip):
    lines = []
    lines.append(f"\n!*** IR{ip} Optics***")
    lines += _save_optics_triplet(collider, ip)
    lines += _save_optics_ms(collider, ip)
    lines += _save_optics_ds(collider, ip)

    lines += _save_optics_mcbx(collider, ip)

    lines += _save_optics_orb28(collider, ip)
    lines += _save_optics_orbarc2468(collider, ip)

    lines += _save_optics_summ(collider, ip)
    lines += _save_optics_summ_cross(collider, ip)

    return lines


def _save_optics_ir46(collider, ip):
    quads_nums = {4: [5, 6], 6: [4, 5]}
    lines = []
    lines.append(f"\n!*** IR{ip} Optics***")
    lines += _save_optics_quad(collider, "q", quads_nums[ip][0], ip)
    lines += _save_optics_quad(collider, "q", quads_nums[ip][1], ip)
    lines += _save_optics_ds(collider, ip)

    lines += _save_optics_orbarc2468(collider, ip)

    lines += _save_optics_summ(collider, ip)

    return lines


def _save_optics_ir37(collider, ip):
    lines = []
    lines.append(f"\n!*** IR{ip} Optics***")
    lines += _save_optics_coll(collider, ip)
    lines += _save_optics_summ(collider, ip)
    return lines


import sys


def save_optics_hllhc(collider, file=sys.stdout):
    tw = collider.twiss()

    terms_summary = _save_optics_summary(collider, tw)
    terms_orbit = _save_orbit_configuration(collider)
    terms_exp_magnets = _save_experimental_magnets(collider)
    terms_dipoles = _save_dipoles(collider)
    terms_optics_arcs = _save_optics_arcs(collider)
    terms_optics_ip1 = _save_optics_ir15(collider, 1)
    terms_optics_ip5 = _save_optics_ir15(collider, 5)
    terms_optics_ip2 = _save_optics_ir28(collider, 2)
    terms_optics_ip8 = _save_optics_ir28(collider, 8)
    terms_optics_ip4 = _save_optics_ir46(collider, 4)
    terms_optics_ip6 = _save_optics_ir46(collider, 6)
    terms_optics_ip3 = _save_optics_ir37(collider, 3)
    terms_optics_ip7 = _save_optics_ir37(collider, 7)

    ll = (
        terms_summary
        + terms_orbit
        + terms_exp_magnets
        + terms_dipoles
        + terms_optics_arcs
        + terms_optics_ip1
        + terms_optics_ip5
        + terms_optics_ip2
        + terms_optics_ip8
        + terms_optics_ip4
        + terms_optics_ip6
        + terms_optics_ip3
        + terms_optics_ip7
    )

    for l in ll:
        print(l, file=file)
