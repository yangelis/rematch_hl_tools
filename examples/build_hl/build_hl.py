# %%
import xtrack as xt
from cpymad.madx import Madx

# %%
# opt_path = "../../../hl16"
opt_path = "../../../hl19"
# optics_name = f"{opt_path}/strengths/ramp/opt_ramp_6000.madx"

optics_name = f"{opt_path}/strengths/round/opt_round_150_1500.madx"

# optics_name = f"{opt_path}/strengths/round/opt_round_150_1000.madx"
# optics_name = "../../../acc-models-lhc_orig/strengths/round/start_collapse/opt_collapse_1320_1500.madx"
# optics_name = f"{opt_path}/strengths/round/start_collapse/opt_collapse_1000_1500.madx"

# optics_name = "../../../summer_optics/collapse/opt_collapse_1000_1500.madx"

nrj = 6800.0
# %%
mad = Madx(stdout=False)
mad.call(f"{opt_path}/lhc.seq")
mad.call(f"{opt_path}/lhc_hl19.seq")
mad.call(f"{opt_path}/hllhc_sequence.madx")
mad.call(optics_name)
mad.input(f"beam, sequence=lhcb1, particle=proton, energy={nrj};")
mad.input(f"beam, sequence=lhcb2, particle=proton, energy={nrj},bv=-1;")
mad.use("lhcb1")
mad.use("lhcb2")

# %%
lhcb1_ref = xt.Line.from_madx_sequence(mad.sequence.lhcb1, deferred_expressions=True)
lhcb2_ref = xt.Line.from_madx_sequence(mad.sequence.lhcb2, deferred_expressions=True)

# %%
particle_ref = xt.Particles(mass0=xt.PROTON_MASS_EV, p0c=nrj * 1e9)
lhcb1_ref.particle_ref = particle_ref
lhcb2_ref.particle_ref = particle_ref
# %%
tw_refb1 = lhcb1_ref.twiss4d()
tw_refb2 = lhcb2_ref.twiss4d()

print("beam1 qx", tw_refb1.qx, "beam1 qy", tw_refb1.qy)
print("beam2 qx", tw_refb2.qx, "beam2 qy", tw_refb2.qy)
# %%
tw_refb1.rows["ip.*"].cols["betx bety"]
# %%
env = xt.Environment(lines={"lhcb1": lhcb1_ref, "lhcb2": lhcb2_ref})
env.lhcb1.twiss_default["method"] = "4d"
env.lhcb2.twiss_default["method"] = "4d"
env.lhcb2.twiss_default["reverse"] = True

# %%
# env.to_json("hl19_inj.json")
env.to_json("hl19_round_150_1500.json")

# env.to_json("hl_round_150.json")
# %%
