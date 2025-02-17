import xtrack as xt


correctors_dx1hs_dx1hl_dsep1h = [
    "acbh12.r8b1",
    "acbh14.r8b1",
    "acbh16.r8b1",
    "acbh14.l1b1",
    "acbh12.l1b1",
    "acbh13.r1b1",
    "acbh15.r1b1",
    "acbh15.l2b1",
    "acbh13.l2b1",
    "acbh13.r8b2",
    "acbh15.r8b2",
    "acbh15.l1b2",
    "acbh13.l1b2",
    "acbh12.r1b2",
    "acbh14.r1b2",
    "acbh16.l2b2",
    "acbh14.l2b2",
    "acbh12.l2b2",
]

correctors_dx1vs_dx1vl_dsep1v = [
    "acbv13.r8b1",
    "acbv15.r8b1",
    "acbv15.l1b1",
    "acbv13.l1b1",
    "acbv12.r1b1",
    "acbv14.r1b1",
    "acbv16.l2b1",
    "acbv14.l2b1",
    "acbv14.r8b2",
    "acbv16.r8b2",
    "acbv14.l1b2",
    "acbv12.l1b2",
    "acbv13.r1b2",
    "acbv15.r1b2",
    "acbv15.l2b2",
    "acbv13.l2b2",
]

correctors_ir1b1_h = [
    "acbh16.r8b1",
    "acbh14.l1b1",
    "acbh12.l1b1",
    "acbh13.r1b1",
    "acbh15.r1b1",
    "acbh15.l2b1",
]
correctors_ir1b1_v = [
    "acbv15.r8b1",
    "acbv15.l1b1",
    "acbv13.l1b1",
    "acbv12.r1b1",
    "acbv14.r1b1",
    "acbv16.l2b1",
]
correctors_ir1b2_h = [
    "acbh15.r8b2",
    "acbh15.l1b2",
    "acbh13.l1b2",
    "acbh12.r1b2",
    "acbh14.r1b2",
    "acbh16.l2b2",
]
correctors_ir1b2_v = [
    "acbv16.r8b2",
    "acbv14.l1b2",
    "acbv12.l1b2",
    "acbv13.r1b2",
    "acbv15.r1b2",
    "acbv15.l2b2",
]

disp_correctors_ir1_h = {"b1": correctors_ir1b1_h, "b2": correctors_ir1b2_h}
disp_correctors_ir1_v = {"b1": correctors_ir1b1_v, "b2": correctors_ir1b2_v}


correctors_dx5hs_dx5hl_dsep5h = [
    "acbh12.r4b1",
    "acbh14.r4b1",
    "acbh16.r4b1",
    "acbh14.l5b1",
    "acbh12.l5b1",
    "acbh13.r5b1",
    "acbh15.r5b1",
    "acbh15.l6b1",
    "acbh13.l6b1",
    "acbh13.r4b2",
    "acbh15.r4b2",
    "acbh15.l5b2",
    "acbh13.l5b2",
    "acbh12.r5b2",
    "acbh14.r5b2",
    "acbh16.l6b2",
    "acbh14.l6b2",
    "acbh12.l6b2",
]


correctors_dx5vs_dx5vl_dsep5v = [
    "acbv13.r4b1",
    "acbv15.r4b1",
    "acbv15.l5b1",
    "acbv13.l5b1",
    "acbv12.r5b1",
    "acbv14.r5b1",
    "acbv16.l6b1",
    "acbv14.l6b1",
    "acbv14.r4b2",
    "acbv16.r4b2",
    "acbv14.l5b2",
    "acbv12.l5b2",
    "acbv13.r5b2",
    "acbv15.r5b2",
    "acbv15.l6b2",
    "acbv13.l6b2",
]


correctors_ir5b1_h = [
    "acbh16.r4b1",
    "acbh14.l5b1",
    "acbh12.l5b1",
    "acbh13.r5b1",
    "acbh15.r5b1",
    "acbh15.l6b1",
]
correctors_ir5b1_v = [
    "acbv15.r4b1",
    "acbv15.l5b1",
    "acbv13.l5b1",
    "acbv12.r5b1",
    "acbv14.r5b1",
    "acbv16.l6b1",
]
correctors_ir5b2_h = [
    "acbh15.r4b2",
    "acbh15.l5b2",
    "acbh13.l5b2",
    "acbh12.r5b2",
    "acbh14.r5b2",
    "acbh16.l6b2",
]
correctors_ir5b2_v = [
    "acbv16.r4b2",
    "acbv14.l5b2",
    "acbv12.l5b2",
    "acbv13.r5b2",
    "acbv15.r5b2",
    "acbv15.l6b2",
]


disp_correctors_ir5_h = {"b1": correctors_ir5b1_h, "b2": correctors_ir5b2_h}
disp_correctors_ir5_v = {"b1": correctors_ir5b1_v, "b2": correctors_ir5b2_v}


disp_correctors_ir15_h = {"ip1": disp_correctors_ir1_h, "ip5": disp_correctors_ir5_h}
disp_correctors_ir15_v = {"ip1": disp_correctors_ir1_v, "ip5": disp_correctors_ir5_v}


def rematch_disp_ir15(
    collider,
    line_name,
    ip,
    tw_ref,
    solve=False,
    default_tol=None,
):
    line = collider[line_name]
    beam_name = line_name[-2:]

    left_ip = {"ip1": "ip8", "ip5": "ip4"}[ip]
    right_ip = {"ip1": "ip2", "ip5": "ip6"}[ip]

    twinit = xt.TwissInit(dx=tw_ref["dx", left_ip], dpx=tw_ref["dpx", left_ip])

    opt = line.match(
        solve=False,
        start=left_ip,
        end=right_ip,
        init=twinit,
        # solver_options={"min_step": 1e-18, "n_steps_max": 10},
        default_tol=default_tol,
        restore_if_fail=False,
        assert_within_tol=False,
        vary=[
            xt.VaryList(disp_correctors_ir15_h[ip][beam_name]),
            xt.VaryList(disp_correctors_ir15_v[ip][beam_name]),
        ],
        targets=[
            # Constraints on dispersion
            xt.TargetSet(["dx", "dy"], value=0, at=ip),
            xt.TargetSet(["dx", "dy"], value=tw_ref, at=right_ip),
            # Constraints on orbit
            xt.TargetSet(
                ["x", "px", "y", "py"], value=0, at=f"e.ds.l{ip[-1:]}.{beam_name}"
            ),
            xt.TargetSet(
                ["x", "px", "y", "py"], value=0, at=f"e.ds.l{right_ip[-1:]}.{beam_name}"
            ),
        ],
    )

    if solve:
        opt.solve()

    return opt


def rematch_disp(
    collider, solve=True, default_tol=None, angle_ref=295, sep_ref=1, cycle=True
):
    # Set the default values
    collider.vars["cd2q4"] = 0
    collider.vars["on_disp"] = 0
    collider.vars["on_x1"] = 0
    collider.vars["on_x5"] = 0
    collider.vars["on_sep1"] = 0
    collider.vars["on_sep5"] = 0
    collider.vars["phi_ir1"] = 0
    collider.vars["phi_ir5"] = 90

    if cycle:
        collider["lhcb1"].cycle("s.ds.l3.b1", inplace=True)
        collider["lhcb2"].cycle("s.ds.l3.b2", inplace=True)
        collider["lhcb1"].twiss_default["method"] = "4d"
        collider["lhcb2"].twiss_default["method"] = "4d"
        collider["lhcb2"].twiss_default["reverse"] = True

    tw_init_b1 = collider["lhcb1"].twiss()
    tw_init_b2 = collider["lhcb2"].twiss()

    # Destroy previous knobs
    for cn in correctors_dx1hs_dx1hl_dsep1h + correctors_dx1vs_dx1vl_dsep1v:
        collider.vars[cn] = 0

    ###############################
    ####### dx1hs + dsep1v ########
    ###############################

    collider.vars["on_disp"] = 0
    collider.vars["on_x1"] = angle_ref
    collider.vars["on_sep1"] = sep_ref
    print("Matching dx1hs + dsep1v")
    opt_x1hs_sep1v_b1 = rematch_disp_ir15(
        collider,
        line_name="lhcb1",
        tw_ref=tw_init_b1,
        ip="ip1",
        solve=False,
        default_tol=default_tol,
    )
    opt_x1hs_sep1v_b2 = rematch_disp_ir15(
        collider,
        line_name="lhcb2",
        tw_ref=tw_init_b2,
        ip="ip1",
        solve=False,
        default_tol=default_tol,
    )

    if solve:
        opt_x1hs_sep1v_b1.solve()
        opt_x1hs_sep1v_b2.solve()

    collider.vars["phi_ir1"] = 0
    collider.vars["on_x1"] = 0
    collider.vars["on_sep1"] = 0

    corrector_values_x1hs_sep1v = {}
    for cn in correctors_dx1hs_dx1hl_dsep1h + correctors_dx1vs_dx1vl_dsep1v:
        corrector_values_x1hs_sep1v[cn] = collider.varval[cn]
        collider.varval[cn] = 0

    ###############################
    ####### dx1vs + dsep1h ########
    ###############################

    collider.vars["phi_ir1"] = 90
    collider.vars["on_x1"] = angle_ref
    collider.vars["on_sep1"] = -sep_ref
    print("Matching dx1vs + dsep1h")
    opt_x1vs_sep1h_b1 = rematch_disp_ir15(
        collider,
        line_name="lhcb1",
        tw_ref=tw_init_b1,
        ip="ip1",
        solve=False,
        default_tol=default_tol,
    )
    opt_x1vs_sep1h_b2 = rematch_disp_ir15(
        collider,
        line_name="lhcb2",
        tw_ref=tw_init_b2,
        ip="ip1",
        solve=False,
        default_tol=default_tol,
    )

    if solve:
        opt_x1vs_sep1h_b1.solve()
        opt_x1vs_sep1h_b2.solve()

    collider.vars["phi_ir1"] = 0
    collider.vars["on_x1"] = 0
    collider.vars["on_sep1"] = 0

    corrector_values_x1vs_sep1h = {}
    for cn in correctors_dx1hs_dx1hl_dsep1h + correctors_dx1vs_dx1vl_dsep1v:
        corrector_values_x1vs_sep1h[cn] = collider.varval[cn]
        collider.varval[cn] = 0

    ###############################
    ####### dx1hl + dsep1v ########
    ###############################

    collider.vars["on_disp"] = 0
    collider.vars["cd2q4"] = 1
    collider.vars["on_x1"] = angle_ref
    collider.vars["on_sep1"] = sep_ref
    print("Matching dx1hl + dsep1v")
    opt_x1hl_sep1v_b1 = rematch_disp_ir15(
        collider,
        line_name="lhcb1",
        tw_ref=tw_init_b1,
        ip="ip1",
        solve=False,
        default_tol=default_tol,
    )
    opt_x1hl_sep1v_b2 = rematch_disp_ir15(
        collider,
        line_name="lhcb2",
        tw_ref=tw_init_b2,
        ip="ip1",
        solve=False,
        default_tol=default_tol,
    )

    if solve:
        opt_x1hl_sep1v_b1.solve()
        opt_x1hl_sep1v_b2.solve()

    collider.vars["phi_ir1"] = 0
    collider.vars["on_x1"] = 0
    collider.vars["on_sep1"] = 0
    collider.vars["cd2q4"] = 0

    corrector_values_x1hl_sep1v = {}
    for cn in correctors_dx1hs_dx1hl_dsep1h + correctors_dx1vs_dx1vl_dsep1v:
        corrector_values_x1hl_sep1v[cn] = collider.varval[cn]
        collider.varval[cn] = 0

    ###############################
    ####### dx1vl + dsep1h ########
    ###############################

    collider.vars["phi_ir1"] = 90
    collider.vars["cd2q4"] = 1
    collider.vars["on_x1"] = angle_ref
    collider.vars["on_sep1"] = -sep_ref
    print("Matching dx1vl + dsep1h")
    opt_x1vl_sep1h_b1 = rematch_disp_ir15(
        collider,
        line_name="lhcb1",
        tw_ref=tw_init_b1,
        ip="ip1",
        solve=False,
        default_tol=default_tol,
    )
    opt_x1vl_sep1h_b2 = rematch_disp_ir15(
        collider,
        line_name="lhcb2",
        tw_ref=tw_init_b2,
        ip="ip1",
        solve=False,
        default_tol=default_tol,
    )

    if solve:
        opt_x1vl_sep1h_b1.solve()
        opt_x1vl_sep1h_b2.solve()

    collider.vars["phi_ir1"] = 0
    collider.vars["on_x1"] = 0
    collider.vars["on_sep1"] = 0
    collider.vars["cd2q4"] = 0

    corrector_values_x1vl_sep1h = {}
    for cn in correctors_dx1hs_dx1hl_dsep1h + correctors_dx1vs_dx1vl_dsep1v:
        corrector_values_x1vl_sep1h[cn] = collider.varval[cn]
        collider.varval[cn] = 0

    ###############################
    ####### dx5hs + dsep5v ########
    ###############################

    collider.vars["on_disp"] = 0
    collider.vars["phi_ir5"] = 0
    collider.vars["on_x5"] = angle_ref
    collider.vars["on_sep5"] = sep_ref
    print("Matching dx5hs + dsep5v")
    opt_x5hs_sep5v_b1 = rematch_disp_ir15(
        collider,
        line_name="lhcb1",
        tw_ref=tw_init_b1,
        ip="ip5",
        solve=False,
        default_tol=default_tol,
    )
    opt_x5hs_sep5v_b2 = rematch_disp_ir15(
        collider,
        line_name="lhcb2",
        tw_ref=tw_init_b2,
        ip="ip5",
        solve=False,
        default_tol=default_tol,
    )

    if solve:
        opt_x5hs_sep5v_b1.solve()
        opt_x5hs_sep5v_b2.solve()

    collider.vars["on_disp"] = 0
    collider.vars["phi_ir5"] = 0
    collider.vars["on_x5"] = 0
    collider.vars["on_sep5"] = 0

    corrector_values_x5hs_sep5v = {}
    for cn in correctors_dx5hs_dx5hl_dsep5h + correctors_dx5vs_dx5vl_dsep5v:
        corrector_values_x5hs_sep5v[cn] = collider.varval[cn]
        collider.varval[cn] = 0

    ###############################
    ####### dx5vs + dsep5h ########
    ###############################

    collider.vars["phi_ir5"] = 90
    collider.vars["on_x5"] = angle_ref
    collider.vars["on_sep5"] = -sep_ref
    print("Matching dx5vs + dsep5h")
    opt_x5vs_sep5h_b1 = rematch_disp_ir15(
        collider,
        line_name="lhcb1",
        tw_ref=tw_init_b1,
        ip="ip5",
        solve=False,
        default_tol=default_tol,
    )
    opt_x5vs_sep5h_b2 = rematch_disp_ir15(
        collider,
        line_name="lhcb2",
        tw_ref=tw_init_b2,
        ip="ip5",
        solve=False,
        default_tol=default_tol,
    )

    if solve:
        opt_x5vs_sep5h_b1.solve()
        opt_x5vs_sep5h_b2.solve()

    collider.vars["phi_ir5"] = 90
    collider.vars["on_x5"] = 0
    collider.vars["on_sep5"] = 0

    corrector_values_x5vs_sep5h = {}
    for cn in correctors_dx5hs_dx5hl_dsep5h + correctors_dx5vs_dx5vl_dsep5v:
        corrector_values_x5vs_sep5h[cn] = collider.varval[cn]
        collider.varval[cn] = 0

    ###############################
    ####### dx5hl + dsep5v ########
    ###############################

    collider.vars["on_disp"] = 0
    collider.vars["cd2q4"] = 1
    collider.vars["phi_ir5"] = 0
    collider.vars["on_x5"] = angle_ref
    collider.vars["on_sep5"] = sep_ref
    print("Matching dx5hl + dsep5v")
    opt_x5hl_sep5v_b1 = rematch_disp_ir15(
        collider,
        line_name="lhcb1",
        tw_ref=tw_init_b1,
        ip="ip5",
        solve=False,
        default_tol=default_tol,
    )
    opt_x5hl_sep5v_b2 = rematch_disp_ir15(
        collider,
        line_name="lhcb2",
        tw_ref=tw_init_b2,
        ip="ip5",
        solve=False,
        default_tol=default_tol,
    )

    if solve:
        opt_x5hl_sep5v_b1.solve()
        opt_x5hl_sep5v_b2.solve()

    collider.vars["phi_ir5"] = 90
    collider.vars["on_x5"] = 0
    collider.vars["on_sep5"] = 0
    collider.vars["cd2q4"] = 0

    corrector_values_x5hl_sep5v = {}
    for cn in correctors_dx5hs_dx5hl_dsep5h + correctors_dx5vs_dx5vl_dsep5v:
        corrector_values_x5hl_sep5v[cn] = collider.varval[cn]
        collider.varval[cn] = 0

    ###############################
    ####### dx5vl + dsep5h ########
    ###############################

    collider.vars["phi_ir5"] = 90
    collider.vars["cd2q4"] = 1
    collider.vars["on_x5"] = angle_ref
    collider.vars["on_sep5"] = -sep_ref
    print("Matching dx5vl + dsep5h")
    opt_x5vl_sep5h_b1 = rematch_disp_ir15(
        collider,
        line_name="lhcb1",
        tw_ref=tw_init_b1,
        ip="ip5",
        solve=False,
        default_tol=default_tol,
    )
    opt_x5vl_sep5h_b2 = rematch_disp_ir15(
        collider,
        line_name="lhcb2",
        tw_ref=tw_init_b2,
        ip="ip5",
        solve=False,
        default_tol=default_tol,
    )

    if solve:
        opt_x5vl_sep5h_b1.solve()
        opt_x5vl_sep5h_b2.solve()

    collider.vars["phi_ir5"] = 90
    collider.vars["on_x5"] = 0
    collider.vars["on_sep5"] = 0
    collider.vars["cd2q4"] = 0

    corrector_values_x5vl_sep5h = {}
    for cn in correctors_dx5hs_dx5hl_dsep5h + correctors_dx5vs_dx5vl_dsep5v:
        corrector_values_x5vl_sep5h[cn] = collider.varval[cn]
        collider.varval[cn] = 0

    # Reset again just in case
    for cn in (
        correctors_dx1hs_dx1hl_dsep1h
        + correctors_dx1vs_dx1vl_dsep1v
        + correctors_dx5hs_dx5hl_dsep5h
        + correctors_dx5vs_dx5vl_dsep5v
    ):
        collider.vars[cn] = 0

    # Create knob expressions by hand
    for cn in correctors_dx1hs_dx1hl_dsep1h:
        collider.vars[cn] += (
            corrector_values_x1hs_sep1v[cn] / angle_ref * collider.vars["on_dx1hs"]
        )
    for cn in correctors_dx1hs_dx1hl_dsep1h:
        collider.vars[cn] += (
            corrector_values_x1hl_sep1v[cn] / angle_ref * collider.vars["on_dx1hl"]
        )
    for cn in correctors_dx1hs_dx1hl_dsep1h:
        # collider.vars[cn] += (
        #     corrector_values_x1vs_sep1h[cn] / sep_ref * collider.vars["on_dsep1h"]
        # )
        collider.vars[cn] += (
            corrector_values_x1vl_sep1h[cn] / sep_ref * collider.vars["on_dsep1h"]
        )

    for cn in correctors_dx1vs_dx1vl_dsep1v:
        collider.vars[cn] += (
            corrector_values_x1vs_sep1h[cn] / angle_ref * collider.vars["on_dx1vs"]
        )
    for cn in correctors_dx1vs_dx1vl_dsep1v:
        collider.vars[cn] += (
            corrector_values_x1vl_sep1h[cn] / angle_ref * collider.vars["on_dx1vl"]
        )
    for cn in correctors_dx1vs_dx1vl_dsep1v:
        # collider.vars[cn] += (
        #     corrector_values_x1hs_sep1v[cn] / sep_ref * collider.vars["on_dsep1v"]
        # )
        collider.vars[cn] += (
            corrector_values_x1hl_sep1v[cn] / sep_ref * collider.vars["on_dsep1v"]
        )

    for cn in correctors_dx5hs_dx5hl_dsep5h:
        collider.vars[cn] += (
            corrector_values_x5hs_sep5v[cn] / angle_ref * collider.vars["on_dx5hs"]
        )
    for cn in correctors_dx5hs_dx5hl_dsep5h:
        collider.vars[cn] += (
            corrector_values_x5hl_sep5v[cn] / angle_ref * collider.vars["on_dx5hl"]
        )
    for cn in correctors_dx5hs_dx5hl_dsep5h:
        # collider.vars[cn] += (
        #     corrector_values_x5vs_sep5h[cn] / sep_ref * collider.vars["on_dsep5h"]
        # )
        collider.vars[cn] += (
            corrector_values_x5vl_sep5h[cn] / sep_ref * collider.vars["on_dsep5h"]
        )

    for cn in correctors_dx5vs_dx5vl_dsep5v:
        collider.vars[cn] += (
            corrector_values_x5vs_sep5h[cn] / angle_ref * collider.vars["on_dx5vs"]
        )
    for cn in correctors_dx5vs_dx5vl_dsep5v:
        collider.vars[cn] += (
            corrector_values_x5vl_sep5h[cn] / angle_ref * collider.vars["on_dx5vl"]
        )
    for cn in correctors_dx5vs_dx5vl_dsep5v:
        # collider.vars[cn] += (
        #     corrector_values_x5hs_sep5v[cn] / sep_ref * collider.vars["on_dsep5v"]
        # )
        collider.vars[cn] += (
            corrector_values_x5hl_sep5v[cn] / sep_ref * collider.vars["on_dsep5v"]
        )

    if cycle:
        collider["lhcb1"].cycle("lhcb1$start", inplace=True)
        collider["lhcb2"].cycle("lhcb2$start", inplace=True)
        collider["lhcb1"].twiss_default["method"] = "4d"
        collider["lhcb2"].twiss_default["method"] = "4d"
        collider["lhcb2"].twiss_default["reverse"] = True

    opts = {
        "dx1hs_dsep1v_b1": opt_x1hs_sep1v_b1,
        "dx1hs_dsep1v_b2": opt_x1hs_sep1v_b2,
        "dx1vs_dsep1h_b1": opt_x1vs_sep1h_b1,
        "dx1vs_dsep1h_b2": opt_x1vs_sep1h_b2,
        "dx1hl_dsep1v_b1": opt_x1hl_sep1v_b1,
        "dx1hl_dsep1v_b2": opt_x1hl_sep1v_b2,
        "dx1vl_dsep1h_b1": opt_x1vl_sep1h_b1,
        "dx1vl_dsep1h_b2": opt_x1vl_sep1h_b2,
        "dx5hs_dsep5v_b1": opt_x5hs_sep5v_b1,
        "dx5hs_dsep5v_b2": opt_x5hs_sep5v_b2,
        "dx5vs_dsep5h_b1": opt_x5vs_sep5h_b1,
        "dx5vs_dsep5h_b2": opt_x5vs_sep5h_b2,
        "dx5hl_dsep5v_b1": opt_x5hl_sep5v_b1,
        "dx5hl_dsep5v_b2": opt_x5hl_sep5v_b2,
        "dx5vl_dsep5h_b1": opt_x5vl_sep5h_b1,
        "dx5vl_dsep5h_b2": opt_x5vl_sep5h_b2,
    }
    return opts
