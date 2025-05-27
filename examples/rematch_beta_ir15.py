# %%
import xtrack as xt
import rematch_hl_tools
from rematch_hl_tools import qtlim1
from xtrack._temp.lhc_match import get_arc_periodic_solution
from matplotlib import pyplot as plt
import numpy as np
# %%
# env1 = xt.Environment.from_json("build_hl/hl_coll.json")
# env = xt.Environment.from_json("build_hl/hl_coll.json")
# env = xt.Environment.from_json("rematch_round_1300_v2.json")


env1 = xt.Environment.from_json("build_hl/hl_round_1000.json")
env = xt.Environment.from_json("build_hl/hl_round_1000.json")
# env = xt.Environment.from_json("build_hl/hl_round_150.json")

# %%
twb1 = env.lhcb1.twiss()
# %%
rematch_hl_tools.set_limits_steps_quads_ip15(env)
env.vars.vary_default.update(
    {
        "kqx1.l1": {"step": 1e-6, "limits": (-qtlim1, -qtlim1 * 0.91)},
        "kqx2a.l1": {"step": 1e-6, "limits": (-qtlim1, -qtlim1 * 0.91)},
        "kqx3.l1": {"step": 1e-6, "limits": (-qtlim1, -qtlim1 * 0.91)},
    }
)

# %%
tw45_56_xt = get_arc_periodic_solution(env, arc_name=["45", "56"])
tw81_12_xt = get_arc_periodic_solution(env, arc_name=["81", "12"])
# %%
beta0 = tw81_12_xt["lhcb1"]["81"].get_twiss_init("s.ds.l1.b1")
beta0.mux = 0
beta0.muy = 0
tw_ip1 = env.lhcb1.twiss(start="s.ds.l1.b1", end="e.ds.r1.b1", init=beta0)


beta0 = tw45_56_xt["lhcb1"]["45"].get_twiss_init("s.ds.l5.b1")
beta0.mux = 0
beta0.muy = 0
tw_ip5 = env.lhcb1.twiss(start="s.ds.l5.b1", end="e.ds.r5.b1", init=beta0)

# %%
fig, axs = plt.subplots(2, 1, figsize=(14, 10.5))
axs[0].set_title("IP1")
axs[0].plot(tw_ip1.s, tw_ip1.betx, ls="--", color="blue", label=r"Old $\beta_x$")
axs[0].plot(tw_ip1.s, tw_ip1.bety, ls="--", color="green", label=r"Old $\beta_y$")

axs[0].set_xlabel("s [m]")
axs[0].set_ylabel(r"$\beta_{x,y} [m]$")
axs[0].legend()

axs[1].set_title("IP5")
axs[1].plot(tw_ip5.s, tw_ip5.betx, ls="--", color="blue", label=r"Old $\beta_x$")
axs[1].plot(tw_ip5.s, tw_ip5.bety, ls="--", color="green", label=r"Old $\beta_y$")

axs[1].set_xlabel("s [m]")
axs[1].set_ylabel(r"$\beta_{x,y} [m]$")
axs[1].legend()

axs[0].grid()
axs[1].grid()

plt.show()
# %%
print(twb1.rows["ip.*"].cols["betx bety"])
# %%
optimizers = {}
# %%
extra_tars = [
    # xt.Target(
    #     lambda tt: np.sqrt(
    #         tt.rows["acfca.4bl5.b1"].betx[0] * tt.rows["acfca.4bl5.b1"].bety[0]
    #     ),
    #     line="lhcb1",
    #     value=850,
    #     tol=1e-5,
    # ),
    xt.Target(line="lhcb1", betx=1100, tol=1e-3, at="acfca.4bl5.b1"),
]
# %%
betxy = 1
# %%
optimizers["ir15"] = rematch_hl_tools.rematch_ir15(
    env,
    betxy,
    betxy,
    tw_sq_a45_ip5_a56=tw45_56_xt,
    restore=False,
    ir5q4sym=0,
    ir5q5sym=0,
    ir5q6sym=0,
    solve=True,
    match_on_triplet=5,
    beta_peak_ratio=0.9,
)
# %%
optimizers["ir15_2"] = rematch_hl_tools.rematch_ir15(
    env,
    betxy,
    betxy,
    # tw_sq_a45_ip5_a56=tw45_56_xt,
    restore=False,
    ir5q4sym=0,
    ir5q5sym=0,
    ir5q6sym=0,
    solve=True,
    match_on_triplet=0,
)
# %%

tw45_56_xt = get_arc_periodic_solution(env, arc_name=["45", "56"])
beta0 = tw45_56_xt["lhcb1"]["45"].get_twiss_init("s.ds.l5.b1")
beta0.mux = 0
beta0.muy = 0
tw_ip5_n = env.lhcb1.twiss(start="s.ds.l5.b1", end="e.ds.r5.b1", init=beta0)

# %%
print(tw_ip5_n["bety", "mqxfb.a2r5/lhcb1"] / tw_ip5_n["betx", "mqxfa.b3r5/lhcb1"])
# %%
fig, axs = plt.subplots(figsize=(14, 10.5))
axs.set_title("IP5")
axs.plot(tw_ip5.s, tw_ip5.betx, ls="--", color="blue", label=r"Old $\beta_x$")
axs.plot(tw_ip5_n.s, tw_ip5_n.betx, ls="-", color="blue", label=r"$\beta_x$")
axs.plot(tw_ip5.s, tw_ip5.bety, ls="--", color="green", label=r"Old $\beta_y$")
axs.plot(tw_ip5_n.s, tw_ip5_n.bety, ls="-", color="green", label=r"$\beta_y$")


# axs.vlines(tw_ip5_n["s", "mqxfb.a2r5/lhcb1"], ymin=0, ymax=axs.get_ylim()[1],lw=2)
# axs.vlines(tw_ip5_n["s", "mqxfa.b3r5/lhcb1"], ymin=0, ymax=axs.get_ylim()[1],lw=2)

axs.set_xlabel("s [m]")
axs.set_ylabel(r"$\beta_{x,y} [m]$")
axs.legend()
axs.grid()

plt.show()
# %%

twnb1 = env.lhcb1.twiss()
twnb2 = env.lhcb2.twiss()
# %%
print(twnb1.rows["ip.*"].cols["betx bety"])
print(twnb2.rows["ip.*"].cols["betx bety"])
# %%
rmat1 = tw_ip5.get_R_matrix_table()
rmat2 = tw_ip5_n.get_R_matrix_table()

# %%
fig, axs = plt.subplots(figsize=(14, 10.5))
axs.set_title("IP5")
axs.plot(rmat1.s, rmat1.r11, ls="-", label=r"Old $R_{11}$")
axs.plot(rmat2.s, rmat2.r11, ls="-", label=r"New $R_{11}$")

axs.plot(rmat1.s, rmat1.r22, ls="-", label=r"Old $R_{22}$")
axs.plot(rmat2.s, rmat2.r22, ls="-", label=r"New $R_{22}$")

axs.set_xlabel("s [m]")
axs.set_ylabel(r"$R_{11}$")
axs.legend()
axs.grid()

plt.show()

# %%
# env.to_json("optics/opt_round_900_ir15.json")

# %%
