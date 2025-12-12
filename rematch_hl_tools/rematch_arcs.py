import xtrack as xt
from xtrack._temp.lhc_match import (
    ARC_NAMES,
    ActionArcPhaseAdvanceFromCell,
    propagate_optics_from_beta_star,
    get_arc_periodic_solution,
)

from .rematch_irs import get_presqueezed_tw

def rephase_arc_trim():
    pass


def rephase_arc(collider):
    pass


def rebal_arc_trim(
    collider,
    target_mux_b1:float,
    target_muy_b1:float,
    target_mux_b2:float,
    target_muy_b2:float,
    arc_name:str,
    default_tol,
    solve=False,
):
    assert collider.lhcb1.twiss_default.get("reverse", False) is False
    assert collider.lhcb2.twiss_default["reverse"] is True

    assert arc_name in ARC_NAMES

    action_phase_b1 = ActionArcPhaseAdvanceFromCell(
        collider=collider, line_name="lhcb1", arc_name=arc_name
    )
    action_phase_b2 = ActionArcPhaseAdvanceFromCell(
        collider=collider, line_name="lhcb2", arc_name=arc_name
    )

    collider.vars[f"kqtf.a{arc_name}b1"] = -collider.vars[f"kqtf.a{arc_name}b2"]
    collider.vars[f"kqtd.a{arc_name}b1"] = -collider.vars[f"kqtd.a{arc_name}b2"]

    opt = collider.match(
        solve=False,
        default_tol=default_tol,
        targets=[
            action_phase_b1.target("mux", target_mux_b1),
            action_phase_b1.target("muy", target_muy_b1),
            action_phase_b2.target("mux", target_mux_b2),
            action_phase_b2.target("muy", target_muy_b2),
        ],
        vary=[
            xt.VaryList(
                [
                    f"kqtf.a{arc_name}b2",
                    f"kqtd.a{arc_name}b2",
                    f"kqf.a{arc_name}",
                    f"kqd.a{arc_name}",
                ]
            ),
        ],
    )

    if solve:
        opt.solve()

    return opt


def ats_phase_aux_ir(collider, nir1:int, nir2:int, nir3:int, line_name:str, betx:float, bety:float):
    assert line_name in ['lhcb1', 'lhcb2']
    bn = line_name[-2:]

    tw_aux = propagate_optics_from_beta_star(
        collider,
        ip_name=f"ip{nir2}",
        line_name=f"lhc{bn}",
        start=f"s.ds.r{nir1}.{bn}",
        end=f"e.ds.l{nir3}.{bn}",
        beta_star_x=betx,
        beta_star_y=bety,
    )
    tw = collider[line_name].twiss()
    tw_ip = get_presqueezed_tw(collider, nir2)
    arc_left = f'{nir1}{nir2}'
    arc_right = f'{nir2}{nir3}'
    tw_arcs = get_arc_periodic_solution(collider=collider, line_name=[line_name], arc_name=[arc_left, arc_right])

    mux_arcleft = tw_arcs[line_name][arc_left].mux[-1]
    muy_arcleft = tw_arcs[line_name][arc_left].muy[-1]
    mux_arcright = tw_arcs[line_name][arc_right].mux[-1]
    muy_arcright = tw_arcs[line_name][arc_right].muy[-1]


    muxip_l = tw_ip[line_name]["mux", f"ip{nir2}"] - tw_ip[line_name]["mux", f"s.ds.l{nir2}.{bn}"]
    muyip_l = tw_ip[line_name]["muy", f"ip{nir2}"] - tw_ip[line_name]["muy", f"s.ds.l{nir2}.{bn}"]
    muxip_r = tw_ip[line_name]["mux", f"e.ds.r{nir2}.{bn}"] - tw_ip[line_name]["mux", f"ip{nir2}"]
    muyip_r = tw_ip[line_name]["muy", f"e.ds.r{nir2}.{bn}"] - tw_ip[line_name]["muy", f"ip{nir2}"]

    mux_ipright = (
            tw["mux", f"e.ds.r{nir3}.{bn}"]
            - tw["mux", f"ip{nir2}"]
            - muxip_r
            - tw_arcs[line_name][arc_right].mux[-1]
        )
    muy_ipright = (
            tw["muy", f"e.ds.r{nir3}.{bn}"]
            - tw["muy", f"ip{nir2}"]
            - muyip_r
            - tw_arcs[line_name][arc_right].muy[-1]
        )
    
    mux_ipleft = (
            tw["mux", f"ip{nir2}"]
            - tw["mux", f"s.ds.l{nir1}.{bn}"]
            - muxip_l
            - tw_arcs[line_name][arc_left].mux[-1]
        )
    muy_ipleft = (
            tw["muy", f"ip{nir2}"]
            - tw["muy", f"s.ds.l{nir1}.{bn}"]
            - muyip_l
            - tw_arcs[line_name][arc_left].muy[-1]
        )


    mux_compensate_ir_right = (tw_aux['mux', f's.ds.l{nir3}.{bn}'] - tw_aux['mux', f'ip{nir2}']
                          - muxip_r - mux_arcright)
    mux_ir_right_target = mux_ipright - mux_compensate_ir_right
    muy_compensate_ir_right = (tw_aux['muy', f's.ds.l{nir3}.{bn}'] - tw_aux['muy', f'ip{nir2}']
                          - muyip_r - muy_arcright)
    muy_ir_right_target = muy_ipright - muy_compensate_ir_right


    ip = f'ip{nir2}'
    if nir2 == 1:
        ip = f'ip{nir2}.l1'
    mux_compensate_ir_left = (tw_aux['mux', ip] - tw_aux['mux', f'e.ds.r{nir1}.{bn}']
                          - muxip_l - mux_arcleft)
    mux_ir_left_target = mux_ipleft - mux_compensate_ir_left
    muy_compensate_ir_left = (tw_aux['muy', ip] - tw_aux['muy', f'e.ds.r{nir1}.{bn}']
                          - muyip_l - muy_arcleft)
    muy_ir_left_target = muy_ipleft - muy_compensate_ir_left

    if mux_ir_right_target < 0:
        mux_ir_right_target += tw.qx
    if muy_ir_right_target < 0:
        muy_ir_right_target += tw.qy

    if mux_ir_left_target < 0:
        mux_ir_left_target += tw.qx
    if muy_ir_left_target < 0:
        muy_ir_left_target += tw.qy
    
    res = {f'mux_ir{nir3}_{bn}': mux_ir_right_target,
           f'muy_ir{nir3}_{bn}': muy_ir_right_target,
           f'mux_ir{nir1}_{bn}': mux_ir_left_target,
           f'muy_ir{nir1}_{bn}': muy_ir_left_target}

    return res
