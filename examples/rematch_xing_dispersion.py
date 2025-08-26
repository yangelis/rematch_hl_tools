# %%
import xtrack as xt
import rematch_hl_tools
from matplotlib import pyplot as plt
from rematch_hl_tools.utils import set_vars, configs

# %%
# env1 = xt.Environment.from_json("rematch_round_1300_v3.json")
# env = xt.Environment.from_json("opt_round_1300_xing.json")

env1 = xt.Environment.from_json("rematch_round_1000.json")
env = xt.Environment.from_json("opt_round_1000_xing.json")

# %%
twb1 = env1["lhcb1"].cycle("ip3").twiss(method="4d")
twb2 = env1["lhcb2"].cycle("ip3").twiss(method="4d")

# %%
set_vars(env1, config=configs["on_0"])
set_vars(env, config=configs["on_0"])
# %%
default_tol = {None: 1e-8, "betx": 1e-6, "bety": 1e-6}
# %%
rematch_hl_tools.set_limits_steps_disp_correctors(env)

# %%
opts = rematch_hl_tools.rematch_disp(
    env, solve=True, default_tol=default_tol, angle_ref=295, sep_ref=1, cycle=True
)
# %%
env1.vars["on_disp"] = 1
env.vars["on_disp"] = 1
set_vars(env1, config=configs["on_x15hvs"])
set_vars(env, config=configs["on_x15hvs"])
twb1 = env1["lhcb1"].cycle("ip3").twiss(method="4d")

env["lhcb1"].cycle("s.ds.l3.b1", inplace=True)
env["lhcb2"].cycle("s.ds.l3.b2", inplace=True)
env.lhcb1.twiss_default["method"] = "4d"
env.lhcb2.twiss_default["method"] = "4d"
env.lhcb2.twiss_default["reverse"] = True

twnb1 = env["lhcb1"].cycle("ip3").twiss(method="4d")
twnb2 = env["lhcb2"].cycle("ip3").twiss(method="4d")

env["lhcb1"].cycle("lhcb1$start", inplace=True)
env["lhcb2"].cycle("lhcb2$start", inplace=True)
env.lhcb1.twiss_default["method"] = "4d"
env.lhcb2.twiss_default["method"] = "4d"
env.lhcb2.twiss_default["reverse"] = True

set_vars(env1, config=configs["on_0"])
set_vars(env, config=configs["on_0"])
# %%
fig, axs = plt.subplots(2, 1, figsize=(14, 10.5))
axs[0].set_title("New")
axs[0].plot(twnb1.s, twnb1.x * 1e3, label="X")
axs[0].plot(twnb1.s, twnb1.y * 1e3, label="Y")

axs[1].set_title("Old")
axs[1].plot(twb1.s, twb1.x * 1e3, label="X")
axs[1].plot(twb1.s, twb1.y * 1e3, label="Y")

for i in range(2):
    axs[i].grid()
    axs[i].legend()
    axs[i].set_xlabel("s [m]")
    axs[i].set_ylabel("$X,Y\ [mm]$")

    axs_t = axs[i].twiny()
    axs_t.set_xticks(
        twb1.rows["ip.*"].s,
        twb1.rows["ip.*"].name,
        rotation=90,
        size=8,
    )
    axs_t.set_xlim(axs[i].get_xlim()[0], axs[i].get_xlim()[1])
plt.show()

# %%
# env.to_json("opt_round_1000_xing_disp.json")
# %%
fig, axs = plt.subplots(2, 1, figsize=(14, 10.5))
axs[0].set_title("New")
axs[0].plot(twnb1.s, twnb1.x * 1e3, label="X")
axs[0].plot(twnb1.s, twnb1.y * 1e3, label="Y")

axs[1].set_title("Old")
axs[1].plot(twnb2.s, twnb2.x * 1e3, label="X")
axs[1].plot(twnb2.s, twnb2.y * 1e3, label="Y")

axs_t = axs[0].twiny()
axs_t.set_xticks(twnb1.rows["ip.*"].s, twnb1.rows["ip.*"].name)
axs_t.set_xlim(axs[0].get_xlim())
[axs_t.axvline(xpos, linestyle="--") for xpos in twnb1.rows["ip.*"].s]

axs_t = axs[1].twiny()
axs_t.set_xticks(twnb2.rows["ip.*"].s, twnb2.rows["ip.*"].name)
axs_t.set_xlim(axs[1].get_xlim())
[axs_t.axvline(xpos, linestyle="--") for xpos in twnb2.rows["ip.*"].s]

for i in range(2):
    axs[i].grid()
    axs[i].legend()
    axs[i].set_xlabel("s [m]")
    axs[i].set_ylabel("$X,Y\ [mm]$")
plt.show()

# %%
