# %%
import xtrack as xt
import rematch_hl_tools
from matplotlib import pyplot as plt

from utils import set_vars, configs

# %%
env1 = xt.Environment.from_json("rematch_round_1300_v3.json")
env = xt.Environment.from_json("rematch_round_1300_v3.json")
# %%
twb1 = env1["lhcb1"].cycle("ip3").twiss(method="4d")
twb2 = env1["lhcb2"].cycle("ip3").twiss(method="4d")
# %%
set_vars(env1, config=configs["on_0"])
set_vars(env, config=configs["on_0"])
# %%
default_tol = {None: 1e-8, "betx": 1e-6, "bety": 1e-6}
# %%
rematch_hl_tools.set_limits_steps_orbit_ip15(env)
# %%
opts = rematch_hl_tools.match_orbit_knobs_ip15(
    env, angle_match=290, tolerances=default_tol
)
# %%
rematch_hl_tools.rename_knobs_as_madx(env)
# %%
set_vars(env1, config=configs["on_x15hvs"])
set_vars(env, config=configs["on_x15hvs"])
# %%
twb1 = env1["lhcb1"].cycle("ip3").twiss(method="4d")
twnb1 = env["lhcb1"].cycle("ip3").twiss(method="4d")

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
plt.show()

# %%

env.to_json("opt_round_1300_xing.json")

# %%
