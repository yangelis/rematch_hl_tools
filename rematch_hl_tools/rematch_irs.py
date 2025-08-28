import xtrack as xt
from xtrack._temp.lhc_match import get_arc_periodic_solution, compute_ats_phase_advances_for_auxiliary_irs
from .rematch_ir15 import get_presqueezed_tw


def get_tw_ip(collider, ip, zero_phase=True):
    tw = collider.twiss()
    beta0_b1 = tw["lhcb1"].get_twiss_init(f"s.ds.l{ip}.b1")
    beta0_b2 = tw["lhcb2"].get_twiss_init(f"s.ds.l{ip}.b2")
    
    if zero_phase:
        beta0_b1.mux = 0
        beta0_b1.muy = 0
        beta0_b2.mux = 0
        beta0_b2.muy = 0

    tw_ip = collider.twiss(
        start=[f"s.ds.l{ip}.b1", f"s.ds.l{ip}.b2"],
        end=[f"e.ds.r{ip}.b1", f"e.ds.r{ip}.b2"],
        init=[beta0_b1, beta0_b2],
    )
    return tw_ip


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

    # PHases Arcs
    # for arc in 

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
            - v[f"muyip5{bim}_r"]
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

        # TODO:fix this
        for ph in ["muxip1b1_l", "muxip1b1_r", "muxip5b1_l", "muxip5b1_r",
            "muxip2b1", "muxip4b1", "muxip6b1", "muxip8b1",
            "mux12b1", "mux45b1", "mux56b1", "mux81b1"]:
            if collider.varval[ph] < 0:
                collider.varval[ph] += tw['lhcb1'].qx      

        for ph in ["muyip1b1_l", "muyip1b1_r", "muyip5b1_l", "muyip5b1_r",
                "muyip2b1","muyip4b1","muyip6b1","muyip8b1",
                "muy12b1","muy45b1","muy56b1","muy81b1"]:
            if collider.varval[ph] < 0:
                collider.varval[ph] += tw['lhcb1'].qy

        for ph in ["muxip1b2_l", "muxip1b2_r", "muxip5b2_l", "muxip5b2_r",
                "muxip2b2", "muxip4b2", "muxip6b2", "muxip8b2",
                "mux12b2", "mux45b2", "mux56b2", "mux81b2"]:
            if collider.varval[ph] < 0:
                collider.varval[ph] += tw['lhcb2'].qx      

        for ph in ["muyip1b2_l", "muyip1b2_r", "muyip5b2_l", "muyip5b2_r",
                "muyip2b2","muyip4b2","muyip6b2","muyip8b2",
                "muy12b2","muy45b2","muy56b2","muy81b2"]:
            if collider.varval[ph] < 0:
                collider.varval[ph] += tw['lhcb2'].qy   
                
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


def ats_phase_aux(collider, tw, tw_sq_a81_ip1_a12_b1, tw_sq_a45_ip5_a56_b1, tw_sq_a81_ip1_a12_b2, tw_sq_a45_ip5_a56_b2):
    for ph in ["muxip1b1_l", "muxip1b1_r", "muxip5b1_l", "muxip5b1_r",
            "muxip2b1", "muxip4b1", "muxip6b1", "muxip8b1",
            "mux12b1", "mux45b1", "mux56b1", "mux81b1"]:
        if collider.varval[ph] < 0:
            collider.varval[ph] += tw['lhcb1'].qx      

    for ph in ["muyip1b1_l", "muyip1b1_r", "muyip5b1_l", "muyip5b1_r",
            "muyip2b1","muyip4b1","muyip6b1","muyip8b1",
            "muy12b1","muy45b1","muy56b1","muy81b1"]:
        if collider.varval[ph] < 0:
            collider.varval[ph] += tw['lhcb1'].qy

    for ph in ["muxip1b2_l", "muxip1b2_r", "muxip5b2_l", "muxip5b2_r",
            "muxip2b2", "muxip4b2", "muxip6b2", "muxip8b2",
            "mux12b2", "mux45b2", "mux56b2", "mux81b2"]:
        if collider.varval[ph] < 0:
            collider.varval[ph] += tw['lhcb2'].qx      

    for ph in ["muyip1b2_l", "muyip1b2_r", "muyip5b2_l", "muyip5b2_r",
            "muyip2b2","muyip4b2","muyip6b2","muyip8b2",
            "muy12b2","muy45b2","muy56b2","muy81b2"]:
        if collider.varval[ph] < 0:
            collider.varval[ph] += tw['lhcb2'].qy   
       
    (
    mux_ir2_target_b1,
    muy_ir2_target_b1,
    mux_ir4_target_b1,
    muy_ir4_target_b1,
    mux_ir6_target_b1,
    muy_ir6_target_b1,
    mux_ir8_target_b1,
    muy_ir8_target_b1,
    ) = compute_ats_phase_advances_for_auxiliary_irs(
        "lhcb1",
        tw_sq_a81_ip1_a12_b1,
        tw_sq_a45_ip5_a56_b1,
        collider.varval["muxip1b1_l"],
        collider.varval["muyip1b1_l"],
        collider.varval["muxip1b1_r"],
        collider.varval["muyip1b1_r"],
        collider.varval["muxip5b1_l"],
        collider.varval["muyip5b1_l"],
        collider.varval["muxip5b1_r"],
        collider.varval["muyip5b1_r"],
        collider.varval["muxip2b1"],
        collider.varval["muyip2b1"],
        collider.varval["muxip4b1"],
        collider.varval["muyip4b1"],
        collider.varval["muxip6b1"],
        collider.varval["muyip6b1"],
        collider.varval["muxip8b1"],
        collider.varval["muyip8b1"],
        collider.varval["mux12b1"],
        collider.varval["muy12b1"],
        collider.varval["mux45b1"],
        collider.varval["muy45b1"],
        collider.varval["mux56b1"],
        collider.varval["muy56b1"],
        collider.varval["mux81b1"],
        collider.varval["muy81b1"],
    )


    (
    mux_ir2_target_b2,
    muy_ir2_target_b2,
    mux_ir4_target_b2,
    muy_ir4_target_b2,
    mux_ir6_target_b2,
    muy_ir6_target_b2,
    mux_ir8_target_b2,
    muy_ir8_target_b2,
    ) = compute_ats_phase_advances_for_auxiliary_irs(
        "lhcb2",
        tw_sq_a81_ip1_a12_b2,
        tw_sq_a45_ip5_a56_b2,
        collider.varval["muxip1b2_l"],
        collider.varval["muyip1b2_l"],
        collider.varval["muxip1b2_r"],
        collider.varval["muyip1b2_r"],
        collider.varval["muxip5b2_l"],
        collider.varval["muyip5b2_l"],
        collider.varval["muxip5b2_r"],
        collider.varval["muyip5b2_r"],
        collider.varval["muxip2b2"],
        collider.varval["muyip2b2"],
        collider.varval["muxip4b2"],
        collider.varval["muyip4b2"],
        collider.varval["muxip6b2"],
        collider.varval["muyip6b2"],
        collider.varval["muxip8b2"],
        collider.varval["muyip8b2"],
        collider.varval["mux12b2"],
        collider.varval["muy12b2"],
        collider.varval["mux45b2"],
        collider.varval["muy45b2"],
        collider.varval["mux56b2"],
        collider.varval["muy56b2"],
        collider.varval["mux81b2"],
        collider.varval["muy81b2"],
    )


    return {
        'mux_ir2_target_b1': mux_ir2_target_b1,
        'muy_ir2_target_b1': muy_ir2_target_b1,
        'mux_ir4_target_b1': mux_ir4_target_b1,
        'muy_ir4_target_b1': muy_ir4_target_b1,
        'mux_ir6_target_b1': mux_ir6_target_b1,
        'muy_ir6_target_b1': muy_ir6_target_b1,
        'mux_ir8_target_b1': mux_ir8_target_b1,
        'muy_ir8_target_b1': muy_ir8_target_b1,
        'mux_ir2_target_b2': mux_ir2_target_b2,
        'muy_ir2_target_b2': muy_ir2_target_b2,
        'mux_ir4_target_b2': mux_ir4_target_b2,
        'muy_ir4_target_b2': muy_ir4_target_b2,
        'mux_ir6_target_b2': mux_ir6_target_b2,
        'muy_ir6_target_b2': muy_ir6_target_b2,
        'mux_ir8_target_b2': mux_ir8_target_b2,
        'muy_ir8_target_b2': muy_ir8_target_b2,
    }


def ats_phase_aux2(collider, tw, tw_sq_a81_ip1_a12_b1, tw_sq_a45_ip5_a56_b1, tw_sq_a81_ip1_a12_b2, tw_sq_a45_ip5_a56_b2):
    phases = {}
    tws = {}
    for ir in [1,5,2,4,6,8]:
        tws[ir] = get_tw_ip(collider, ir)
        phases[f'muxip{ir}b1'] = tws[ir].lhcb1.mux[-1]
        phases[f'muyip{ir}b1'] = tws[ir].lhcb1.muy[-1]
        phases[f'muxip{ir}b2'] = tws[ir].lhcb2.mux[-1]
        phases[f'muyip{ir}b2'] = tws[ir].lhcb2.muy[-1]

        # tw_arcs = lm.get_arc_periodic_solution(collider, f"lhc{bim}", arc)
        #     beta0 = tw_arcs.get_twiss_init(f"s.ds.l{arc[1]}.{bim}")
        #     beta0.mux = 0
        #     beta0.muy = 0

        #     tw_pre = None
        #     if arc == "81":
        #         tw_pre = (
        #             collider[f"lhc{bim}"]
        #             .cycle("ip3")
        #             .twiss(
        #                 start=f"s.ds.l{arc[1]}.{bim}",
        #                 end=f"e.ds.r{arc[1]}.{bim}",
        #                 init=beta0,
        #                 method="4d",
        #                 reverse={"b1": False, "b2": True}[bim],
        #             )
        #         )
        #     else:
        #         tw_pre = collider[f"lhc{bim}"].twiss(
        #             start=f"s.ds.l{arc[1]}.{bim}",
        #             end=f"e.ds.r{arc[1]}.{bim}",
        #             init=beta0,
        #         )

        #     mux = (
        #         tw_pre["mux", f"e.ds.r{arc[1]}.{bim}"]
        #         - tw_pre["mux", f"s.ds.l{arc[1]}.{bim}"]
        #     )
        #     muy = (
        #         tw_pre["muy", f"e.ds.r{arc[1]}.{bim}"]
        #         - tw_pre["muy", f"s.ds.l{arc[1]}.{bim}"]
        #     )

        #     muxip_l = (
        #         tw_pre["mux", f"ip{arc[1]}"] - tw_pre["mux", f"s.ds.l{arc[1]}.{bim}"]
        #     )
        #     muyip_l = (
        #         tw_pre["muy", f"ip{arc[1]}"] - tw_pre["muy", f"s.ds.l{arc[1]}.{bim}"]
        #     )
        #     muxip_r = (
        #         tw_pre["mux", f"e.ds.r{arc[1]}.{bim}"] - tw_pre["mux", f"ip{arc[1]}"]
        #     )
        #     muyip_r = (
        #         tw_pre["muy", f"e.ds.r{arc[1]}.{bim}"] - tw_pre["muy", f"ip{arc[1]}"]
        #     )
        

    for ph in ["muxip1b1_l", "muxip1b1_r", "muxip5b1_l", "muxip5b1_r",
            "muxip2b1", "muxip4b1", "muxip6b1", "muxip8b1",
            "mux12b1", "mux45b1", "mux56b1", "mux81b1"]:
        if collider.varval[ph] < 0:
            collider.varval[ph] += tw['lhcb1'].qx      

    for ph in ["muyip1b1_l", "muyip1b1_r", "muyip5b1_l", "muyip5b1_r",
            "muyip2b1","muyip4b1","muyip6b1","muyip8b1",
            "muy12b1","muy45b1","muy56b1","muy81b1"]:
        if collider.varval[ph] < 0:
            collider.varval[ph] += tw['lhcb1'].qy

    for ph in ["muxip1b2_l", "muxip1b2_r", "muxip5b2_l", "muxip5b2_r",
            "muxip2b2", "muxip4b2", "muxip6b2", "muxip8b2",
            "mux12b2", "mux45b2", "mux56b2", "mux81b2"]:
        if collider.varval[ph] < 0:
            collider.varval[ph] += tw['lhcb2'].qx      

    for ph in ["muyip1b2_l", "muyip1b2_r", "muyip5b2_l", "muyip5b2_r",
            "muyip2b2","muyip4b2","muyip6b2","muyip8b2",
            "muy12b2","muy45b2","muy56b2","muy81b2"]:
        if collider.varval[ph] < 0:
            collider.varval[ph] += tw['lhcb2'].qy   
       
    (
    mux_ir2_target_b1,
    muy_ir2_target_b1,
    mux_ir4_target_b1,
    muy_ir4_target_b1,
    mux_ir6_target_b1,
    muy_ir6_target_b1,
    mux_ir8_target_b1,
    muy_ir8_target_b1,
    ) = compute_ats_phase_advances_for_auxiliary_irs(
        "lhcb1",
        tw_sq_a81_ip1_a12_b1,
        tw_sq_a45_ip5_a56_b1,
        collider.varval["muxip1b1_l"],
        collider.varval["muyip1b1_l"],
        collider.varval["muxip1b1_r"],
        collider.varval["muyip1b1_r"],
        collider.varval["muxip5b1_l"],
        collider.varval["muyip5b1_l"],
        collider.varval["muxip5b1_r"],
        collider.varval["muyip5b1_r"],
        collider.varval["muxip2b1"],
        collider.varval["muyip2b1"],
        collider.varval["muxip4b1"],
        collider.varval["muyip4b1"],
        collider.varval["muxip6b1"],
        collider.varval["muyip6b1"],
        collider.varval["muxip8b1"],
        collider.varval["muyip8b1"],
        collider.varval["mux12b1"],
        collider.varval["muy12b1"],
        collider.varval["mux45b1"],
        collider.varval["muy45b1"],
        collider.varval["mux56b1"],
        collider.varval["muy56b1"],
        collider.varval["mux81b1"],
        collider.varval["muy81b1"],
    )


    (
    mux_ir2_target_b2,
    muy_ir2_target_b2,
    mux_ir4_target_b2,
    muy_ir4_target_b2,
    mux_ir6_target_b2,
    muy_ir6_target_b2,
    mux_ir8_target_b2,
    muy_ir8_target_b2,
    ) = compute_ats_phase_advances_for_auxiliary_irs(
        "lhcb2",
        tw_sq_a81_ip1_a12_b2,
        tw_sq_a45_ip5_a56_b2,
        collider.varval["muxip1b2_l"],
        collider.varval["muyip1b2_l"],
        collider.varval["muxip1b2_r"],
        collider.varval["muyip1b2_r"],
        collider.varval["muxip5b2_l"],
        collider.varval["muyip5b2_l"],
        collider.varval["muxip5b2_r"],
        collider.varval["muyip5b2_r"],
        collider.varval["muxip2b2"],
        collider.varval["muyip2b2"],
        collider.varval["muxip4b2"],
        collider.varval["muyip4b2"],
        collider.varval["muxip6b2"],
        collider.varval["muyip6b2"],
        collider.varval["muxip8b2"],
        collider.varval["muyip8b2"],
        collider.varval["mux12b2"],
        collider.varval["muy12b2"],
        collider.varval["mux45b2"],
        collider.varval["muy45b2"],
        collider.varval["mux56b2"],
        collider.varval["muy56b2"],
        collider.varval["mux81b2"],
        collider.varval["muy81b2"],
    )


    return {
        'mux_ir2_target_b1': mux_ir2_target_b1,
        'muy_ir2_target_b1': muy_ir2_target_b1,
        'mux_ir4_target_b1': mux_ir4_target_b1,
        'muy_ir4_target_b1': muy_ir4_target_b1,
        'mux_ir6_target_b1': mux_ir6_target_b1,
        'muy_ir6_target_b1': muy_ir6_target_b1,
        'mux_ir8_target_b1': mux_ir8_target_b1,
        'muy_ir8_target_b1': muy_ir8_target_b1,
        'mux_ir2_target_b2': mux_ir2_target_b2,
        'muy_ir2_target_b2': muy_ir2_target_b2,
        'mux_ir4_target_b2': mux_ir4_target_b2,
        'muy_ir4_target_b2': muy_ir4_target_b2,
        'mux_ir6_target_b2': mux_ir6_target_b2,
        'muy_ir6_target_b2': muy_ir6_target_b2,
        'mux_ir8_target_b2': mux_ir8_target_b2,
        'muy_ir8_target_b2': muy_ir8_target_b2,
    }


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
    fixed_ip=False,
    solve=True,
    restore=True,
    assert_within_tol=True,
    default_tol=None,
):

    assert line_name in ["lhcb1", "lhcb2"]
    bn = line_name[-2:]

    fixed_optics_ip = {
        'b1':
        {
            'muxip6b1'  : 2.0000,
            'muyip6b1'  : 2.0300,
            'betxip6b1' : 187.297499,
            'betyip6b1' : 168.122917,
            'alfxip6b1' : -0.541994,
            'alfyip6b1' : 0.605891,
            'dxip6b1'   : 0.1400,
            'dpxip6b1'  : 0,
        },
        'b2':
        {
            'muxip6b2'  : 2.0000,
            'muyip6b2'  : 2.0300,
            'betxip6b2' : 187.749224,
            'betyip6b2' : 178.368556,
            'alfxip6b2' : 0.551968,
            'alfyip6b2' : -0.607183,
            'dxip6b2'   : 0.186,
            'dpxip6b2'  : -0.000256,
        },
    }

    if fixed_ip:
        alfx_ip6 = fixed_optics_ip[bn][f'alfxip6{bn}']
        alfy_ip6 = fixed_optics_ip[bn][f'alfyip6{bn}']
        betx_ip6 = fixed_optics_ip[bn][f'betxip6{bn}']
        bety_ip6 = fixed_optics_ip[bn][f'betyip6{bn}']
        dx_ip6   = fixed_optics_ip[bn][f'dxip6{bn}']
        dpx_ip6  = fixed_optics_ip[bn][f'dpxip6{bn}']
        mux_ir6  = fixed_optics_ip[bn][f'muxip6{bn}']
        muy_ir6  = fixed_optics_ip[bn][f'muyip6{bn}']


    opt = collider[f"lhc{bn}"].match(
        solve=False,
        restore_if_fail=restore,
        assert_within_tol=assert_within_tol,
        default_tol=default_tol,
        solver_options={"max_rel_penalty_increase": 2.0},
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
                tag="stage1",
            ),
            xt.Target(at="ip6", dx=dx_ip6, tag="dx_ip6"),
            xt.Target(at="ip6", dpx=dpx_ip6, tag="dpx_ip6"),
            xt.TargetSet(
                at=xt.END,
                tars=("betx", "bety", "alfx", "alfy", "dx", "dpx"),
                value=boundary_conditions_right,
            ),
            xt.TargetRelPhaseAdvance("mux", mux_ir6, weight=10),
            xt.TargetRelPhaseAdvance("muy", muy_ir6, weight=10),
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

    if solve:
        opt.solve()

    return opt


def new_ir7_strengths(collider, apply_all=True, apply_b1=False, apply_b2=False):
    # Addapted from https://gitlab.cern.ch/acc-models/acc-models-lhc/-/blob/hl19/strengths/ir7/re12c6b.str
    
    strs = {"b1":
        {
            "kqt4.l7" : 0.0012257364160585084,
            "kqt4.r7" : 0.0012659632628095638,
            "kqt13.l7b1" : -0.0048823483573787445,
            "kqt12.l7b1" : -0.004882279788343516,
            "kqtl11.l7b1" : 0.0027739663492968103,
            "kqtl10.l7b1" : 0.004623538857746193,
            "kqtl9.l7b1" : -0.003372747954072591,
            "kqtl8.l7b1" : -0.0023127417813640786,
            "kqtl7.l7b1" : -0.002011344510772721,
            "kq6.l7b1" : 0.0031173363410593766,
            "kq6.r7b1" : -0.0031388056161611565,
            "kqtl7.r7b1" : 0.0009532375359442739,
            "kqtl8.r7b1" : 0.002688438505728887,
            "kqtl9.r7b1" : 0.0033416607916765947,
            "kqtl10.r7b1" : -0.003461273410884878,
            "kqtl11.r7b1" : 0.0010531054411466265,
            "kqt12.r7b1" : -0.0027831205556483702,
            "kqt13.r7b1" : -0.0013509460856456692,
        },
        "b2":
        {
            "kqt13.l7b2" : -0.004192310485204978,
            "kqt12.l7b2" : -0.0035271197718106688,
            "kqtl11.l7b2" : 0.0008993274235722462,
            "kqtl10.l7b2" : -0.0035044843946580337,
            "kqtl9.l7b2" : 0.003295485018957867,
            "kqtl8.l7b2" : 0.002429071850457167,
            "kqtl7.l7b2" : 0.0008310840304967491,
            "kq6.l7b2" : -0.0031817725498278727,
            "kq6.r7b2" : 0.003183554427942885,
            "kqtl7.r7b2" : -0.0012886165853725183,
            "kqtl8.r7b2" : -0.0037917967174795034,
            "kqtl9.r7b2" : -0.0033703081873609005,
            "kqtl10.r7b2" : 0.0049711605825101994,
            "kqtl11.r7b2" : 0.002278252114016244,
            "kqt12.r7b2" : -0.0048808187874553495,
            "kqt13.r7b2" : -0.0048815559298144,   
        },
        "common":
        {
            "kqt4.l7": 0.0012257364160585084,
            "kqt4.r7": 0.0012659632628095638,
            "kq4.lr7": 0.0011653779946877393,
            "kq5.lr7": -0.001202569087048791,
        }
    }

    if apply_all:
        for n, k in strs["b1"].items():
            collider.vars[n] = k

        for n, k in strs["b2"].items():
            collider.vars[n] = k

        for n, k in strs["common"].items():
            collider.vars[n] = k
    elif apply_b1:
        for n, k in strs["b1"].items():
            collider.vars[n] = k
    elif apply_b2:
        for n, k in strs["b2"].items():
            collider.vars[n] = k
    
    return strs


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


def new_ir7_col_targets():
    tol = 1
    targets_b1 = [
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcp.d6l7.b1", betx=354.989, bety=298.968, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcp.c6l7.b1", betx=338.912, bety=319.528, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcp.b6l7.b1", betx=323.231, bety=340.798, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcapa.6l7.b1", betx=172.4, bety=633.496, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcapb.6l7.b1", betx=141.825, bety=724.005, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcsg.a6l7.b1", betx=95.3755, bety=902.617, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcpcv.a6l7.b1", betx=57.7261, bety=1117.76, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcapc.6l7.b1", betx=45.1717, bety=1220.65, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcsg.b5l7.b1", betx=60.1482, bety=787.091, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcsg.a5l7.b1", betx=70.8225, bety=700.973, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcsg.d4l7.b1", betx=141.475, bety=352.584, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcpch.a4l7.b1", betx=148.712, bety=327.456, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcsg.b4l7.b1", betx=99.5584, bety=265.589, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcspm.b4l7.b1", betx=98.3511, bety=266.417, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcsg.a4l7.b1", betx=97.232, bety=267.276, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcsg.a4r7.b1", betx=95.2585, bety=269.09, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcsg.b5r7.b1", betx=224.532, bety=198.217, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcsg.d5r7.b1", betx=348.338, bety=118.897, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcsg.e5r7.b1", betx=383.806, bety=102.739, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcspm.e5r7.b1", betx=402.217, bety=95.2115, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcsg.6r7.b1", betx=447.333, bety=46.8857, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcspm.6r7.b1", betx=431.439, bety=47.7367, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcla.a6r7.b1", betx=392.548, bety=50.6834, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcla.b6r7.b1", betx=197.929, bety=93.1682, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcla.c6r7.b1", betx=69.7591, bety=186.117, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcla.d6r7.b1", betx=64.7495, bety=193.264, tol=tol),
        xt.TargetSet(tag="collb1", line="lhcb1", at="tcla.a7r7.b1", betx=52.8241, bety=173.578, tol=tol),
    ]

    targets_b2 = [
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcla.a7l7.b2", betx=50.8888, bety=204.503, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcla.d6l7.b2", betx=57.3029, bety=234.07, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcla.c6l7.b2", betx=61.7668, bety=224.549, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcla.b6l7.b2", betx=180.304, bety=100.29, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcla.a6l7.b2", betx=365.046, bety=42.5421, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcspm.6l7.b2", betx=402.231, bety=38.3592, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcsg.6l7.b2", betx=417.444, bety=37.1186, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcspm.e5l7.b2", betx=394.864, bety=76.9155, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcsg.e5l7.b2", betx=377.268, bety=83.9082, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcsg.d5l7.b2", betx=343.339, bety=99.1051, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcsg.b5l7.b2", betx=224.499, bety=176.044, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcsg.a4l7.b2", betx=100.816, bety=290.332, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcsg.a4r7.b2", betx=109.27, bety=289.687, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcspm.b4r7.b2", betx=110.696, bety=289.731, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcsg.b4r7.b2", betx=112.203, bety=289.802, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcspm.d4r7.b2", betx=158.873, bety=389.812, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcsg.d4r7.b2", betx=152.848, bety=412.296, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcpch.a5r7.b2", betx=80.6815, bety=785.078, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcsg.a5r7.b2", betx=74.8885, bety=829.398, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcsg.b5r7.b2", betx=62.8386, bety=934.524, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcapc.6r7.b2", betx=41.5991, bety=1523.45, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcpcv.a6r7.b2", betx=56.1439, bety=1382.88, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcsg.a6r7.b2", betx=92.0841, bety=1142.15, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcapb.6r7.b2", betx=144.915, bety=905.764, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcapa.6r7.b2", betx=173.042, bety=809.277, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcp.b6r7.b2", betx=337.187, bety=438.701, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcp.c6r7.b2", betx=354.083, bety=412.116, tol=tol),
        xt.TargetSet(tag="collb2", line="lhcb2", at="tcp.d6r7.b2", betx=371.415, bety=386.38, tol=tol),
    ]

    return targets_b1, targets_b2


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


def rematch_new_ir7_both(
    collider,
    boundary_conditions_left,
    boundary_conditions_right,
    mux_ir7_b1,
    muy_ir7_b1,
    mux_ir7_b2,
    muy_ir7_b2,
    solve=True,
    restore=True,
    assert_within_tol=True,
    default_tol=None,
    collimator_targets=False,
):

    if collimator_targets:
        coll_targets = new_ir7_col_targets()
    else:
        coll_targets = [[], []]

    opt = collider.match(
        solve=False,
        restore_if_fail=restore,
        assert_within_tol=assert_within_tol,
        default_tol=default_tol,
        solver_options={"n_bisections": 3, "min_step": 1e-7},
        start=["s.ds.l7.b1", "s.ds.l7.b2"],
        end=["e.ds.r7.b1", "e.ds.r7.b2"],
        init=[
            boundary_conditions_left["lhcb1"]["67"],
            boundary_conditions_left["lhcb2"]["67"],
        ],
        init_at=[xt.START, xt.START],
        targets=[
            xt.TargetSet(
                line="lhcb1",
                at="ip7",
                alfx=new_ir7_optics["b1"]["alfx"],
                alfy=new_ir7_optics["b1"]["alfy"],
                betx=new_ir7_optics["b1"]["betx"],
                bety=new_ir7_optics["b1"]["bety"],
                dx=new_ir7_optics["b1"]["dx"],
                dpx=new_ir7_optics["b1"]["dpx"],
                tag="ip7_b1",
            ),
            xt.TargetSet(
                line="lhcb1",
                at="ip7",
                mux=new_ir7_optics["b1"]["mux"] + boundary_conditions_left["lhcb1"]["67"].mux[-1],
                muy=new_ir7_optics["b1"]["muy"] + boundary_conditions_left["lhcb1"]["67"].muy[-1],
                tag='ip7_b1_mu',
            ),
            xt.TargetSet(
                line="lhcb2",
                at="ip7",
                alfx=new_ir7_optics["b2"]["alfx"],
                alfy=new_ir7_optics["b2"]["alfy"],
                betx=new_ir7_optics["b2"]["betx"],
                bety=new_ir7_optics["b2"]["bety"],
                dx=new_ir7_optics["b2"]["dx"],
                dpx=new_ir7_optics["b2"]["dpx"],
                tag="ip7_b2",
            ),
            xt.TargetSet(
                line="lhcb2",
                at="ip7",
                mux=new_ir7_optics["b2"]["mux"] + boundary_conditions_left["lhcb2"]["67"].mux[-1],
                muy=new_ir7_optics["b2"]["muy"] + boundary_conditions_left["lhcb2"]["67"].muy[-1],
                tag='ip7_b2_mu',
            ),
            xt.TargetSet(
                line="lhcb1",
                at=xt.END,
                tars=("betx", "bety", "alfx", "alfy", "dx", "dpx"),
                value=boundary_conditions_right["lhcb1"]["78"],
            ),
            xt.TargetSet(
                line="lhcb2",
                at=xt.END,
                tars=("betx", "bety", "alfx", "alfy", "dx", "dpx"),
                value=boundary_conditions_right["lhcb2"]["78"],
            ),
            xt.TargetSet(
                line="lhcb1",
                at="e.ds.r7.b1",
                mux=mux_ir7_b1+boundary_conditions_left["lhcb1"]["67"]['mux', 's.ds.l7.b1'],
                muy=muy_ir7_b1+boundary_conditions_left["lhcb1"]["67"]['muy', 's.ds.l7.b1'],
            ),
            xt.TargetSet(
                line="lhcb2",
                at="e.ds.r7.b2",
                mux=mux_ir7_b2+boundary_conditions_left["lhcb2"]["67"]['mux', 's.ds.l7.b2'],
                muy=muy_ir7_b2+boundary_conditions_left["lhcb2"]["67"]['muy', 's.ds.l7.b2'],
            ),
        ] + coll_targets[0] + coll_targets[1],
        vary=[
            xt.VaryList(
                [
                    "kqt13.l7b1",
                    "kqt12.l7b1",
                    "kqtl11.l7b1",
                    "kqtl10.l7b1",
                    "kqtl9.l7b1",
                    "kqtl8.l7b1",
                    "kqtl7.l7b1",
                    "kq6.l7b1",
                    "kq6.r7b1",
                    "kqtl7.r7b1",
                    "kqtl8.r7b1",
                    "kqtl9.r7b1",
                    "kqtl10.r7b1",
                    "kqtl11.r7b1",
                    "kqt12.r7b1",
                    "kqt13.r7b1",
                ],
                tag="quads_b1",
            ),
            xt.VaryList(
                [
                    "kqt13.l7b2",
                    "kqt12.l7b2",
                    "kqtl11.l7b2",
                    "kqtl10.l7b2",
                    "kqtl9.l7b2",
                    "kqtl8.l7b2",
                    "kqtl7.l7b2",
                    "kq6.l7b2",
                    "kq6.r7b2",
                    "kqtl7.r7b2",
                    "kqtl8.r7b2",
                    "kqtl9.r7b2",
                    "kqtl10.r7b2",
                    "kqtl11.r7b2",
                    "kqt12.r7b2",
                    "kqt13.r7b2",
                ],
                tag="quads_b2",
            ),
            xt.Vary("kq4.lr7", tag="common"),
            xt.Vary("kq5.lr7", tag="common"),
            xt.Vary("kqt4.l7", tag="common"),
            xt.Vary("kqt4.r7", tag="common"),
        ],
    )

    opt.disable_targets(tag=["ip7_b1_mu", "ip7_b2_mu"])

    if solve:
        opt.solve()

    return opt
