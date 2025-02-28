import xtrack as xt
import xtrack._temp.lhc_match as lm
import numpy as np

default_tol = {
    None: 1e-8,
    "betx": 1e-6,
    "bety": 1e-6,
}  # to have no rematching w.r.t. madx


def connect_lr_qx(collider, nqx=0, ir=5):
    """Connect specified right kqx in IP5 of IP1 with the left kqx"""
    assert ir == 1 or ir == 5
    collider.vars[f"kqx{nqx}.r{ir}"] = -collider.vars[f"kqx{nqx}.l{ir}"]


def connect_lr_qs(collider, nq=0, ir=5, bim=1):
    """Connect specified kq in ir for either beam with the left kq"""
    collider.vars[f"kq{nq}.r{ir}b{bim}"] = -collider.vars[f"kq{nq}.l{ir}b{bim}"]


def connect_q2s(collider, ir=5):
    """Connect Q2 in IP5, or IP1 to be used as one for matching"""
    assert ir == 1 or ir == 5
    collider.vars[f"kqx2b.l{ir}"] = +collider.vars[f"kqx2a.l{ir}"]
    collider.vars[f"kqx2a.r{ir}"] = -collider.vars[f"kqx2a.l{ir}"]
    collider.vars[f"kqx2b.r{ir}"] = -collider.vars[f"kqx2a.l{ir}"]


def rematch_ir15(
    collider,
    betxip5,
    betyip5,
    tw_sq_a45_ip5_a56=None,
    match_on_triplet=0,
    match_inj_tunes=0,
    no_match_beta=False,
    ir5q4sym=0,
    ir5q5sym=0,
    ir5q6sym=0,
    restore=True,
    solve=False,
    ratio_at_CC=1.0,
    beta_peak_ratio=0.995,
    n_steps=25,
    extra_targets=None,
):
    """Match IP5 for the beta_x, beta_y, and copy strenghts to IP1

    Parameters
    ----------
    collider : xtrack.Multiline
        HL-LHC collider with b1 and b2
    betxip5 : float
        betax for ip1 and ip5
    betyip5 : float
        betay for ip1 and ip5
    tw_sq_a45_ip5_a56 : dict
        Dictionary for beam1, beam2 with twiss tables for arcs 45, 56
    match_on_triplet: int
        Flag to select how to match the triplet.
        0 : Don't touch the triplet
        1 : Q1, Q2, Q3 free
        2 : Q2 free
        3 :
        4 : Link Q1 with Q3
        5 : Match on max(betax)/max(betay)
    match_inj_tunes: bool
    no_match_beta: bool
        If False, match beta at the ip
    ir5q4sym: int
        Flag to connect Q4
        0 : Connect Q4 left for both beams and Q4 right for both beams
        1 : Connect Q4 left and right
    ir5q5sym: int
        Flag to connect Q5
        0 : Connect Q5 left for both beams and Q5 right for both beams
        1 : Connect Q5 left and right
    ir5q6sym: int
        Flag to connect Q6
        0 : Connect Q6 left for both beams and Q6 right for both beams
        1 : Connect Q6 left and right
    restore: bool
        Flag to restore the variables if the match fails
    solve: bool
        Flag to solve or not

    """
    imb = 1.50

    if tw_sq_a45_ip5_a56 is None:
        tw_sq_a45_ip5_a56 = lm.get_arc_periodic_solution(
            collider, arc_name=["45", "56"]
        )

    targets = []

    if no_match_beta == False:
        targets.append(
            xt.TargetSet(
                line="lhcb1",
                at="ip5",
                betx=betxip5,
                bety=betyip5,
                alfx=0,
                alfy=0,
                dx=0,
                dpx=0,
            )
        )
        targets.append(
            xt.TargetSet(
                line="lhcb2",
                at="ip5",
                betx=betxip5,
                bety=betyip5,
                alfx=0,
                alfy=0,
                dx=0,
                dpx=0,
            )
        )
    else:
        targets.append(
            xt.TargetSet(line="lhcb1", at="ip5", alfx=0, alfy=0, dx=0, dpx=0)
        )
        targets.append(
            xt.TargetSet(line="lhcb2", at="ip5", alfx=0, alfy=0, dx=0, dpx=0)
        )

    targets.append(
        xt.TargetSet(
            line="lhcb1",
            at="e.ds.r5.b1",
            betx=tw_sq_a45_ip5_a56["lhcb1"]["56"]["betx", "e.ds.r5.b1"],
            bety=tw_sq_a45_ip5_a56["lhcb1"]["56"]["bety", "e.ds.r5.b1"],
            alfx=tw_sq_a45_ip5_a56["lhcb1"]["56"]["alfx", "e.ds.r5.b1"],
            alfy=tw_sq_a45_ip5_a56["lhcb1"]["56"]["alfy", "e.ds.r5.b1"],
            dx=tw_sq_a45_ip5_a56["lhcb1"]["56"]["dx", "e.ds.r5.b1"],
            dpx=tw_sq_a45_ip5_a56["lhcb1"]["56"]["dpx", "e.ds.r5.b1"],
        )
    )
    targets.append(
        xt.TargetSet(
            line="lhcb2",
            at="e.ds.r5.b2",
            betx=tw_sq_a45_ip5_a56["lhcb2"]["56"]["betx", "e.ds.r5.b2"],
            bety=tw_sq_a45_ip5_a56["lhcb2"]["56"]["bety", "e.ds.r5.b2"],
            alfx=tw_sq_a45_ip5_a56["lhcb2"]["56"]["alfx", "e.ds.r5.b2"],
            alfy=tw_sq_a45_ip5_a56["lhcb2"]["56"]["alfy", "e.ds.r5.b2"],
            dx=tw_sq_a45_ip5_a56["lhcb2"]["56"]["dx", "e.ds.r5.b2"],
            dpx=tw_sq_a45_ip5_a56["lhcb2"]["56"]["dpx", "e.ds.r5.b2"],
        )
    )

    muxIP5b1_l = collider["lhcb1"].varval["muxip5b1_l"]
    muxIP5b1_r = collider["lhcb1"].varval["muxip5b1_r"]
    muyIP5b1_l = collider["lhcb1"].varval["muyip5b1_l"]
    muyIP5b1_r = collider["lhcb1"].varval["muyip5b1_r"]
    muxIP5b1 = muxIP5b1_l + muxIP5b1_r
    muyIP5b1 = muyIP5b1_l + muyIP5b1_r

    muxIP5b2_l = collider["lhcb2"].varval["muxip5b2_l"]
    muxIP5b2_r = collider["lhcb2"].varval["muxip5b2_r"]
    muyIP5b2_l = collider["lhcb2"].varval["muyip5b2_l"]
    muyIP5b2_r = collider["lhcb2"].varval["muyip5b2_r"]
    muxIP5b2 = muxIP5b2_l + muxIP5b2_r
    muyIP5b2 = muyIP5b2_l + muyIP5b2_r

    if match_inj_tunes == 0:
        targets.append(
            xt.TargetSet(line="lhcb1", at="ip5", mux=muxIP5b1_l, muy=muyIP5b1_l)
        )
        targets.append(
            xt.TargetSet(line="lhcb1", at="e.ds.r5.b1", mux=muxIP5b1, muy=muyIP5b1)
        )
        targets.append(
            xt.TargetSet(line="lhcb2", at="ip5", mux=muxIP5b2_l, muy=muyIP5b2_l)
        )
        targets.append(
            xt.TargetSet(line="lhcb2", at="e.ds.r5.b2", mux=muxIP5b2, muy=muyIP5b2)
        )

    else:
        targets.append(
            xt.TargetSet(
                line="lhcb1",
                at="e.ds.r5.b1",
                mux=muxIP5b1,
                muy=muyIP5b1,
            )
        )
        targets.append(
            xt.TargetSet(
                line="lhcb2",
                at="e.ds.r5.b2",
                mux=muxIP5b2,
                muy=muyIP5b2,
            )
        )

    if extra_targets is not None:
        if isinstance(extra_targets, xt.Target) or isinstance(
            extra_targets, xt.TargetSet
        ):
            targets.append(extra_targets)
        if isinstance(extra_targets, list):
            targets += extra_targets

    vary_list = []

    if ir5q4sym == 0:
        collider.vars["imq4l"] = (
            -collider.vars["kq4.l5b2"] / collider.vars["kq4.l5b1"] / 100
        )
        collider.vars["imq4r"] = (
            -collider.vars["kq4.r5b2"] / collider.vars["kq4.r5b1"] / 100
        )

        collider.vars["kq4.l5b2"] = -(
            collider.vars["kq4.l5b1"] * collider.vars["imq4l"] * 100
        )
        collider.vars["kq4.r5b2"] = -(
            collider.vars["kq4.r5b1"] * collider.vars["imq4r"] * 100
        )

        if (
            collider.varval["imq4l"] < 1 / imb / 100
            or collider.varval["imq4l"] > imb / 100
        ):
            collider.vars["imq4l"]._set_value(1 / imb / 100)
        if (
            collider.varval["imq4r"] < 1 / imb / 100
            or collider.varval["imq4r"] > imb / 100
        ):
            collider.vars["imq4r"]._set_value(1 / imb / 100)

        vary_list.append(xt.Vary("imq4l", limits=(1 / imb / 100, imb / 100), step=1e-6))
        vary_list.append(xt.Vary("imq4r", limits=(1 / imb / 100, imb / 100), step=1e-6))
        vary_list.append(xt.Vary("kq4.l5b1"))
        vary_list.append(xt.Vary("kq4.r5b1"))
    elif ir5q4sym == 1:
        connect_lr_qs(collider, nq=4, ir=5, bim=1)
        connect_lr_qs(collider, nq=4, ir=5, bim=2)
        vary_list.append(xt.Vary("kq4.l5b1"))
        vary_list.append(xt.Vary("kq4.l5b2"))

    if ir5q5sym == 0:
        collider.vars["imq5l"] = (
            -collider.vars["kq5.l5b2"] / collider.vars["kq5.l5b1"] / 100
        )
        collider.vars["imq5r"] = (
            -collider.vars["kq5.r5b2"] / collider.vars["kq5.r5b1"] / 100
        )

        collider.vars["kq5.l5b2"] = -(
            collider.vars["kq5.l5b1"] * collider.vars["imq5l"] * 100
        )
        collider.vars["kq5.r5b2"] = -(
            collider.vars["kq5.r5b1"] * collider.vars["imq5r"] * 100
        )

        if (
            collider.varval["imq5l"] < 1 / imb / 100
            or collider.varval["imq5l"] > imb / 100
        ):
            collider.vars["imq5l"]._set_value(1 / imb / 100)
        if (
            collider.varval["imq5r"] < 1 / imb / 100
            or collider.varval["imq5r"] > imb / 100
        ):
            collider.vars["imq5r"]._set_value(1 / imb / 100)

        vary_list.append(xt.Vary("imq5l", limits=(1 / imb / 100, imb / 100), step=1e-6))
        vary_list.append(xt.Vary("imq5r", limits=(1 / imb / 100, imb / 100), step=1e-6))
        vary_list.append(xt.Vary("kq5.l5b1"))
        vary_list.append(xt.Vary("kq5.r5b1"))
    elif ir5q5sym == 1:
        connect_lr_qs(collider, nq=5, ir=5, bim=1)
        connect_lr_qs(collider, nq=5, ir=5, bim=2)
        vary_list.append(xt.Vary("kq5.l5b1"))
        vary_list.append(xt.Vary("kq5.l5b2"))

    if ir5q6sym == 0:
        collider.vars["imq6l"] = (
            -collider.vars["kq6.l5b2"] / collider.vars["kq6.l5b1"] / 100
        )
        collider.vars["imq6r"] = (
            -collider.vars["kq6.r5b2"] / collider.vars["kq6.r5b1"] / 100
        )

        collider.vars["kq6.l5b2"] = -(
            collider.vars["kq6.l5b1"] * collider.vars["imq6l"] * 100
        )
        collider.vars["kq6.r5b2"] = -(
            collider.vars["kq6.r5b1"] * collider.vars["imq6r"] * 100
        )

        if (
            collider.varval["imq6l"] < 1 / imb / 100
            or collider.varval["imq6l"] > imb / 100
        ):
            collider.vars["imq6l"]._set_value(1 / imb / 100)
        if (
            collider.varval["imq6r"] < 1 / imb / 100
            or collider.varval["imq6r"] > imb / 100
        ):
            collider.vars["imq6r"]._set_value(1 / imb / 100)

        vary_list.append(xt.Vary("imq6l", limits=(1 / imb / 100, imb / 100), step=1e-6))
        vary_list.append(xt.Vary("imq6r", limits=(1 / imb / 100, imb / 100), step=1e-6))
        vary_list.append(xt.Vary("kq6.l5b1"))
        vary_list.append(xt.Vary("kq6.r5b1"))
    elif ir5q6sym == 1:
        connect_lr_qs(collider, nq=6, ir=5, bim=1)
        connect_lr_qs(collider, nq=6, ir=5, bim=2)
        vary_list.append(xt.Vary("kq6.l5b1"))
        vary_list.append(xt.Vary("kq6.l5b2"))

    quads_ir5_b1 = (
        "kq4.l5b1 kq4.r5b1 kq5.l5b1 kq5.r5b1 kq6.l5b1 kq6.r5b1 "
        "kq7.l5b1 kq7.r5b1 kq8.l5b1 kq8.r5b1 kq9.l5b1 kq9.r5b1 "
        "kq10.l5b1 kq10.r5b1 kqtl11.l5b1 kqtl11.r5b1 "
        "kqt12.l5b1 kqt12.r5b1 kqt13.l5b1 kqt13.r5b1"
    )

    quads_ir5_b2 = (
        "kq4.l5b2 kq4.r5b2 kq5.l5b2 kq5.r5b2 kq6.l5b2 kq6.r5b2 "
        "kq7.l5b2 kq7.r5b2 kq8.l5b2 kq8.r5b2 kq9.l5b2 kq9.r5b2 "
        "kq10.l5b2 kq10.r5b2 kqtl11.l5b2 kqtl11.r5b2 kqt12.l5b2 "
        "kqt12.r5b2 kqt13.l5b2 kqt13.r5b2"
    )
    # Beam 1
    for quad in quads_ir5_b1.split()[6:]:
        vary_list.append(xt.Vary(quad))

    # Beam 2
    for quad in quads_ir5_b2.split()[6:]:
        vary_list.append(xt.Vary(quad))

    if match_on_triplet == 0:  # q1 q2 q3 untouched
        pass
    elif match_on_triplet == 1:  # Q1 Q2 Q3 free
        connect_q2s(collider)
        connect_lr_qx(collider, 1)
        connect_lr_qx(collider, 3)
        vary_list.append(xt.Vary("kqx1.l5"))
        vary_list.append(xt.Vary("kqx2a.l5"))
        vary_list.append(xt.Vary("kqx3.l5"))
    elif match_on_triplet == 2:
        # connect kqx2a and kqx2b left and right
        connect_q2s(collider)
        vary_list.append(xt.Vary("kqx2a.l5"))
    elif match_on_triplet == 4:
        # link q3 and q1

        connect_lr_qx(collider, 1)
        collider.vars["kqx3.l5"] = +collider.vars["kqx1.l5"]
        collider.vars["kqx3.r5"] = -collider.vars["kqx1.l5"]

        connect_q2s(collider)
        vary_list.append(xt.Vary("kqx1.l5"))
        vary_list.append(xt.Vary("kqx2a.l5"))
    elif match_on_triplet == 5:
        connect_q2s(collider)
        connect_lr_qx(collider, 1)
        connect_lr_qx(collider, 3)
        vary_list.append(xt.Vary("kqx1.l5"))
        vary_list.append(xt.Vary("kqx2a.l5"))
        # Ratio of max betas in x and y
        targets.append(
            xt.Target(
                lambda tt: np.max(tt.lhcb1.rows["ip5":"ip5>>70"].betx)
                / np.max(tt.lhcb1.rows["ip5":"ip5>>70"].bety),
                value=beta_peak_ratio,
                tol=1e-2,
            )
        )

    twiss_init_b1 = tw_sq_a45_ip5_a56["lhcb1"]["45"].get_twiss_init("s.ds.l5.b1")
    twiss_init_b1.mux = 0
    twiss_init_b1.muy = 0

    twiss_init_b2 = tw_sq_a45_ip5_a56["lhcb2"]["45"].get_twiss_init("s.ds.l5.b2")
    twiss_init_b2.mux = 0
    twiss_init_b2.muy = 0

    opt = collider.match(
        solve=False,
        only_markers=False,
        method="4d",
        solver_options={"n_bisections": 3, "min_step": 1e-7, "n_steps_max": n_steps},
        default_tol=default_tol,
        start=["s.ds.l5.b1", "s.ds.l5.b2"],
        end=["e.ds.r5.b1", "e.ds.r5.b2"],
        restore_if_fail=restore,
        assert_within_tol=False,
        init=[twiss_init_b1, twiss_init_b2],
        targets=targets,
        vary=vary_list,
        verbose=False,
    )

    if solve:
        opt.solve()

    collider.vars["kqx1.r5"] = -collider.varval["kqx1.l5"]
    collider.vars["kqx2.l5"] = collider.varval["kqx2a.l5"]
    collider.vars["kqx2a.l5"] = collider.varval["kqx2.l5"]
    collider.vars["kqx2b.l5"] = collider.varval["kqx2.l5"]
    collider.vars["kqx2a.r5"] = -collider.varval["kqx2.l5"]
    collider.vars["kqx2b.r5"] = -collider.varval["kqx2.l5"]
    collider.vars["kqx3.r5"] = -collider.varval["kqx3.l5"]

    collider.vars["kqx1.l1"] = collider.varval["kqx1.l5"]
    collider.vars["kqx2a.l1"] = collider.varval["kqx2a.l5"]
    collider.vars["kqx2b.l1"] = collider.varval["kqx2b.l5"]
    collider.vars["kqx3.l1"] = collider.varval["kqx3.l5"]
    collider.vars["kqx1.r1"] = collider.varval["kqx1.r5"]
    collider.vars["kqx2a.r1"] = collider.varval["kqx2a.r5"]
    collider.vars["kqx2b.r1"] = collider.varval["kqx2b.r5"]
    collider.vars["kqx3.r1"] = collider.varval["kqx3.r5"]

    # remove the imqXlr knobs if any
    quads_imqlr = "kq4.l5b2 kq4.r5b2 kq5.l5b2 kq5.r5b2 kq6.l5b2 kq6.r5b2"
    for quad in quads_imqlr.split():
        collider.vars[quad] = collider.varval[quad]

    for quad in quads_ir5_b1.split():
        collider.vars[quad.replace("5b", "1b")] = collider.varval[quad]

    for quad in quads_ir5_b2.split():
        collider.vars[quad.replace("5b", "1b")] = collider.varval[quad]

    return opt
