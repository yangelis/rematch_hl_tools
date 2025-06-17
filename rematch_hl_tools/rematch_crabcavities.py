import xtrack as xt
import numpy as np


def match_cc(
    collider,
    line_name,
    ip,
    hv,
    z_crab=1e-3,
    default_tol={"x": 1e-20, "px": 1e-20, "y": 1e-20, "py": 1e-20},
    solve=True,
):
    collider.vars["z_crab"] = z_crab

    irn = ip[2]
    bim = line_name[-2:]
    signb = 1
    if line_name == "lhcb2":
        signb = -1

    targets = None
    if hv == "h":
        targets = [xt.TargetSet(at=f"{ip}", px=0, x=1e-6 * z_crab * signb)]
    elif hv == "v":
        targets = [xt.TargetSet(at=f"{ip}", py=0, y=1e-6 * z_crab * signb)]

    vary = xt.VaryList([f"a{hv}crab_l{irn}{bim}", f"a{hv}crab_r{irn}{bim}"])

    collider.vars[f"on_crab{irn}"] = 1

    opt = collider[line_name].match(
        solve=False,
        only_markers=False,
        restore_if_fail=False,
        assert_within_tol=False,
        verbose=False,
        default_tol=default_tol,
        # solver_options={"n_steps_max": 15},
        targets=targets,
        vary=vary,
    )

    if solve:
        opt.solve()

    collider.vars[f"on_crab{irn}"] = 0

    return opt


def rematch_crabs(
    collider,
    z_crab=1e-3,
    nrj=7000,
    default_tol={"x": 1e-20, "px": 1e-20, "y": 1e-20, "py": 1e-20},
    reset_values=True,
    solve=True,
):
    collider.vars["nrj"] = nrj
    collider.vars["z_crab"] = z_crab
    phi_ir1 = collider.varval["phi_ir1"]
    phi_ir5 = collider.varval["phi_ir5"]
    # reset everything
    if reset_values:
        for ip in [1, 5]:
            for bim in ["b1", "b2"]:
                # Initial condition of 10 MV
                collider.vars[f"ahcrab_l{ip}{bim}"] = 0.01 / nrj
                collider.vars[f"ahcrab_r{ip}{bim}"] = 0.01 / nrj
                collider.vars[f"avcrab_l{ip}{bim}"] = 0.01 / nrj
                collider.vars[f"avcrab_r{ip}{bim}"] = 0.01 / nrj

    collider.vars["phi_ir1"] = 0
    collider.vars["phi_ir5"] = 0
    opt_cc_h1_b1 = match_cc(collider, "lhcb1", "ip1", "h", z_crab, default_tol, solve)
    opt_cc_h1_b2 = match_cc(collider, "lhcb2", "ip1", "h", z_crab, default_tol, solve)
    opt_cc_h5_b1 = match_cc(collider, "lhcb1", "ip5", "h", z_crab, default_tol, solve)
    opt_cc_h5_b2 = match_cc(collider, "lhcb2", "ip5", "h", z_crab, default_tol, solve)

    collider.vars["phi_ir1"] = 90
    collider.vars["phi_ir5"] = 90
    opt_cc_v1_b1 = match_cc(collider, "lhcb1", "ip1", "v", z_crab, default_tol, solve)
    opt_cc_v1_b2 = match_cc(collider, "lhcb2", "ip1", "v", z_crab, default_tol, solve)
    opt_cc_v5_b1 = match_cc(collider, "lhcb1", "ip5", "v", z_crab, default_tol, solve)
    opt_cc_v5_b2 = match_cc(collider, "lhcb2", "ip5", "v", z_crab, default_tol, solve)

    opts = {
        "cc_ip1_b1_h": opt_cc_h1_b1,
        "cc_ip1_b2_h": opt_cc_h1_b2,
        "cc_ip5_b1_h": opt_cc_h5_b1,
        "cc_ip5_b2_h": opt_cc_h5_b2,
        "cc_ip1_b1_v": opt_cc_v1_b1,
        "cc_ip1_b2_v": opt_cc_v1_b2,
        "cc_ip5_b1_v": opt_cc_v5_b1,
        "cc_ip5_b2_v": opt_cc_v5_b2,
    }

    # reset variables
    collider.vars["phi_ir1"] = phi_ir1
    collider.vars["phi_ir5"] = phi_ir5

    v_crabh_l1b1 = collider.varval["ahcrab_l1b1"] * nrj * 1e9 * 1e-6
    v_crabh_r1b1 = collider.varval["ahcrab_r1b1"] * nrj * 1e9 * 1e-6
    v_crabh_l1b2 = collider.varval["ahcrab_l1b2"] * nrj * 1e9 * 1e-6
    v_crabh_r1b2 = collider.varval["ahcrab_r1b2"] * nrj * 1e9 * 1e-6
    v_crabh_l5b1 = collider.varval["ahcrab_l5b1"] * nrj * 1e9 * 1e-6
    v_crabh_r5b1 = collider.varval["ahcrab_r5b1"] * nrj * 1e9 * 1e-6
    v_crabh_l5b2 = collider.varval["ahcrab_l5b2"] * nrj * 1e9 * 1e-6
    v_crabh_r5b2 = collider.varval["ahcrab_r5b2"] * nrj * 1e9 * 1e-6

    v_crabv_l1b1 = collider.varval["avcrab_l1b1"] * nrj * 1e9 * 1e-6
    v_crabv_r1b1 = collider.varval["avcrab_r1b1"] * nrj * 1e9 * 1e-6
    v_crabv_l1b2 = collider.varval["avcrab_l1b2"] * nrj * 1e9 * 1e-6
    v_crabv_r1b2 = collider.varval["avcrab_r1b2"] * nrj * 1e9 * 1e-6
    v_crabv_l5b1 = collider.varval["avcrab_l5b1"] * nrj * 1e9 * 1e-6
    v_crabv_r5b1 = collider.varval["avcrab_r5b1"] * nrj * 1e9 * 1e-6
    v_crabv_l5b2 = collider.varval["avcrab_l5b2"] * nrj * 1e9 * 1e-6
    v_crabv_r5b2 = collider.varval["avcrab_r5b2"] * nrj * 1e9 * 1e-6

    v_crab_h = [
        v_crabh_l1b1,
        v_crabh_r1b1,
        v_crabh_l1b2,
        v_crabh_r1b2,
        v_crabh_l5b1,
        v_crabh_r5b1,
        v_crabh_l5b2,
        v_crabh_r5b2,
    ]
    v_crab_v = [
        v_crabv_l1b1,
        v_crabv_r1b1,
        v_crabv_l1b2,
        v_crabv_r1b2,
        v_crabv_l5b1,
        v_crabv_r5b1,
        v_crabv_l5b2,
        v_crabv_r5b2,
    ]

    crab_names_fmt = [
        "ahvcrab_l1b1",
        "ahvcrab_r1b1",
        "ahvcrab_l1b2",
        "ahvcrab_r1b2",
        "ahvcrab_l5b1",
        "ahvcrab_r5b1",
        "ahvcrab_l5b2",
        "ahvcrab_r5b2",
    ]

    vcrabh_max = np.max(np.abs(v_crab_h))

    vcrabv_max = np.max(np.abs(v_crab_v))

    for nn, vh, vv in zip(crab_names_fmt, v_crab_h, v_crab_v):
        print(nn, 3.4 * 4 / vh, 3.4 * 4 / vv)

    crabh_angle_max = 3.4 * 4 / vcrabh_max
    crabv_angle_max = 3.4 * 4 / vcrabv_max

    print(f"{crabh_angle_max=}, {crabv_angle_max=}")

    collider.vars["z_crab"] = 0

    crab_angles = {
        "crabh_angle_max": crabh_angle_max,
        "crabv_angle_max": crabv_angle_max,
    }

    return (opts, crab_angles)
