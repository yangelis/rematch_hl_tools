# %%
import xtrack as xt
import xpart as xp
from cpymad.madx import Madx

from rematch_hl_tools.utils import check_ip

# %%
opt_path = "../../../hllhc16"
optics_name = f"{opt_path}/strengths/round/opt_round_150_1500_optphases.madx"
# optics_name = f"{opt_path}/strengths/round/opt_round_150_1000.madx"

nrj = 7000
# %%
mad = Madx(stdout=True)
mad.call(f"{opt_path}/lhc.seq")
mad.call(f"{opt_path}/hllhc_sequence.madx")
mad.call(f"{opt_path}/toolkit/macro.madx")
mad.call(optics_name)
# mad.input(f'exec, mk_beam({nrj});')
mad.input(f"beam, sequence=lhcb1, particle=proton, energy={nrj};")
mad.input(f"beam, sequence=lhcb2, particle=proton, energy={nrj},bv=-1;")
mad.input("l.mbh = 0.001000;")
mad.use("lhcb1")
mad.use("lhcb2")


# %%
lines = xt.Environment.from_madx(madx=mad, return_lines=True)
# %%
env = xt.Environment(lines=lines)
# %%
# env.lhcb1.twiss_default["co_search_at"] = "ip7"
# env.lhcb2.twiss_default["co_search_at"] = "ip7"
env.lhcb1.twiss_default["method"] = "4d"
env.lhcb2.twiss_default["method"] = "4d"
env.lhcb2.twiss_default["reverse"] = True
# %%
# %%
check_ip(env, "b1")
# %%
check_ip(env, "b2")
# %%
env.to_json("hl16.json")

# %%
