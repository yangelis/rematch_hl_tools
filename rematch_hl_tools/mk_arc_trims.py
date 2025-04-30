def mkkqt_trim(collider, kq_type, bim):
    knob_template = "kqtfd.a78bim kqtfd.a23bim kqtfd.a34bim kqtfd.a67bim"
    knob_attach = f"{kq_type}.{bim}"
    for kt in knob_template.split():
        kn = kt.replace("kqtfd", kq_type).replace("bim", bim)
        collider.vars[kn] = collider.varval[kn] + (1 * collider.vars[knob_attach])


def mkks_trim(collider, ks_type, bim):
    knob_template = "ksfdn.a78bim ksfdn.a23bim ksfdn.a34bim ksfdn.a67bim"
    knob_attach = f"{ks_type}.{bim}"
    for kt in knob_template.split():
        for stype in ["1", "2"]:
            sn = kt.replace("n", stype).replace("ksfd", ks_type).replace("bim", bim)
            collider.vars[sn] = collider.varval[sn] + (1 * collider.vars[knob_attach])


def mk_arc_trims(collider):
    knobs_names = (
        "kqf.a81 kqf.a12 kqf.a45 kqf.a56 "
        "kqd.a81 kqd.a12 kqd.a45 kqd.a56 "
        "kqf.a78 kqf.a23 kqf.a34 kqf.a67 "
        "kqd.a78 kqd.a23 kqd.a34 kqd.a67 "
        "kqtf.a81b1 kqtf.a12b1 kqtf.a45b1 kqtf.a56b1 "
        "kqtd.a81b1 kqtd.a12b1 kqtd.a45b1 kqtd.a56b1 "
        "kqtf.a78b1 kqtf.a23b1 kqtf.a34b1 kqtf.a67b1 "
        "kqtd.a78b1 kqtd.a23b1 kqtd.a34b1 kqtd.a67b1 "
        "kqtf.a81b2 kqtf.a12b2 kqtf.a45b2 kqtf.a56b2 "
        "kqtd.a81b2 kqtd.a12b2 kqtd.a45b2 kqtd.a56b2 "
        "kqtf.a78b2 kqtf.a23b2 kqtf.a34b2 kqtf.a67b2 "
        "kqtd.a78b2 kqtd.a23b2 kqtd.a34b2 kqtd.a67b2"
    )

    for sk in knobs_names.split():
        collider.vars[sk] = collider.varval[sk]

    mkkqt_trim(collider, "kqtf", "b1")
    mkkqt_trim(collider, "kqtd", "b1")
    mkkqt_trim(collider, "kqtf", "b2")
    mkkqt_trim(collider, "kqtd", "b2")

    mkks_trim(collider, "ksf", "b1")
    mkks_trim(collider, "ksd", "b1")
    mkks_trim(collider, "ksf", "b2")
    mkks_trim(collider, "ksd", "b2")
