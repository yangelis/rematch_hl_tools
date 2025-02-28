# %%
import xtrack as xt
import rematch_hl_tools
from matplotlib import pyplot as plt

from utils import set_vars, configs

# %%
env1 = xt.Environment.from_json("rematch_round_1000.json")
env = xt.Environment.from_json("rematch_round_1000.json")


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