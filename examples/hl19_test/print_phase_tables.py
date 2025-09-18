# %%
import xtrack as xt
import rematch_hl_tools

from rematch_hl_tools.utils import check_ip, crit_phases

from pprint import pprint
import pandas as pd

# %%
hl19_path = "/home/iangelis/Projects/hllhc_optics/hl19"
# %%
env = xt.Environment.from_json("../build_hl/hl19_cc.json")
# %%
pre = "optics"
optics = [
    # f"{pre}/hl19_opt_round_150_ir7_both_v2_20250711.madx",
    # f"{pre}/opt_round_150_ir7_b12_phases_iter4.madx",
    # f"{pre}/opt_round_150_ir7_b12_phases_a34_67_iter3.madx",
    # f"{pre}/hl19_opt_round_150_ir7_both_20250801.madx",
    # f"{pre}/hl19_opt_round_150_ir7_both_20250801_v2.madx",
    # f"{pre}/hl19_opt_round_150_ir7_both_20250801_v2_phase_try1.madx",
    # f"{pre}/hl19_opt_round_150_ir7_both_20250801_v2_phase_middle.madx",
    # f"{pre}/hl19_opt_round_150_ir7_both_20250801_v2_phase_middle2.madx",
    # f"{pre}/hl19_opt_round_150_ir7_both_20250801_v2_phase_middle3.madx",
    # f"{pre}/hl19_opt_round_150_ir7_both_20250801_v2_phase_middle4.madx",
    # f"{pre}/hl19_opt_round_150_ir7_both_20250801_v2_phase_middle4_rematched.madx",
    # f"{pre}/hl19_opt_round_150_ir7_both_20250801_v2_phase_middle4_rematched_v2.madx",
    # f"{pre}/hl19_opt_round_150_ir7_both_20250801_v2_phase_middle4_rematched_v3.madx",
    # f"{pre}/hl19_opt_round_150_ir7_both_20250801_v2_phase_middle4_rematched_v6.madx",
    # f"{pre}/opt_round_15cm_ir7_no_crabs_v2.madx",
    f"{pre}/opt_round_20cm_ir7_no_crabs_v2.madx",
    # f"{pre}/opt_round_47cm_ir7_no_crabs_v3.madx",
    # f"{pre}/opt_round_64cm_ir7_no_crabs.madx",
]
# %%
for opt in optics:
    print(opt)
    env.vars.load_madx_optics_file(opt)
    phases = crit_phases(env)
    print(pd.DataFrame(phases[0]).transpose().to_markdown())
    print(pd.DataFrame(phases[1]).transpose().to_markdown())
    print(pd.DataFrame(phases[2]).transpose().to_markdown())
    print("\n\n\n")
# %%
env.vars.load_madx_optics_file(optics[-1])
# %%
check_ip(env, "b1")
# %%
check_ip(env, "b2")

# %%
