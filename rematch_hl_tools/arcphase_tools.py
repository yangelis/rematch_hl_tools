from xtrack._temp.lhc_match import get_arc_periodic_solution, propagate_optics_from_beta_star
from xtrack._temp.lhc_match import rematch_ir8, rematch_ir2, rematch_ir3, rematch_ir4
from .rematch_arcs import rebal_arc_trim, ats_phase_aux_ir
from .rematch_irs import rematch_new_ir7_both, rematch_ir6
from .mk_arc_trims import mk_arc_trims
from .rematch_tune_chroma import rematch_tune_non_ats, rematch_chroma


def rephase_arc_a23_a78(collider, betx, bety, dmux_b1, dmuy_b1, dmux_b2, dmuy_b2, default_tol=None):
    optimizers = {}

    tw = collider.twiss()

    tw_non_ats_arcs = get_arc_periodic_solution(collider, arc_name=["23", "34", "67", "78"])

    optimizers["a78"] = rebal_arc_trim(
        collider,
        target_mux_b1=tw_non_ats_arcs["lhcb1"]["78"].mux[-1] - (tw.lhcb1.qx - 62.31) + dmux_b1,
        target_muy_b1=tw_non_ats_arcs["lhcb1"]["78"].muy[-1] - (tw.lhcb1.qy - 60.32) + dmuy_b1,
        target_mux_b2=tw_non_ats_arcs["lhcb2"]["78"].mux[-1] - (tw.lhcb2.qx - 62.31) + dmux_b2,
        target_muy_b2=tw_non_ats_arcs["lhcb2"]["78"].muy[-1] - (tw.lhcb2.qy - 60.32) + dmuy_b2,
        arc_name="78",
        default_tol=default_tol,
    )

    optimizers["a23"] = rebal_arc_trim(
        collider,
        target_mux_b1=tw_non_ats_arcs["lhcb1"]["23"].mux[-1] - (tw.lhcb1.qx - 62.31) - dmux_b1,
        target_muy_b1=tw_non_ats_arcs["lhcb1"]["23"].muy[-1] - (tw.lhcb1.qy - 60.32) - dmuy_b1,
        target_mux_b2=tw_non_ats_arcs["lhcb2"]["23"].mux[-1] - (tw.lhcb2.qx - 62.31) - dmux_b2,
        target_muy_b2=tw_non_ats_arcs["lhcb2"]["23"].muy[-1] - (tw.lhcb2.qy - 60.32) - dmuy_b2,
        arc_name="23",
        default_tol=default_tol,
    )

    optimizers["a78"].solve()
    optimizers["a23"].solve()

    collider.vars["kqtf.a78b1"] = collider.varval["kqtf.a78b1"]
    collider.vars["kqtd.a78b1"] = collider.varval["kqtd.a78b1"]

    collider.vars["kqtf.a23b1"] = collider.varval["kqtf.a23b1"]
    collider.vars["kqtd.a23b1"] = collider.varval["kqtd.a23b1"]

    tw_sq_a81_ip1_a12_b1 = propagate_optics_from_beta_star(
        collider,
        ip_name="ip1",
        line_name="lhcb1",
        start="s.ds.r8.b1",
        end="e.ds.l2.b1",
        beta_star_x=betx,
        beta_star_y=bety,
    )

    tw_sq_a81_ip1_a12_b2 = propagate_optics_from_beta_star(
        collider,
        ip_name="ip1",
        line_name="lhcb2",
        start="s.ds.r8.b2",
        end="e.ds.l2.b2",
        beta_star_x=betx,
        beta_star_y=bety,
    )

    mu_tar_b1 = ats_phase_aux_ir(collider, 8, 1, 2, line_name="lhcb1", betx=betx, bety=bety)
    mu_tar_b2 = ats_phase_aux_ir(collider, 8, 1, 2, line_name="lhcb2", betx=betx, bety=bety)

    tw_non_ats_arcs_v2 = get_arc_periodic_solution(collider, arc_name=["23", "34", "67", "78"])
    
    optimizers["ir7"] = rematch_new_ir7_both(
        collider=collider,
        boundary_conditions_left=tw_non_ats_arcs_v2,
        boundary_conditions_right=tw_non_ats_arcs_v2,
        mux_ir7_b1=collider.varval["muxip7b1"],
        muy_ir7_b1=collider.varval["muyip7b1"],
        mux_ir7_b2=collider.varval["muxip7b2"],
        muy_ir7_b2=collider.varval["muyip7b2"],
        solve=False,
        restore=False,
        assert_within_tol=False,
        default_tol=default_tol,
    )
    optimizers["ir7"].disable_targets(tag=["collb1", "collb2"])
    optimizers["ir7"].solve()
   
    optimizers["ir8b1"] = rematch_ir8(
        collider,
        line_name="lhcb1",
        boundary_conditions_left=tw_non_ats_arcs_v2["lhcb1"]["78"],
        boundary_conditions_right=tw_sq_a81_ip1_a12_b1,
        solve=True,
        mux_ir8=mu_tar_b1["mux_ir8_b1"],
        muy_ir8=mu_tar_b1["muy_ir8_b1"],
        alfx_ip8=collider.varval["alfxip8b1"],
        alfy_ip8=collider.varval["alfyip8b1"],
        betx_ip8=collider.varval["betxip8b1"],
        bety_ip8=collider.varval["betyip8b1"],
        dx_ip8=collider.varval["dxip8b1"],
        dpx_ip8=collider.varval["dpxip8b1"],
        staged_match=True,
        default_tol=default_tol,
    )

    optimizers["ir8b2"] = rematch_ir8(
        collider,
        line_name="lhcb2",
        boundary_conditions_left=tw_non_ats_arcs_v2["lhcb2"]["78"],
        boundary_conditions_right=tw_sq_a81_ip1_a12_b2,
        solve=True,
        mux_ir8=mu_tar_b2["mux_ir8_b2"],
        muy_ir8=mu_tar_b2["muy_ir8_b2"],
        alfx_ip8=collider.varval["alfxip8b2"],
        alfy_ip8=collider.varval["alfyip8b2"],
        betx_ip8=collider.varval["betxip8b2"],
        bety_ip8=collider.varval["betyip8b2"],
        dx_ip8=collider.varval["dxip8b2"],
        dpx_ip8=collider.varval["dpxip8b2"],
        staged_match=True,
        default_tol=default_tol,
    )

    optimizers["ir2b1"] = rematch_ir2(
        collider,
        line_name="lhcb1",
        boundary_conditions_left=tw_sq_a81_ip1_a12_b1,
        boundary_conditions_right=tw_non_ats_arcs_v2["lhcb1"]["23"],
        mux_ir2=mu_tar_b1["mux_ir2_b1"],
        muy_ir2=mu_tar_b1["muy_ir2_b1"],
        betx_ip2=collider.varval["betxip2b1"],
        bety_ip2=collider.varval["betyip2b1"],
        solve=True,
        staged_match=True,
        default_tol=default_tol,
    )

    optimizers["ir2b2"] = rematch_ir2(
        collider,
        line_name="lhcb2",
        boundary_conditions_left=tw_sq_a81_ip1_a12_b2,
        boundary_conditions_right=tw_non_ats_arcs_v2["lhcb2"]["23"],
        mux_ir2=mu_tar_b2["mux_ir2_b2"],
        muy_ir2=mu_tar_b2["muy_ir2_b2"],
        betx_ip2=collider.varval["betxip2b2"],
        bety_ip2=collider.varval["betyip2b2"],
        solve=True,
        staged_match=True,
        default_tol=default_tol,
    )
   
    for bim in ["b1", "b2"]:
        optimizers[f"ir3{bim}"] = rematch_ir3(
            collider=collider,
            line_name=f"lhc{bim}",
            boundary_conditions_left=tw_non_ats_arcs_v2[f"lhc{bim}"]["23"],
            boundary_conditions_right=tw_non_ats_arcs_v2[f"lhc{bim}"]["34"],
            mux_ir3=collider.varval[f"muxip3{bim}"],
            muy_ir3=collider.varval[f"muyip3{bim}"],
            alfx_ip3=collider.varval[f"alfxip3{bim}"],
            alfy_ip3=collider.varval[f"alfyip3{bim}"],
            betx_ip3=collider.varval[f"betxip3{bim}"],
            bety_ip3=collider.varval[f"betyip3{bim}"],
            dx_ip3=collider.varval[f"dxip3{bim}"],
            dpx_ip3=collider.varval[f"dpxip3{bim}"],
            solve=True,
            staged_match=True,
            default_tol=default_tol,
        )

    optimizers["tune"] = rematch_tune_non_ats(collider, default_targets=True, solve=True)
    optimizers["chroma"] = rematch_chroma(collider, default_targets=True, solve=True)

    mk_arc_trims(collider)
    
    collider.vars["kqtf.b1"] = 0
    collider.vars["kqtd.b1"] = 0
    collider.vars["kqtf.b2"] = 0
    collider.vars["kqtd.b2"] = 0

    collider.vars["ksf.b1"] = 0
    collider.vars["ksd.b1"] = 0
    collider.vars["ksf.b2"] = 0
    collider.vars["ksd.b2"] = 0

    return optimizers



def rephase_arc_a34_a67(collider, betx, bety, dmux_b1, dmuy_b1, dmux_b2, dmuy_b2, default_tol=None):
    optimizers = {}

    tw = collider.twiss()

    tw_non_ats_arcs = get_arc_periodic_solution(collider, arc_name=["23", "34", "67", "78"])

    optimizers["a67"] = rebal_arc_trim(
        collider,
        target_mux_b1=tw_non_ats_arcs["lhcb1"]["67"].mux[-1] - (tw.lhcb1.qx - 62.31) + dmux_b1,
        target_muy_b1=tw_non_ats_arcs["lhcb1"]["67"].muy[-1] - (tw.lhcb1.qy - 60.32) + dmuy_b1,
        target_mux_b2=tw_non_ats_arcs["lhcb2"]["67"].mux[-1] - (tw.lhcb2.qx - 62.31) + dmux_b2,
        target_muy_b2=tw_non_ats_arcs["lhcb2"]["67"].muy[-1] - (tw.lhcb2.qy - 60.32) + dmuy_b2,
        arc_name="67",
        default_tol=default_tol,
    )

    optimizers["a34"] = rebal_arc_trim(
        collider,
        target_mux_b1=tw_non_ats_arcs["lhcb1"]["34"].mux[-1] - (tw.lhcb1.qx - 62.31) - dmux_b1,
        target_muy_b1=tw_non_ats_arcs["lhcb1"]["34"].muy[-1] - (tw.lhcb1.qy - 60.32) - dmuy_b1,
        target_mux_b2=tw_non_ats_arcs["lhcb2"]["34"].mux[-1] - (tw.lhcb2.qx - 62.31) - dmux_b2,
        target_muy_b2=tw_non_ats_arcs["lhcb2"]["34"].muy[-1] - (tw.lhcb2.qy - 60.32) - dmuy_b2,
        arc_name="34",
        default_tol=default_tol,
    )

    optimizers["a67"].solve()
    optimizers["a34"].solve()

    collider.vars["kqtf.a67b1"] = collider.varval["kqtf.a67b1"]
    collider.vars["kqtd.a67b1"] = collider.varval["kqtd.a67b1"]

    collider.vars["kqtf.a34b1"] = collider.varval["kqtf.a34b1"]
    collider.vars["kqtd.a34b1"] = collider.varval["kqtd.a34b1"]

   
    tw_sq_a45_ip5_a56_b1 = propagate_optics_from_beta_star(
        collider,
        ip_name="ip5",
        line_name="lhcb1",
        start="s.ds.r4.b1",
        end="e.ds.l6.b1",
        beta_star_x=bety,
        beta_star_y=bety,
    )

    tw_sq_a45_ip5_a56_b2 = propagate_optics_from_beta_star(
        collider,
        ip_name="ip5",
        line_name="lhcb2",
        start="s.ds.r4.b2",
        end="e.ds.l6.b2",
        beta_star_x=betx,
        beta_star_y=bety,
    )

    mu_tar_b1 = ats_phase_aux_ir(collider, 4, 5, 6, line_name="lhcb1", betx=betx, bety=bety)
    mu_tar_b2 = ats_phase_aux_ir(collider, 4, 5, 6, line_name="lhcb2", betx=betx, bety=bety)

    tw_non_ats_arcs_v2 = get_arc_periodic_solution(collider, arc_name=["23", "34", "67", "78"])
    
    optimizers["ir7"] = rematch_new_ir7_both(
        collider=collider,
        boundary_conditions_left=tw_non_ats_arcs_v2,
        boundary_conditions_right=tw_non_ats_arcs_v2,
        mux_ir7_b1=collider.varval["muxip7b1"],
        muy_ir7_b1=collider.varval["muyip7b1"],
        mux_ir7_b2=collider.varval["muxip7b2"],
        muy_ir7_b2=collider.varval["muyip7b2"],
        solve=False,
        restore=False,
        assert_within_tol=False,
        default_tol=default_tol,
    )
    optimizers["ir7"].disable_targets(tag=["collb1", "collb2"])
    optimizers["ir7"].solve()
   
    optimizers["ir6b1"] = rematch_ir6(
        restore=False,
        assert_within_tol=False,
        collider=collider,
        line_name="lhcb1",
        boundary_conditions_left=tw_sq_a45_ip5_a56_b1,
        boundary_conditions_right=tw_non_ats_arcs["lhcb1"]["67"],
        mux_ir6=mu_tar_b1["mux_ir6_b1"],
        muy_ir6=mu_tar_b1["muy_ir6_b1"],
        alfx_ip6=collider.varval["alfxip6b1"],
        alfy_ip6=collider.varval["alfyip6b1"],
        betx_ip6=collider.varval["betxip6b1"],
        bety_ip6=collider.varval["betyip6b1"],
        dx_ip6=collider.varval["dxip6b1"],
        dpx_ip6=collider.varval["dpxip6b1"],
        solve=False,
        match_dx=True,
        match_dpx=True,
        default_tol=default_tol,
    )
    optimizers["ir6b1"].solve()

    optimizers["ir6b1"].disable_targets(tag=["dx_ip6", "dpx_ip6"])
    optimizers["ir6b1"].solve()

    optimizers["ir6b2"] = rematch_ir6(
        restore=False,
        assert_within_tol=False,
        collider=collider,
        line_name="lhcb2",
        boundary_conditions_left=tw_sq_a45_ip5_a56_b2,
        boundary_conditions_right=tw_non_ats_arcs["lhcb2"]["67"],
        mux_ir6=mu_tar_b2["mux_ir6_b2"],
        muy_ir6=mu_tar_b2["muy_ir6_b2"],
        alfx_ip6=collider.varval["alfxip6b2"],
        alfy_ip6=collider.varval["alfyip6b2"],
        betx_ip6=collider.varval["betxip6b2"],
        bety_ip6=collider.varval["betyip6b2"],
        dx_ip6=collider.varval["dxip6b2"],
        dpx_ip6=collider.varval["dpxip6b2"],
        solve=False,
        match_dx=True,
        match_dpx=True,
        default_tol=default_tol,
    )
    optimizers["ir6b2"].solve()
    optimizers["ir6b2"].disable_targets(tag=["dx_ip6", "dpx_ip6"])
    optimizers["ir6b2"].solve()


    for bim in ["b1", "b2"]:
        optimizers[f"ir3{bim}"] = rematch_ir3(
            collider=collider,
            line_name=f"lhc{bim}",
            boundary_conditions_left=tw_non_ats_arcs_v2[f"lhc{bim}"]["23"],
            boundary_conditions_right=tw_non_ats_arcs_v2[f"lhc{bim}"]["34"],
            mux_ir3=collider.varval[f"muxip3{bim}"],
            muy_ir3=collider.varval[f"muyip3{bim}"],
            alfx_ip3=collider.varval[f"alfxip3{bim}"],
            alfy_ip3=collider.varval[f"alfyip3{bim}"],
            betx_ip3=collider.varval[f"betxip3{bim}"],
            bety_ip3=collider.varval[f"betyip3{bim}"],
            dx_ip3=collider.varval[f"dxip3{bim}"],
            dpx_ip3=collider.varval[f"dpxip3{bim}"],
            solve=True,
            staged_match=True,
            default_tol=default_tol,
        )
   
    optimizers["ir4b1"] = rematch_ir4(
        collider=collider,
        line_name="lhcb1",
        boundary_conditions_left=tw_non_ats_arcs["lhcb1"]["34"],
        boundary_conditions_right=tw_sq_a45_ip5_a56_b1,
        mux_ir4=mu_tar_b1["mux_ir4_b1"],
        muy_ir4=mu_tar_b1["muy_ir4_b1"],
        alfx_ip4=collider.varval["alfxip4b1"],
        alfy_ip4=collider.varval["alfyip4b1"],
        betx_ip4=collider.varval["betxip4b1"],
        bety_ip4=collider.varval["betyip4b1"],
        dx_ip4=collider.varval["dxip4b1"],
        dpx_ip4=collider.varval["dpxip4b1"],
        solve=True,
        staged_match=True,
        default_tol=default_tol,
    )

    optimizers["ir4b2"] = rematch_ir4(
        collider=collider,
        line_name="lhcb2",
        boundary_conditions_left=tw_non_ats_arcs["lhcb2"]["34"],
        boundary_conditions_right=tw_sq_a45_ip5_a56_b2,
        mux_ir4=mu_tar_b2["mux_ir4_b2"],
        muy_ir4=mu_tar_b2["muy_ir4_b2"],
        alfx_ip4=collider.varval["alfxip4b2"],
        alfy_ip4=collider.varval["alfyip4b2"],
        betx_ip4=collider.varval["betxip4b2"],
        bety_ip4=collider.varval["betyip4b2"],
        dx_ip4=collider.varval["dxip4b2"],
        dpx_ip4=collider.varval["dpxip4b2"],
        solve=True,
        staged_match=True,
        default_tol=default_tol,
    )

    optimizers["tune"] = rematch_tune_non_ats(collider, default_targets=True, solve=True)
    optimizers["chroma"] = rematch_chroma(collider, default_targets=True, solve=True)

    mk_arc_trims(collider)
    
    collider.vars["kqtf.b1"] = 0
    collider.vars["kqtd.b1"] = 0
    collider.vars["kqtf.b2"] = 0
    collider.vars["kqtd.b2"] = 0

    collider.vars["ksf.b1"] = 0
    collider.vars["ksd.b1"] = 0
    collider.vars["ksf.b2"] = 0
    collider.vars["ksd.b2"] = 0

    return optimizers


def rephase_arc_a67_a78(collider, betx, bety, dmux_b1, dmuy_b1, dmux_b2, dmuy_b2, default_tol=None, tune_chroma=False):
    optimizers = {}

    tw = collider.twiss()

    tw_non_ats_arcs = get_arc_periodic_solution(collider, arc_name=["23", "34", "67", "78"])

    optimizers["a67"] = rebal_arc_trim(
        collider,
        target_mux_b1=tw_non_ats_arcs["lhcb1"]["67"].mux[-1] - (tw.lhcb1.qx - 62.31) + dmux_b1,
        target_muy_b1=tw_non_ats_arcs["lhcb1"]["67"].muy[-1] - (tw.lhcb1.qy - 60.32) + dmuy_b1,
        target_mux_b2=tw_non_ats_arcs["lhcb2"]["67"].mux[-1] - (tw.lhcb2.qx - 62.31) + dmux_b2,
        target_muy_b2=tw_non_ats_arcs["lhcb2"]["67"].muy[-1] - (tw.lhcb2.qy - 60.32) + dmuy_b2,
        arc_name="67",
        default_tol=default_tol,
    )

    print('Arc 67')
    optimizers["a67"].solve()
    collider.vars["kqtf.a67b1"] = collider.varval["kqtf.a67b1"]
    collider.vars["kqtd.a67b1"] = collider.varval["kqtd.a67b1"]


    optimizers["a78"] = rebal_arc_trim(
        collider,
        target_mux_b1=tw_non_ats_arcs["lhcb1"]["78"].mux[-1] - (tw.lhcb1.qx - 62.31) - dmux_b1,
        target_muy_b1=tw_non_ats_arcs["lhcb1"]["78"].muy[-1] - (tw.lhcb1.qy - 60.32) - dmuy_b1,
        target_mux_b2=tw_non_ats_arcs["lhcb2"]["78"].mux[-1] - (tw.lhcb2.qx - 62.31) - dmux_b2,
        target_muy_b2=tw_non_ats_arcs["lhcb2"]["78"].muy[-1] - (tw.lhcb2.qy - 60.32) - dmuy_b2,
        arc_name="78",
        default_tol=default_tol,
    )

    print('Arc 78')
    optimizers["a78"].solve()
    collider.vars["kqtf.a78b1"] = collider.varval["kqtf.a78b1"]
    collider.vars["kqtd.a78b1"] = collider.varval["kqtd.a78b1"]


   
    tw_sq_a45_ip5_a56_b1 = propagate_optics_from_beta_star(
        collider,
        ip_name="ip5",
        line_name="lhcb1",
        start="s.ds.r4.b1",
        end="e.ds.l6.b1",
        beta_star_x=betx,
        beta_star_y=bety,
    )

    tw_sq_a45_ip5_a56_b2 = propagate_optics_from_beta_star(
        collider,
        ip_name="ip5",
        line_name="lhcb2",
        start="s.ds.r4.b2",
        end="e.ds.l6.b2",
        beta_star_x=betx,
        beta_star_y=bety,
    )

    tw_sq_a81_ip1_a12_b1 = propagate_optics_from_beta_star(
        collider,
        ip_name="ip1",
        line_name="lhcb1",
        start="s.ds.r8.b1",
        end="e.ds.l2.b1",
        beta_star_x=betx,
        beta_star_y=bety,
    )

    tw_sq_a81_ip1_a12_b2 = propagate_optics_from_beta_star(
        collider,
        ip_name="ip1",
        line_name="lhcb2",
        start="s.ds.r8.b2",
        end="e.ds.l2.b2",
        beta_star_x=betx,
        beta_star_y=bety,
    )

    mu_tar_b1_ir8 = ats_phase_aux_ir(collider, 8, 1, 2, line_name="lhcb1", betx=betx, bety=bety)
    mu_tar_b2_ir8 = ats_phase_aux_ir(collider, 8, 1, 2, line_name="lhcb2", betx=betx, bety=bety)
 
    mu_tar_b1_ir6 = ats_phase_aux_ir(collider, 4, 5, 6, line_name="lhcb1", betx=betx, bety=bety)
    mu_tar_b2_ir6 = ats_phase_aux_ir(collider, 4, 5, 6, line_name="lhcb2", betx=betx, bety=bety)

    tw_non_ats_arcs_v2 = get_arc_periodic_solution(collider, arc_name=["23", "34", "67", "78"])
    
    print('IR7')
    optimizers["ir7"] = rematch_new_ir7_both(
        collider=collider,
        boundary_conditions_left=tw_non_ats_arcs_v2,
        boundary_conditions_right=tw_non_ats_arcs_v2,
        mux_ir7_b1=collider.varval["muxip7b1"],
        muy_ir7_b1=collider.varval["muyip7b1"],
        mux_ir7_b2=collider.varval["muxip7b2"],
        muy_ir7_b2=collider.varval["muyip7b2"],
        solve=False,
        restore=False,
        assert_within_tol=False,
        default_tol=default_tol,
    )
    optimizers["ir7"].disable_targets(tag=["collb1", "collb2"])
    optimizers["ir7"].solve()
   
    optimizers["ir6b1"] = rematch_ir6(
        restore=False,
        assert_within_tol=False,
        collider=collider,
        line_name="lhcb1",
        boundary_conditions_left=tw_sq_a45_ip5_a56_b1,
        boundary_conditions_right=tw_non_ats_arcs_v2["lhcb1"]["67"],
        mux_ir6=mu_tar_b1_ir6["mux_ir6_b1"],
        muy_ir6=mu_tar_b1_ir6["muy_ir6_b1"],
        alfx_ip6=collider.varval["alfxip6b1"],
        alfy_ip6=collider.varval["alfyip6b1"],
        betx_ip6=collider.varval["betxip6b1"],
        bety_ip6=collider.varval["betyip6b1"],
        dx_ip6=collider.varval["dxip6b1"],
        dpx_ip6=collider.varval["dpxip6b1"],
        solve=False,
        match_dx=True,
        match_dpx=True,
        default_tol=default_tol,
    )
    optimizers["ir6b1"].solve()

    optimizers["ir6b1"].disable_targets(tag=["dx_ip6", "dpx_ip6"])
    optimizers["ir6b1"].solve()

    optimizers["ir6b2"] = rematch_ir6(
        restore=False,
        assert_within_tol=False,
        collider=collider,
        line_name="lhcb2",
        boundary_conditions_left=tw_sq_a45_ip5_a56_b2,
        boundary_conditions_right=tw_non_ats_arcs_v2["lhcb2"]["67"],
        mux_ir6=mu_tar_b2_ir6["mux_ir6_b2"],
        muy_ir6=mu_tar_b2_ir6["muy_ir6_b2"],
        alfx_ip6=collider.varval["alfxip6b2"],
        alfy_ip6=collider.varval["alfyip6b2"],
        betx_ip6=collider.varval["betxip6b2"],
        bety_ip6=collider.varval["betyip6b2"],
        dx_ip6=collider.varval["dxip6b2"],
        dpx_ip6=collider.varval["dpxip6b2"],
        solve=False,
        match_dx=True,
        match_dpx=True,
        default_tol=default_tol,
    )
    optimizers["ir6b2"].solve()
    optimizers["ir6b2"].disable_targets(tag=["dx_ip6", "dpx_ip6"])
    optimizers["ir6b2"].solve()


    optimizers["ir8b1"] = rematch_ir8(
        collider,
        line_name="lhcb1",
        boundary_conditions_left=tw_non_ats_arcs_v2["lhcb1"]["78"],
        boundary_conditions_right=tw_sq_a81_ip1_a12_b1,
        solve=True,
        mux_ir8=mu_tar_b1_ir8["mux_ir8_b1"],
        muy_ir8=mu_tar_b1_ir8["muy_ir8_b1"],
        alfx_ip8=collider.varval["alfxip8b1"],
        alfy_ip8=collider.varval["alfyip8b1"],
        betx_ip8=collider.varval["betxip8b1"],
        bety_ip8=collider.varval["betyip8b1"],
        dx_ip8=collider.varval["dxip8b1"],
        dpx_ip8=collider.varval["dpxip8b1"],
        staged_match=True,
        default_tol=default_tol,
    )

    optimizers["ir8b2"] = rematch_ir8(
        collider,
        line_name="lhcb2",
        boundary_conditions_left=tw_non_ats_arcs_v2["lhcb2"]["78"],
        boundary_conditions_right=tw_sq_a81_ip1_a12_b2,
        solve=True,
        mux_ir8=mu_tar_b2_ir8["mux_ir8_b2"],
        muy_ir8=mu_tar_b2_ir8["muy_ir8_b2"],
        alfx_ip8=collider.varval["alfxip8b2"],
        alfy_ip8=collider.varval["alfyip8b2"],
        betx_ip8=collider.varval["betxip8b2"],
        bety_ip8=collider.varval["betyip8b2"],
        dx_ip8=collider.varval["dxip8b2"],
        dpx_ip8=collider.varval["dpxip8b2"],
        staged_match=True,
        default_tol=default_tol,
    )
 

    if tune_chroma:
        optimizers["tune"] = rematch_tune_non_ats(collider, default_targets=True, solve=True)
        optimizers["chroma"] = rematch_chroma(collider, default_targets=True, solve=True)

        mk_arc_trims(collider)
        
        collider.vars["kqtf.b1"] = 0
        collider.vars["kqtd.b1"] = 0
        collider.vars["kqtf.b2"] = 0
        collider.vars["kqtd.b2"] = 0

        collider.vars["ksf.b1"] = 0
        collider.vars["ksd.b1"] = 0
        collider.vars["ksf.b2"] = 0
        collider.vars["ksd.b2"] = 0

    return optimizers