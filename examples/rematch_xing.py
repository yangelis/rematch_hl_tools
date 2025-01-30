# %%
import xtrack as xt
import rematch_hl_tools
from rematch_hl_tools.rematch_w import _reset_sext_knobs
from matplotlib import pyplot as plt

# %%
env1 = xt.Environment.from_json("rematch_round_1300_v3.json")
env = xt.Environment.from_json("rematch_round_1300_v3.json")
# %%
twb1 = env1["lhcb1"].cycle("ip3").twiss(method="4d")
twb2 = env1["lhcb2"].cycle("ip3").twiss(method="4d")


# %%
def set_vars(collider, config):
    print(config)
    for key, val in config.items():
        collider.varval[key] = val


configs = {
    "on_0": {
        "cd2q4": 0,
        "on_disp": 0,
        "on_x1": 0,
        "on_x5": 0,
        "on_sep1": 0,
        "on_sep5": 0,
        "phi_ir1": 0,
        "phi_ir5": 90,
        "on_a1": 0,
        "on_a5": 0,
    },
    "on_x1hs": {
        "cd2q4": 0,
        "on_x1": 250,
        "on_x5": 0,
        "on_sep1": 0,
        "phi_ir1": 0,
        "phi_ir5": 90,
    },
    "on_x1hl": {
        "cd2q4": 1,
        "on_x1": 250,
        "on_x5": 0,
        "on_sep1": 0,
        "phi_ir1": 0,
        "phi_ir5": 90,
    },
    "on_x1vs": {
        "cd2q4": 0,
        "on_x1": 250,
        "on_x5": 0,
        "on_sep1": 0,
        "phi_ir1": 90,
        "phi_ir5": 0,
    },
    "on_x1vl": {
        "cd2q4": 1,
        "on_x1": 250,
        "on_x5": 0,
        "on_sep1": 0,
        "phi_ir1": 90,
        "phi_ir5": 0,
    },
    "on_x5hs": {
        "cd2q4": 0,
        "on_x1": 0,
        "on_x5": 250,
        "on_sep1": 0,
        "phi_ir1": 90,
        "phi_ir5": 0,
    },
    "on_x5hl": {
        "cd2q4": 1,
        "on_x1": 0,
        "on_x5": 250,
        "on_sep1": 0,
        "phi_ir1": 90,
        "phi_ir5": 0,
    },
    "on_x5vs": {
        "cd2q4": 0,
        "on_x1": 0,
        "on_x5": 250,
        "on_sep1": 0,
        "phi_ir1": 0,
        "phi_ir5": 90,
    },
    "on_x5vl": {
        "cd2q4": 1,
        "on_x1": 0,
        "on_x5": 250,
        "on_sep1": 0,
        "phi_ir1": 0,
        "phi_ir5": 90,
    },
    "on_x15hvs": {
        "cd2q4": 0,
        "on_x1": 250,
        "on_x5": 250,
        "on_sep1": 0,
        "phi_ir1": 0,
        "phi_ir5": 90,
    },
    "on_x15hvl": {
        "cd2q4": 1,
        "on_x1": 250,
        "on_x5": 250,
        "on_sep1": 0,
        "phi_ir1": 0,
        "phi_ir5": 90,
    },
    "on_sep1v": {"on_sep1": 2, "phi_ir1": 0},
    "on_sep5h": {"on_sep5": 2, "phi_ir5": 90},
    "on_sep1h": {"on_sep1": 2, "phi_ir1": 90},
    "on_sep5v": {"on_sep5": 2, "phi_ir5": 0},
    "on_a1v": {"on_a1": 1},
    "on_a1h": {"on_a1": 1, "phi_ir1": 90},
    "on_a5h": {"on_a5": 1},
    "on_a5v": {"on_a5": 1, "phi_ir5": 0},
}
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

env.to_json('opt_round_1300_xing.json')

# %%
