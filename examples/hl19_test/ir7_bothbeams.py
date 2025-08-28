# %%
import xtrack as xt
import rematch_hl_tools
from rematch_hl_tools import get_tw_ip
import xtrack._temp.lhc_match as lm
from xtrack._temp.lhc_match import (
    get_arc_periodic_solution,
    match_arc_phase_advance,
    ARC_NAMES,
)
from matplotlib import pyplot as plt
import numpy as np

from rematch_hl_tools import save_to_madx
from rematch_hl_tools.rematch_arcs import rebal_arc_trim, ats_phase_aux_ir
from rematch_hl_tools import utils

# %%
plt.rcParams.update(
    {
        # "figure.figsize": (7, 6),
        "figure.figsize": (14, 10.3),
        "font.size": 17,
        "axes.titlesize": 17,
        "axes.labelsize": 17,
        "xtick.labelsize": 17,
        "ytick.labelsize": 17,
        "legend.fontsize": 15,
        "figure.titlesize": 12,
        "lines.linewidth": 2.0,
        "lines.markersize": 4,
        "legend.loc": "best",
        "legend.frameon": True,
    }
)
plt.rcParams["font.family"] = "sans-serif"

# %%
# get_ipython().run_line_magic("matplotlib", "qt5")
# plt.ion()
get_ipython().run_line_magic("matplotlib", "inline")
# %%
hl19_path = "/home/iangelis/Projects/hllhc_optics/hl19"
# %%
env = xt.Environment.from_json("../build_hl/hl19.json")
env1 = xt.Environment.from_json("../build_hl/hl19.json")

# %%
# env.vars.load_madx_optics_file("optics/opt_round_150_newir7_v1_fix.madx")
# env.vars.load_madx_optics_file("optics/opt_round_150_newir7_both_beams.madx")
# env.vars.load_madx_optics_file("optics/opt_rount_150_ir7_b12_good3.madx")
# env.vars.load_madx_optics_file("optics/opt_round_150_ir7_b12_test4.madx")

# env.vars.load_madx_optics_file(
#     f"{hl19_path}/strengths/round/opt_round_150_1500_optphases.madx"
# )
env.vars.load_madx_optics_file(
    "optics/hl19_opt_round_150_ir7_both_20250801_v2_phase_middle4_rematched_v6.madx"
)

# env.vars.load_madx_optics_file("optics/hl19_opt_round_150_ir7_both_v1_20250711.madx")

env1.vars.load_madx_optics_file(
    f"{hl19_path}/strengths/round/opt_round_150_1500_optphases.madx"
)
# %%
tw = env.twiss()
# %%
rematch_hl_tools.set_limits_steps_ir234678(env, nrj=7000)
# %%
default_tol = {None: 1e-8, "betx": 1e-6, "bety": 1e-6}
# %%
twir7_v1 = get_tw_ip(env, 7)
# %%
fig, axs = plt.subplots(figsize=(8, 7), dpi=300, sharex=True)
twir7_v1["lhcb1"].plot("betx bety", "dx", figure=fig, ax=axs)
plt.show()
fig, axs = plt.subplots(figsize=(8, 7), dpi=300, sharex=True)
twir7_v1["lhcb2"].plot("betx bety", "dx", figure=fig, ax=axs)
plt.show()
# %%
tw_non_ats_arcs = get_arc_periodic_solution(env, arc_name=["23", "34", "67", "78"])
# %%
mu_tar_b1 = ats_phase_aux_ir(env, 8, 1, 2, line_name="lhcb1", betx=0.15, bety=0.15)
mu_tar_b2 = ats_phase_aux_ir(env, 8, 1, 2, line_name="lhcb2", betx=0.15, bety=0.15)
# %%
betxy = 0.15
# %%
tw_sq_a81_ip1_a12_b1 = lm.propagate_optics_from_beta_star(
    env,
    ip_name="ip1",
    line_name="lhcb1",
    start="s.ds.r8.b1",
    end="e.ds.l2.b1",
    beta_star_x=betxy,
    beta_star_y=betxy,
)

tw_sq_a81_ip1_a12_b2 = lm.propagate_optics_from_beta_star(
    env,
    ip_name="ip1",
    line_name="lhcb2",
    start="s.ds.r8.b2",
    end="e.ds.l2.b2",
    beta_star_x=betxy,
    beta_star_y=betxy,
)

# %%
optimizers = {}
# %%
# asdf = rematch_hl_tools.rematch_irs.new_ir7_strengths(env, apply_all=False)
# # %%
# muxip7b1 = 2.2777833984714384
# muyip7b1 = 2.0016998109612176
# muxip7b2 = 2.270921354088204
# muyip7b2 = 2.0682869617448625
asdf = rematch_hl_tools.rematch_irs.new_ir7_optics
# %%
optimizers["ir7"] = rematch_hl_tools.rematch_irs.rematch_new_ir7_both(
    collider=env,
    boundary_conditions_left=tw_non_ats_arcs,
    boundary_conditions_right=tw_non_ats_arcs,
    # mux_ir7_b1=env.varval["muxip7b1"],
    # muy_ir7_b1=env.varval["muyip7b1"],
    # mux_ir7_b2=env.varval["muxip7b2"],
    # muy_ir7_b2=env.varval["muyip7b2"],
    mux_ir7_b1=asdf['b1']['mux'],
    muy_ir7_b1=asdf['b1']['muy'],
    mux_ir7_b2=asdf['b2']['mux'],
    muy_ir7_b2=asdf['b2']['muy'],
    solve=False,
    restore=False,
    assert_within_tol=False,
    default_tol=default_tol,
)
optimizers["ir7"].disable_targets(tag=["collb1", "collb2"])

# %%
optimizers["ir7"].target_status()
# %%
# optimizers["ir7"].enable_targets(id=14)
optimizers["ir7"].solve()
# %%
optimizers["ir7"].disable_targets(id=[28, 29, 30, 31])
# %%
optimizers["ir7"].enable_targets(tag=["collb1", "collb2"])
# %%
optimizers["ir7"].disable_targets(id=[16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])
# optimizers["ir7"].disable_targets(tag=["ip7_b1", "ip7_b2"])
optimizers["ir7"].disable_targets(tag=["ip7_b1_mu", "ip7_b2_mu"])
# optimizers["ir7"].enable_targets(tag=["ip7_b1_mu", "ip7_b2_mu"])

optimizers["ir7"].disable_targets(id=[i for i in range(62, 142)])

# %%
optimizers["ir7"].solve()
# %%
optimizers["ir7"].target_status()
# %%
# optimizers["ir7"].enable_targets(id=31)
# %%
utils.plot_dmu(env1.twiss(), env.twiss())
# %%
tw_ir7_v2 = get_tw_ip(env, 7)
# %%
fig, axs = plt.subplots(figsize=(8, 7), dpi=300, sharex=True)
tw_ir7_v2["lhcb1"].plot("betx bety", "dx", figure=fig, ax=axs)
plt.show()
fig, axs = plt.subplots(figsize=(8, 7), dpi=300, sharex=True)
tw_ir7_v2["lhcb2"].plot("betx bety", "dx", figure=fig, ax=axs)
plt.show()
# %%
tw_non_ats_arcs_v2 = get_arc_periodic_solution(env, arc_name=["23", "34", "67", "78"])
# %%
tw = env.twiss()
# %%
opt = rebal_arc_trim(
    env,
    target_mux_b1=tw_non_ats_arcs_v2["lhcb1"]["78"].mux[-1] - (tw.lhcb1.qx - 62.31),
    target_muy_b1=tw_non_ats_arcs_v2["lhcb1"]["78"].muy[-1] - (tw.lhcb1.qy - 60.32),
    target_mux_b2=tw_non_ats_arcs_v2["lhcb2"]["78"].mux[-1] - (tw.lhcb2.qx - 62.31),
    target_muy_b2=tw_non_ats_arcs_v2["lhcb2"]["78"].muy[-1] - (tw.lhcb2.qy - 60.32),
    arc_name="78",
    default_tol=default_tol,
)


# opt = match_arc_phase_advance(
#     env,
#     "78",
#     env.varval["mux78b1"],
#     env.varval["muy78b1"],
#     env.varval["mux78b2"],
#     env.varval["muy78b2"],
#     solve=True,
#     default_tol=default_tol,
# )
# %%
opt.target_status()
# %%
opt.solve()
# %%
opt.target_status()
# %%
env.vars["kqtf.a78b1"] = env.varval["kqtf.a78b1"]
env.vars["kqtd.a78b1"] = env.varval["kqtd.a78b1"]

# %%
rematch_hl_tools.update_stored_vals_ips(env)
# %%
optimizers["ir7_2"] = rematch_hl_tools.rematch_irs.rematch_new_ir7_both(
    collider=env,
    boundary_conditions_left=tw_non_ats_arcs_v2,
    boundary_conditions_right=tw_non_ats_arcs_v2,
    # mux_ir7_b1=env.varval["muxip7b1"],
    # muy_ir7_b1=env.varval["muyip7b1"],
    # mux_ir7_b2=env.varval["muxip7b2"],
    # muy_ir7_b2=env.varval["muyip7b2"],
    mux_ir7_b1=tw_ir7_v2.lhcb1.mux[-1],
    muy_ir7_b1=tw_ir7_v2.lhcb1.muy[-1],
    mux_ir7_b2=tw_ir7_v2.lhcb2.mux[-1],
    muy_ir7_b2=tw_ir7_v2.lhcb2.muy[-1],
    solve=False,
    restore=False,
    assert_within_tol=False,
    default_tol=default_tol,
)
# %%
optimizers["ir7_2"].disable_targets(tag=["collb1", "collb2"])
optimizers["ir7_2"].target_status()
# %%
optimizers["ir7_2"].disable_targets(tag=["ip7_b1", "ip7_b2"])
# optimizers["ir7_2"].disable_targets(id=[28, 29, 30, 31])
# optimizers["ir7_2"].enable_targets(id=[28, 29, 30, 31])
# %%
optimizers["ir7_2"].solve()
# %%
optimizers["ir7_2"].enable_targets(tag=["ip7_b1", "ip7_b2"])
optimizers["ir7_2"].solve()
# %%
optimizers["ir7_2"].target_status()
# %%
# NOTE: rematch ip8 ip7
optimizers["ir8b1"] = lm.rematch_ir8(
    env,
    line_name="lhcb1",
    boundary_conditions_left=tw_non_ats_arcs_v2["lhcb1"]["78"],
    boundary_conditions_right=tw_sq_a81_ip1_a12_b1,
    solve=True,
    mux_ir8=mu_tar_b1["mux_ir8_b1"],
    muy_ir8=mu_tar_b1["muy_ir8_b1"],
    alfx_ip8=env1.varval["alfxip8b1"],
    alfy_ip8=env1.varval["alfyip8b1"],
    betx_ip8=env1.varval["betxip8b1"],
    bety_ip8=env1.varval["betyip8b1"],
    dx_ip8=env1.varval["dxip8b1"],
    dpx_ip8=env1.varval["dpxip8b1"],
    staged_match=True,
    default_tol=default_tol,
)
# %%
optimizers["ir8b1"].target_status()
# %%
optimizers["ir8b2"] = lm.rematch_ir8(
    env,
    line_name="lhcb2",
    boundary_conditions_left=tw_non_ats_arcs_v2["lhcb2"]["78"],
    boundary_conditions_right=tw_sq_a81_ip1_a12_b2,
    solve=True,
    mux_ir8=mu_tar_b2["mux_ir8_b2"],
    muy_ir8=mu_tar_b2["muy_ir8_b2"],
    alfx_ip8=env1.varval["alfxip8b2"],
    alfy_ip8=env1.varval["alfyip8b2"],
    betx_ip8=env1.varval["betxip8b2"],
    bety_ip8=env1.varval["betyip8b2"],
    dx_ip8=env1.varval["dxip8b2"],
    dpx_ip8=env1.varval["dpxip8b2"],
    staged_match=True,
    default_tol=default_tol,
)
# %%
optimizers["ir8b1"].target_status()
# %%
optimizers["ir8b2"].target_status()
# %%
utils.check_ip(env, "b1")
# %%
utils.check_ip(env, "b2")
# %%
# opt_tune = rematch_hl_tools.rematch_tune_non_ats(env, default_targets=True, solve=True)
opt_tune = rematch_hl_tools.rematch_tune_chroma.rematch_tune_arc(env, arcs=['23', '34', '67'], default_targets=True, solve=True)
# %%
opt_chroma = rematch_hl_tools.rematch_chroma(env, default_targets=True, solve=True)
# %%
rematch_hl_tools.mk_arc_trims(env)
# %%
env.vars["kqtf.b1"] = 0
env.vars["kqtd.b1"] = 0
env.vars["kqtf.b2"] = 0
env.vars["kqtd.b2"] = 0

env.vars["ksf.b1"] = 0
env.vars["ksd.b1"] = 0
env.vars["ksf.b1"] = 0
env.vars["ksd.b2"] = 0
# %%
utils.check_ip(env, "b1")
# %%
utils.check_ip(env, "b2")
# %%
rematch_hl_tools.update_stored_vals_ips(env)
# %%
with open("optics/hl19_opt_round_150_ir7_both_20250801_v2.madx", "w") as f:
    save_to_madx.save_optics_hllhc(env, f)
# %%
utils.crit_phases(env)
# %%
