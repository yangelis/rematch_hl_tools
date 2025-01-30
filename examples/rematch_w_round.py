# %%
import xtrack as xt
import rematch_hl_tools
from rematch_hl_tools.rematch_w import _reset_sext_knobs
from matplotlib import pyplot as plt

# %%
# env1 = xt.Environment.from_json("build_hl/hl_coll.json")
# env = xt.Environment.from_json("build_hl/hl_coll.json")

env1 = xt.Environment.from_json("rematch_round_1300.json")
env = xt.Environment.from_json("rematch_round_1300_v3.json")

# %%
rematch_hl_tools.set_limits_steps_sextupoles_w(env)

env.varval["on_x1"] = 0
env.varval["on_x5"] = 0
env.varval["on_x2"] = 0
env.varval["on_sep2"] = 0
env.varval["on_x8v"] = 0
env.varval["on_sep8h"] = 0
env.varval["on_sep8v"] = 0
# %%
twb1 = env1["lhcb1"].cycle("ip3").twiss(method="4d")
twb2 = env1["lhcb2"].cycle("ip3").twiss(method="4d")

# %%
opts = rematch_hl_tools.rematch_w_default(env)
# %%
twb1_w = env["lhcb1"].cycle("ip3").twiss(method="4d")
twb2_w = env["lhcb2"].cycle("ip3").twiss(method="4d")
# %%
fig, axs = plt.subplots(figsize=(14, 10.5))
axs.plot(
    twb1.s, twb1.wx_chrom, label=r"$W_x$ Original", ls="--", alpha=0.4, color="black"
)
axs.plot(
    twb1.s, twb1.wy_chrom, label=r"$W_y$ Original", ls="--", alpha=0.4, color="red"
)

axs.plot(twb1_w.s, twb1_w.wx_chrom, label=r"$W_x$, Rematched", color="black")
axs.plot(twb1_w.s, twb1_w.wy_chrom, label=r"$W_y$, Rematched", color="red")

axs_t = axs.twiny()
axs_t.set_xticks(twb1_w.rows["ip.*"].s, twb1_w.rows["ip.*"].name)
axs_t.set_xlim(axs.get_xlim())
[axs_t.axvline(xpos, linestyle="--") for xpos in twb1_w.rows["ip.*"].s]
axs.set_xlabel("s [m]")
axs.set_ylabel(r"$W_{x,y}$")
axs.legend()
plt.show()

# %%
fig, axs = plt.subplots(figsize=(14, 10.5))
axs.plot(
    twb2.s, twb2.wx_chrom, label=r"$W_x$ Original", ls="--", alpha=0.4, color="black"
)
axs.plot(
    twb2.s, twb2.wy_chrom, label=r"$W_y$ Original", ls="--", alpha=0.4, color="red"
)

axs.plot(twb2_w.s, twb2_w.wx_chrom, label=r"$W_x$, Rematched", color="black")
axs.plot(twb2_w.s, twb2_w.wy_chrom, label=r"$W_y$, Rematched", color="red")

axs_t = axs.twiny()
axs_t.set_xticks(twb2_w.rows["ip.*"].s, twb2_w.rows["ip.*"].name)
axs_t.set_xlim(axs.get_xlim())
[axs_t.axvline(xpos, linestyle="--") for xpos in twb2_w.rows["ip.*"].s]
axs.set_xlabel("s [m]")
axs.set_ylabel(r"$W_{x,y}$")
axs.legend()
plt.show()
# %%
for ksfd in (
    rematch_hl_tools.ksf_names_non_ats_arcs.split()
    + rematch_hl_tools.ksd_names_non_ats_arcs.split()
):
    ksf_name = ksfd.replace("bim", "b1")
    temp_expr1 = env1.vars[ksf_name]._expr
    temp_expr = env.vars[ksf_name]._expr
    print(f"{ksf_name}: Old: {temp_expr1}, New: {temp_expr}")
# %%
for ksfd in (
    rematch_hl_tools.ksf_names_ats_arcs.split()
    + rematch_hl_tools.ksd_names_ats_arcs.split()
):
    ksf_name = ksfd.replace("bim", "b1")
    print(f"{ksf_name}: Old: {env1.varval[ksf_name]}, New: {env.varval[ksf_name]}")

# %%
