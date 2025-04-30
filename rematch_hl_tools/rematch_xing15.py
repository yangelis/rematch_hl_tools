import xtrack as xt


def match_xing15_hv(
    collider,
    knob_fmt,
    ip,
    hv,
    targets,
    knob_value_end,
    twinit_zero_orbit,
    bump_range_ip,
    tolerances=None,
):
    opt_x = collider.match_knob(
        knob_name=knob_fmt.replace("ip", str(ip)).replace("hv", hv),
        knob_value_start=0,
        knob_value_end=knob_value_end,
        targets=targets,
        vary=[
            xt.VaryList(
                [
                    f"acbrd{hv}4.l{ip}b1aux",
                    f"acbrd{hv}4.l{ip}b2aux",
                    f"acbrd{hv}4.r{ip}b1aux",
                    f"acbrd{hv}4.r{ip}b2aux",
                ],
            ),
            xt.VaryList(
                [f"acbx{hv}1.l{ip}", f"acbx{hv}1.r{ip}"],
                tag="mcbx",
            ),
            xt.VaryList(
                [f"acbx{hv}3.l{ip}", f"acbx{hv}3.r{ip}"],
                tag="mcbx",
            ),
        ],
        run=False,
        assert_within_tol=False,
        restore_if_fail=False,
        init=twinit_zero_orbit,
        n_steps_max=25,
        default_tol=tolerances,
        **bump_range_ip,
    )

    return opt_x


def match_orbit15_hv(
    collider,
    knob_fmt,
    ip,
    hv,
    targets,
    knob_value_end,
    twinit_zero_orbit,
    bump_range_ip,
    tolerances=None,
):
    opt_x = collider.match_knob(
        knob_name=knob_fmt.replace("ip", str(ip)).replace("hv", hv),
        knob_value_start=0,
        knob_value_end=knob_value_end,
        targets=targets,
        vary=[
            xt.VaryList(
                [
                    f"acbrd{hv}4.l{ip}b1",
                    f"acbrd{hv}4.l{ip}b2",
                    f"acbrd{hv}4.r{ip}b1",
                    f"acbrd{hv}4.r{ip}b2",
                ],
            ),
            xt.VaryList(
                [f"acbx{hv}1.l{ip}", f"acbx{hv}1.r{ip}"],
                tag="mcbx",
            ),
            xt.VaryList(
                [f"acbx{hv}3.l{ip}", f"acbx{hv}3.r{ip}"],
                tag="mcbx",
            ),
        ],
        run=False,
        assert_within_tol=False,
        restore_if_fail=False,
        init=twinit_zero_orbit,
        n_steps_max=25,
        default_tol=tolerances,
        **bump_range_ip,
    )

    return opt_x


def match_ccpm(
    collider,
    knob_fmt,
    ip,
    hv,
    targets,
    knob_value_end,
    twinit_zero_orbit,
    bump_range_ip,
    tolerances=None,
):
    acbc56_vary = []
    if hv == "h":
        acbc56_vary = xt.VaryList(
            [
                f"acbch5.l{ip}b2",
                f"acbch5.r{ip}b1",
                f"acbch6.l{ip}b1",
                f"acbch6.r{ip}b2",
            ],
        )
    elif hv == "v":
        acbc56_vary = xt.VaryList(
            [
                f"acbcv5.l{ip}b1",
                f"acbcv5.r{ip}b2",
                f"acbcv6.l{ip}b2",
                f"acbcv6.r{ip}b1",
            ],
        )

    opt_x = collider.match_knob(
        knob_name=knob_fmt.replace("ip", str(ip)).replace("hv", hv),
        knob_value_start=0,
        knob_value_end=knob_value_end,
        targets=targets,
        vary=[
            xt.VaryList(
                [
                    f"acbrd{hv}4.l{ip}b1",
                    f"acbrd{hv}4.l{ip}b2",
                    f"acbrd{hv}4.r{ip}b1",
                    f"acbrd{hv}4.r{ip}b2",
                ],
            ),
            xt.VaryList(
                [f"acbx{hv}1.l{ip}", f"acbx{hv}1.r{ip}"],
                tag="mcbx",
            ),
            xt.VaryList(
                [f"acbx{hv}3.l{ip}", f"acbx{hv}3.r{ip}"],
                tag="mcbx",
            ),
            xt.VaryList(
                [
                    f"acby{hv}s4.l{ip}b1",
                    f"acby{hv}s4.l{ip}b2",
                    f"acby{hv}s4.r{ip}b1",
                    f"acby{hv}s4.r{ip}b2",
                ],
            ),
            acbc56_vary,
        ],
        run=False,
        assert_within_tol=False,
        restore_if_fail=False,
        init=twinit_zero_orbit,
        n_steps_max=25,
        default_tol=tolerances,
        **bump_range_ip,
    )

    return opt_x


def match_off(
    collider,
    knob_fmt,
    ip,
    hv,
    targets,
    knob_value_end,
    twinit_zero_orbit,
    bump_range_ip,
    tolerances=None,
):
    mcbc_vary = []
    if hv == "h":
        mcbc_vary = xt.VaryList(
            [
                f"acbch5.l{ip}b2",
                f"acbch5.r{ip}b1",
                f"acbch6.l{ip}b1",
                f"acbch6.r{ip}b2",
                f"acbch7.l{ip}b2",
                f"acbch7.r{ip}b1",
            ],
        )
    elif hv == "v":
        mcbc_vary = xt.VaryList(
            [
                f"acbcv5.l{ip}b1",
                f"acbcv5.r{ip}b2",
                f"acbcv6.l{ip}b2",
                f"acbcv6.r{ip}b1",
                f"acbcv7.l{ip}b1",
                f"acbcv7.r{ip}b2",
            ],
        )

    opt_x = collider.match_knob(
        knob_name=knob_fmt.replace("ip", str(ip)).replace("hv", hv),
        knob_value_start=0,
        knob_value_end=knob_value_end,
        targets=targets,
        vary=[
            xt.VaryList(
                [
                    f"acby{hv}s4.l{ip}b1",
                    f"acby{hv}s4.l{ip}b2",
                    f"acby{hv}s4.r{ip}b1",
                    f"acby{hv}s4.r{ip}b2",
                ],
            ),
            xt.VaryList(
                [f"acbx{hv}1.l{ip}", f"acbx{hv}1.r{ip}"],
                tag="mcbx",
            ),
            xt.VaryList(
                [f"acbx{hv}2.l{ip}", f"acbx{hv}2.r{ip}"],
                tag="mcbx",
            ),
            xt.VaryList(
                [f"acbx{hv}3.l{ip}", f"acbx{hv}3.r{ip}"],
                tag="mcbx",
            ),
            mcbc_vary,
        ],
        run=False,
        assert_within_tol=False,
        restore_if_fail=False,
        init=twinit_zero_orbit,
        n_steps_max=25,
        default_tol=tolerances,
        **bump_range_ip,
    )

    return opt_x


def match_orbit_knobs_ip15(
    collider,
    tolerances=None,
    first_pass=True,
    angle_match=295,
    sep_match=2,
    aangle_match=1,
):
    cvars = collider.vars

    correctors_xing = [
        "acbxhv1.lirn",
        "acbxhv1.rirn",
        "acbxhv2.lirn",
        "acbxhv2.rirn",
        "acbxhv3.lirn",
        "acbxhv3.rirn",
        "acbrdhv4.lirnb1",
        "acbrdhv4.lirnb2",
        "acbrdhv4.rirnb1",
        "acbrdhv4.rirnb2",
        "acbyhvs4.lirnb1",
        "acbyhvs4.lirnb2",
        "acbyhvs4.rirnb1",
        "acbyhvs4.rirnb2",
        "acbyhv4.lirnb1",
        "acbyhv4.lirnb2",
        "acbyhv4.rirnb1",
        "acbyhv4.rirnb2",
        "pxyipirnb1",
        "pxyipirnb2",
    ]

    correctors_psep = [
        "acbxhv1.lirn",
        "acbxhv1.rirn",
        "acbxhv2.lirn",
        "acbxhv2.rirn",
        "acbxhv3.lirn",
        "acbxhv3.rirn",
        "acbrdhv4.lirnb1",
        "acbrdhv4.lirnb2",
        "acbrdhv4.rirnb1",
        "acbrdhv4.rirnb2",
        "acbyhvs4.lirnb1",
        "acbyhvs4.lirnb2",
        "acbyhvs4.rirnb1",
        "acbyhvs4.rirnb2",
        "acbyhv4.lirnb1",
        "acbyhv4.lirnb2",
        "acbyhv4.rirnb1",
        "acbyhv4.rirnb2",
        "xyipirnb1",
        "xyipirnb2",
    ]

    correctors_mcbc = [
        "acbch5.lirnb1",
        "acbch5.rirnb1",
        "acbch6.lirnb1",
        "acbch6.rirnb2",
        "acbch7.lirnb2",
        "acbch7.rirnb1",
        "acbcv5.lirnb1",
        "acbcv5.rirnb2",
        "acbcv6.lirnb2",
        "acbcv6.rirnb1",
        "acbcv7.lirnb1",
        "acbcv7.rirnb2",
    ]

    # kill all existing knobs
    if first_pass:
        for irn in ["1", "5"]:
            for hv in ["h", "v"]:
                for xy in ["x", "y"]:
                    for cor in correctors_psep + correctors_xing:
                        cor_name = (
                            cor.replace("hv", hv).replace("xy", xy).replace("irn", irn)
                        )
                        cvars[cor_name] = 0
            for cor in correctors_mcbc:
                cor_name = cor.replace("irn", irn)
                cvars[cor_name] = 0

    twinit_zero_orbit = [xt.TwissInit(), xt.TwissInit()]

    targets_close_bump = [
        xt.TargetSet(line="lhcb1", at=xt.END, x=0, px=0, y=0, py=0),
        xt.TargetSet(line="lhcb2", at=xt.END, x=0, px=0, y=0, py=0),
    ]

    bump_range_ip1 = {
        "start": ["s.ds.l1.b1", "s.ds.l1.b2"],
        "end": ["e.ds.r1.b1", "e.ds.r1.b2"],
    }

    angle_match = angle_match * 1e-6
    sep_match = sep_match * 1e-3
    aangle_match = aangle_match * 1e-6

    for irn in ["1", "5"]:
        for hv in ["h", "v"]:
            for bim in ["b1", "b2"]:
                # Connect acbx2 with acbx1
                connect_target = "acbxhv2.lirn".replace("irn", irn).replace("hv", hv)
                connect_from = "acbxhv1.lirn".replace("irn", irn).replace("hv", hv)
                cvars[connect_target] = cvars[connect_from]
                connect_target = connect_target.replace("l", "r")
                connect_from = connect_from.replace("l", "r")
                cvars[connect_target] = cvars[connect_from]

                # Create auxiliary knobs
                aux_name_l = (
                    "acbrdhv4.lirnb1aux".replace("irn", irn)
                    .replace("hv", hv)
                    .replace("b1", bim)
                )
                cvars[aux_name_l] = 0
                aux_name_r = (
                    "acbrdhv4.rirnb1aux".replace("irn", irn)
                    .replace("hv", hv)
                    .replace("b1", bim)
                )
                cvars[aux_name_r] = 0

                # Connect acbrdhv4 with the auxiliary knobs and cd2q4 for long and short bumps
                connect_target = (
                    "acbrdhv4.lirnb1".replace("irn", irn)
                    .replace("hv", hv)
                    .replace("b1", bim)
                )
                cvars[connect_target] = (1 - cvars["cd2q4"]) * cvars[aux_name_l]

                connect_target = connect_target.replace("l", "r")
                cvars[connect_target] = (1 - cvars["cd2q4"]) * cvars[aux_name_r]

                # Connect acbyhvs4 with the auxiliary knobs and cd2q4 for long and short bumps
                connect_target = (
                    "acbyhvs4.lirnb1".replace("irn", irn)
                    .replace("hv", hv)
                    .replace("b1", bim)
                )
                cvars[connect_target] = cvars["cd2q4"] * cvars[aux_name_l]
                connect_target = connect_target.replace("l", "r")
                cvars[connect_target] = cvars["cd2q4"] * cvars[aux_name_r]

                connect_target = (
                    "acbyhv4.lirnb1".replace("irn", irn)
                    .replace("hv", hv)
                    .replace("b1", bim)
                )
                connect_from = (
                    "acbyhvs4.lirnb1".replace("irn", irn)
                    .replace("hv", hv)
                    .replace("b1", bim)
                )
                cvars[connect_target] = cvars[connect_from]
                connect_target = connect_target.replace("l", "r")
                connect_from = connect_from.replace("l", "r")
                cvars[connect_target] = cvars[connect_from]

    targets_x1h = targets_close_bump + [
        xt.TargetSet(line="lhcb1", at="ip1", x=0, px=angle_match),
        xt.TargetSet(line="lhcb2", at="ip1", x=0, px=-angle_match),
    ]

    targets_x1v = targets_close_bump + [
        xt.TargetSet(line="lhcb1", at="ip1", y=0, py=angle_match),
        xt.TargetSet(line="lhcb2", at="ip1", y=0, py=-angle_match),
    ]

    targets_x5h = targets_close_bump + [
        xt.TargetSet(line="lhcb1", at="ip5", x=0, px=angle_match),
        xt.TargetSet(line="lhcb2", at="ip5", x=0, px=-angle_match),
    ]

    targets_x5v = targets_close_bump + [
        xt.TargetSet(line="lhcb1", at="ip5", y=0, py=angle_match),
        xt.TargetSet(line="lhcb2", at="ip5", y=0, py=-angle_match),
    ]

    knob_fmt_on_x_short = "on_xiphvs"
    knob_fmt_on_x_long = "on_xiphvl"

    ###############################
    ########### on_x1hs ###########
    ###############################
    cvars["cd2q4"] = 0
    opt_x1hs = match_xing15_hv(
        collider,
        knob_fmt_on_x_short,
        1,
        "h",
        targets_x1h,
        angle_match * 1e6,
        twinit_zero_orbit,
        bump_range_ip1,
        tolerances=tolerances,
    )
    opt_x1hs.solve()
    opt_x1hs.generate_knob()

    ###############################
    ########### on_x1vs ###########
    ###############################
    cvars["cd2q4"] = 0
    opt_x1vs = match_xing15_hv(
        collider,
        knob_fmt_on_x_short,
        1,
        "v",
        targets_x1v,
        angle_match * 1e6,
        twinit_zero_orbit,
        bump_range_ip1,
        tolerances=tolerances,
    )
    opt_x1vs.solve()
    opt_x1vs.generate_knob()

    ###############################
    ########### on_x1hl ###########
    ###############################
    cvars["cd2q4"] = 1
    opt_x1hl = match_xing15_hv(
        collider,
        knob_fmt_on_x_long,
        1,
        "h",
        targets_x1h,
        angle_match * 1e6,
        twinit_zero_orbit,
        bump_range_ip1,
    )
    opt_x1hl.solve()
    opt_x1hl.generate_knob()

    ###############################
    ########### on_x1vl ###########
    ###############################
    cvars["cd2q4"] = 1
    opt_x1vl = match_xing15_hv(
        collider,
        knob_fmt_on_x_long,
        1,
        "v",
        targets_x1v,
        angle_match * 1e6,
        twinit_zero_orbit,
        bump_range_ip1,
    )
    opt_x1vl.solve()
    opt_x1vl.generate_knob()

    #################
    ###### IP5 ######
    #################

    bump_range_ip5 = {
        "start": ["s.ds.l5.b1", "s.ds.l5.b2"],
        "end": ["e.ds.r5.b1", "e.ds.r5.b2"],
    }

    ###############################
    ########### on_x5hs ###########
    ###############################
    cvars["cd2q4"] = 0
    opt_x5hs = match_xing15_hv(
        collider,
        knob_fmt_on_x_short,
        5,
        "h",
        targets_x5h,
        angle_match * 1e6,
        twinit_zero_orbit,
        bump_range_ip5,
    )
    opt_x5hs.solve()
    opt_x5hs.generate_knob()

    ###############################
    ########### on_x5vs ###########
    ###############################
    cvars["cd2q4"] = 0
    opt_x5vs = match_xing15_hv(
        collider,
        knob_fmt_on_x_short,
        5,
        "v",
        targets_x5v,
        angle_match * 1e6,
        twinit_zero_orbit,
        bump_range_ip5,
    )
    opt_x5vs.solve()
    opt_x5vs.generate_knob()

    ###############################
    ########### on_x5hl ###########
    ###############################
    cvars["cd2q4"] = 1
    opt_x5hl = match_xing15_hv(
        collider,
        knob_fmt_on_x_long,
        5,
        "h",
        targets_x5h,
        angle_match * 1e6,
        twinit_zero_orbit,
        bump_range_ip5,
    )
    opt_x5hl.solve()
    opt_x5hl.generate_knob()

    ###############################
    ########### on_x5vl ###########
    ###############################
    cvars["cd2q4"] = 1
    opt_x5vl = match_xing15_hv(
        collider,
        knob_fmt_on_x_long,
        5,
        "v",
        targets_x5v,
        angle_match * 1e6,
        twinit_zero_orbit,
        bump_range_ip5,
    )
    opt_x5vl.solve()
    opt_x5vl.generate_knob()

    # Disconnect from aux knobs
    for irn in ["1", "5"]:
        for hv in ["h", "v"]:
            for bim in ["b1", "b2"]:
                connect_target = (
                    "acbyhvs4.lirnb1".replace("irn", irn)
                    .replace("hv", hv)
                    .replace("b1", bim)
                )
                connect_from = (
                    "acbrdhv4.lirnb1".replace("irn", irn)
                    .replace("hv", hv)
                    .replace("b1", bim)
                )

                cvars[connect_from] = 0

                cvars[connect_target] = cvars["cd2q4"] * cvars[connect_from]
                connect_target = connect_target.replace("l", "r")
                connect_from = connect_from.replace("l", "r")
                cvars[connect_from] = 0
                cvars[connect_target] = cvars["cd2q4"] * cvars[connect_from]

                connect_target = (
                    "acbyhv4.lirnb1".replace("irn", irn)
                    .replace("hv", hv)
                    .replace("b1", bim)
                )
                connect_from = (
                    "acbyhvs4.lirnb1".replace("irn", irn)
                    .replace("hv", hv)
                    .replace("b1", bim)
                )
                cvars[connect_target] = cvars[connect_from]
                connect_target = connect_target.replace("l", "r")
                connect_from = connect_from.replace("l", "r")
                cvars[connect_target] = cvars[connect_from]

    ###############################
    ########### on_sep1h ##########
    ###############################
    targets_sep1h = targets_close_bump + [
        xt.TargetSet(line="lhcb1", at="ip1", x=sep_match, px=0),
        xt.TargetSet(line="lhcb2", at="ip1", x=-sep_match, px=0),
    ]

    knob_fmt_on_sep = "on_sepiphv"

    cvars["cd2q4"] = 1
    opt_sep1h = match_orbit15_hv(
        collider,
        knob_fmt_on_sep,
        1,
        "h",
        targets_sep1h,
        sep_match * 1e3,
        twinit_zero_orbit,
        bump_range_ip1,
    )
    opt_sep1h.solve()
    opt_sep1h.generate_knob()

    ###############################
    ########### on_sep1v ##########
    ###############################
    targets_sep1v = targets_close_bump + [
        xt.TargetSet(line="lhcb1", at="ip1", y=sep_match, py=0),
        xt.TargetSet(line="lhcb2", at="ip1", y=-sep_match, py=0),
    ]

    cvars["cd2q4"] = 1
    opt_sep1v = match_orbit15_hv(
        collider,
        knob_fmt_on_sep,
        1,
        "v",
        targets_sep1v,
        sep_match * 1e3,
        twinit_zero_orbit,
        bump_range_ip1,
    )
    opt_sep1v.solve()
    opt_sep1v.generate_knob()

    ###############################
    ########### on_sep5h ##########
    ###############################
    targets_sep5h = targets_close_bump + [
        xt.TargetSet(line="lhcb1", at="ip5", x=sep_match, px=0),
        xt.TargetSet(line="lhcb2", at="ip5", x=-sep_match, px=0),
    ]

    cvars["cd2q4"] = 1
    opt_sep5h = match_orbit15_hv(
        collider,
        knob_fmt_on_sep,
        5,
        "h",
        targets_sep5h,
        sep_match * 1e3,
        twinit_zero_orbit,
        bump_range_ip5,
    )

    opt_sep5h.solve()
    opt_sep5h.generate_knob()

    ###############################
    ########### on_sep5v ##########
    ###############################
    targets_sep5v = targets_close_bump + [
        xt.TargetSet(line="lhcb1", at="ip5", y=sep_match, py=0),
        xt.TargetSet(line="lhcb2", at="ip5", y=-sep_match, py=0),
    ]

    cvars["cd2q4"] = 1
    opt_sep5v = match_orbit15_hv(
        collider,
        knob_fmt_on_sep,
        5,
        "v",
        targets_sep5v,
        sep_match * 1e3,
        twinit_zero_orbit,
        bump_range_ip5,
    )
    opt_sep5v.solve()
    opt_sep5v.generate_knob()

    # To ignore acby connection from before set cd2q4 to zero
    cvars["cd2q4"] = 0
    ###############################
    ########### on_a1h ############
    ###############################

    knob_fmt_on_a = "on_aiphv"

    ang_match = 1e-6
    targets_a1h = targets_close_bump + [
        xt.TargetSet(line="lhcb1", at="ip1", x=0, px=ang_match),
        xt.TargetSet(line="lhcb2", at="ip1", x=0, px=ang_match),
    ]

    opt_a1h = match_orbit15_hv(
        collider,
        knob_fmt_on_a,
        1,
        "h",
        targets_a1h,
        ang_match * 1e6,
        twinit_zero_orbit,
        bump_range_ip1,
    )

    opt_a1h.solve()
    opt_a1h.generate_knob()

    ###############################
    ########### on_a1v ############
    ###############################
    targets_a1v = targets_close_bump + [
        xt.TargetSet(line="lhcb1", at="ip1", y=0, py=ang_match),
        xt.TargetSet(line="lhcb2", at="ip1", y=0, py=ang_match),
    ]
    opt_a1v = match_orbit15_hv(
        collider,
        knob_fmt_on_a,
        1,
        "v",
        targets_a1v,
        ang_match * 1e6,
        twinit_zero_orbit,
        bump_range_ip1,
    )

    opt_a1v.solve()
    opt_a1v.generate_knob()

    ###############################
    ########### on_a5h ############
    ###############################
    ang_match = 1e-6
    targets_a5h = targets_close_bump + [
        xt.TargetSet(line="lhcb1", at="ip5", x=0, px=ang_match),
        xt.TargetSet(line="lhcb2", at="ip5", x=0, px=ang_match),
    ]

    opt_a5h = match_orbit15_hv(
        collider,
        knob_fmt_on_a,
        5,
        "h",
        targets_a5h,
        ang_match * 1e6,
        twinit_zero_orbit,
        bump_range_ip5,
    )

    opt_a5h.solve()
    opt_a5h.generate_knob()

    ###############################
    ########### on_a5v ############
    ###############################
    targets_a5v = targets_close_bump + [
        xt.TargetSet(line="lhcb1", at="ip5", y=0, py=ang_match),
        xt.TargetSet(line="lhcb2", at="ip5", y=0, py=ang_match),
    ]
    opt_a5v = match_orbit15_hv(
        collider,
        knob_fmt_on_a,
        5,
        "v",
        targets_a5v,
        ang_match * 1e6,
        twinit_zero_orbit,
        bump_range_ip5,
    )

    opt_a5v.solve()
    opt_a5v.generate_knob()

    ###############################
    ########### on_ccp ###########
    ###############################
    off = 0.5

    targets_ccp1h = (
        targets_close_bump
        + [
            xt.TargetSet(line="lhcb1", at="ip1", x=0, px=0),
            xt.TargetSet(line="lhcb2", at="ip1", x=0, px=0),
        ]
        + [
            xt.TargetSet(line="lhcb1", at="acfca.4bl1.b1", x=off * 1e-3, px=0),
            xt.TargetSet(line="lhcb2", at="acfca.4bl1.b2", x=off * 1e-3, px=0),
            xt.TargetSet(line="lhcb1", at="acfca.4br1.b1", x=off * 1e-3, px=0),
            xt.TargetSet(line="lhcb2", at="acfca.4br1.b2", x=off * 1e-3, px=0),
        ]
    )

    opt_ccp1h = match_ccpm(
        collider,
        "on_ccpiphv",
        1,
        "h",
        targets_ccp1h,
        off,
        twinit_zero_orbit,
        bump_range_ip1,
    )
    opt_ccp1h.solve()
    opt_ccp1h.generate_knob()

    targets_ccp1v = (
        targets_close_bump
        + [
            xt.TargetSet(line="lhcb1", at="ip1", y=0, py=0),
            xt.TargetSet(line="lhcb2", at="ip1", y=0, py=0),
        ]
        + [
            xt.TargetSet(line="lhcb1", at="acfca.4bl1.b1", y=off * 1e-3, py=0),
            xt.TargetSet(line="lhcb2", at="acfca.4bl1.b2", y=off * 1e-3, py=0),
            xt.TargetSet(line="lhcb1", at="acfca.4br1.b1", y=off * 1e-3, py=0),
            xt.TargetSet(line="lhcb2", at="acfca.4br1.b2", y=off * 1e-3, py=0),
        ]
    )

    opt_ccp1v = match_ccpm(
        collider,
        "on_ccpiphv",
        1,
        "v",
        targets_ccp1v,
        off,
        twinit_zero_orbit,
        bump_range_ip1,
    )
    opt_ccp1v.solve()
    opt_ccp1v.generate_knob()

    targets_ccp5h = (
        targets_close_bump
        + [
            xt.TargetSet(line="lhcb1", at="ip5", x=0, px=0),
            xt.TargetSet(line="lhcb2", at="ip5", x=0, px=0),
        ]
        + [
            xt.TargetSet(line="lhcb1", at="acfca.4bl5.b1", x=off * 1e-3, px=0),
            xt.TargetSet(line="lhcb2", at="acfca.4bl5.b2", x=off * 1e-3, px=0),
            xt.TargetSet(line="lhcb1", at="acfca.4br5.b1", x=off * 1e-3, px=0),
            xt.TargetSet(line="lhcb2", at="acfca.4br5.b2", x=off * 1e-3, px=0),
        ]
    )

    opt_ccp5h = match_ccpm(
        collider,
        "on_ccpiphv",
        5,
        "h",
        targets_ccp5h,
        off,
        twinit_zero_orbit,
        bump_range_ip5,
    )
    opt_ccp5h.solve()
    opt_ccp5h.generate_knob()

    targets_ccp5v = (
        targets_close_bump
        + [
            xt.TargetSet(line="lhcb1", at="ip5", y=0, py=0),
            xt.TargetSet(line="lhcb2", at="ip5", y=0, py=0),
        ]
        + [
            xt.TargetSet(line="lhcb1", at="acfca.4bl5.b1", y=off * 1e-3, py=0),
            xt.TargetSet(line="lhcb2", at="acfca.4bl5.b2", y=off * 1e-3, py=0),
            xt.TargetSet(line="lhcb1", at="acfca.4br5.b1", y=off * 1e-3, py=0),
            xt.TargetSet(line="lhcb2", at="acfca.4br5.b2", y=off * 1e-3, py=0),
        ]
    )

    opt_ccp5v = match_ccpm(
        collider,
        "on_ccpiphv",
        5,
        "v",
        targets_ccp5v,
        off,
        twinit_zero_orbit,
        bump_range_ip5,
    )
    opt_ccp5v.solve()
    opt_ccp5v.generate_knob()

    ###############################
    ########### on_ccm ###########
    ###############################
    off = 0.5

    targets_ccm1h = (
        targets_close_bump
        + [
            xt.TargetSet(line="lhcb1", at="ip1", x=0, px=0),
            xt.TargetSet(line="lhcb2", at="ip1", x=0, px=0),
        ]
        + [
            xt.TargetSet(line="lhcb1", at="acfca.4bl1.b1", x=off * 1e-3, px=0),
            xt.TargetSet(line="lhcb2", at="acfca.4bl1.b2", x=-off * 1e-3, px=0),
            xt.TargetSet(line="lhcb1", at="acfca.4br1.b1", x=off * 1e-3, px=0),
            xt.TargetSet(line="lhcb2", at="acfca.4br1.b2", x=-off * 1e-3, px=0),
        ]
    )

    opt_ccm1h = match_ccpm(
        collider,
        "on_ccmiphv",
        1,
        "h",
        targets_ccm1h,
        off,
        twinit_zero_orbit,
        bump_range_ip1,
    )
    opt_ccm1h.solve()
    opt_ccm1h.generate_knob()

    targets_ccm1v = (
        targets_close_bump
        + [
            xt.TargetSet(line="lhcb1", at="ip1", y=0, py=0),
            xt.TargetSet(line="lhcb2", at="ip1", y=0, py=0),
        ]
        + [
            xt.TargetSet(line="lhcb1", at="acfca.4bl1.b1", y=off * 1e-3, py=0),
            xt.TargetSet(line="lhcb2", at="acfca.4bl1.b2", y=-off * 1e-3, py=0),
            xt.TargetSet(line="lhcb1", at="acfca.4br1.b1", y=off * 1e-3, py=0),
            xt.TargetSet(line="lhcb2", at="acfca.4br1.b2", y=-off * 1e-3, py=0),
        ]
    )

    opt_ccm1v = match_ccpm(
        collider,
        "on_ccmiphv",
        1,
        "v",
        targets_ccm1v,
        off,
        twinit_zero_orbit,
        bump_range_ip1,
    )
    opt_ccm1v.solve()
    opt_ccm1v.generate_knob()

    targets_ccm5h = (
        targets_close_bump
        + [
            xt.TargetSet(line="lhcb1", at="ip5", x=0, px=0),
            xt.TargetSet(line="lhcb2", at="ip5", x=0, px=0),
        ]
        + [
            xt.TargetSet(line="lhcb1", at="acfca.4bl5.b1", x=off * 1e-3, px=0),
            xt.TargetSet(line="lhcb2", at="acfca.4bl5.b2", x=-off * 1e-3, px=0),
            xt.TargetSet(line="lhcb1", at="acfca.4br5.b1", x=off * 1e-3, px=0),
            xt.TargetSet(line="lhcb2", at="acfca.4br5.b2", x=-off * 1e-3, px=0),
        ]
    )

    opt_ccm5h = match_ccpm(
        collider,
        "on_ccmiphv",
        5,
        "h",
        targets_ccm5h,
        off,
        twinit_zero_orbit,
        bump_range_ip5,
    )
    opt_ccm5h.solve()
    opt_ccm5h.generate_knob()

    targets_ccm5v = (
        targets_close_bump
        + [
            xt.TargetSet(line="lhcb1", at="ip5", y=0, py=0),
            xt.TargetSet(line="lhcb2", at="ip5", y=0, py=0),
        ]
        + [
            xt.TargetSet(line="lhcb1", at="acfca.4bl5.b1", y=off * 1e-3, py=0),
            xt.TargetSet(line="lhcb2", at="acfca.4bl5.b2", y=-off * 1e-3, py=0),
            xt.TargetSet(line="lhcb1", at="acfca.4br5.b1", y=off * 1e-3, py=0),
            xt.TargetSet(line="lhcb2", at="acfca.4br5.b2", y=-off * 1e-3, py=0),
        ]
    )

    opt_ccm5v = match_ccpm(
        collider,
        "on_ccmiphv",
        5,
        "v",
        targets_ccm5v,
        off,
        twinit_zero_orbit,
        bump_range_ip5,
    )
    opt_ccm5v.solve()
    opt_ccm5v.generate_knob()

    ###############################
    ########### on_ccs1h ##########
    ###############################
    off = 0.2

    targets_ccs1h = (
        targets_close_bump
        + [
            xt.TargetSet(line="lhcb1", at="ip1", x=0, px=0),
            xt.TargetSet(line="lhcb2", at="ip1", x=0, px=0),
        ]
        + [
            xt.TargetSet(line="lhcb1", at="acfca.4bl1.b1", x=off * 1e-3),
            xt.TargetSet(line="lhcb2", at="acfca.4bl1.b2", x=off * 1e-3),
            xt.TargetSet(line="lhcb1", at="acfca.4br1.b1", x=off * 1e-3),
            xt.TargetSet(line="lhcb2", at="acfca.4br1.b2", x=off * 1e-3),
        ]
    )

    opt_ccs1h = match_ccpm(
        collider,
        "on_ccsiphv",
        1,
        "h",
        targets_ccs1h,
        off,
        twinit_zero_orbit,
        bump_range_ip1,
    )
    opt_ccs1h.disable_vary(tag="mcbx")
    opt_ccs1h.solve()
    opt_ccs1h.generate_knob()

    ###############################
    ########### on_ccs1v ##########
    ###############################

    targets_ccs1v = (
        targets_close_bump
        + [
            xt.TargetSet(line="lhcb1", at="ip1", y=0, py=0),
            xt.TargetSet(line="lhcb2", at="ip1", y=0, py=0),
        ]
        + [
            xt.TargetSet(line="lhcb1", at="acfca.4bl1.b1", y=off * 1e-3),
            xt.TargetSet(line="lhcb2", at="acfca.4bl1.b2", y=off * 1e-3),
            xt.TargetSet(line="lhcb1", at="acfca.4br1.b1", y=off * 1e-3),
            xt.TargetSet(line="lhcb2", at="acfca.4br1.b2", y=off * 1e-3),
        ]
    )

    opt_ccs1v = match_ccpm(
        collider,
        "on_ccsiphv",
        1,
        "v",
        targets_ccs1v,
        off,
        twinit_zero_orbit,
        bump_range_ip1,
    )
    opt_ccs1v.disable_vary(tag="mcbx")
    opt_ccs1v.solve()
    opt_ccs1v.generate_knob()

    ###############################
    ########### on_ccs5h ##########
    ###############################

    targets_ccs5h = (
        targets_close_bump
        + [
            xt.TargetSet(line="lhcb1", at="ip5", x=0, px=0),
            xt.TargetSet(line="lhcb2", at="ip5", x=0, px=0),
        ]
        + [
            xt.TargetSet(line="lhcb1", at="acfca.4bl5.b1", x=off * 1e-3),
            xt.TargetSet(line="lhcb2", at="acfca.4bl5.b2", x=off * 1e-3),
            xt.TargetSet(line="lhcb1", at="acfca.4br5.b1", x=off * 1e-3),
            xt.TargetSet(line="lhcb2", at="acfca.4br5.b2", x=off * 1e-3),
        ]
    )

    opt_ccs5h = match_ccpm(
        collider,
        "on_ccsiphv",
        5,
        "h",
        targets_ccs5h,
        off,
        twinit_zero_orbit,
        bump_range_ip5,
    )
    opt_ccs5h.disable_vary(tag="mcbx")
    opt_ccs5h.solve()
    opt_ccs5h.generate_knob()

    ###############################
    ########### on_ccs5v ##########
    ###############################

    targets_ccs5v = (
        targets_close_bump
        + [
            xt.TargetSet(line="lhcb1", at="ip5", y=0, py=0),
            xt.TargetSet(line="lhcb2", at="ip5", y=0, py=0),
        ]
        + [
            xt.TargetSet(line="lhcb1", at="acfca.4bl5.b1", y=off * 1e-3),
            xt.TargetSet(line="lhcb2", at="acfca.4bl5.b2", y=off * 1e-3),
            xt.TargetSet(line="lhcb1", at="acfca.4br5.b1", y=off * 1e-3),
            xt.TargetSet(line="lhcb2", at="acfca.4br5.b2", y=off * 1e-3),
        ]
    )

    opt_ccs5v = match_ccpm(
        collider,
        "on_ccsiphv",
        5,
        "v",
        targets_ccs5v,
        off,
        twinit_zero_orbit,
        bump_range_ip5,
    )
    opt_ccs5v.disable_vary(tag="mcbx")
    opt_ccs5v.solve()
    opt_ccs5v.generate_knob()

    ################ on_o

    # Disconnect acbx2
    cvars["acbxh2.l1"] = 0
    cvars["acbxh2.r1"] = 0
    cvars["acbxh2.l5"] = 0
    cvars["acbxh2.r5"] = 0
    cvars["acbxv2.l1"] = 0
    cvars["acbxv2.r1"] = 0
    cvars["acbxv2.l5"] = 0
    cvars["acbxv2.r5"] = 0

    ipoff = 0.5
    on_o_fmt = "on_oiphv"
    ###############################
    ########### on_o1h ############
    ###############################
    targets_o1h = [
        xt.TargetSet(line="lhcb1", at=xt.END, x=0, px=0),
        xt.TargetSet(line="lhcb2", at=xt.END, x=0, px=0),
        xt.TargetSet(line="lhcb1", at="ip1", x=ipoff * 1e-3, px=0),
        xt.TargetSet(line="lhcb2", at="ip1", x=ipoff * 1e-3, px=0),
    ]

    opt_o1h = match_off(
        collider,
        on_o_fmt,
        1,
        "h",
        targets_o1h,
        ipoff,
        twinit_zero_orbit,
        bump_range_ip1,
        tolerances,
    )
    opt_o1h.solve()
    opt_o1h.generate_knob()

    ###############################
    ########### on_o1v ############
    ###############################
    targets_o1v = [
        xt.TargetSet(line="lhcb1", at=xt.END, y=0, py=0),
        xt.TargetSet(line="lhcb2", at=xt.END, y=0, py=0),
        xt.TargetSet(line="lhcb1", at="ip1", y=ipoff * 1e-3, py=0),
        xt.TargetSet(line="lhcb2", at="ip1", y=ipoff * 1e-3, py=0),
    ]

    opt_o1v = match_off(
        collider,
        on_o_fmt,
        1,
        "v",
        targets_o1v,
        ipoff,
        twinit_zero_orbit,
        bump_range_ip1,
        tolerances,
    )
    opt_o1v.solve()
    opt_o1v.generate_knob()

    ###############################
    ########### on_o5h ############
    ###############################
    targets_o5h = [
        xt.TargetSet(line="lhcb1", at=xt.END, x=0, px=0),
        xt.TargetSet(line="lhcb2", at=xt.END, x=0, px=0),
        xt.TargetSet(line="lhcb1", at="ip5", x=ipoff * 1e-3, px=0),
        xt.TargetSet(line="lhcb2", at="ip5", x=ipoff * 1e-3, px=0),
    ]

    opt_o5h = match_off(
        collider,
        on_o_fmt,
        5,
        "h",
        targets_o5h,
        ipoff,
        twinit_zero_orbit,
        bump_range_ip5,
        tolerances,
    )
    opt_o5h.solve()
    opt_o5h.generate_knob()

    ###############################
    ########### on_o5v ############
    ###############################
    targets_o5v = [
        xt.TargetSet(line="lhcb1", at=xt.END, y=0, py=0),
        xt.TargetSet(line="lhcb2", at=xt.END, y=0, py=0),
        xt.TargetSet(line="lhcb1", at="ip5", y=ipoff * 1e-3, py=0),
        xt.TargetSet(line="lhcb2", at="ip5", y=ipoff * 1e-3, py=0),
    ]

    opt_o5v = match_off(
        collider,
        on_o_fmt,
        5,
        "v",
        targets_o5v,
        ipoff,
        twinit_zero_orbit,
        bump_range_ip5,
        tolerances,
    )
    opt_o5v.solve()
    opt_o5v.generate_knob()

    opt = {
        "on_x1hs": opt_x1hs,
        "on_x1vs": opt_x1vs,
        "on_x1hl": opt_x1hl,
        "on_x1vl": opt_x1vl,
        "on_x5hs": opt_x5hs,
        "on_x5vs": opt_x5vs,
        "on_x5hl": opt_x5hl,
        "on_x5vl": opt_x5vl,
        "on_sep1h": opt_sep1h,
        "on_sep1v": opt_sep1v,
        "on_sep5h": opt_sep5h,
        "on_sep5v": opt_sep5v,
        "on_a1h": opt_a1h,
        "on_a1v": opt_a1v,
        "on_a5h": opt_a5h,
        "on_a5v": opt_a5v,
        "on_ccp1h": opt_ccp1h,
        "on_ccp1v": opt_ccp1v,
        "on_ccp5h": opt_ccp5h,
        "on_ccp5v": opt_ccp5v,
        "on_ccm1h": opt_ccm1h,
        "on_ccm1v": opt_ccm1v,
        "on_ccm5h": opt_ccm5h,
        "on_ccm5v": opt_ccm5v,
        "on_ccs1h": opt_ccs1h,
        "on_ccs1v": opt_ccs1v,
        "on_ccs5h": opt_ccs5h,
        "on_ccs5v": opt_ccs5v,
        "on_o1h": opt_o1h,
        "on_o1v": opt_o1v,
        "on_o5h": opt_o5h,
        "on_o5v": opt_o5v,
    }
    return opt


def rename_knobs_as_madx(collider):
    v = collider.vars

    knobs_mcbx = "acbxhv1.lrirn acbxhv3.lrirn"
    for lr in ["l", "r"]:
        for irn in ["1", "5"]:
            for hv in ["h", "v"]:
                for kk in knobs_mcbx.split():
                    kn = kk.replace("lr", lr).replace("irn", irn).replace("hv", hv)
                    v[kn] = (
                        v[f"{kn}_from_on_x{irn}{hv}s"]._expr
                        + v[f"{kn}_from_on_x{irn}{hv}l"]._expr
                        + v[f"{kn}_from_on_sep{irn}{hv}"]._expr
                        + v[f"{kn}_from_on_o{irn}{hv}"]._expr
                        + v[f"{kn}_from_on_a{irn}{hv}"]._expr
                        + (
                            v[f"{kn}_from_on_ccp{irn}{hv}"]._expr._lhs
                            * v[f"on_ccp{lr}{irn}{hv}"]
                        )
                        + (
                            v[f"{kn}_from_on_ccm{irn}{hv}"]._expr._lhs
                            * v[f"on_ccm{lr}{irn}{hv}"]
                        )
                    )

                    kn2 = (
                        kk.replace("hv1", "hv2")
                        .replace("lr", lr)
                        .replace("irn", irn)
                        .replace("hv", hv)
                    )
                    v[kn2] = (
                        v[f"{kn}_from_on_x{irn}{hv}s"]._expr
                        + v[f"{kn}_from_on_x{irn}{hv}l"]._expr
                        + v[f"{kn}_from_on_sep{irn}{hv}"]._expr
                        + v[f"{kn}_from_on_o{irn}{hv}"]._expr
                        + v[f"{kn}_from_on_a{irn}{hv}"]._expr
                        + (
                            v[f"{kn}_from_on_ccp{irn}{hv}"]._expr._lhs
                            * v[f"on_ccp{lr}{irn}{hv}"]
                        )
                        + (
                            v[f"{kn}_from_on_ccm{irn}{hv}"]._expr._lhs
                            * v[f"on_ccm{lr}{irn}{hv}"]
                        )
                    )

    knobs_mcbrd_hv = "acbrdhv4.lrirnb1 acbrdhv4.lrirnb2"
    knobs_mcbys_hv = "acbyhvs4.lrirnb1 acbyhvs4.lrirnb2"
    for lr in ["l", "r"]:
        for irn in ["1", "5"]:
            for hv in ["h", "v"]:
                for n1, n2 in zip(knobs_mcbrd_hv.split(), knobs_mcbys_hv.split()):
                    bim = n1[-2:]
                    kn1 = n1.replace("lr", lr).replace("hv", hv).replace("irn", irn)
                    kn2 = n2.replace("lr", lr).replace("hv", hv).replace("irn", irn)
                    v[kn1] = (
                        v[f"{kn1}aux_from_on_x{irn}{hv}s"]._expr
                        + v[f"{kn1}_from_on_sep{irn}{hv}"]._expr
                        + v[f"{kn1}_from_on_a{irn}{hv}"]._expr
                        + (
                            v[f"{kn1}_from_on_ccp{irn}{hv}"]._expr._lhs
                            * v[f"on_ccp{lr}{irn}{hv}"]
                        )
                        + (
                            v[f"{kn1}_from_on_ccm{irn}{hv}"]._expr._lhs
                            * v[f"on_ccm{lr}{irn}{hv}"]
                        )
                        + (
                            v[f"{kn1}_from_on_ccs{irn}{hv}"]._expr._lhs
                            * v[f"on_ccs{lr}{irn}{hv}{bim}"]
                        )
                    )

                    v[kn2] = (
                        v[f"{kn1}aux_from_on_x{irn}{hv}l"]._expr
                        + v[f"{kn1}_from_on_sep{irn}{hv}"]._expr
                        + v[f"{kn2}_from_on_o{irn}{hv}"]._expr
                        + (
                            v[f"{kn1}_from_on_ccp{irn}{hv}"]._expr._lhs
                            * v[f"on_ccp{lr}{irn}{hv}"]
                        )
                        + (
                            v[f"{kn1}_from_on_ccm{irn}{hv}"]._expr._lhs
                            * v[f"on_ccm{lr}{irn}{hv}"]
                        )
                        + (
                            v[f"{kn2}_from_on_ccs{irn}{hv}"]._expr._lhs
                            * v[f"on_ccs{lr}{irn}{hv}{bim}"]
                        )
                    )

    v["acbyh4.r1b1"] = (
        v["acbrdh4.r1b1aux_from_on_x1hl"]._expr
        + v["acbrdh4.r1b1_from_on_sep1h"]._expr
        + v["acbyhs4.r1b1_from_on_o1h"]._expr
        + v["acbyhs4.r1b1_from_on_ccp1h"]._expr._lhs * v["on_ccpr1h"]
        + v["acbyhs4.r1b1_from_on_ccm1h"]._expr._lhs * v["on_ccmr1h"]
        + v["acbyhs4.r1b1_from_on_ccs1h"]._expr._lhs * v["on_ccsr1hb1"]
    )
    v["acbyh4.l1b2"] = (
        v["acbrdh4.l1b2aux_from_on_x1hl"]._expr
        + v["acbrdh4.l1b2_from_on_sep1h"]._expr
        + v["acbyhs4.l1b2_from_on_o1h"]._expr
        + v["acbyhs4.l1b2_from_on_ccp1h"]._expr._lhs * v["on_ccpl1h"]
        + v["acbyhs4.l1b2_from_on_ccm1h"]._expr._lhs * v["on_ccml1h"]
        + v["acbyhs4.l1b2_from_on_ccs1h"]._expr._lhs * v["on_ccsl1hb2"]
    )
    v["acbyv4.l1b1"] = (
        v["acbrdv4.l1b1aux_from_on_x1vl"]._expr
        + v["acbrdv4.l1b1_from_on_sep1v"]._expr
        + v["acbyvs4.l1b1_from_on_o1v"]._expr
        + v["acbyvs4.l1b1_from_on_ccp1v"]._expr._lhs * v["on_ccpl1v"]
        + v["acbyvs4.l1b1_from_on_ccm1v"]._expr._lhs * v["on_ccml1v"]
        + v["acbyvs4.l1b1_from_on_ccs1v"]._expr._lhs * v["on_ccsl1vb1"]
    )
    v["acbyv4.r1b2"] = (
        v["acbrdv4.r1b2aux_from_on_x1vl"]._expr
        + v["acbrdv4.r1b2_from_on_sep1v"]._expr
        + v["acbyvs4.r1b2_from_on_o1v"]._expr
        + v["acbyvs4.r1b2_from_on_ccp1v"]._expr._lhs * v["on_ccpr1v"]
        + v["acbyvs4.r1b2_from_on_ccm1v"]._expr._lhs * v["on_ccmr1v"]
        + v["acbyvs4.r1b2_from_on_ccs1v"]._expr._lhs * v["on_ccsr1vb2"]
    )

    v["acbyh4.r5b1"] = (
        v["acbrdh4.r5b1aux_from_on_x5hl"]._expr
        + v["acbrdh4.r5b1_from_on_sep5h"]._expr
        + v["acbyhs4.r5b1_from_on_o5h"]._expr
        + v["acbyhs4.r5b1_from_on_ccp5h"]._expr._lhs * v["on_ccpr5h"]
        + v["acbyhs4.r5b1_from_on_ccm5h"]._expr._lhs * v["on_ccmr5h"]
        + v["acbyhs4.r5b1_from_on_ccs5h"]._expr._lhs * v["on_ccsr5hb1"]
    )
    v["acbyh4.l5b2"] = (
        v["acbrdh4.l5b2aux_from_on_x5hl"]._expr
        + v["acbrdh4.l5b2_from_on_sep5h"]._expr
        + v["acbyhs4.l5b2_from_on_o5h"]._expr
        + v["acbyhs4.l5b2_from_on_ccp5h"]._expr._lhs * v["on_ccpl5h"]
        + v["acbyhs4.l5b2_from_on_ccm5h"]._expr._lhs * v["on_ccml5h"]
        + v["acbyhs4.l5b2_from_on_ccs5h"]._expr._lhs * v["on_ccsl5hb2"]
    )

    v["acbyv4.l5b1"] = (
        v["acbrdv4.l5b1aux_from_on_x5vl"]._expr
        + v["acbrdv4.l5b1_from_on_sep5v"]._expr
        + v["acbyvs4.l5b1_from_on_o5v"]._expr
        + v["acbyvs4.l5b1_from_on_ccp5v"]._expr._lhs * v["on_ccpl5v"]
        + v["acbyvs4.l5b1_from_on_ccm5v"]._expr._lhs * v["on_ccml5v"]
        + v["acbyvs4.l5b1_from_on_ccs5v"]._expr._lhs * v["on_ccsl5vb1"]
    )
    v["acbyv4.r5b2"] = (
        v["acbrdv4.r5b2aux_from_on_x5vl"]._expr
        + v["acbrdv4.r5b2_from_on_sep5v"]._expr
        + v["acbyvs4.r5b2_from_on_o5v"]._expr
        + v["acbyvs4.r5b2_from_on_ccp5v"]._expr._lhs * v["on_ccpr5v"]
        + v["acbyvs4.r5b2_from_on_ccm5v"]._expr._lhs * v["on_ccmr5v"]
        + v["acbyvs4.r5b2_from_on_ccs5v"]._expr._lhs * v["on_ccsr5vb2"]
    )

    # IP1
    v["acbch5.l1b2"] = (
        v["acbch5.l1b2_from_on_o1h"]._expr
        + v["acbch5.l1b2_from_on_ccp1h"]._expr._lhs * v["on_ccpl1h"]
        + v["acbch5.l1b2_from_on_ccm1h"]._expr._lhs * v["on_ccml1h"]
    )
    v["acbch5.r1b1"] = (
        v["acbch5.r1b1_from_on_o1h"]._expr
        + v["acbch5.r1b1_from_on_ccp1h"]._expr._lhs * v["on_ccpr1h"]
        + v["acbch5.r1b1_from_on_ccm1h"]._expr._lhs * v["on_ccmr1h"]
    )
    v["acbcv5.l1b1"] = (
        v["acbcv5.l1b1_from_on_o1v"]._expr
        + v["acbcv5.l1b1_from_on_ccp1v"]._expr._lhs * v["on_ccpl1v"]
        + v["acbcv5.l1b1_from_on_ccm1v"]._expr._lhs * v["on_ccml1v"]
    )
    v["acbcv5.r1b2"] = (
        v["acbcv5.r1b2_from_on_o1v"]._expr
        + v["acbcv5.r1b2_from_on_ccp1v"]._expr._lhs * v["on_ccpr1v"]
        + v["acbcv5.r1b2_from_on_ccm1v"]._expr._lhs * v["on_ccmr1v"]
    )

    v["acbch6.l1b1"] = (
        v["acbch6.l1b1_from_on_o1h"]._expr
        + v["acbch6.l1b1_from_on_ccp1h"]._expr._lhs * v["on_ccpl1h"]
        + v["acbch6.l1b1_from_on_ccm1h"]._expr._lhs * v["on_ccml1h"]
    )
    v["acbch6.r1b2"] = (
        v["acbch6.r1b2_from_on_o1h"]._expr
        + v["acbch6.r1b2_from_on_ccp1h"]._expr._lhs * v["on_ccpr1h"]
        + v["acbch6.r1b2_from_on_ccm1h"]._expr._lhs * v["on_ccmr1h"]
    )
    v["acbcv6.l1b2"] = (
        v["acbcv6.l1b2_from_on_o1v"]._expr
        + v["acbcv6.l1b2_from_on_ccp1v"]._expr._lhs * v["on_ccpl1v"]
        + v["acbcv6.l1b2_from_on_ccm1v"]._expr._lhs * v["on_ccml1v"]
    )
    v["acbcv6.r1b1"] = (
        v["acbcv6.r1b1_from_on_o1v"]._expr
        + v["acbcv6.r1b1_from_on_ccp1v"]._expr._lhs * v["on_ccpr1v"]
        + v["acbcv6.r1b1_from_on_ccm1v"]._expr._lhs * v["on_ccmr1v"]
    )

    # IP5
    v["acbch5.l5b2"] = (
        v["acbch5.l5b2_from_on_o5h"]._expr
        + v["acbch5.l5b2_from_on_ccp5h"]._expr._lhs * v["on_ccpl5h"]
        + v["acbch5.l5b2_from_on_ccm5h"]._expr._lhs * v["on_ccml5h"]
    )
    v["acbch5.r5b1"] = (
        v["acbch5.r5b1_from_on_o5h"]._expr
        + v["acbch5.r5b1_from_on_ccp5h"]._expr._lhs * v["on_ccpr5h"]
        + v["acbch5.r5b1_from_on_ccm5h"]._expr._lhs * v["on_ccmr5h"]
    )
    v["acbcv5.l5b1"] = (
        v["acbcv5.l5b1_from_on_o5v"]._expr
        + v["acbcv5.l5b1_from_on_ccp5v"]._expr._lhs * v["on_ccpl5v"]
        + v["acbcv5.l5b1_from_on_ccm5v"]._expr._lhs * v["on_ccml5v"]
    )
    v["acbcv5.r5b2"] = (
        v["acbcv5.r5b2_from_on_o5v"]._expr
        + v["acbcv5.r5b2_from_on_ccp5v"]._expr._lhs * v["on_ccpr5v"]
        + v["acbcv5.r5b2_from_on_ccm5v"]._expr._lhs * v["on_ccmr5v"]
    )

    v["acbch6.l5b1"] = (
        v["acbch6.l5b1_from_on_o5h"]._expr
        + v["acbch6.l5b1_from_on_ccp5h"]._expr._lhs * v["on_ccpl5h"]
        + v["acbch6.l5b1_from_on_ccm5h"]._expr._lhs * v["on_ccml5h"]
    )
    v["acbch6.r5b2"] = (
        v["acbch6.r5b2_from_on_o5h"]._expr
        + v["acbch6.r5b2_from_on_ccp5h"]._expr._lhs * v["on_ccpr5h"]
        + v["acbch6.r5b2_from_on_ccm5h"]._expr._lhs * v["on_ccmr5h"]
    )
    v["acbcv6.l5b2"] = (
        v["acbcv6.l5b2_from_on_o5v"]._expr
        + v["acbcv6.l5b2_from_on_ccp5v"]._expr._lhs * v["on_ccpl5v"]
        + v["acbcv6.l5b2_from_on_ccm5v"]._expr._lhs * v["on_ccml5v"]
    )
    v["acbcv6.r5b1"] = (
        v["acbcv6.r5b1_from_on_o5v"]._expr
        + v["acbcv6.r5b1_from_on_ccp5v"]._expr._lhs * v["on_ccpr5v"]
        + v["acbcv6.r5b1_from_on_ccm5v"]._expr._lhs * v["on_ccmr5v"]
    )

    # IP1
    v["acbch7.l1b2"] = v["acbch7.l1b2_from_on_o1h"]._expr._lhs * v["on_o1h"]
    v["acbch7.r1b1"] = v["acbch7.r1b1_from_on_o1h"]._expr._lhs * v["on_o1h"]
    v["acbcv7.l1b1"] = v["acbcv7.l1b1_from_on_o1v"]._expr._lhs * v["on_o1v"]
    v["acbcv7.r1b2"] = v["acbcv7.r1b2_from_on_o1v"]._expr._lhs * v["on_o1v"]

    # IP5
    v["acbch7.l5b2"] = v["acbch7.l5b2_from_on_o5h"]._expr._lhs * v["on_o5h"]
    v["acbch7.r5b1"] = v["acbch7.r5b1_from_on_o5h"]._expr._lhs * v["on_o5h"]
    v["acbcv7.l5b1"] = v["acbcv7.l5b1_from_on_o5v"]._expr._lhs * v["on_o5v"]
    v["acbcv7.r5b2"] = v["acbcv7.r5b2_from_on_o5v"]._expr._lhs * v["on_o5v"]

    f = collider.functions
    v["phi_ir1"] = 0.0
    v["phi_ir5"] = 90.0
    v["cd2q4"] = 0
    for irn in [1, 5]:
        v[f"cphi_ir{irn}"] = f.cos(v[f"phi_ir{irn}"] * v['pi'] / 180.0)
        v[f"sphi_ir{irn}"] = f.sin(v[f"phi_ir{irn}"] * v['pi'] / 180.0)
        v[f"on_x{irn}hs"]  =  (1.0 - v["cd2q4"]) * v[f"on_x{irn}"] * v[f"cphi_ir{irn}"]
        v[f"on_x{irn}hl"]  =  v["cd2q4"] * v[f"on_x{irn}"] * v[f"cphi_ir{irn}"]
        v[f"on_x{irn}vs"]  =  (1.0 - v["cd2q4"]) * v[f"on_x{irn}"] * v[f"sphi_ir{irn}"]
        v[f"on_x{irn}vl"]  =  v["cd2q4"] * v[f"on_x{irn}"] * v[f"sphi_ir{irn}"]
        v[f"on_sep{irn}h"] = -v[f"on_sep{irn}"] * v[f"sphi_ir{irn}"]
        v[f"on_sep{irn}v"] =  v[f"on_sep{irn}"] * v[f"cphi_ir{irn}"]
        v[f"on_a{irn}h"]   = -v[f"on_a{irn}"] * v[f"sphi_ir{irn}"]
        v[f"on_a{irn}v"]   =  v[f"on_a{irn}"] * v[f"cphi_ir{irn}"]
        v[f"on_o{irn}h"]   =  v[f"on_o{irn}"] * v[f"cphi_ir{irn}"]
        v[f"on_o{irn}v"]   =  v[f"on_o{irn}"] * v[f"sphi_ir{irn}"]


        v[f'xip{irn}b1'] = +1e-3*v[f'on_sep{irn}h'] + 1e-3*v[f'on_o{irn}h']
        v[f'xip{irn}b2'] = -1e-3*v[f'on_sep{irn}h'] + 1e-3*v[f'on_o{irn}h']
        v[f'yip{irn}b1'] = +1e-3*v[f'on_sep{irn}v'] + 1e-3*v[f'on_o{irn}v']
        v[f'yip{irn}b2'] = -1e-3*v[f'on_sep{irn}v'] + 1e-3*v[f'on_o{irn}v']

        v[f'pxip{irn}b1'] = +1e-6*v[f'on_x{irn}hs'] + 1e-6*v[f'on_x{irn}hl'] + 1e-6*v[f'on_a{irn}h']
        v[f'pxip{irn}b2'] = -1e-6*v[f'on_x{irn}hs'] - 1e-6*v[f'on_x{irn}hl'] + 1e-6*v[f'on_a{irn}h']
        v[f'pyip{irn}b1'] = +1e-6*v[f'on_x{irn}vs'] + 1e-6*v[f'on_x{irn}vl'] + 1e-6*v[f'on_a{irn}v']
        v[f'pyip{irn}b2'] = -1e-6*v[f'on_x{irn}vs'] - 1e-6*v[f'on_x{irn}vl'] + 1e-6*v[f'on_a{irn}v']
