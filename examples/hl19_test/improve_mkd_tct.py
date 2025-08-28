# %%
import xtrack as xt
import rematch_hl_tools
from rematch_hl_tools import qtlim1
import xtrack._temp.lhc_match as lm
from xtrack._temp.lhc_match import (
    get_arc_periodic_solution,
    match_arc_phase_advance,
    ARC_NAMES,
)
from rematch_hl_tools.rematch_arcs import rebal_arc_trim, ats_phase_aux_ir

from matplotlib import pyplot as plt
import numpy as np

from rematch_hl_tools.rematch_irs import rematch_new_ir7_both, rematch_ir6
from rematch_hl_tools import save_to_madx, arcphase_tools
import rematch_hl_tools.rematch_arcs

import rematch_hl_tools.utils as utils

from pprint import pprint
import pandas as pd


# %%
def phases_table(env, table=None):
    if table is None:
        table = utils.crit_phases(env)
    print(pd.DataFrame(table[0]).transpose().to_markdown())
    print(pd.DataFrame(table[1]).transpose().to_markdown())
    print(pd.DataFrame(table[2]).transpose().to_markdown())
    print("\n\n\n")


# %%

default_tol = {None: 1e-8, "betx": 1e-6, "bety": 1e-6}

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
# env.vars.load_madx_optics_file("optics/hl19_opt_round_150_ir7_both_v2_20250711.madx")

# env.vars.load_madx_optics_file("optics/opt_round_150_ir7_b12_phases_iter4.madx")
# env.vars.load_madx_optics_file("optics/opt_round_150_ir7_b12_phases_a34_67_iter3.madx")

# env.vars.load_madx_optics_file("optics/hl19_opt_round_150_ir7_both_20250801_v2.madx")

# env.vars.load_madx_optics_file("optics/hl19_opt_round_150_ir7_both_20250801_v2_phase_middle4.madx")
# env.vars.load_madx_optics_file("optics/hl19_opt_round_150_ir7_both_20250801_v2_phase_middle4_rematched_v2.madx")

# env.vars.load_madx_optics_file("optics/hl19_opt_round_150_ir7_both_20250801_v2_phase_middle4_rematched_v3.madx")
env.vars.load_madx_optics_file(
    "optics/hl19_opt_round_150_ir7_both_20250801_v2_phase_middle4_rematched_v6.madx"
)


env1.vars.load_madx_optics_file(
    "optics/hl19_opt_round_150_ir7_both_20250801_v2_phase_middle4_rematched_v6.madx"
)

# env1.vars.load_madx_optics_file(
#     f"{hl19_path}/strengths/round/opt_round_150_1500_optphases.madx"
# )
rematch_hl_tools.set_limits_steps_ir234678(env, nrj=7000)
# %%
# %%
# env.vars['kqt12.r7b2'] = env.vars.vary_default['kqt12.r7b2']['limits'][0]
# %%
betxy = 0.15
# %%
tw1 = env1.twiss()
tw = env.twiss()
# %%
utils.check_ip(env, "b1")
# %%
utils.check_ip(env, "b2")
# %%
a = utils.crit_phases(env)
# %%
pprint(a, sort_dicts=False)
# %%
opts = arcphase_tools.rephase_arc_a23_a78(
    env,
    betxy,
    betxy,
    dmux_b1=0.0,
    dmuy_b1=0.01,
    dmux_b2=-0.01,
    dmuy_b2=0.0,
    default_tol=default_tol,
)
b = utils.crit_phases(env)
# %%
pprint(b, sort_dicts=False)
# %%
opts2 = arcphase_tools.rephase_arc_a34_a67(
    env,
    betxy,
    betxy,
    dmux_b1=-0.005,
    dmuy_b1=-0.005,
    dmux_b2=0.00,
    dmuy_b2=0.00,
    default_tol=default_tol,
)
c = utils.crit_phases(env)
# %%
# pprint(c, sort_dicts=False)
phases_table(env, table=c)
# %%
opts3 = arcphase_tools.rephase_arc_a67_a78(
    env,
    betxy,
    betxy,
    dmux_b1=-0.001,
    dmuy_b1=-0.001,
    dmux_b2=0.001,
    dmuy_b2=0.001,
    default_tol=default_tol,
)
# %%
d = utils.crit_phases(env)
# %%
pprint(d, sort_dicts=False)
# %%
# rematch_hl_tools.update_stored_vals_ips(env)
# with open("optics/opt_rount_150_ir7_b12_to_be_matched.madx", "w") as f:
#     save_to_madx.save_optics_hllhc(env, f)
# %%
tw_non_ats_arcs = get_arc_periodic_solution(env, arc_name=["23", "34", "67", "78"])
# %%
optimizers = {}
# %%

optimizers["a67"] = rebal_arc_trim(
    env,
    target_mux_b1=tw_non_ats_arcs["lhcb1"]["67"].mux[-1] - (tw.lhcb1.qx - 62.31),
    target_muy_b1=tw_non_ats_arcs["lhcb1"]["67"].muy[-1] - (tw.lhcb1.qy - 60.32),
    target_mux_b2=tw_non_ats_arcs["lhcb2"]["67"].mux[-1] - (tw.lhcb2.qx - 62.31),
    target_muy_b2=tw_non_ats_arcs["lhcb2"]["67"].muy[-1] - (tw.lhcb2.qy - 60.32),
    arc_name="67",
    default_tol=default_tol,
)
# %%
optimizers["a78"] = rebal_arc_trim(
    env,
    target_mux_b1=tw_non_ats_arcs["lhcb1"]["78"].mux[-1] - (tw.lhcb1.qx - 62.31),
    target_muy_b1=tw_non_ats_arcs["lhcb1"]["78"].muy[-1] - (tw.lhcb1.qy - 60.32),
    target_mux_b2=tw_non_ats_arcs["lhcb2"]["78"].mux[-1] - (tw.lhcb2.qx - 62.31),
    target_muy_b2=tw_non_ats_arcs["lhcb2"]["78"].muy[-1] - (tw.lhcb2.qy - 60.32),
    arc_name="78",
    default_tol=default_tol,
)
# %%
optimizers["a78"].target_status()
# %%
optimizers["a78"].solve()
# %%
optimizers["a67"].target_status()
# %%
optimizers["a67"].solve()
# %%
env.vars["kqtf.a78b1"] = env.varval["kqtf.a78b1"]
env.vars["kqtd.a78b1"] = env.varval["kqtd.a78b1"]

env.vars["kqtf.a23b1"] = env.varval["kqtf.a23b1"]
env.vars["kqtd.a23b1"] = env.varval["kqtd.a23b1"]

# %%
pprint(utils.check_ip(env, "b1"), sort_dicts=False)
pprint(utils.check_ip(env, "b2"), sort_dicts=False)
# %%
# rematch_hl_tools.update_stored_vals_ips(env)
# %%
# env.lhcb1.cycle('lhcb1$start', inplace=True)
# env.lhcb2.cycle('lhcb2$end', inplace=True)
# %%
tw_sq_a45_ip5_a56_b1 = lm.propagate_optics_from_beta_star(
    env,
    ip_name="ip5",
    line_name="lhcb1",
    start="s.ds.r4.b1",
    end="e.ds.l6.b1",
    beta_star_x=betxy,
    beta_star_y=betxy,
)

tw_sq_a45_ip5_a56_b2 = lm.propagate_optics_from_beta_star(
    env,
    ip_name="ip5",
    line_name="lhcb2",
    start="s.ds.r4.b2",
    end="e.ds.l6.b2",
    beta_star_x=betxy,
    beta_star_y=betxy,
)

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

mu_tar_b1_ir8 = ats_phase_aux_ir(
    env, 8, 1, 2, line_name="lhcb1", betx=betxy, bety=betxy
)
mu_tar_b2_ir8 = ats_phase_aux_ir(
    env, 8, 1, 2, line_name="lhcb2", betx=betxy, bety=betxy
)

mu_tar_b1_ir6 = ats_phase_aux_ir(
    env, 4, 5, 6, line_name="lhcb1", betx=betxy, bety=betxy
)
mu_tar_b2_ir6 = ats_phase_aux_ir(
    env, 4, 5, 6, line_name="lhcb2", betx=betxy, bety=betxy
)

# %%
tw_non_ats_arcs_v2 = get_arc_periodic_solution(env, arc_name=["23", "34", "67", "78"])
# %%
optimizers["ir7"] = rematch_hl_tools.rematch_irs.rematch_new_ir7_both(
    collider=env,
    boundary_conditions_left=tw_non_ats_arcs_v2,
    boundary_conditions_right=tw_non_ats_arcs_v2,
    mux_ir7_b1=env.varval["muxip7b1"],
    muy_ir7_b1=env.varval["muyip7b1"],
    mux_ir7_b2=env.varval["muxip7b2"],
    muy_ir7_b2=env.varval["muyip7b2"],
    solve=False,
    restore=False,
    assert_within_tol=False,
    default_tol=default_tol,
)
# %%
optimizers["ir7"].target_status()
# %%
optimizers["ir7"].solve()
# %%
pprint(utils.check_ip(env, "b1"), sort_dicts=False)
pprint(utils.check_ip(env, "b2"), sort_dicts=False)
# %%
optimizers["ir8b1"] = lm.rematch_ir8(
    env,
    line_name="lhcb1",
    boundary_conditions_left=tw_non_ats_arcs_v2["lhcb1"]["78"],
    boundary_conditions_right=tw_sq_a81_ip1_a12_b1,
    solve=True,
    mux_ir8=mu_tar_b1_ir8["mux_ir8_b1"],
    muy_ir8=mu_tar_b1_ir8["muy_ir8_b1"],
    alfx_ip8=env.varval["alfxip8b1"],
    alfy_ip8=env.varval["alfyip8b1"],
    betx_ip8=env.varval["betxip8b1"],
    bety_ip8=env.varval["betyip8b1"],
    dx_ip8=env.varval["dxip8b1"],
    dpx_ip8=env.varval["dpxip8b1"],
    staged_match=True,
    default_tol=default_tol,
)

# %%
optimizers["ir8b2"] = lm.rematch_ir8(
    env,
    line_name="lhcb2",
    boundary_conditions_left=tw_non_ats_arcs_v2["lhcb2"]["78"],
    boundary_conditions_right=tw_sq_a81_ip1_a12_b2,
    solve=True,
    mux_ir8=mu_tar_b2_ir8["mux_ir8_b2"],
    muy_ir8=mu_tar_b2_ir8["muy_ir8_b2"],
    alfx_ip8=env.varval["alfxip8b2"],
    alfy_ip8=env.varval["alfyip8b2"],
    betx_ip8=env.varval["betxip8b2"],
    bety_ip8=env.varval["betyip8b2"],
    dx_ip8=env.varval["dxip8b2"],
    dpx_ip8=env.varval["dpxip8b2"],
    staged_match=True,
    default_tol=default_tol,
)
# %%
optimizers["ir8b1"].target_status()
# %%
optimizers["ir8b2"].target_status()

# %%
pprint(utils.check_ip(env, "b1"), sort_dicts=False)
pprint(utils.check_ip(env, "b2"), sort_dicts=False)
# %%
optimizers["ir6b1"] = rematch_ir6(
    restore=False,
    assert_within_tol=False,
    collider=env,
    line_name="lhcb1",
    boundary_conditions_left=tw_sq_a45_ip5_a56_b1,
    boundary_conditions_right=tw_non_ats_arcs_v2["lhcb1"]["67"],
    mux_ir6=mu_tar_b1_ir6["mux_ir6_b1"],
    muy_ir6=mu_tar_b1_ir6["muy_ir6_b1"],
    alfx_ip6=env.varval["alfxip6b1"],
    alfy_ip6=env.varval["alfyip6b1"],
    betx_ip6=env.varval["betxip6b1"],
    bety_ip6=env.varval["betyip6b1"],
    dx_ip6=env.varval["dxip6b1"],
    dpx_ip6=env.varval["dpxip6b1"],
    solve=False,
    match_dx=True,
    match_dpx=True,
    default_tol=default_tol,
)
optimizers["ir6b1"].solve()
optimizers["ir6b1"].disable_targets(tag=["dx_ip6", "dpx_ip6"])
optimizers["ir6b1"].solve()

# %%
optimizers["ir6b2"] = rematch_ir6(
    restore=False,
    assert_within_tol=False,
    collider=env,
    line_name="lhcb2",
    boundary_conditions_left=tw_sq_a45_ip5_a56_b2,
    boundary_conditions_right=tw_non_ats_arcs_v2["lhcb2"]["67"],
    mux_ir6=mu_tar_b2_ir6["mux_ir6_b2"],
    muy_ir6=mu_tar_b2_ir6["muy_ir6_b2"],
    alfx_ip6=env.varval["alfxip6b2"],
    alfy_ip6=env.varval["alfyip6b2"],
    betx_ip6=env.varval["betxip6b2"],
    bety_ip6=env.varval["betyip6b2"],
    dx_ip6=env.varval["dxip6b2"],
    dpx_ip6=env.varval["dpxip6b2"],
    solve=False,
    match_dx=True,
    match_dpx=True,
    default_tol=default_tol,
)
optimizers["ir6b2"].solve()
optimizers["ir6b2"].disable_targets(tag=["dx_ip6", "dpx_ip6"])
optimizers["ir6b2"].solve()
# %%
pprint(utils.check_ip(env, "b1"), sort_dicts=False)
pprint(utils.check_ip(env, "b2"), sort_dicts=False)
# %%
opt_tune = rematch_hl_tools.rematch_tune_non_ats(env, default_targets=True, solve=True)
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
env.vars["ksf.b2"] = 0
env.vars["ksd.b2"] = 0
# %%
pprint(utils.check_ip(env, "b1"), sort_dicts=False)
pprint(utils.check_ip(env, "b2"), sort_dicts=False)
# %%
pprint(utils.crit_phases(env1), sort_dicts=False)
# %%
pprint(utils.crit_phases(env), sort_dicts=False)
# %%
# env1.lhcb1.cycle("e.ds.l3.b1", inplace=True)
# env1.lhcb2.cycle("e.ds.l3.b2", inplace=True)
# env.lhcb1.cycle("e.ds.l3.b1", inplace=True)
# env.lhcb2.cycle("e.ds.l3.b2", inplace=True)

utils.plot_dmu(env1.twiss(), env.twiss())

# env1.lhcb1.cycle("lhcb1$start", inplace=True)
# env1.lhcb2.cycle("lhcb2$end", inplace=True)
# env.lhcb1.cycle("lhcb1$start", inplace=True)
# env.lhcb2.cycle("lhcb2$end", inplace=True)
# %%
tw2 = env.twiss()
fig, axs = plt.subplots(2, 1, figsize=(14, 10.3), dpi=100, sharex=True)

for i, bim in enumerate(["lhcb1", "lhcb2"]):
    dbetx = (tw2[bim].betx - tw1[bim].betx) / tw1[bim].betx
    dbety = (tw2[bim].bety - tw1[bim].bety) / tw1[bim].bety

    axs[i].plot(tw2[bim].s, dbetx, label=r"$\Delta \beta_{x}/ \beta_{x}$", lw=3)
    axs[i].plot(tw2[bim].s, dbety, label=r"$\Delta \beta_{y}/ \beta_{y}$", lw=3)

    # axs[i].set_xlim(15000, 25000)
    # axs[i].set_ylim(-0.2,0.2)
    axs_t = axs[i].twiny()
    axs_t.set_xticks(tw[bim].rows["ip.*"].s, tw[bim].rows["ip.*"].name)
    axs_t.set_xlim(axs[i].get_xlim()[0], axs[i].get_xlim()[1])

for i in range(2):
    axs[i].grid()
    axs[i].legend()
    axs[i].set_xlabel("s [m]")
    axs[i].set_ylabel(r"$\Delta \beta_{x,y}/ \beta_{x,y}$")

plt.show()
# %%
rematch_hl_tools.update_stored_vals_ips(env)
with open(
    "optics/hl19_opt_round_150_ir7_both_20250801_v2_phase_middle4_rematched_v4.madx",
    "w",
) as f:
    save_to_madx.save_optics_hllhc(env, f)
# %%
twir7 = rematch_hl_tools.get_tw_ip(env, 7)
# %%
fig, axs = plt.subplots(figsize=(8, 7), dpi=300, sharex=True)
twir7["lhcb1"].plot("betx bety", "dx", figure=fig, ax=axs)
plt.show()
fig, axs = plt.subplots(figsize=(8, 7), dpi=300, sharex=True)
twir7["lhcb2"].plot("betx bety", "dx", figure=fig, ax=axs)
plt.show()
# %%
