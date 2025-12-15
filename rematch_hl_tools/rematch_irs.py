import xtrack as xt
from xtrack._temp.lhc_match import get_arc_periodic_solution, compute_ats_phase_advances_for_auxiliary_irs
from .rematch_ir15 import get_presqueezed_tw
import numpy as np


def get_tw_ip(collider, ip, zero_phase=True, strengths=False):
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
        strengths=strengths,
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

        # HACK: to get around the phases
        if v[f"muxip8{bim}_r"] < 0:
            v[f"muxip8{bim}_r"] = np.mod(v[f"muxip8{bim}_r"], tw[f'lhc{bim}'].qx)

        if v[f"muyip8{bim}_r"] < 0:
            v[f"muyip8{bim}_r"] = np.mod(v[f"muyip8{bim}_r"], tw[f'lhc{bim}'].qy)

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