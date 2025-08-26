# %%
import xtrack as xt
import rematch_hl_tools
from rematch_hl_tools import get_tw_ip, save_to_madx
import xtrack._temp.lhc_match as lm
from xtrack._temp.lhc_match import (
    get_arc_periodic_solution,
    match_arc_phase_advance,
    ARC_NAMES,
)
from matplotlib import pyplot as plt
import numpy as np

from rematch_hl_tools.utils import plot_dmu, check_ip


# %%
plt.rcParams.update(
    {
        "figure.figsize": (7, 6),
        # "font.size": 19,
        "axes.titlesize": 19,
        "axes.labelsize": 19,
        "xtick.labelsize": 18,
        "ytick.labelsize": 18,
        "legend.fontsize": 19,
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
# env.vars.load_madx_optics_file(
#     f"{hl19_path}/strengths/round/opt_round_150_1500_optphases.madx"
# )
env.vars.load_madx_optics_file("optics/hl19_opt_round_150_newir7_single.madx")


env1.vars.load_madx_optics_file(
    f"{hl19_path}/strengths/round/opt_round_150_1500_optphases.madx"
)
# %%
tw = env.twiss()
# %%
rematch_hl_tools.set_limits_steps_ir234678(env, nrj=7000)
# %%
# env.lhcb1.cycle('s.ds.l3.b1',inplace=True)
# %%
default_tol = {None: 1e-8, "betx": 1e-6, "bety": 1e-6}
# %%
twir7_v1 = get_tw_ip(env, 7)
# %%
twir7_v1["lhcb1"].plot("betx bety", "dx")
twir7_v1["lhcb2"].plot("betx bety", "dx")
# %%
tw_non_ats_arcs = get_arc_periodic_solution(env, arc_name=["23", "34", "67", "78"])
# %%
optimizers = {}
# %%
ir7_ks = rematch_hl_tools.rematch_irs.new_ir7_strengths(env, apply_all=True)
# %%
tw2 = env.twiss()
# %%
twir7_v2 = get_tw_ip(env, 7)
# %%
twir7_v2["lhcb1"].plot("betx bety", "dx")
twir7_v2["lhcb2"].plot("betx bety", "dx")
# %%
optimizers["ir7b1"] = rematch_hl_tools.rematch_irs.rematch_new_ir7(
    restore=False,
    collider=env,
    line_name="lhcb1",
    boundary_conditions_left=tw_non_ats_arcs["lhcb1"]["67"],
    boundary_conditions_right=tw_non_ats_arcs["lhcb1"]["78"],
    mux_ir7=env.varval["muxip7b1"],
    muy_ir7=env.varval["muyip7b1"],
    solve=False,
    default_tol=default_tol,
    assert_within_tol=False,
)
# %%
optimizers["ir7b1"].disable_targets(tag=["ip7_mux", "ip7_muy"])
optimizers["ir7b1"].solve()
# %%
optimizers["ir7b1"].disable_targets(tag="ip7")
optimizers["ir7b1"].disable_targets(tag=["ip7_mux", "ip7_muy"])
# optimizers["ir7b1"].disable_targets(id=[12, 13])
# %%
optimizers["ir7b1"].solve()
# %%
optimizers["ir7b1"].target_status()

# %%
optimizers["ir7b2"] = rematch_hl_tools.rematch_irs.rematch_new_ir7(
    restore=False,
    collider=env,
    line_name="lhcb2",
    boundary_conditions_left=tw_non_ats_arcs["lhcb2"]["67"],
    boundary_conditions_right=tw_non_ats_arcs["lhcb2"]["78"],
    mux_ir7=env.varval["muxip7b2"],
    muy_ir7=env.varval["muyip7b2"],
    solve=False,
    default_tol=default_tol,
    assert_within_tol=False,
)
# %%
optimizers["ir7b2"].disable_targets(tag=["ip7_mux", "ip7_muy"])
# optimizers["ir7b2"].disable_vary(id=7)
optimizers["ir7b2"].solve()
# %%
optimizers["ir7b2"].disable_targets(tag="ip7")
optimizers["ir7b2"].disable_targets(tag=["ip7_mux", "ip7_muy"])
# optimizers["ir7b2"].disable_targets(id=[12, 13])
# %%
optimizers["ir7b2"].enable_targets(id=1)
# optimizers["ir7b2"].enable_vary(id=7)
optimizers["ir7b2"].solve()
# %%
optimizers["ir7b2"].target_status()
# %%
tw_v2 = env.twiss()
# %%
twir7 = get_tw_ip(env, 7)
# %%
twir7["lhcb1"].plot("betx bety", "dx")
twir7["lhcb2"].plot("betx bety", "dx")
# %%
print(twir7.lhcb1.rows["ip7"].cols["betx bety alfx alfy dx dpx"])
print(twir7.lhcb1.rows["ip7"].cols["mux muy"])
# %%
rematch_hl_tools.rematch_irs.new_ir7_optics["b1"]
# %%
print(twir7.lhcb2.rows["ip7"].cols["betx bety alfx alfy dx dpx"])
print(twir7.lhcb2.rows["ip7"].cols["mux muy"])
# %%
rematch_hl_tools.rematch_irs.new_ir7_optics["b2"]
# %%
tw_v2 = env.twiss()
tw = env1.twiss()

# %%
fig, axs = plt.subplots(2, 1, figsize=(11, 8), dpi=100, sharex=False)
tw1=env1.twiss(); tw2=env.twiss()
fig.subplots_adjust(hspace=0.5)
for i, bim in enumerate(["lhcb1", "lhcb2"]):
    dmux = ((tw2[bim].mux % 1) - (tw1[bim].mux % 1)) % 1
    dmux = np.where(dmux > 0.5, dmux - 1, dmux)
    dmuy = ((tw2[bim].muy % 1) - (tw1[bim].muy % 1)) % 1
    dmuy = np.where(dmuy > 0.5, dmuy - 1, dmuy)

    axs[i].plot(tw2[bim].s, dmux, label=r"$\Delta \mu_{x}$")
    axs[i].plot(tw2[bim].s, dmuy, label=r"$\Delta \mu_{y}$")

    axs[i].set_xlim(tw2[bim]['s', 'ip6'], tw2[bim]['s', 'ip8'])

for i in range(2):
    axs_t = axs[i].twiny()
    axs_t.set_xticks(tw1[f"lhcb{i+1}"].rows["ip.*"].s, tw1[f"lhcb{i+1}"].rows["ip.*"].name)
    axs_t.set_xlim(axs[i].get_xlim()[0], axs[i].get_xlim()[1])
    axs[i].grid()
    axs[i].legend()
    axs[i].set_xlabel("s [m]")
    axs[i].set_ylabel(r"$\Delta \mu_{x,y} {\rm [2\pi]}$")
plt.show()
# %%
check_ip(env, "b1")
# %%
check_ip(env, "b2")

# %%
# opt_tune_again = rematch_hl_tools.rematch_tune_chroma.rematch_tune_arc(
#     env, arcs=[23, 34], default_targets=True, solve=True
# )
# %%
# opt_tune_all = rematch_hl_tools.rematch_tune(env, default_targets=True, solve=True)
# %%
opt_chroma = rematch_hl_tools.rematch_chroma(env, default_targets=True, solve=True)
# %%
opt_chroma["b1"].target_status()
# %%
opt_chroma["b2"].target_status()
# %%
check_ip(env, "b1")
# %%
check_ip(env, "b2")
# %%
rematch_hl_tools.mk_arc_trims(env)
# %%
rematch_hl_tools.update_stored_vals_ips(env)
# %%
with open("optics/hl19_opt_round_150_newir7_single.madx", "w") as f:
    save_to_madx.save_optics_hllhc(env, f)

# %%
