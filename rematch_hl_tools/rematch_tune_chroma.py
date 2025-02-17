import xtrack as xt


def default_tune_chroma_targets():
    return {
        "b1": {"qx": 62.31, "qy": 60.32, "dqx": 2, "dqy": 2},
        "b2": {"qx": 62.31, "qy": 60.32, "dqx": 2, "dqy": 2},
    }


def rematch_tune(collider, targets, default_targets=False, solve=False):
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


def rematch_chroma(collider, targets, default_targets=False, solve=False):
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
