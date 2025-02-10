# %%
import xtrack as xt
from cpymad.madx import Madx

# %%
# optics_name = "../../../acc-models-lhc/strengths/round/opt_round_150_1000.madx"
optics_name = "../../../acc-models-lhc_orig/strengths/round/start_collapse/opt_collapse_1320_1500.madx"
# %%
mad = Madx(stdout=False)
mad.call("../../../acc-models-lhc/lhc.seq")
mad.call("../../../acc-models-lhc/hllhc_sequence.madx")
mad.call("../../../acc-models-lhc/hllhc_sequence.madx")
mad.call(optics_name)
mad.input("beam, sequence=lhcb1, particle=proton, energy=6800;")
mad.input("beam, sequence=lhcb2, particle=proton, energy=6800,bv=-1;")
mad.use("lhcb1")
mad.use("lhcb2")

# %%
lhcb1_ref = xt.Line.from_madx_sequence(mad.sequence.lhcb1, deferred_expressions=True)
lhcb2_ref = xt.Line.from_madx_sequence(mad.sequence.lhcb2, deferred_expressions=True)

# %%
particle_ref = xt.Particles(mass0=xt.PROTON_MASS_EV, p0c=7000e9)
lhcb1_ref.particle_ref = particle_ref
lhcb2_ref.particle_ref = particle_ref
# %%
tw_refb1 = lhcb1_ref.twiss4d()
tw_refb2 = lhcb2_ref.twiss4d()

print("line beam1 qx", tw_refb1.qx)
print("line beam2 qx", tw_refb2.qx)

# %%
env = xt.Environment(lines={"lhcb1": lhcb1_ref, "lhcb2": lhcb2_ref})
env.lhcb1.twiss_default["method"] = "4d"
env.lhcb2.twiss_default["method"] = "4d"
env.lhcb2.twiss_default["reverse"] = True

# %%

env.to_json("hl_coll.json")
# %%
