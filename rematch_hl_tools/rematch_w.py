import xtrack as xt

from .match_limits_steps import set_limits_steps_sextupoles_w


def set_sext_all(collider, ksf_b1, ksd_b1, ksf_b2, ksd_b2):
    collider.vars["ksd1.a12b1"] = ksd_b1
    collider.vars["ksd1.a56b1"] = ksd_b1
    collider.vars["ksd2.a12b1"] = ksd_b1
    collider.vars["ksd2.a56b1"] = ksd_b1
    collider.vars["ksf1.a12b1"] = ksf_b1
    collider.vars["ksf1.a56b1"] = ksf_b1
    collider.vars["ksf2.a12b1"] = ksf_b1
    collider.vars["ksf2.a56b1"] = ksf_b1
    collider.vars["ksd1.a12b2"] = ksd_b2
    collider.vars["ksd1.a56b2"] = ksd_b2
    collider.vars["ksd2.a12b2"] = ksd_b2
    collider.vars["ksd2.a56b2"] = ksd_b2
    collider.vars["ksf1.a12b2"] = ksf_b2
    collider.vars["ksf1.a56b2"] = ksf_b2
    collider.vars["ksf2.a12b2"] = ksf_b2
    collider.vars["ksf2.a56b2"] = ksf_b2

    collider.vars["ksd1.a23b1"] = ksd_b1
    collider.vars["ksd1.a67b1"] = ksd_b1
    collider.vars["ksd2.a23b1"] = ksd_b1
    collider.vars["ksd2.a67b1"] = ksd_b1
    collider.vars["ksf1.a23b1"] = ksf_b1
    collider.vars["ksf1.a67b1"] = ksf_b1
    collider.vars["ksf2.a23b1"] = ksf_b1
    collider.vars["ksf2.a67b1"] = ksf_b1
    collider.vars["ksd1.a23b2"] = ksd_b2
    collider.vars["ksd1.a67b2"] = ksd_b2
    collider.vars["ksd2.a23b2"] = ksd_b2
    collider.vars["ksd2.a67b2"] = ksd_b2
    collider.vars["ksf1.a23b2"] = ksf_b2
    collider.vars["ksf1.a67b2"] = ksf_b2
    collider.vars["ksf2.a23b2"] = ksf_b2
    collider.vars["ksf2.a67b2"] = ksf_b2

    collider.vars["ksd1.a34b1"] = ksd_b1
    collider.vars["ksd1.a78b1"] = ksd_b1
    collider.vars["ksd2.a34b1"] = ksd_b1
    collider.vars["ksd2.a78b1"] = ksd_b1
    collider.vars["ksf1.a34b1"] = ksf_b1
    collider.vars["ksf1.a78b1"] = ksf_b1
    collider.vars["ksf2.a34b1"] = ksf_b1
    collider.vars["ksf2.a78b1"] = ksf_b1
    collider.vars["ksd1.a34b2"] = ksd_b2
    collider.vars["ksd1.a78b2"] = ksd_b2
    collider.vars["ksd2.a34b2"] = ksd_b2
    collider.vars["ksd2.a78b2"] = ksd_b2
    collider.vars["ksf1.a34b2"] = ksf_b2
    collider.vars["ksf1.a78b2"] = ksf_b2
    collider.vars["ksf2.a34b2"] = ksf_b2
    collider.vars["ksf2.a78b2"] = ksf_b2

    collider.vars["ksd1.a45b1"] = ksd_b1
    collider.vars["ksd1.a81b1"] = ksd_b1
    collider.vars["ksd2.a45b1"] = ksd_b1
    collider.vars["ksd2.a81b1"] = ksd_b1
    collider.vars["ksf1.a45b1"] = ksf_b1
    collider.vars["ksf1.a81b1"] = ksf_b1
    collider.vars["ksf2.a45b1"] = ksf_b1
    collider.vars["ksf2.a81b1"] = ksf_b1
    collider.vars["ksd1.a45b2"] = ksd_b2
    collider.vars["ksd1.a81b2"] = ksd_b2
    collider.vars["ksd2.a45b2"] = ksd_b2
    collider.vars["ksd2.a81b2"] = ksd_b2
    collider.vars["ksf1.a45b2"] = ksf_b2
    collider.vars["ksf1.a81b2"] = ksf_b2
    collider.vars["ksf2.a45b2"] = ksf_b2
    collider.vars["ksf2.a81b2"] = ksf_b2


ksf_names_non_ats_arcs = (
    "ksf1.a23bim ksf2.a23bim ksf1.a34bim ksf2.a34bim "
    "ksf1.a67bim ksf2.a67bim ksf1.a78bim ksf2.a78bim"
)

ksd_names_non_ats_arcs = (
    "ksd1.a23bim ksd2.a23bim ksd1.a34bim ksd2.a34bim "
    "ksd1.a67bim ksd2.a67bim ksd1.a78bim ksd2.a78bim"
)

ksf_names_ats_arcs = (
    "ksf1.a12bim ksf1.a12bim ksf2.a12bim ksf2.a12bim "
    "ksf1.a81bim ksf1.a81bim ksf2.a81bim ksf2.a81bim "
    "ksf1.a56bim ksf1.a56bim ksf2.a56bim ksf2.a56bim "
    "ksf1.a45bim ksf1.a45bim ksf2.a45bim ksf2.a45bim"
)

ksd_names_ats_arcs = (
    "ksd1.a12bim ksd1.a12bim ksd2.a12bim ksd2.a12bim "
    "ksd1.a81bim ksd1.a81bim ksd2.a81bim ksd2.a81bim "
    "ksd1.a56bim ksd1.a56bim ksd2.a56bim ksd2.a56bim "
    "ksd1.a45bim ksd1.a45bim ksd2.a45bim ksd2.a45bim"
)


def _reset_sext_knobs(collider):
    old_vals = {}

    for ksfd in ksf_names_ats_arcs.split() + ksd_names_ats_arcs.split():
        for bim in ["b1", "b2"]:
            ks_name = ksfd.replace("bim", bim)
            old_vals[ks_name] = collider.varval[ks_name]
            collider.vars[ks_name] = old_vals[ks_name]

    for ksfd in ksf_names_non_ats_arcs.split():
        for bim in ["b1", "b2"]:
            ksf_name = ksfd.replace("bim", bim)
            old_vals[ksf_name] = collider.varval[ksf_name]
            collider.vars[ksf_name] = old_vals[ksf_name] + (
                1.0 * collider.vars[f"ksf.{bim}"]
            )

    for ksfd in ksd_names_non_ats_arcs.split():
        for bim in ["b1", "b2"]:
            ksd_name = ksfd.replace("bim", bim)
            old_vals[ksd_name] = collider.varval[ksd_name]
            collider.vars[ksd_name] = old_vals[ksd_name] + (
                1.0 * collider.vars[f"ksd.{bim}"]
            )

    return old_vals


def corchroma_weak(collider, qprime, bim):
    """
    correct Q' using the SF/SD families of sectors 23/34/56/67
    """

    opt = collider[f"lhc{bim}"].match(
        assert_within_tol=False,
        restore_if_fail=False,
        solver_options={"n_bisections": 1, "min_step": 1e-4, "n_steps_max": 4},
        vary=[
            xt.VaryList([f"ksf.{bim}", f"ksd.{bim}"], step=1e-8, limits=(-0.38, 0.38)),
        ],
        targets=[
            xt.TargetSet(dqx=qprime, dqy=qprime, tol=0.05),
        ],
    )

    for ksfd in ksf_names_non_ats_arcs.split():
        ksf_name = ksfd.replace("bim", bim)
        matched_value = collider.varval[ksf_name]
        collider.vars[ksf_name] = matched_value + (1.0 * collider.vars[f"ksf.{bim}"])

    for ksfd in ksd_names_non_ats_arcs.split():
        ksd_name = ksfd.replace("bim", bim)
        matched_value = collider.varval[ksd_name]
        collider.vars[ksd_name] = matched_value + (1.0 * collider.vars[f"ksd.{bim}"])

    collider.vars[f"ksf.{bim}"] = 0
    collider.vars[f"ksd.{bim}"] = 0

    return opt


def rematch_w(collider, bim, solve=False, nsteps=4):
    sign_I = {"b1": 1, "b2": -1}[bim]

    ksfd = {
        "b1": [
            "ksf1.a81b1",
            "ksd2.a81b1",
            "ksf1.a12b1",
            "ksf1.a45b1",
            "ksd2.a45b1",
            "ksf1.a56b1",
        ],
        "b2": [
            "ksf2.a81b2",
            "ksf2.a12b2",
            "ksd1.a12b2",
            "ksf2.a45b2",
            "ksf2.a56b2",
            "ksd1.a56b2",
        ],
    }

    ksfd_w = {"b1": ["ksd2.a12b1", "ksd2.a56b1"], "b2": ["ksd1.a81b2", "ksd1.a45b2"]}

    ksfd_w2 = {"b1": ["ksd1.a12b1", "ksd1.a56b1"], "b2": ["ksd2.a81b2", "ksd2.a45b2"]}

    line1 = collider[f"lhc{bim}"].cycle("ip3")
    tw = line1.twiss(method="4d")

    start_range = f"mbxf.4l1/lhc{bim}"
    end_range = "ip1"
    twiss_init = tw.get_twiss_init(start_range)
    twiss_init.ax_chrom = 0
    twiss_init.bx_chrom = 0
    twiss_init.ay_chrom = 0
    twiss_init.by_chrom = 0
    tw_l1 = line1.twiss(
        start=start_range,
        end=end_range,
        init=twiss_init,
        compute_chromatic_properties=True,
    )
    start_range = "ip1"
    end_range = f"mbxf.4r1/lhc{bim}"
    twiss_init = tw.get_twiss_init(end_range)
    twiss_init.ax_chrom = 0
    twiss_init.bx_chrom = 0
    twiss_init.ay_chrom = 0
    twiss_init.by_chrom = 0
    tw_r1 = line1.twiss(
        start=start_range,
        end=end_range,
        init=twiss_init,
        compute_chromatic_properties=True,
    )

    start_range = f"mbxf.4l5/lhc{bim}"
    end_range = "ip5"
    twiss_init = tw.get_twiss_init(start_range)
    twiss_init.ax_chrom = 0
    twiss_init.bx_chrom = 0
    twiss_init.ay_chrom = 0
    twiss_init.by_chrom = 0
    tw_l5 = line1.twiss(
        start=start_range,
        end=end_range,
        init=twiss_init,
        compute_chromatic_properties=True,
    )

    # Measure chromaticities of IR5
    start_range = "ip5"
    end_range = f"mbxf.4r5/lhc{bim}"
    twiss_init = tw.get_twiss_init(end_range)
    twiss_init.ax_chrom = 0
    twiss_init.bx_chrom = 0
    twiss_init.ay_chrom = 0
    twiss_init.by_chrom = 0
    tw_r5 = line1.twiss(
        start=start_range,
        end=end_range,
        init=twiss_init,
        compute_chromatic_properties=True,
    )

    tar_ix1 = 0.5 * (tw_l1.ax_chrom[-1] - tw_r1.ax_chrom[-1])
    tar_iy1 = 0.5 * (tw_l1.ay_chrom[-1] - tw_r1.ay_chrom[-1])
    tar_ix5 = 0.5 * (tw_l5.ax_chrom[-1] - tw_r5.ax_chrom[-1])
    tar_iy5 = 0.5 * (tw_l5.ay_chrom[-1] - tw_r5.ay_chrom[-1])

    opt = collider[f"lhc{bim}"].match(
        solve=False,
        assert_within_tol=False,
        restore_if_fail=False,
        verbose=False,
        solver_options={"n_bisections": 1, "min_step": 1e-4, "n_steps_max": nsteps},
        n_steps_max=nsteps,
        vary=[
            xt.VaryList(vars=ksfd[bim]),
            xt.VaryList(tag="w", vars=ksfd_w[bim]),
            xt.VaryList(tag="w2", vars=ksfd_w2[bim]),
        ],
        targets=[
            # IR3, IR7
            xt.Target(tag="bxy", at="ip3", tar="bx_chrom", value=0),
            xt.Target(tag="bxy", at="ip3", tar="by_chrom", value=0),
            xt.Target(tag="axy", at="ip3", tar="ax_chrom", value=0, tol=1e-2),
            xt.Target(tag="axy", at="ip3", tar="ay_chrom", value=0, tol=1e-2),
            xt.Target(tag="bxy", at="ip7", tar="bx_chrom", value=0),
            xt.Target(tag="bxy", at="ip7", tar="by_chrom", value=0),
            xt.Target(tag="axy", at="ip7", tar="ax_chrom", value=0, tol=1e-2),
            xt.Target(tag="axy", at="ip7", tar="ay_chrom", value=0, tol=1e-2),
            # IP1, IP5
            xt.Target(tag="bxy", at="ip1", tar="bx_chrom", value=0),
            xt.Target(tag="bxy", at="ip1", tar="by_chrom", value=0),
            xt.Target(
                tag="axy", at="ip1", tar="ax_chrom", value=sign_I * tar_ix1, tol=1e-2
            ),
            xt.Target(
                tag="axy", at="ip1", tar="ay_chrom", value=-sign_I * tar_iy1, tol=1e-2
            ),
            xt.Target(tag="bxy", at="ip5", tar="bx_chrom", value=0),
            xt.Target(tag="bxy", at="ip5", tar="by_chrom", value=0),
            xt.Target(
                tag="axy", at="ip5", tar="ax_chrom", value=sign_I * tar_ix5, tol=1e-2
            ),
            xt.Target(
                tag="axy", at="ip5", tar="ay_chrom", value=-sign_I * tar_iy5, tol=1e-2
            ),
        ],
    )

    opt.disable_vary(tag="w2")

    if solve:
        opt.solve()
    return opt


def corchroma_weak_b12(collider, qp=2):
    optimizers = {}
    optimizers["dqxw_b1"] = corchroma_weak(collider, qp, "b1")
    optimizers["dqxw_b2"] = corchroma_weak(collider, qp, "b2")

    return optimizers


def rematch_w_b12(collider):
    optimizers = {}
    optimizers["w_b1"] = rematch_w(collider, "b1", solve=True)
    optimizers["w_b2"] = rematch_w(collider, "b2", solve=True)

    return optimizers


def rematch_w_default(collider):
    set_limits_steps_sextupoles_w(collider)

    set_sext_all(collider, 0.06, -0.099, 0.06, -0.099)
    _ = _reset_sext_knobs(collider)

    optimizers = {}
    opt_chroma = corchroma_weak_b12(collider, 2)
    optimizers.update(opt_chroma)

    opt_w = rematch_w_b12(collider)
    optimizers.update(opt_w)

    opt_chroma = corchroma_weak_b12(collider, 2)
    optimizers["dqxw2_b1"] = opt_chroma["dqxw_b1"]
    optimizers["dqxw2_b2"] = opt_chroma["dqxw_b2"]

    return optimizers
