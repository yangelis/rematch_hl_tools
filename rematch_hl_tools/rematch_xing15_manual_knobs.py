import numpy as np
import xtrack as xt

from .match_limits_steps import set_var_limits_and_steps_correctors_on_o

def get_cc_names(hl_version='1.6'):
    ''' 
    Crab names for the match of orbit knobs in IP1, IP5
    '''
    crabs = {}
    crabs['ip1'] = {}
    crabs["ip5"] = {}
    if hl_version == '1.9':
        crabs['ip1']['b1'] = ["acfcah.b4l1.b1", "acfcah.b4r1.b1"]
        crabs["ip5"]['b1'] = ["acfcav.b4l5.b1", "acfcav.b4r5.b1"]
        crabs['ip1']['b2'] = ["acfcah.b4l1.b2", "acfcah.b4r1.b2"]
        crabs["ip5"]['b2'] = ["acfcav.b4l5.b2", "acfcav.b4r5.b2"]

    elif hl_version == '1.6':
        crabs['ip1']['b1'] = ["acfca.4bl1.b1", "acfca.4br1.b1"]
        crabs["ip5"]['b1'] = ["acfca.4bl5.b1", "acfca.4br5.b1"]
        crabs['ip1']['b2'] = ["acfca.4bl1.b2", "acfca.4br1.b2"]
        crabs["ip5"]['b2'] = ["acfca.4bl5.b2", "acfca.4br5.b2"]

    return crabs


def match_xing15_hv(
    collider,
    ip,
    hv,
    targets,
    twinit_zero_orbit,
    bump_range_ip,
    tolerances=None,
):
    opt_x = collider.match(
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
        solve=False,
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
    ip,
    hv,
    targets,
    twinit_zero_orbit,
    bump_range_ip,
    tolerances=None,
):
    opt_x = collider.match(
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
        solve=False,
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
    ip,
    hv,
    targets,
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

    opt_x = collider.match(
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
        solve=False,
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
    ip,
    hv,
    targets,
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

    opt_x = collider.match(
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
        solve=False,
        assert_within_tol=False,
        restore_if_fail=False,
        init=twinit_zero_orbit,
        n_steps_max=30,
        default_tol=tolerances,
        **bump_range_ip,
    )

    return opt_x


def save_vals_and_reset(knobs_vals, collider, optimizer, matched_val, knob):
    for vary in optimizer.vary:
        knobs_vals[knob][vary.name] = (
            collider.varval[vary.name] / (matched_val) * collider.vars[knob]
        )
        collider.vars[vary.name] = 0


def save_vals_and_reset_cc(knobs_vals, collider, optimizer, matched_val, knob):
    for vary in optimizer.vary:
        knobs_vals[knob][vary.name] = collider.varval[vary.name] / (matched_val)
        collider.vars[vary.name] = 0


def match_orbit_knobs_ip15_manual(
    collider,
    tolerances=None,
    first_pass=True,
    angle_match=295,
    sep_match=2,
    aangle_match=1,
    hl_version='1.6',
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

    knobs_vals = {
        "on_x1hs": {},
        "on_x1vs": {},
        "on_x1hl": {},
        "on_x1vl": {},
        "on_x5hs": {},
        "on_x5vs": {},
        "on_x5hl": {},
        "on_x5vl": {},
        "on_sep1h": {},
        "on_sep1v": {},
        "on_sep5h": {},
        "on_sep5v": {},
        "on_a1h": {},
        "on_a1v": {},
        "on_a5h": {},
        "on_a5v": {},
        "on_ccp1h": {},
        "on_ccp1v": {},
        "on_ccp5h": {},
        "on_ccp5v": {},
        "on_ccm1h": {},
        "on_ccm1v": {},
        "on_ccm5h": {},
        "on_ccm5v": {},
        "on_ccs1h": {},
        "on_ccs1v": {},
        "on_ccs5h": {},
        "on_ccs5v": {},
        "on_o1h": {},
        "on_o1v": {},
        "on_o5h": {},
        "on_o5v": {},
    }

    ###############################
    ########### on_x1hs ###########
    ###############################
    cvars["cd2q4"] = 0
    print("Matching on_x1hs")
    opt_x1hs = match_xing15_hv(
        collider,
        1,
        "h",
        targets_x1h,
        twinit_zero_orbit,
        bump_range_ip1,
        tolerances=tolerances,
    )
    opt_x1hs.solve()
    save_vals_and_reset(knobs_vals, collider, opt_x1hs, angle_match * 1e6, "on_x1hs")

    ###############################
    ########### on_x1vs ###########
    ###############################
    cvars["cd2q4"] = 0
    print("Matching on_x1vs")
    opt_x1vs = match_xing15_hv(
        collider,
        1,
        "v",
        targets_x1v,
        twinit_zero_orbit,
        bump_range_ip1,
        tolerances=tolerances,
    )
    opt_x1vs.solve()
    save_vals_and_reset(knobs_vals, collider, opt_x1vs, angle_match * 1e6, "on_x1vs")

    ###############################
    ########### on_x1hl ###########
    ###############################
    cvars["cd2q4"] = 1
    print("Matching on_x1hl")
    opt_x1hl = match_xing15_hv(
        collider,
        1,
        "h",
        targets_x1h,
        twinit_zero_orbit,
        bump_range_ip1,
        tolerances=tolerances,
    )
    opt_x1hl.solve()
    save_vals_and_reset(knobs_vals, collider, opt_x1hl, angle_match * 1e6, "on_x1hl")

    ###############################
    ########### on_x1vl ###########
    ###############################
    cvars["cd2q4"] = 1
    print("Matching on_x1vl")
    opt_x1vl = match_xing15_hv(
        collider,
        1,
        "v",
        targets_x1v,
        twinit_zero_orbit,
        bump_range_ip1,
        tolerances,
    )
    opt_x1vl.solve()
    save_vals_and_reset(knobs_vals, collider, opt_x1vl, angle_match * 1e6, "on_x1vl")

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
    print("Matching on_x5hs")
    opt_x5hs = match_xing15_hv(
        collider,
        5,
        "h",
        targets_x5h,
        twinit_zero_orbit,
        bump_range_ip5,
        tolerances,
    )
    opt_x5hs.solve()
    save_vals_and_reset(knobs_vals, collider, opt_x5hs, angle_match * 1e6, "on_x5hs")

    ###############################
    ########### on_x5vs ###########
    ###############################
    cvars["cd2q4"] = 0
    print("Matching on_x5vs")
    opt_x5vs = match_xing15_hv(
        collider,
        5,
        "v",
        targets_x5v,
        twinit_zero_orbit,
        bump_range_ip5,
        tolerances,
    )
    opt_x5vs.solve()
    save_vals_and_reset(knobs_vals, collider, opt_x5vs, angle_match * 1e6, "on_x5vs")

    ###############################
    ########### on_x5hl ###########
    ###############################
    cvars["cd2q4"] = 1
    print("Matching on_x5hl")
    opt_x5hl = match_xing15_hv(
        collider,
        5,
        "h",
        targets_x5h,
        twinit_zero_orbit,
        bump_range_ip5,
        tolerances,
    )
    opt_x5hl.solve()
    save_vals_and_reset(knobs_vals, collider, opt_x5hl, angle_match * 1e6, "on_x5hl")

    ###############################
    ########### on_x5vl ###########
    ###############################
    cvars["cd2q4"] = 1
    print("Matching on_x5vl")
    opt_x5vl = match_xing15_hv(
        collider,
        5,
        "v",
        targets_x5v,
        twinit_zero_orbit,
        bump_range_ip5,
        tolerances,
    )
    opt_x5vl.solve()
    save_vals_and_reset(knobs_vals, collider, opt_x5vl, angle_match * 1e6, "on_x5vl")

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

    cvars["cd2q4"] = 1
    print("Matching on_sep1h")
    opt_sep1h = match_orbit15_hv(
        collider,
        1,
        "h",
        targets_sep1h,
        twinit_zero_orbit,
        bump_range_ip1,
        tolerances,
    )
    opt_sep1h.solve()
    save_vals_and_reset(knobs_vals, collider, opt_sep1h, sep_match * 1e3, "on_sep1h")

    ###############################
    ########### on_sep1v ##########
    ###############################
    targets_sep1v = targets_close_bump + [
        xt.TargetSet(line="lhcb1", at="ip1", y=sep_match, py=0),
        xt.TargetSet(line="lhcb2", at="ip1", y=-sep_match, py=0),
    ]

    cvars["cd2q4"] = 1
    print("Matching on_sep1v")
    opt_sep1v = match_orbit15_hv(
        collider,
        1,
        "v",
        targets_sep1v,
        twinit_zero_orbit,
        bump_range_ip1,
        tolerances,
    )
    opt_sep1v.solve()
    save_vals_and_reset(knobs_vals, collider, opt_sep1v, sep_match * 1e3, "on_sep1v")

    ###############################
    ########### on_sep5h ##########
    ###############################
    targets_sep5h = targets_close_bump + [
        xt.TargetSet(line="lhcb1", at="ip5", x=sep_match, px=0),
        xt.TargetSet(line="lhcb2", at="ip5", x=-sep_match, px=0),
    ]

    cvars["cd2q4"] = 1
    print("Matching on_sep5h")
    opt_sep5h = match_orbit15_hv(
        collider,
        5,
        "h",
        targets_sep5h,
        twinit_zero_orbit,
        bump_range_ip5,
        tolerances,
    )
    opt_sep5h.solve()
    save_vals_and_reset(knobs_vals, collider, opt_sep5h, sep_match * 1e3, "on_sep5h")

    ###############################
    ########### on_sep5v ##########
    ###############################
    targets_sep5v = targets_close_bump + [
        xt.TargetSet(line="lhcb1", at="ip5", y=sep_match, py=0),
        xt.TargetSet(line="lhcb2", at="ip5", y=-sep_match, py=0),
    ]

    cvars["cd2q4"] = 1
    print("Matching on_sep5v")
    opt_sep5v = match_orbit15_hv(
        collider,
        5,
        "v",
        targets_sep5v,
        twinit_zero_orbit,
        bump_range_ip5,
        tolerances,
    )
    opt_sep5v.solve()
    save_vals_and_reset(knobs_vals, collider, opt_sep5v, sep_match * 1e3, "on_sep5v")

    # To ignore acby connection from before set cd2q4 to zero
    cvars["cd2q4"] = 0

    ###############################
    ########### on_a1h ############
    ###############################

    targets_a1h = targets_close_bump + [
        xt.TargetSet(line="lhcb1", at="ip1", x=0, px=aangle_match),
        xt.TargetSet(line="lhcb2", at="ip1", x=0, px=aangle_match),
    ]

    print("Matching on_a1h")
    opt_a1h = match_orbit15_hv(
        collider,
        1,
        "h",
        targets_a1h,
        twinit_zero_orbit,
        bump_range_ip1,
        tolerances,
    )
    opt_a1h.solve()
    save_vals_and_reset(knobs_vals, collider, opt_a1h, aangle_match * 1e6, "on_a1h")

    ###############################
    ########### on_a1v ############
    ###############################
    targets_a1v = targets_close_bump + [
        xt.TargetSet(line="lhcb1", at="ip1", y=0, py=aangle_match),
        xt.TargetSet(line="lhcb2", at="ip1", y=0, py=aangle_match),
    ]

    print("Matching on_a1v")
    opt_a1v = match_orbit15_hv(
        collider,
        1,
        "v",
        targets_a1v,
        twinit_zero_orbit,
        bump_range_ip1,
        tolerances,
    )
    opt_a1v.solve()
    save_vals_and_reset(knobs_vals, collider, opt_a1v, aangle_match * 1e6, "on_a1v")

    ###############################
    ########### on_a5h ############
    ###############################
    ang_match = 1e-6
    targets_a5h = targets_close_bump + [
        xt.TargetSet(line="lhcb1", at="ip5", x=0, px=ang_match),
        xt.TargetSet(line="lhcb2", at="ip5", x=0, px=ang_match),
    ]

    print("Matching on_a5h")
    opt_a5h = match_orbit15_hv(
        collider,
        5,
        "h",
        targets_a5h,
        twinit_zero_orbit,
        bump_range_ip5,
        tolerances,
    )
    opt_a5h.solve()
    save_vals_and_reset(knobs_vals, collider, opt_a5h, aangle_match * 1e6, "on_a5h")

    ###############################
    ########### on_a5v ############
    ###############################
    targets_a5v = targets_close_bump + [
        xt.TargetSet(line="lhcb1", at="ip5", y=0, py=ang_match),
        xt.TargetSet(line="lhcb2", at="ip5", y=0, py=ang_match),
    ]

    print("Matching on_a5v")
    opt_a5v = match_orbit15_hv(
        collider,
        5,
        "v",
        targets_a5v,
        twinit_zero_orbit,
        bump_range_ip5,
        tolerances,
    )
    opt_a5v.solve()
    save_vals_and_reset(knobs_vals, collider, opt_a5v, aangle_match * 1e6, "on_a5v")

     # Get correct crab names
    crab_names = get_cc_names(hl_version=hl_version) 

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
            xt.TargetSet(line="lhcb1", at=crab_names['ip1']['b1'][0], x=off * 1e-3, px=0),
            xt.TargetSet(line="lhcb2", at=crab_names['ip1']['b2'][0], x=off * 1e-3, px=0),
            xt.TargetSet(line="lhcb1", at=crab_names['ip1']['b1'][1], x=off * 1e-3, px=0),
            xt.TargetSet(line="lhcb2", at=crab_names['ip1']['b2'][1], x=off * 1e-3, px=0),
        ]
    )

    print("Matching on_ccp1h")
    opt_ccp1h = match_ccpm(
        collider,
        1,
        "h",
        targets_ccp1h,
        twinit_zero_orbit,
        bump_range_ip1,
        tolerances,
    )
    opt_ccp1h.solve()
    save_vals_and_reset_cc(knobs_vals, collider, opt_ccp1h, off, "on_ccp1h")

    targets_ccp1v = (
        targets_close_bump
        + [
            xt.TargetSet(line="lhcb1", at="ip1", y=0, py=0),
            xt.TargetSet(line="lhcb2", at="ip1", y=0, py=0),
        ]
        + [
            xt.TargetSet(line="lhcb1", at=crab_names['ip1']['b1'][0], y=off * 1e-3, py=0),
            xt.TargetSet(line="lhcb2", at=crab_names['ip1']['b2'][0], y=off * 1e-3, py=0),
            xt.TargetSet(line="lhcb1", at=crab_names['ip1']['b1'][1], y=off * 1e-3, py=0),
            xt.TargetSet(line="lhcb2", at=crab_names['ip1']['b2'][1], y=off * 1e-3, py=0),
        ]
    )

    print("Matching on_ccp1v")
    opt_ccp1v = match_ccpm(
        collider,
        1,
        "v",
        targets_ccp1v,
        twinit_zero_orbit,
        bump_range_ip1,
        tolerances,
    )
    opt_ccp1v.solve()
    save_vals_and_reset_cc(knobs_vals, collider, opt_ccp1v, off, "on_ccp1v")

    targets_ccp5h = (
        targets_close_bump
        + [
            xt.TargetSet(line="lhcb1", at="ip5", x=0, px=0),
            xt.TargetSet(line="lhcb2", at="ip5", x=0, px=0),
        ]
        + [
            xt.TargetSet(line="lhcb1", at=crab_names['ip5']['b1'][0], x=off * 1e-3, px=0),
            xt.TargetSet(line="lhcb2", at=crab_names['ip5']['b2'][0], x=off * 1e-3, px=0),
            xt.TargetSet(line="lhcb1", at=crab_names['ip5']['b1'][1], x=off * 1e-3, px=0),
            xt.TargetSet(line="lhcb2", at=crab_names['ip5']['b2'][1], x=off * 1e-3, px=0),
        ]
    )

    print("Matching on_ccp5h")
    opt_ccp5h = match_ccpm(
        collider,
        5,
        "h",
        targets_ccp5h,
        twinit_zero_orbit,
        bump_range_ip5,
        tolerances,
    )
    opt_ccp5h.solve()
    save_vals_and_reset_cc(knobs_vals, collider, opt_ccp5h, off, "on_ccp5h")

    targets_ccp5v = (
        targets_close_bump
        + [
            xt.TargetSet(line="lhcb1", at="ip5", y=0, py=0),
            xt.TargetSet(line="lhcb2", at="ip5", y=0, py=0),
        ]
        + [
            xt.TargetSet(line="lhcb1", at=crab_names['ip5']['b1'][0], y=off * 1e-3, py=0),
            xt.TargetSet(line="lhcb2", at=crab_names['ip5']['b2'][0], y=off * 1e-3, py=0),
            xt.TargetSet(line="lhcb1", at=crab_names['ip5']['b1'][1], y=off * 1e-3, py=0),
            xt.TargetSet(line="lhcb2", at=crab_names['ip5']['b2'][1], y=off * 1e-3, py=0),
        ]
    )

    print("Matching on_ccp5v")
    opt_ccp5v = match_ccpm(
        collider,
        5,
        "v",
        targets_ccp5v,
        twinit_zero_orbit,
        bump_range_ip5,
        tolerances,
    )
    opt_ccp5v.solve()
    save_vals_and_reset_cc(knobs_vals, collider, opt_ccp5v, off, "on_ccp5v")

    ###############################
    ########### on_ccm ############
    ###############################
    off = 0.5

    targets_ccm1h = (
        targets_close_bump
        + [
            xt.TargetSet(line="lhcb1", at="ip1", x=0, px=0),
            xt.TargetSet(line="lhcb2", at="ip1", x=0, px=0),
        ]
        + [
            xt.TargetSet(line="lhcb1", at=crab_names['ip1']['b1'][0], x=off * 1e-3, px=0),
            xt.TargetSet(line="lhcb2", at=crab_names['ip1']['b2'][0], x=-off * 1e-3, px=0),
            xt.TargetSet(line="lhcb1", at=crab_names['ip1']['b1'][1], x=off * 1e-3, px=0),
            xt.TargetSet(line="lhcb2", at=crab_names['ip1']['b2'][1], x=-off * 1e-3, px=0),
        ]
    )

    print("Matching on_ccm1h")
    opt_ccm1h = match_ccpm(
        collider,
        1,
        "h",
        targets_ccm1h,
        twinit_zero_orbit,
        bump_range_ip1,
        tolerances,
    )
    opt_ccm1h.solve()
    save_vals_and_reset_cc(knobs_vals, collider, opt_ccm1h, off, "on_ccm1h")

    targets_ccm1v = (
        targets_close_bump
        + [
            xt.TargetSet(line="lhcb1", at="ip1", y=0, py=0),
            xt.TargetSet(line="lhcb2", at="ip1", y=0, py=0),
        ]
        + [
            xt.TargetSet(line="lhcb1", at=crab_names['ip1']['b1'][0], y=off * 1e-3, py=0),
            xt.TargetSet(line="lhcb2", at=crab_names['ip1']['b2'][0], y=-off * 1e-3, py=0),
            xt.TargetSet(line="lhcb1", at=crab_names['ip1']['b1'][1], y=off * 1e-3, py=0),
            xt.TargetSet(line="lhcb2", at=crab_names['ip1']['b2'][1], y=-off * 1e-3, py=0),
        ]
    )

    print("Matching on_ccm1v")
    opt_ccm1v = match_ccpm(
        collider,
        1,
        "v",
        targets_ccm1v,
        twinit_zero_orbit,
        bump_range_ip1,
        tolerances,
    )
    opt_ccm1v.solve()
    save_vals_and_reset_cc(knobs_vals, collider, opt_ccm1v, off, "on_ccm1v")

    targets_ccm5h = (
        targets_close_bump
        + [
            xt.TargetSet(line="lhcb1", at="ip5", x=0, px=0),
            xt.TargetSet(line="lhcb2", at="ip5", x=0, px=0),
        ]
        + [
            xt.TargetSet(line="lhcb1", at=crab_names['ip5']['b1'][0], x=off * 1e-3, px=0),
            xt.TargetSet(line="lhcb2", at=crab_names['ip5']['b2'][0], x=-off * 1e-3, px=0),
            xt.TargetSet(line="lhcb1", at=crab_names['ip5']['b1'][1], x=off * 1e-3, px=0),
            xt.TargetSet(line="lhcb2", at=crab_names['ip5']['b2'][1], x=-off * 1e-3, px=0),
        ]
    )

    print("Matching on_ccm5h")
    opt_ccm5h = match_ccpm(
        collider,
        5,
        "h",
        targets_ccm5h,
        twinit_zero_orbit,
        bump_range_ip5,
        tolerances,
    )
    opt_ccm5h.solve()
    save_vals_and_reset_cc(knobs_vals, collider, opt_ccm5h, off, "on_ccm5h")

    targets_ccm5v = (
        targets_close_bump
        + [
            xt.TargetSet(line="lhcb1", at="ip5", y=0, py=0),
            xt.TargetSet(line="lhcb2", at="ip5", y=0, py=0),
        ]
        + [
            xt.TargetSet(line="lhcb1", at=crab_names['ip5']['b1'][0], y=off * 1e-3, py=0),
            xt.TargetSet(line="lhcb2", at=crab_names['ip5']['b2'][0], y=-off * 1e-3, py=0),
            xt.TargetSet(line="lhcb1", at=crab_names['ip5']['b1'][1], y=off * 1e-3, py=0),
            xt.TargetSet(line="lhcb2", at=crab_names['ip5']['b2'][1], y=-off * 1e-3, py=0),
        ]
    )

    print("Matching on_ccm5v")
    opt_ccm5v = match_ccpm(
        collider,
        5,
        "v",
        targets_ccm5v,
        twinit_zero_orbit,
        bump_range_ip5,
        tolerances,
    )
    opt_ccm5v.solve()
    save_vals_and_reset_cc(knobs_vals, collider, opt_ccm5v, off, "on_ccm5v")

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
            xt.TargetSet(line="lhcb1", at=crab_names['ip1']['b1'][0], x=off * 1e-3),
            xt.TargetSet(line="lhcb2", at=crab_names['ip1']['b2'][0], x=off * 1e-3),
            xt.TargetSet(line="lhcb1", at=crab_names['ip1']['b1'][1], x=off * 1e-3),
            xt.TargetSet(line="lhcb2", at=crab_names['ip1']['b2'][1], x=off * 1e-3),
        ]
    )

    print("Matching on_ccs1h")
    opt_ccs1h = match_ccpm(
        collider,
        1,
        "h",
        targets_ccs1h,
        twinit_zero_orbit,
        bump_range_ip1,
        tolerances,
    )
    opt_ccs1h.disable_vary(tag="mcbx")
    opt_ccs1h.solve()
    save_vals_and_reset_cc(knobs_vals, collider, opt_ccs1h, off, "on_ccs1h")

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
            xt.TargetSet(line="lhcb1", at=crab_names['ip1']['b1'][0], y=off * 1e-3),
            xt.TargetSet(line="lhcb2", at=crab_names['ip1']['b2'][0], y=off * 1e-3),
            xt.TargetSet(line="lhcb1", at=crab_names['ip1']['b1'][1], y=off * 1e-3),
            xt.TargetSet(line="lhcb2", at=crab_names['ip1']['b2'][1], y=off * 1e-3),
        ]
    )

    print("Matching on_ccs1v")
    opt_ccs1v = match_ccpm(
        collider,
        1,
        "v",
        targets_ccs1v,
        twinit_zero_orbit,
        bump_range_ip1,
        tolerances,
    )
    opt_ccs1v.disable_vary(tag="mcbx")
    opt_ccs1v.solve()
    save_vals_and_reset_cc(knobs_vals, collider, opt_ccs1v, off, "on_ccs1v")

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
            xt.TargetSet(line="lhcb1", at=crab_names['ip5']['b1'][0], x=off * 1e-3),
            xt.TargetSet(line="lhcb2", at=crab_names['ip5']['b2'][0], x=off * 1e-3),
            xt.TargetSet(line="lhcb1", at=crab_names['ip5']['b1'][1], x=off * 1e-3),
            xt.TargetSet(line="lhcb2", at=crab_names['ip5']['b2'][1], x=off * 1e-3),
        ]
    )

    print("Matching on_ccs5h")
    opt_ccs5h = match_ccpm(
        collider,
        5,
        "h",
        targets_ccs5h,
        twinit_zero_orbit,
        bump_range_ip5,
        tolerances,
    )
    opt_ccs5h.disable_vary(tag="mcbx")
    opt_ccs5h.solve()
    save_vals_and_reset_cc(knobs_vals, collider, opt_ccs5h, off, "on_ccs5h")

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
            xt.TargetSet(line="lhcb1", at=crab_names['ip5']['b1'][0], y=off * 1e-3),
            xt.TargetSet(line="lhcb2", at=crab_names['ip5']['b2'][0], y=off * 1e-3),
            xt.TargetSet(line="lhcb1", at=crab_names['ip5']['b1'][1], y=off * 1e-3),
            xt.TargetSet(line="lhcb2", at=crab_names['ip5']['b2'][1], y=off * 1e-3),
        ]
    )

    print("Matching on_ccs5v")
    opt_ccs5v = match_ccpm(
        collider,
        5,
        "v",
        targets_ccs5v,
        twinit_zero_orbit,
        bump_range_ip5,
        tolerances,
    )
    opt_ccs5v.disable_vary(tag="mcbx")
    opt_ccs5v.solve()
    save_vals_and_reset_cc(knobs_vals, collider, opt_ccs5v, off, "on_ccs5v")

    ### offset
    set_var_limits_and_steps_correctors_on_o(collider)

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
    ###############################
    ########### on_o1h ############
    ###############################
    targets_o1h = [
        xt.TargetSet(line="lhcb1", at=xt.END, x=0, px=0),
        xt.TargetSet(line="lhcb2", at=xt.END, x=0, px=0),
        xt.TargetSet(line="lhcb1", at="ip1", x=ipoff * 1e-3, px=0),
        xt.TargetSet(line="lhcb2", at="ip1", x=ipoff * 1e-3, px=0),
    ]
    print("Matching on_o1h")
    opt_o1h = match_off(
        collider,
        1,
        "h",
        targets_o1h,
        twinit_zero_orbit,
        bump_range_ip1,
        tolerances,
    )
    opt_o1h.solve()
    save_vals_and_reset(knobs_vals, collider, opt_o1h, ipoff, "on_o1h")

    ###############################
    ########### on_o1v ############
    ###############################
    targets_o1v = [
        xt.TargetSet(line="lhcb1", at=xt.END, y=0, py=0),
        xt.TargetSet(line="lhcb2", at=xt.END, y=0, py=0),
        xt.TargetSet(line="lhcb1", at="ip1", y=ipoff * 1e-3, py=0),
        xt.TargetSet(line="lhcb2", at="ip1", y=ipoff * 1e-3, py=0),
    ]
    print("Matching on_o1v")
    opt_o1v = match_off(
        collider,
        1,
        "v",
        targets_o1v,
        twinit_zero_orbit,
        bump_range_ip1,
        tolerances,
    )
    opt_o1v.solve()
    save_vals_and_reset(knobs_vals, collider, opt_o1v, ipoff, "on_o1v")

    ###############################
    ########### on_o5h ############
    ###############################
    targets_o5h = [
        xt.TargetSet(line="lhcb1", at=xt.END, x=0, px=0),
        xt.TargetSet(line="lhcb2", at=xt.END, x=0, px=0),
        xt.TargetSet(line="lhcb1", at="ip5", x=ipoff * 1e-3, px=0),
        xt.TargetSet(line="lhcb2", at="ip5", x=ipoff * 1e-3, px=0),
    ]
    print("Matching on_o5h")
    opt_o5h = match_off(
        collider,
        5,
        "h",
        targets_o5h,
        twinit_zero_orbit,
        bump_range_ip5,
        tolerances,
    )
    opt_o5h.solve()
    save_vals_and_reset(knobs_vals, collider, opt_o5h, ipoff, "on_o5h")

    ###############################
    ########### on_o5v ############
    ###############################
    targets_o5v = [
        xt.TargetSet(line="lhcb1", at=xt.END, y=0, py=0),
        xt.TargetSet(line="lhcb2", at=xt.END, y=0, py=0),
        xt.TargetSet(line="lhcb1", at="ip5", y=ipoff * 1e-3, py=0),
        xt.TargetSet(line="lhcb2", at="ip5", y=ipoff * 1e-3, py=0),
    ]
    print("Matching on_o5v")
    opt_o5v = match_off(
        collider,
        5,
        "v",
        targets_o5v,
        twinit_zero_orbit,
        bump_range_ip5,
        tolerances,
    )
    opt_o5v.solve()
    save_vals_and_reset(knobs_vals, collider, opt_o5v, ipoff, "on_o5v")

    rename_knobs_as_madx(collider, knobs_vals)

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


def rename_knobs_as_madx(collider, knobs_vals):

    # Fix knob expressions manually
    v = collider.vars

    knobs_mcbx = "acbxhv1.lrirn acbxhv3.lrirn"
    for lr in ["l", "r"]:
        for irn in ["1", "5"]:
            for hv in ["h", "v"]:
                for kk in knobs_mcbx.split():
                    kn = kk.replace("lr", lr).replace("irn", irn).replace("hv", hv)
                    v[kn] = (
                        knobs_vals[f"on_x{irn}{hv}s"][kn]
                        + knobs_vals[f"on_x{irn}{hv}l"][kn]
                        + knobs_vals[f"on_sep{irn}{hv}"][kn]
                        + knobs_vals[f"on_o{irn}{hv}"][kn]
                        + knobs_vals[f"on_a{irn}{hv}"][kn]
                        + knobs_vals[f"on_ccp{irn}{hv}"][kn] * v[f"on_ccp{lr}{irn}{hv}"]
                        + knobs_vals[f"on_ccm{irn}{hv}"][kn] * v[f"on_ccm{lr}{irn}{hv}"]
                    )

                    kn2 = (
                        kk.replace("hv1", "hv2")
                        .replace("lr", lr)
                        .replace("irn", irn)
                        .replace("hv", hv)
                    )
                    v[kn2] = (
                        knobs_vals[f"on_x{irn}{hv}s"][kn]
                        + knobs_vals[f"on_x{irn}{hv}l"][kn]
                        + knobs_vals[f"on_sep{irn}{hv}"][kn]
                        + knobs_vals[f"on_o{irn}{hv}"][kn2]
                        + knobs_vals[f"on_a{irn}{hv}"][kn]
                        + knobs_vals[f"on_ccp{irn}{hv}"][kn] * v[f"on_ccp{lr}{irn}{hv}"]
                        + knobs_vals[f"on_ccm{irn}{hv}"][kn] * v[f"on_ccm{lr}{irn}{hv}"]
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
                        knobs_vals[f"on_x{irn}{hv}s"][f"{kn1}aux"]
                        + knobs_vals[f"on_sep{irn}{hv}"][kn1]
                        + knobs_vals[f"on_a{irn}{hv}"][kn1]
                        + knobs_vals[f"on_ccp{irn}{hv}"][kn1]
                        * v[f"on_ccp{lr}{irn}{hv}"]
                        + knobs_vals[f"on_ccm{irn}{hv}"][kn1]
                        * v[f"on_ccm{lr}{irn}{hv}"]
                        + knobs_vals[f"on_ccs{irn}{hv}"][kn1]
                        * v[f"on_ccs{lr}{irn}{hv}{bim}"]
                    )

                    v[kn2] = (
                        knobs_vals[f"on_x{irn}{hv}l"][f"{kn1}aux"]
                        + knobs_vals[f"on_sep{irn}{hv}"][kn1]
                        + knobs_vals[f"on_o{irn}{hv}"][kn2]
                        + knobs_vals[f"on_ccp{irn}{hv}"][kn1]
                        * v[f"on_ccp{lr}{irn}{hv}"]
                        + knobs_vals[f"on_ccm{irn}{hv}"][kn1]
                        * v[f"on_ccm{lr}{irn}{hv}"]
                        + knobs_vals[f"on_ccs{irn}{hv}"][kn2]
                        * v[f"on_ccs{lr}{irn}{hv}{bim}"]
                    )

    v["acbyh4.r1b1"] = (
        knobs_vals["on_x1hl"]["acbrdh4.r1b1aux"]
        + knobs_vals["on_sep1h"]["acbrdh4.r1b1"]
        + knobs_vals["on_o1h"]["acbyhs4.r1b1"]
        + knobs_vals["on_ccp1h"]["acbyhs4.r1b1"] * v["on_ccpr1h"]
        + knobs_vals["on_ccm1h"]["acbyhs4.r1b1"] * v["on_ccmr1h"]
        + knobs_vals["on_ccs1h"]["acbyhs4.r1b1"] * v["on_ccsr1hb1"]
    )
    v["acbyh4.l1b2"] = (
        knobs_vals["on_x1hl"]["acbrdh4.l1b2aux"]
        + knobs_vals["on_sep1h"]["acbrdh4.l1b2"]
        + knobs_vals["on_o1h"]["acbyhs4.l1b2"]
        + knobs_vals["on_ccp1h"]["acbyhs4.l1b2"] * v["on_ccpl1h"]
        + knobs_vals["on_ccm1h"]["acbyhs4.l1b2"] * v["on_ccml1h"]
        + knobs_vals["on_ccs1h"]["acbyhs4.l1b2"] * v["on_ccsl1hb2"]
    )
    v["acbyv4.l1b1"] = (
        knobs_vals["on_x1vl"]["acbrdv4.l1b1aux"]
        + knobs_vals["on_sep1v"]["acbrdv4.l1b1"]
        + knobs_vals["on_o1v"]["acbyvs4.l1b1"]
        + knobs_vals["on_ccp1v"]["acbyvs4.l1b1"] * v["on_ccpl1v"]
        + knobs_vals["on_ccm1v"]["acbyvs4.l1b1"] * v["on_ccml1v"]
        + knobs_vals["on_ccs1v"]["acbyvs4.l1b1"] * v["on_ccsl1vb1"]
    )
    v["acbyv4.r1b2"] = (
        knobs_vals["on_x1vl"]["acbrdv4.r1b2aux"]
        + knobs_vals["on_sep1v"]["acbrdv4.r1b2"]
        + knobs_vals["on_o1v"]["acbyvs4.r1b2"]
        + knobs_vals["on_ccp1v"]["acbyvs4.r1b2"] * v["on_ccpr1v"]
        + knobs_vals["on_ccm1v"]["acbyvs4.r1b2"] * v["on_ccmr1v"]
        + knobs_vals["on_ccs1v"]["acbyvs4.r1b2"] * v["on_ccsr1vb2"]
    )

    v["acbyh4.r5b1"] = (
        knobs_vals["on_x5hl"]["acbrdh4.r5b1aux"]
        + knobs_vals["on_sep5h"]["acbrdh4.r5b1"]
        + knobs_vals["on_o5h"]["acbyhs4.r5b1"]
        + knobs_vals["on_ccp5h"]["acbyhs4.r5b1"] * v["on_ccpr5h"]
        + knobs_vals["on_ccm5h"]["acbyhs4.r5b1"] * v["on_ccmr5h"]
        + knobs_vals["on_ccs5h"]["acbyhs4.r5b1"] * v["on_ccsr5hb1"]
    )
    v["acbyh4.l5b2"] = (
        knobs_vals["on_x5hl"]["acbrdh4.l5b2aux"]
        + knobs_vals["on_sep5h"]["acbrdh4.l5b2"]
        + knobs_vals["on_o5h"]["acbyhs4.l5b2"]
        + knobs_vals["on_ccp5h"]["acbyhs4.l5b2"] * v["on_ccpl5h"]
        + knobs_vals["on_ccm5h"]["acbyhs4.l5b2"] * v["on_ccml5h"]
        + knobs_vals["on_ccs5h"]["acbyhs4.l5b2"] * v["on_ccsl5hb2"]
    )

    v["acbyv4.l5b1"] = (
        knobs_vals["on_x5vl"]["acbrdv4.l5b1aux"]
        + knobs_vals["on_sep5v"]["acbrdv4.l5b1"]
        + knobs_vals["on_o5v"]["acbyvs4.l5b1"]
        + knobs_vals["on_ccp5v"]["acbyvs4.l5b1"] * v["on_ccpl5v"]
        + knobs_vals["on_ccm5v"]["acbyvs4.l5b1"] * v["on_ccml5v"]
        + knobs_vals["on_ccs5v"]["acbyvs4.l5b1"] * v["on_ccsl5vb1"]
    )
    v["acbyv4.r5b2"] = (
        knobs_vals["on_x5vl"]["acbrdv4.r5b2aux"]
        + knobs_vals["on_sep5v"]["acbrdv4.r5b2"]
        + knobs_vals["on_o5v"]["acbyvs4.r5b2"]
        + knobs_vals["on_ccp5v"]["acbyvs4.r5b2"] * v["on_ccpr5v"]
        + knobs_vals["on_ccm5v"]["acbyvs4.r5b2"] * v["on_ccmr5v"]
        + knobs_vals["on_ccs5v"]["acbyvs4.r5b2"] * v["on_ccsr5vb2"]
    )

    acbc5_fmt = "acbchv"
    dir_dict = {
        "5": {"h": ["lipb2", "ripb1"], "v": ["lipb1", "ripb2"]},
        "6": {"h": ["lipb1", "ripb2"], "v": ["lipb2", "ripb1"]},
    }

    # IP1
    v["acbch5.l1b2"] = (
        knobs_vals["on_o1h"]["acbch5.l1b2"]
        + knobs_vals["on_ccp1h"]["acbch5.l1b2"] * v["on_ccpl1h"]
        + knobs_vals["on_ccm1h"]["acbch5.l1b2"] * v["on_ccml1h"]
    )
    v["acbch5.r1b1"] = (
        knobs_vals["on_o1h"]["acbch5.r1b1"]
        + knobs_vals["on_ccp1h"]["acbch5.r1b1"] * v["on_ccpr1h"]
        + knobs_vals["on_ccm1h"]["acbch5.r1b1"] * v["on_ccmr1h"]
    )
    v["acbcv5.l1b1"] = (
        knobs_vals["on_o1v"]["acbcv5.l1b1"]
        + knobs_vals["on_ccp1v"]["acbcv5.l1b1"] * v["on_ccpl1v"]
        + knobs_vals["on_ccm1v"]["acbcv5.l1b1"] * v["on_ccml1v"]
    )
    v["acbcv5.r1b2"] = (
        knobs_vals["on_o1v"]["acbcv5.r1b2"]
        + knobs_vals["on_ccp1v"]["acbcv5.r1b2"] * v["on_ccpr1v"]
        + knobs_vals["on_ccm1v"]["acbcv5.r1b2"] * v["on_ccmr1v"]
    )

    v["acbch6.l1b1"] = (
        knobs_vals["on_o1h"]["acbch6.l1b1"]
        + knobs_vals["on_ccp1h"]["acbch6.l1b1"] * v["on_ccpl1h"]
        + knobs_vals["on_ccm1h"]["acbch6.l1b1"] * v["on_ccml1h"]
    )
    v["acbch6.r1b2"] = (
        knobs_vals["on_o1h"]["acbch6.r1b2"]
        + knobs_vals["on_ccp1h"]["acbch6.r1b2"] * v["on_ccpr1h"]
        + knobs_vals["on_ccm1h"]["acbch6.r1b2"] * v["on_ccmr1h"]
    )
    v["acbcv6.l1b2"] = (
        knobs_vals["on_o1v"]["acbcv6.l1b2"]
        + knobs_vals["on_ccp1v"]["acbcv6.l1b2"] * v["on_ccpl1v"]
        + knobs_vals["on_ccm1v"]["acbcv6.l1b2"] * v["on_ccml1v"]
    )
    v["acbcv6.r1b1"] = (
        knobs_vals["on_o1v"]["acbcv6.r1b1"]
        + knobs_vals["on_ccp1v"]["acbcv6.r1b1"] * v["on_ccpr1v"]
        + knobs_vals["on_ccm1v"]["acbcv6.r1b1"] * v["on_ccmr1v"]
    )

    # IP5
    v["acbch5.l5b2"] = (
        knobs_vals["on_o5h"]["acbch5.l5b2"]
        + knobs_vals["on_ccp5h"]["acbch5.l5b2"] * v["on_ccpl5h"]
        + knobs_vals["on_ccm5h"]["acbch5.l5b2"] * v["on_ccml5h"]
    )
    v["acbch5.r5b1"] = (
        knobs_vals["on_o5h"]["acbch5.r5b1"]
        + knobs_vals["on_ccp5h"]["acbch5.r5b1"] * v["on_ccpr5h"]
        + knobs_vals["on_ccm5h"]["acbch5.r5b1"] * v["on_ccmr5h"]
    )
    v["acbcv5.l5b1"] = (
        knobs_vals["on_o5v"]["acbcv5.l5b1"]
        + knobs_vals["on_ccp5v"]["acbcv5.l5b1"] * v["on_ccpl5v"]
        + knobs_vals["on_ccm5v"]["acbcv5.l5b1"] * v["on_ccml5v"]
    )
    v["acbcv5.r5b2"] = (
        knobs_vals["on_o5v"]["acbcv5.r5b2"]
        + knobs_vals["on_ccp5v"]["acbcv5.r5b2"] * v["on_ccpr5v"]
        + knobs_vals["on_ccm5v"]["acbcv5.r5b2"] * v["on_ccmr5v"]
    )

    v["acbch6.l5b1"] = (
        knobs_vals["on_o5h"]["acbch6.l5b1"]
        + knobs_vals["on_ccp5h"]["acbch6.l5b1"] * v["on_ccpl5h"]
        + knobs_vals["on_ccm5h"]["acbch6.l5b1"] * v["on_ccml5h"]
    )
    v["acbch6.r5b2"] = (
        knobs_vals["on_o5h"]["acbch6.r5b2"]
        + knobs_vals["on_ccp5h"]["acbch6.r5b2"] * v["on_ccpr5h"]
        + knobs_vals["on_ccm5h"]["acbch6.r5b2"] * v["on_ccmr5h"]
    )
    v["acbcv6.l5b2"] = (
        knobs_vals["on_o5v"]["acbcv6.l5b2"]
        + knobs_vals["on_ccp5v"]["acbcv6.l5b2"] * v["on_ccpl5v"]
        + knobs_vals["on_ccm5v"]["acbcv6.l5b2"] * v["on_ccml5v"]
    )
    v["acbcv6.r5b1"] = (
        knobs_vals["on_o5v"]["acbcv6.r5b1"]
        + knobs_vals["on_ccp5v"]["acbcv6.r5b1"] * v["on_ccpr5v"]
        + knobs_vals["on_ccm5v"]["acbcv6.r5b1"] * v["on_ccmr5v"]
    )

    # IP1
    v["acbch7.l1b2"] = knobs_vals["on_o1h"]["acbch7.l1b2"]
    v["acbch7.r1b1"] = knobs_vals["on_o1h"]["acbch7.r1b1"]
    v["acbcv7.l1b1"] = knobs_vals["on_o1v"]["acbcv7.l1b1"]
    v["acbcv7.r1b2"] = knobs_vals["on_o1v"]["acbcv7.r1b2"]

    # IP5
    v["acbch7.l5b2"] = knobs_vals["on_o5h"]["acbch7.l5b2"]
    v["acbch7.r5b1"] = knobs_vals["on_o5h"]["acbch7.r5b1"]
    v["acbcv7.l5b1"] = knobs_vals["on_o5v"]["acbcv7.l5b1"]
    v["acbcv7.r5b2"] = knobs_vals["on_o5v"]["acbcv7.r5b2"]

    f = collider.functions
    v["phi_ir1"] = 0.0
    v["phi_ir5"] = 90.0
    v["cd2q4"] = 0
    for irn in [1, 5]:
        v[f"cphi_ir{irn}"] = f.cos(v[f"phi_ir{irn}"] * np.pi / 180.0)
        v[f"sphi_ir{irn}"] = f.sin(v[f"phi_ir{irn}"] * np.pi / 180.0)
        v[f"on_x{irn}hs"] = (1.0 - v["cd2q4"]) * v[f"on_x{irn}"] * v[f"cphi_ir{irn}"]
        v[f"on_x{irn}hl"] = v["cd2q4"] * v[f"on_x{irn}"] * v[f"cphi_ir{irn}"]
        v[f"on_x{irn}vs"] = (1.0 - v["cd2q4"]) * v[f"on_x{irn}"] * v[f"sphi_ir{irn}"]
        v[f"on_x{irn}vl"] = v["cd2q4"] * v[f"on_x{irn}"] * v[f"sphi_ir{irn}"]
        v[f"on_sep{irn}h"] = -v[f"on_sep{irn}"] * v[f"sphi_ir{irn}"]
        v[f"on_sep{irn}v"] = v[f"on_sep{irn}"] * v[f"cphi_ir{irn}"]
        v[f"on_a{irn}h"] = -v[f"on_a{irn}"] * v[f"sphi_ir{irn}"]
        v[f"on_a{irn}v"] = v[f"on_a{irn}"] * v[f"cphi_ir{irn}"]
        v[f"on_o{irn}h"] = v[f"on_o{irn}"] * v[f"cphi_ir{irn}"]
        v[f"on_o{irn}v"] = v[f"on_o{irn}"] * v[f"sphi_ir{irn}"]

        v[f'xip{irn}b1'] = +1e-3*v[f'on_sep{irn}h'] + 1e-3*v[f'on_o{irn}h']
        v[f'xip{irn}b2'] = -1e-3*v[f'on_sep{irn}h'] + 1e-3*v[f'on_o{irn}h']
        v[f'yip{irn}b1'] = +1e-3*v[f'on_sep{irn}v'] + 1e-3*v[f'on_o{irn}v']
        v[f'yip{irn}b2'] = -1e-3*v[f'on_sep{irn}v'] + 1e-3*v[f'on_o{irn}v']

        v[f'pxip{irn}b1'] = +1e-6*v[f'on_x{irn}hs'] + 1e-6*v[f'on_x{irn}hl'] + 1e-6*v[f'on_a{irn}h']
        v[f'pxip{irn}b2'] = -1e-6*v[f'on_x{irn}hs'] - 1e-6*v[f'on_x{irn}hl'] + 1e-6*v[f'on_a{irn}h']
        v[f'pyip{irn}b1'] = +1e-6*v[f'on_x{irn}vs'] + 1e-6*v[f'on_x{irn}vl'] + 1e-6*v[f'on_a{irn}v']
        v[f'pyip{irn}b2'] = -1e-6*v[f'on_x{irn}vs'] - 1e-6*v[f'on_x{irn}vl'] + 1e-6*v[f'on_a{irn}v']
