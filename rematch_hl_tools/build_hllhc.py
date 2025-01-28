from cpymad.madx import Madx
import xtrack as xt
import xpart as xp


def build_collider(optics_name, cycling=False, nrj=7000) -> xt.Environment:
    # NOTE: hard coded path of acc models for now
    mad1 = Madx()
    mad1.call("../acc-models-lhc/lhc.seq")
    mad1.call("../acc-models-lhc/hllhc_sequence.madx")
    mad1.input(f"beam, sequence=lhcb1, particle=proton, energy={nrj};")
    mad1.use("lhcb1")
    mad1.call(optics_name)

    mad4 = Madx()
    mad4.input("mylhcbeam=4")
    mad4.call("../acc-models-lhc/lhcb4.seq")
    mad4.call("../acc-models-lhc/hllhc_sequence.madx")
    mad4.input(f"beam, sequence=lhcb2, particle=proton, energy={nrj};")
    mad4.use("lhcb2")
    mad4.call(optics_name)

    line1 = xt.Line.from_madx_sequence(
        mad1.sequence.lhcb1,
        allow_thick=True,
        deferred_expressions=True,
        replace_in_expr={"bv_aux": "bvaux_b1"},
    )

    line4 = xt.Line.from_madx_sequence(
        mad4.sequence.lhcb2,
        allow_thick=True,
        deferred_expressions=True,
        replace_in_expr={"bv_aux": "bvaux_b2"},
    )

    if cycling:
        line1.cycle("ip3", inplace=True)
        line4.cycle("ip3", inplace=True)

    # Remove solenoids (cannot backtwiss for now)
    for ll in [line1, line4]:
        tt = ll.get_table()
        for nn in tt.rows[tt.element_type == "Solenoid"].name:
            ee_elen = ll[nn].length
            ll.element_dict[nn] = xt.Drift(length=ee_elen)

    env = xt.Environment(lines={"lhcb1": line1, "lhcb2": line4})
    env.lhcb1.particle_ref = xp.Particles(mass0=xp.PROTON_MASS_EV, p0c=nrj * 1e9)
    env.lhcb2.particle_ref = xp.Particles(mass0=xp.PROTON_MASS_EV, p0c=nrj * 1e9)

    env.lhcb1.twiss_default["method"] = "4d"
    env.lhcb2.twiss_default["method"] = "4d"
    env.lhcb2.twiss_default["reverse"] = True

    env.build_trackers()

    return env
