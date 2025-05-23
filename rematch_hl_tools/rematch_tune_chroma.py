import xtrack as xt


def default_tune_chroma_targets():
    return {
        "b1": {"qx": 62.31, "qy": 60.32, "dqx": 2, "dqy": 2},
        "b2": {"qx": 62.31, "qy": 60.32, "dqx": 2, "dqy": 2},
    }


def rematch_tune(collider, targets=None, default_targets=False, solve=False):
    if default_targets and targets is None:
        targets = default_tune_chroma_targets()

    optimizers = {}
    for line_name in collider.line_names:
        bim = line_name[-2:]
        opt = collider[line_name].match(
            solve=False,
            assert_within_tol=False,
            restore_if_fail=False,
            verbose=False,
            n_steps_max=5,
            targets=[
                xt.TargetSet(qx=targets[bim]["qx"], qy=targets[bim]["qy"], tol=1e-6)
            ],
            vary=xt.VaryList([f"kqtf.{bim}", f"kqtd.{bim}"], step=1e-8),
        )

        if solve:
            opt.solve()
        optimizers[bim] = opt
    return optimizers


def rematch_tune_non_ats(collider, targets=None, default_targets=False, solve=False):
    if default_targets and targets is None:
        targets = default_tune_chroma_targets()

    optimizers = {}
    for line_name in collider.line_names:
        bim = line_name[-2:]
        opt = collider[line_name].match(
            solve=False,
            assert_within_tol=False,
            restore_if_fail=False,
            verbose=False,
            n_steps_max=5,
            targets=[
                xt.TargetSet(qx=targets[bim]["qx"], qy=targets[bim]["qy"], tol=1e-6)
            ],
            vary=xt.VaryList(
                [
                    f"kqtf.a23{bim}",
                    f"kqtd.a23{bim}",
                    f"kqtf.a34{bim}",
                    f"kqtd.a34{bim}",
                    f"kqtf.a67{bim}",
                    f"kqtd.a67{bim}",
                    f"kqtf.a78{bim}",
                    f"kqtd.a78{bim}",
                ],
                step=1e-8,
            ),
        )

        if solve:
            opt.solve()
        optimizers[bim] = opt
    return optimizers


def rematch_tune_arc(collider, arcs, targets=None, default_targets=False, solve=False):
    if default_targets and targets is None:
        targets = default_tune_chroma_targets()

    optimizers = {}
    for line_name in collider.line_names:
        bim = line_name[-2:]

        vary = []
        for arc in arcs:
            vary.append(xt.Vary(f"kqtf.a{arc}{bim}", step=1e-8))
            vary.append(xt.Vary(f"kqtd.a{arc}{bim}", step=1e-8))

        opt = collider[line_name].match(
            solve=False,
            assert_within_tol=False,
            restore_if_fail=False,
            verbose=False,
            n_steps_max=5,
            targets=[
                xt.TargetSet(qx=targets[bim]["qx"], qy=targets[bim]["qy"], tol=1e-6)
            ],
            vary=vary,
        )

        if solve:
            opt.solve()

        optimizers[bim] = opt
    return optimizers


def rematch_chroma(collider, targets=None, default_targets=False, solve=False):
    if default_targets and targets is None:
        targets = default_tune_chroma_targets()

    optimizers = {}
    for line_name in collider.line_names:
        bim = line_name[-2:]
        opt = collider[line_name].match(
            solve=False,
            assert_within_tol=False,
            restore_if_fail=True,
            verbose=False,
            n_steps_max=10,
            targets=[
                xt.TargetSet(dqx=targets[bim]["dqx"], dqy=targets[bim]["dqy"], tol=1e-4)
            ],
            vary=xt.VaryList([f"ksf.{bim}", f"ksd.{bim}"], step=1e-8),
        )

        if solve:
            opt.solve()
        optimizers[bim] = opt
    return optimizers
