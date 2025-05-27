import xtrack as xt
from xtrack._temp.lhc_match import get_arc_periodic_solution
from .rematch_ir15 import get_presqueezed_tw


def update_stored_vals_ips(collider):
    v = collider.vars
    tw = collider.twiss()
    tw81_12_xt = get_arc_periodic_solution(collider, arc_name=["81", "12"])
    tw45_56_xt = get_arc_periodic_solution(collider, arc_name=["45", "56"])
    tw_non_ats_arcs = get_arc_periodic_solution(
        collider, arc_name=["23", "34", "67", "78"]
    )

    tw_ip1 = get_presqueezed_tw(collider, 1)
    tw_ip5 = get_presqueezed_tw(collider, 5)

    v["betx0_ip1"] = tw_ip1["lhcb1"]["betx", "ip1"]
    v["bety0_ip1"] = tw_ip1["lhcb1"]["bety", "ip1"]
    v["betx0_ip5"] = tw_ip5["lhcb1"]["betx", "ip5"]
    v["bety0_ip5"] = tw_ip5["lhcb1"]["bety", "ip5"]

    # PHASES IP1
    v["muxip1b1"] = (
        tw_ip1["lhcb1"]["mux", "e.ds.r1.b1"] - tw_ip1["lhcb1"]["mux", "s.ds.l1.b1"]
    )
    v["muyip1b1"] = (
        tw_ip1["lhcb1"]["muy", "e.ds.r1.b1"] - tw_ip1["lhcb1"]["muy", "s.ds.l1.b1"]
    )
    v["muxip1b1_l"] = (
        tw_ip1["lhcb1"]["mux", "ip1"] - tw_ip1["lhcb1"]["mux", "s.ds.l1.b1"]
    )
    v["muyip1b1_l"] = (
        tw_ip1["lhcb1"]["muy", "ip1"] - tw_ip1["lhcb1"]["muy", "s.ds.l1.b1"]
    )
    v["muxip1b1_r"] = (
        tw_ip1["lhcb1"]["mux", "e.ds.r1.b1"] - tw_ip1["lhcb1"]["mux", "ip1"]
    )
    v["muyip1b1_r"] = (
        tw_ip1["lhcb1"]["muy", "e.ds.r1.b1"] - tw_ip1["lhcb1"]["muy", "ip1"]
    )

    v["muxip1b2"] = (
        tw_ip1["lhcb2"]["mux", "e.ds.r1.b2"] - tw_ip1["lhcb2"]["mux", "s.ds.l1.b2"]
    )
    v["muyip1b2"] = (
        tw_ip1["lhcb2"]["muy", "e.ds.r1.b2"] - tw_ip1["lhcb2"]["muy", "s.ds.l1.b2"]
    )
    v["muxip1b2_l"] = tw_ip1["lhcb2"]["mux", "ip1"]
    v["muyip1b2_l"] = tw_ip1["lhcb2"]["muy", "ip1"]
    v["muxip1b2_r"] = (
        tw_ip1["lhcb2"]["mux", "e.ds.r1.b2"] - tw_ip1["lhcb2"]["mux", "ip1"]
    )
    v["muyip1b2_r"] = (
        tw_ip1["lhcb2"]["muy", "e.ds.r1.b2"] - tw_ip1["lhcb2"]["muy", "ip1"]
    )

    # PHASES IP5
    v["muxip5b1"] = (
        tw_ip5["lhcb1"]["mux", "e.ds.r5.b1"] - tw_ip5["lhcb1"]["mux", "s.ds.l5.b1"]
    )
    v["muyip5b1"] = (
        tw_ip5["lhcb1"]["muy", "e.ds.r5.b1"] - tw_ip5["lhcb1"]["muy", "s.ds.l5.b1"]
    )
    v["muxip5b1_l"] = (
        tw_ip5["lhcb1"]["mux", "ip5"] - tw_ip5["lhcb1"]["mux", "s.ds.l5.b1"]
    )
    v["muyip5b1_l"] = (
        tw_ip5["lhcb1"]["muy", "ip5"] - tw_ip5["lhcb1"]["muy", "s.ds.l5.b1"]
    )
    v["muxip5b1_r"] = (
        tw_ip5["lhcb1"]["mux", "e.ds.r5.b1"] - tw_ip5["lhcb1"]["mux", "ip5"]
    )
    v["muyip5b1_r"] = (
        tw_ip5["lhcb1"]["muy", "e.ds.r5.b1"] - tw_ip5["lhcb1"]["muy", "ip5"]
    )

    v["muxip5b2"] = (
        tw_ip5["lhcb2"]["mux", "e.ds.r5.b2"] - tw_ip5["lhcb2"]["mux", "s.ds.l5.b2"]
    )
    v["muyip5b2"] = (
        tw_ip5["lhcb2"]["muy", "e.ds.r5.b2"] - tw_ip5["lhcb2"]["muy", "s.ds.l5.b2"]
    )
    v["muxip5b2_l"] = tw_ip5["lhcb2"]["mux", "ip5"]
    v["muyip5b2_l"] = tw_ip5["lhcb2"]["muy", "ip5"]
    v["muxip5b2_r"] = (
        tw_ip5["lhcb2"]["mux", "e.ds.r5.b2"] - tw_ip5["lhcb2"]["mux", "ip5"]
    )
    v["muyip5b2_r"] = (
        tw_ip5["lhcb2"]["muy", "e.ds.r5.b2"] - tw_ip5["lhcb2"]["muy", "ip5"]
    )

    # OPTICS IPs
    for bim in ["b1", "b2"]:
        for ip in [1, 2, 3, 4, 5, 6, 7, 8]:
            v[f"betxip{ip}{bim}"] = tw[f"lhc{bim}"]["betx", f"ip{ip}"]
            v[f"betyip{ip}{bim}"] = tw[f"lhc{bim}"]["bety", f"ip{ip}"]
            v[f"alfxip{ip}{bim}"] = tw[f"lhc{bim}"]["alfx", f"ip{ip}"]
            v[f"alfyip{ip}{bim}"] = tw[f"lhc{bim}"]["alfy", f"ip{ip}"]
            v[f"dxip{ip}{bim}"] = tw[f"lhc{bim}"]["dx", f"ip{ip}"]
            v[f"dpxi{ip}{bim}"] = tw[f"lhc{bim}"]["dpx", f"ip{ip}"]

        v[f"muxip2{bim}"] = (
            tw[f"lhc{bim}"]["mux", f"e.ds.r2.{bim}"]
            - tw[f"lhc{bim}"]["mux", "ip1"]
            - v[f"muxip1{bim}_r"]
            - tw81_12_xt[f"lhc{bim}"]["12"].mux[-1]
        )
        v[f"muxip6{bim}"] = (
            tw[f"lhc{bim}"]["mux", f"e.ds.r6.{bim}"]
            - tw[f"lhc{bim}"]["mux", "ip5"]
            - v[f"muxip5{bim}_r"]
            - tw45_56_xt[f"lhc{bim}"]["56"].mux[-1]
        )
        v[f"muxip8{bim}"] = (
            tw[f"lhc{bim}"]["mux", "ip1"]
            - tw[f"lhc{bim}"]["mux", f"s.ds.l8.{bim}"]
            - v[f"muxip1{bim}_l"]
            - tw81_12_xt[f"lhc{bim}"]["81"].mux[-1]
        )
        v[f"muxip4{bim}"] = (
            tw[f"lhc{bim}"]["mux", "ip5"]
            - tw[f"lhc{bim}"]["mux", f"s.ds.l4.{bim}"]
            - v[f"muxip5{bim}_l"]
            - tw45_56_xt[f"lhc{bim}"]["45"].mux[-1]
        )
        v[f"muxip3{bim}"] = (
            tw[f"lhc{bim}"]["mux", f"e.ds.r3.{bim}"]
            - tw[f"lhc{bim}"]["mux", f"s.ds.l3.{bim}"]
        )
        v[f"muxip7{bim}"] = (
            tw[f"lhc{bim}"]["mux", f"e.ds.r7.{bim}"]
            - tw[f"lhc{bim}"]["mux", f"s.ds.l7.{bim}"]
        )

        v[f"muyip2{bim}"] = (
            tw[f"lhc{bim}"]["muy", f"e.ds.r2.{bim}"]
            - tw[f"lhc{bim}"]["muy", "ip1"]
            - v[f"muyip1{bim}_r"]
            - tw81_12_xt[f"lhc{bim}"]["12"].muy[-1]
        )
        v[f"muyip6{bim}"] = (
            tw[f"lhc{bim}"]["muy", f"e.ds.r6.{bim}"]
            - tw[f"lhc{bim}"]["muy", "ip5"]
            - v[f"muyip5{bim}_l"]
            - tw45_56_xt[f"lhc{bim}"]["56"].muy[-1]
        )
        v[f"muyip8{bim}"] = (
            tw[f"lhc{bim}"]["muy", "ip1"]
            - tw[f"lhc{bim}"]["muy", f"s.ds.l8.{bim}"]
            - v[f"muyip1{bim}_l"]
            - tw81_12_xt[f"lhc{bim}"]["81"].muy[-1]
        )
        v[f"muyip4{bim}"] = (
            tw[f"lhc{bim}"]["muy", "ip5"]
            - tw[f"lhc{bim}"]["muy", f"s.ds.l4.{bim}"]
            - v[f"muyip5{bim}_l"]
            - tw45_56_xt[f"lhc{bim}"]["45"].muy[-1]
        )
        v[f"muyip3{bim}"] = (
            tw[f"lhc{bim}"]["muy", f"e.ds.r3.{bim}"]
            - tw[f"lhc{bim}"]["muy", f"s.ds.l3.{bim}"]
        )
        v[f"muyip7{bim}"] = (
            tw[f"lhc{bim}"]["muy", f"e.ds.r7.{bim}"]
            - tw[f"lhc{bim}"]["muy", f"s.ds.l7.{bim}"]
        )

        v[f"muxip2{bim}_l"] = (
            tw[f"lhc{bim}"]["mux", "ip2"]
            - tw[f"lhc{bim}"]["mux", "ip1"]
            - v[f"muxip1{bim}_r"]
            - tw81_12_xt[f"lhc{bim}"]["12"].mux[-1]
        )
        v[f"muxip6{bim}_l"] = (
            tw[f"lhc{bim}"]["mux", "ip6"]
            - tw[f"lhc{bim}"]["mux", "ip5"]
            - v[f"muxip5{bim}_r"]
            - tw45_56_xt[f"lhc{bim}"]["56"].mux[-1]
        )
        v[f"muxip8{bim}_r"] = (
            tw[f"lhc{bim}"]["mux", "ip1"]
            - tw[f"lhc{bim}"]["mux", "ip8"]
            - v[f"muxip1{bim}_l"]
            - tw81_12_xt[f"lhc{bim}"]["81"].mux[-1]
        )
        v[f"muxip4{bim}_r"] = (
            tw[f"lhc{bim}"]["mux", "ip5"]
            - tw[f"lhc{bim}"]["mux", "ip4"]
            - v[f"muxip5{bim}_l"]
            - tw45_56_xt[f"lhc{bim}"]["45"].mux[-1]
        )
        v[f"muxip3{bim}_r"] = (
            tw[f"lhc{bim}"]["mux", f"e.ds.r3.{bim}"] - tw[f"lhc{bim}"]["mux", "ip3"]
        )
        v[f"muxip7{bim}_r"] = (
            tw[f"lhc{bim}"]["mux", f"e.ds.r7.{bim}"] - tw[f"lhc{bim}"]["mux", "ip7"]
        )
        v[f"muyip2{bim}_l"] = (
            tw[f"lhc{bim}"]["muy", "ip2"]
            - tw[f"lhc{bim}"]["muy", "ip1"]
            - v[f"muyip1{bim}_r"]
            - tw81_12_xt[f"lhc{bim}"]["12"].muy[-1]
        )
        v[f"muyip6{bim}_l"] = (
            tw[f"lhc{bim}"]["muy", "ip6"]
            - tw[f"lhc{bim}"]["muy", "ip5"]
            - v[f"muyip5{bim}_r"]
            - tw45_56_xt[f"lhc{bim}"]["56"].muy[-1]
        )
        v[f"muyip8{bim}_r"] = (
            tw[f"lhc{bim}"]["muy", "ip1"]
            - tw[f"lhc{bim}"]["muy", "ip8"]
            - v[f"muyip1{bim}_l"]
            - tw81_12_xt[f"lhc{bim}"]["81"].muy[-1]
        )
        v[f"muyip4{bim}_r"] = (
            tw[f"lhc{bim}"]["muy", "ip5"]
            - tw[f"lhc{bim}"]["muy", "ip4"]
            - v[f"muyip5{bim}_l"]
            - tw45_56_xt[f"lhc{bim}"]["45"].muy[-1]
        )
        v[f"muyip3{bim}_r"] = (
            tw[f"lhc{bim}"]["muy", f"e.ds.r3.{bim}"] - tw[f"lhc{bim}"]["muy", "ip3"]
        )
        v[f"muyip7{bim}_r"] = (
            tw[f"lhc{bim}"]["muy", f"e.ds.r7.{bim}"] - tw[f"lhc{bim}"]["muy", "ip7"]
        )
        v[f"muxip2{bim}_r"] = v[f"muxip2{bim}"] - v[f"muxip2{bim}_l"]
        v[f"muxip6{bim}_r"] = v[f"muxip6{bim}"] - v[f"muxip6{bim}_l"]
        v[f"muxip8{bim}_l"] = v[f"muxip8{bim}"] - v[f"muxip8{bim}_r"]
        v[f"muxip4{bim}_l"] = v[f"muxip4{bim}"] - v[f"muxip4{bim}_r"]
        v[f"muxip3{bim}_l"] = v[f"muxip3{bim}"] - v[f"muxip3{bim}_r"]
        v[f"muxip7{bim}_l"] = v[f"muxip7{bim}"] - v[f"muxip7{bim}_r"]
        v[f"muyip2{bim}_r"] = v[f"muyip2{bim}"] - v[f"muyip2{bim}_l"]
        v[f"muyip6{bim}_r"] = v[f"muyip6{bim}"] - v[f"muyip6{bim}_l"]
        v[f"muyip8{bim}_l"] = v[f"muyip8{bim}"] - v[f"muyip8{bim}_r"]
        v[f"muyip4{bim}_l"] = v[f"muyip4{bim}"] - v[f"muyip4{bim}_r"]
        v[f"muyip3{bim}_l"] = v[f"muyip3{bim}"] - v[f"muyip3{bim}_r"]
        v[f"muyip7{bim}_l"] = v[f"muyip7{bim}"] - v[f"muyip7{bim}_r"]


def rematch_ir6(
    collider,
    line_name,
    boundary_conditions_left,
    boundary_conditions_right,
    mux_ir6,
    muy_ir6,
    alfx_ip6,
    alfy_ip6,
    betx_ip6,
    bety_ip6,
    dx_ip6,
    dpx_ip6,
    match_dx=False,
    match_dpx=False,
    solve=True,
    restore=True,
    assert_within_tol=True,
    default_tol=None,
):

    assert line_name in ["lhcb1", "lhcb2"]
    bn = line_name[-2:]

    opt = collider[f"lhc{bn}"].match(
        solve=False,
        restore_if_fail=restore,
        assert_within_tol=assert_within_tol,
        default_tol=default_tol,
        start=f"s.ds.l6.{bn}",
        end=f"e.ds.r6.{bn}",
        # Left boundary
        init=boundary_conditions_left,
        init_at=xt.START,
        targets=[
            xt.TargetSet(
                at="ip6",
                alfx=alfx_ip6,
                alfy=alfy_ip6,
                betx=betx_ip6,
                bety=bety_ip6,
                # dx=dx_ip6,
                # dpx=dpx_ip6,
                tag="stage1",
            ),
            xt.Target(at="ip6", dx=dx_ip6, tag="dx_ip6"),
            xt.Target(at="ip6", dpx=dpx_ip6, tag="dpx_ip6"),
            xt.TargetSet(
                at=xt.END,
                tars=("betx", "bety", "alfx", "alfy", "dx", "dpx"),
                value=boundary_conditions_right,
            ),
            xt.TargetRelPhaseAdvance("mux", mux_ir6),
            xt.TargetRelPhaseAdvance("muy", muy_ir6),
        ],
        vary=(
            [
                xt.VaryList(
                    [
                        f"kqt13.l6{bn}",
                        f"kqt12.l6{bn}",
                        f"kqtl11.l6{bn}",
                        f"kq10.l6{bn}",
                        f"kq9.l6{bn}",
                        f"kq8.l6{bn}",
                        f"kq5.l6{bn}",
                        f"kq5.r6{bn}",
                        f"kq8.r6{bn}",
                        f"kq9.r6{bn}",
                        f"kq10.r6{bn}",
                        f"kqtl11.r6{bn}",
                        f"kqt12.r6{bn}",
                        f"kqt13.r6{bn}",
                    ]
                )
            ]
            + [xt.Vary((f"kq4.r6{bn}" if bn == "b1" else f"kq4.l6{bn}"))]
        ),
    )

    if not match_dx:
        opt.disable(target="dx_ip6")

    if not match_dpx:
        opt.disable(target="dpx_ip6")

    # No staged match for IR6
    if solve:
        opt.solve()

    return opt


def set_new_ir7_strengths(collider):
    # Addapted from https://gitlab.cern.ch/acc-models/acc-models-lhc/-/blob/hl19/strengths/ir7/re12c6b.str
    collider.vars["kqt4.l7"] = 0.0012257364160585084
    collider.vars["kqt4.r7"] = 0.0012659632628095638
    collider.vars["kqt13.l7b1"] = -0.0048823483573787445
    collider.vars["kqt12.l7b1"] = -0.004882279788343516
    collider.vars["kqtl11.l7b1"] = 0.0027739663492968103
    collider.vars["kqtl10.l7b1"] = 0.004623538857746193
    collider.vars["kqtl9.l7b1"] = -0.003372747954072591
    collider.vars["kqtl8.l7b1"] = -0.0023127417813640786
    collider.vars["kqtl7.l7b1"] = -0.002011344510772721
    collider.vars["kq6.l7b1"] = 0.0031173363410593766
    collider.vars["kq6.r7b1"] = -0.0031388056161611565
    collider.vars["kqtl7.r7b1"] = 0.0009532375359442739
    collider.vars["kqtl8.r7b1"] = 0.002688438505728887
    collider.vars["kqtl9.r7b1"] = 0.0033416607916765947
    collider.vars["kqtl10.r7b1"] = -0.003461273410884878
    collider.vars["kqtl11.r7b1"] = 0.0010531054411466265
    collider.vars["kqt12.r7b1"] = -0.0027831205556483702
    collider.vars["kqt13.r7b1"] = -0.0013509460856456692

    collider.vars["kqt13.l7b2"] = -0.004192310485204978
    collider.vars["kqt12.l7b2"] = -0.0035271197718106688
    collider.vars["kqtl11.l7b2"] = 0.0008993274235722462
    collider.vars["kqtl10.l7b2"] = -0.0035044843946580337
    collider.vars["kqtl9.l7b2"] = 0.003295485018957867
    collider.vars["kqtl8.l7b2"] = 0.002429071850457167
    collider.vars["kqtl7.l7b2"] = 0.0008310840304967491
    collider.vars["kq6.l7b2"] = -0.0031817725498278727
    collider.vars["kq6.r7b2"] = 0.003183554427942885
    collider.vars["kqtl7.r7b2"] = -0.0012886165853725183
    collider.vars["kqtl8.r7b2"] = -0.0037917967174795034
    collider.vars["kqtl9.r7b2"] = -0.0033703081873609005
    collider.vars["kqtl10.r7b2"] = 0.0049711605825101994
    collider.vars["kqtl11.r7b2"] = 0.002278252114016244
    collider.vars["kqt12.r7b2"] = -0.0048808187874553495
    collider.vars["kqt13.r7b2"] = -0.0048815559298144
    collider.vars["kq4.lr7"] = 0.0011653779946877393
    collider.vars["kq5.lr7"] = -0.001202569087048791


# Addapted from https://gitlab.cern.ch/acc-models/acc-models-lhc/-/blob/hl19/strengths/ir7/re12c6b.str
new_ir7_optics = {
    "b1": {
        "betx": 89.84496726894332,
        "bety": 266.97003605045893,
        "alfx": 0.21970903658222377,
        "alfy": -0.13590419140231066,
        "dx": 0.0312403796059464,
        "dpx": 0.0009957576286563452,
        "mux": 1.1711991570872158,
        "muy": 0.9562584358629991,
    },
    "b2": {
        "betx": 107.0632022391966,
        "bety": 282.7445143417741,
        "alfx": -0.2801456276715532,
        "alfy": 0.10965483134341904,
        "dx": 0.08482535185804546,
        "dpx": 0.0008043571661596836,
        "mux": 1.089238973229854,
        "muy": 1.1069817552100787,
    },
}


def rematch_new_ir7(
    collider,
    line_name,
    boundary_conditions_left,
    boundary_conditions_right,
    mux_ir7,
    muy_ir7,
    solve=True,
    restore=True,
    assert_within_tol=True,
    default_tol=None,
):

    assert line_name in ["lhcb1", "lhcb2"]
    bn = line_name[-2:]

    opt = collider[f"lhc{bn}"].match(
        solve=False,
        restore_if_fail=restore,
        assert_within_tol=assert_within_tol,
        default_tol=default_tol,
        solver_options={"n_bisections": 3, "min_step": 1e-7},
        start=f"s.ds.l7.{bn}",
        end=f"e.ds.r7.{bn}",
        init=boundary_conditions_left,
        init_at=xt.START,
        targets=[
            xt.TargetSet(
                at="ip7",
                alfx=new_ir7_optics[bn]["alfx"],
                alfy=new_ir7_optics[bn]["alfy"],
                betx=new_ir7_optics[bn]["betx"],
                bety=new_ir7_optics[bn]["bety"],
                dx=new_ir7_optics[bn]["dx"],
                dpx=new_ir7_optics[bn]["dpx"],
                # mux=new_ir7_optics[bn]['mux'],
                # muy=new_ir7_optics[bn]['muy'],
                tag="ip7",
            ),
            xt.TargetSet(
                at=xt.END,
                tars=("betx", "bety", "alfx", "alfy", "dx", "dpx"),
                value=boundary_conditions_right,
            ),
            xt.TargetRelPhaseAdvance("mux", mux_ir7),
            xt.TargetRelPhaseAdvance("muy", muy_ir7),
            # for IR7
            xt.TargetRelPhaseAdvance(
                "mux",
                new_ir7_optics[bn]["mux"],
                end="ip7",
                start=f"s.ds.l7.{bn}",
                tag="ip7_mux",
            ),
            xt.TargetRelPhaseAdvance(
                "muy",
                new_ir7_optics[bn]["muy"],
                end="ip7",
                start=f"s.ds.l7.{bn}",
                tag="ip7_muy",
            ),
        ],
        vary=[
            xt.VaryList(
                [
                    f"kqt13.l7{bn}",
                    f"kqt12.l7{bn}",
                    f"kqtl11.l7{bn}",
                    f"kqtl10.l7{bn}",
                    f"kqtl9.l7{bn}",
                    f"kqtl8.l7{bn}",
                    f"kqtl7.l7{bn}",
                    f"kq6.l7{bn}",
                    f"kq6.r7{bn}",
                    f"kqtl7.r7{bn}",
                    f"kqtl8.r7{bn}",
                    f"kqtl9.r7{bn}",
                    f"kqtl10.r7{bn}",
                    f"kqtl11.r7{bn}",
                    f"kqt12.r7{bn}",
                    f"kqt13.r7{bn}",
                ],
                tag="single_quads",
            ),
            xt.Vary("kq4.lr7", tag="q4"),
            xt.Vary("kq5.lr7", tag="q5"),
            xt.Vary("kqt4.l7", tag="qt4l"),
            xt.Vary("kqt4.r7", tag="qt4r"),
        ],
    )

    opt.disable_vary(tag="q4")
    opt.disable_vary(tag="q5")
    opt.disable_vary(tag="qt4l")
    opt.disable_vary(tag="qt4r")

    if solve:
        opt.solve()

    return opt
