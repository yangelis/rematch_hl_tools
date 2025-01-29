# %%
import xtrack as xt
import rematch_hl_tools
from rematch_hl_tools import rematch_tune, rematch_chroma

# %%
env1 = xt.Environment.from_json("build_hl/hl_coll.json")
env = xt.Environment.from_json("build_hl/hl_coll.json")

# %%
tw_b1 = env.lhcb1.twiss4d()
tw_b2 = env.lhcb2.twiss4d()

# %%
print(f"Beam 1, Qx: {tw_b1.qx}, Qy: {tw_b1.qy}")
print(f"Beam 2, Qx: {tw_b2.qx}, Qy: {tw_b2.qy}")

# %%

tune_targets = {
    "b1": {
        "qx": 62.30,
        "qy": 60.34,
    },
    "b2": {
        "qx": 62.28,
        "qy": 60.31,
    },
}
# %%
opts_tune = rematch_tune(env, targets=tune_targets, solve=True)

# %%
tw_new_b1 = env.lhcb1.twiss4d()
tw_new_b2 = env.lhcb2.twiss4d()

print(f"Beam 1, Qx: {tw_new_b1.qx}, Qy: {tw_new_b1.qy}")
print(f"Beam 2, Qx: {tw_new_b2.qx}, Qy: {tw_new_b2.qy}")

# %%
print(f"Beam 1, DQx: {tw_b1.dqx}, DQy: {tw_b1.dqy}")
print(f"Beam 2, DQx: {tw_b2.dqx}, DQy: {tw_b2.dqy}")

# %%
chroma_targets = {
    "b1": {
        "dqx": 8,
        "dqy": 8,
    },
    "b2": {
        "dqx": 6,
        "dqy": 6,
    },
}
# %%
opts_chroma = rematch_chroma(env, targets=chroma_targets, solve=True)

# %%
tw_newc_b1 = env.lhcb1.twiss4d()
tw_newc_b2 = env.lhcb2.twiss4d()

print(f"Beam 1, DQx: {tw_newc_b1.dqx}, DQy: {tw_newc_b1.dqy}")
print(f"Beam 2, DQx: {tw_newc_b2.dqx}, DQy: {tw_newc_b2.dqy}")

# %%
