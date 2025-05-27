# %%
import xtrack as xt
import rematch_hl_tools
from matplotlib import pyplot as plt

from utils import set_vars, configs

# %%
env1 = xt.Environment.from_json("build_hl/hl_round_1000.json")
env = xt.Environment.from_json("build_hl/hl_round_1000.json")

# %%
# env1.vars.load_madx_optics_file('../../hl16/strengths/collapse/opt_collapse_1100_1500.madx')
# env.vars.load_madx_optics_file(
# "../../hl16/strengths/collapse/opt_round_1100_highcrab.madx"
# )
env.vars.load_madx_optics_file(
    "../../hl16/strengths/collapse/opt_round_1100_lowcrab.madx"
)
# %%

set_vars(env, config=configs["on_0"])
set_vars(env1, config=configs["on_0"])
# %%
default_tol = {
    None: 1e-8,
    "betx": 1e-6,
    "bety": 1e-6,
    "x": 1e-17,
    "px": 1e-17,
    "y": 1e-17,
    "py": 1e-17,
}


# %%
rematch_hl_tools.set_limits_steps_ahvcrab(env)
# %%
optcc = rematch_hl_tools.rematch_crabs(env, default_tol=default_tol)

# %%
tw = env.lhcb1.cycle("ip3").twiss4d()

# %%
dmux = tw.rows["ip5"].mux - tw.rows["acfca.4bl5.b1"].mux
dmuy = tw.rows["ip5"].muy - tw.rows["acfca.4bl5.b1"].muy

# %%
tw.rows["acfca.*"]
# %%
env.vars["nrj"] = 7000
env.vars["z_crab"] = 1e-3

env.vars["on_crab1"] = -190
env.vars["on_crab5"] = -190


env1.vars["nrj"] = 7000
env1.vars["z_crab"] = 1e-3
env1.vars["on_crab1"] = -190
env1.vars["on_crab5"] = -190

env.vars["vrf400"] = 16
env1.vars["vrf400"] = 16

# env.vars["nrj"] = 0
# env.vars["z_crab"] = 0

# %%
otw = env1.lhcb1.cycle("ip3").twiss4d()
tw = env.lhcb1.cycle("ip3").twiss4d()
# %%
print(otw.rows["ip.*"])
print(tw.rows["ip.*"])
# %%
tw.plot("x y")
# %%
otw.plot("x y")

# %%
tw.plot("dx_zeta")
# %%
otw.plot("dx_zeta")

# %%
