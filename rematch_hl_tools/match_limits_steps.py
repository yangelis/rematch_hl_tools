scale = 23348.89927
grad = 132.2
scl = 0.06
sch = 0.99
sc79 = 0.999
bmaxds = 500
imb = 1.50

qtlim1 = grad / scale
qtlim2 = 160.0 / scale
qtlimq5 = 160.0 / scale
# qtlimq5= 160.0/scale;
qtlim3 = 200.0 / scale
qtlim4 = 125.0 / scale
qtlim5 = 120.0 / scale
qtlimq4 = 160.0 / scale

scale_cor = 23348.89927 / 2
CLIMmcbxfb = 2.5 / scale_cor
CLIMmcbxfa = 4.5 / scale_cor
CLIMmcbrd = 5.0 / scale_cor
CLIMmcby4 = 2.25 / scale_cor
CLIMmcbc = 2.1 / scale_cor


def set_limits_steps_quads_ip15(collider):
    quads_ir15_defaults = {
        # Triplet
        "kqx1.l1": {"step": 1e-6, "limits": (-qtlim1, -0.90 * qtlim1)},
        "kqx2a.l1": {"step": 1e-6, "limits": (-qtlim1, -0.90 * qtlim1)},
        "kqx3.l1": {"step": 1e-6, "limits": (-qtlim1, -0.90 * qtlim1)},
        "kqx1.l5": {"step": 1e-6, "limits": (-qtlim1, -0.90 * qtlim1)},
        "kqx2a.l5": {"step": 1e-6, "limits": (-qtlim1, -0.90 * qtlim1)},
        "kqx3.l5": {"step": 1e-6, "limits": (-qtlim1, -0.90 * qtlim1)},
        # kq4
        "kq4.l1b1": {"step": 1e-6, "limits": (scl * qtlimq4, sch * qtlimq4)},
        "kq4.r1b1": {"step": 1e-6, "limits": (-sch * qtlimq4, -scl * qtlimq4)},
        "kq4.l1b2": {"step": 1e-6, "limits": (-sch * qtlimq4, -scl * qtlimq4)},
        "kq4.r1b2": {"step": 1e-6, "limits": (scl * qtlimq4, sch * qtlimq4)},
        "kq4.l5b1": {"step": 1e-6, "limits": (scl * qtlimq4, sch * qtlimq4)},
        "kq4.r5b1": {"step": 1e-6, "limits": (-sch * qtlimq4, -scl * qtlimq4)},
        "kq4.l5b2": {"step": 1e-6, "limits": (-sch * qtlimq4, -scl * qtlimq4)},
        "kq4.r5b2": {"step": 1e-6, "limits": (scl * qtlimq4, sch * qtlimq4)},
        # kq5
        "kq5.l1b1": {"step": 1e-6, "limits": (-sch * qtlimq5, -scl * qtlimq5)},
        "kq5.r1b1": {"step": 1e-6, "limits": (scl * qtlimq5, sch * qtlimq5)},
        "kq5.l1b2": {"step": 1e-6, "limits": (scl * qtlimq5, sch * qtlimq5)},
        "kq5.r1b2": {"step": 1e-6, "limits": (-sch * qtlimq5, -scl * qtlimq5)},
        "kq5.l5b1": {"step": 1e-6, "limits": (-sch * qtlimq5, -scl * qtlimq5)},
        "kq5.r5b1": {"step": 1e-6, "limits": (scl * qtlimq5, sch * qtlimq5)},
        "kq5.l5b2": {"step": 1e-6, "limits": (scl * qtlimq5, sch * qtlimq5)},
        "kq5.r5b2": {"step": 1e-6, "limits": (-sch * qtlimq5, -scl * qtlimq5)},
        # kq6
        "kq6.l1b1": {"step": 1e-6, "limits": (scl * qtlim2, sch * qtlim2)},
        "kq6.r1b1": {"step": 1e-6, "limits": (-sch * qtlim2, -scl * qtlim2)},
        "kq6.l1b2": {"step": 1e-6, "limits": (-sch * qtlim2, -scl * qtlim2)},
        "kq6.r1b2": {"step": 1e-6, "limits": (scl * qtlim2, sch * qtlim2)},
        "kq6.l5b1": {"step": 1e-6, "limits": (scl * qtlim2, sch * qtlim2)},
        "kq6.r5b1": {"step": 1e-6, "limits": (-sch * qtlim2, -scl * qtlim2)},
        "kq6.l5b2": {"step": 1e-6, "limits": (-sch * qtlim2, -scl * qtlim2)},
        "kq6.r5b2": {"step": 1e-6, "limits": (scl * qtlim2, sch * qtlim2)},
        # kq7
        "kq7.l1b1": {"step": 1e-6, "limits": (-sc79 * qtlim3, -scl * qtlim3)},
        "kq7.r1b1": {"step": 1e-6, "limits": (scl * qtlim3, sc79 * qtlim3)},
        "kq7.l1b2": {"step": 1e-6, "limits": (scl * qtlim3, sc79 * qtlim3)},
        "kq7.r1b2": {"step": 1e-6, "limits": (-sc79 * qtlim3, -scl * qtlim3)},
        "kq7.l5b1": {"step": 1e-6, "limits": (-sc79 * qtlim3, -scl * qtlim3)},
        "kq7.r5b1": {"step": 1e-6, "limits": (scl * qtlim3, sc79 * qtlim3)},
        "kq7.l5b2": {"step": 1e-6, "limits": (scl * qtlim3, sc79 * qtlim3)},
        "kq7.r5b2": {"step": 1e-6, "limits": (-sc79 * qtlim3, -scl * qtlim3)},
        # kq8
        "kq8.l1b1": {"step": 1e-6, "limits": (scl * qtlim3, sc79 * qtlim3)},
        "kq8.r1b1": {"step": 1e-6, "limits": (-sc79 * qtlim3, -scl * qtlim3)},
        "kq8.l1b2": {"step": 1e-6, "limits": (-sc79 * qtlim3, -scl * qtlim3)},
        "kq8.r1b2": {"step": 1e-6, "limits": (scl * qtlim3, sc79 * qtlim3)},
        "kq8.l5b1": {"step": 1e-6, "limits": (scl * qtlim3, sc79 * qtlim3)},
        "kq8.r5b1": {"step": 1e-6, "limits": (-sc79 * qtlim3, -scl * qtlim3)},
        "kq8.l5b2": {"step": 1e-6, "limits": (-sc79 * qtlim3, -scl * qtlim3)},
        "kq8.r5b2": {"step": 1e-6, "limits": (scl * qtlim3, sc79 * qtlim3)},
        # kq9
        "kq9.l1b1": {"step": 1e-6, "limits": (-sc79 * qtlim3, -scl * qtlim3)},
        "kq9.r1b1": {"step": 1e-6, "limits": (scl * qtlim3, sc79 * qtlim3)},
        "kq9.l1b2": {"step": 1e-6, "limits": (scl * qtlim3, sc79 * qtlim3)},
        "kq9.r1b2": {"step": 1e-6, "limits": (-sc79 * qtlim3, -scl * qtlim3)},
        "kq9.l5b1": {"step": 1e-6, "limits": (-sc79 * qtlim3, -scl * qtlim3)},
        "kq9.r5b1": {"step": 1e-6, "limits": (scl * qtlim3, sc79 * qtlim3)},
        "kq9.l5b2": {"step": 1e-6, "limits": (scl * qtlim3, sc79 * qtlim3)},
        "kq9.r5b2": {"step": 1e-6, "limits": (-sc79 * qtlim3, -scl * qtlim3)},
        # kq10
        "kq10.l1b1": {"step": 1e-6, "limits": (scl * qtlim3, sch * qtlim3)},
        "kq10.r1b1": {"step": 1e-6, "limits": (-sch * qtlim3, -scl * qtlim3)},
        "kq10.l1b2": {"step": 1e-6, "limits": (-sch * qtlim3, -scl * qtlim3)},
        "kq10.r1b2": {"step": 1e-6, "limits": (scl * qtlim3, sch * qtlim3)},
        "kq10.l5b1": {"step": 1e-6, "limits": (scl * qtlim3, sch * qtlim3)},
        "kq10.r5b1": {"step": 1e-6, "limits": (-sch * qtlim3, -scl * qtlim3)},
        "kq10.l5b2": {"step": 1e-6, "limits": (-sch * qtlim3, -scl * qtlim3)},
        "kq10.r5b2": {"step": 1e-6, "limits": (scl * qtlim3, sch * qtlim3)},
        # kqtl11
        "kqtl11.l1b1": {"step": 1e-6, "limits": (-sch * qtlim4, sch * qtlim4)},
        "kqtl11.r1b1": {"step": 1e-6, "limits": (-sch * qtlim4, sch * qtlim4)},
        "kqtl11.l1b2": {"step": 1e-6, "limits": (-sch * qtlim4, sch * qtlim4)},
        "kqtl11.r1b2": {
            "step": 1e-6,
            "limits": (-sch * qtlim4 * 500 / 550, sch * qtlim4 * 500 / 550),
        },
        "kqtl11.l5b1": {"step": 1e-6, "limits": (-sch * qtlim4, sch * qtlim4)},
        "kqtl11.r5b1": {"step": 1e-6, "limits": (-sch * qtlim4, sch * qtlim4)},
        "kqtl11.l5b2": {"step": 1e-6, "limits": (-sch * qtlim4, sch * qtlim4)},
        "kqtl11.r5b2": {
            "step": 1e-6,
            "limits": (-sch * qtlim4 * 500 / 550, sch * qtlim4 * 500 / 550),
        },
        # kqt12
        "kqt12.l1b1": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
        "kqt12.r1b1": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
        "kqt12.l1b2": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
        "kqt12.r1b2": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
        "kqt12.l5b1": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
        "kqt12.r5b1": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
        "kqt12.l5b2": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
        "kqt12.r5b2": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
        # kqt13
        "kqt13.l1b1": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
        "kqt13.r1b1": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
        "kqt13.l1b2": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
        "kqt13.r1b2": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
        "kqt13.l5b1": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
        "kqt13.r5b1": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
        "kqt13.l5b2": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
        "kqt13.r5b2": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
    }


def set_limits_steps_orbit_ip15(collider):
    orbit_correctors_ip15_limits = {
        # MCBX
        "acbxh1.l1": {"step": 1e-12, "limits": (-CLIMmcbxfb, CLIMmcbxfb)},
        "acbxh1.r1": {"step": 1e-12, "limits": (-CLIMmcbxfb, CLIMmcbxfb)},
        "acbxh2.l1": {"step": 1e-12, "limits": (-CLIMmcbxfb, CLIMmcbxfb)},
        "acbxh2.r1": {"step": 1e-12, "limits": (-CLIMmcbxfb, CLIMmcbxfb)},
        "acbxh3.l1": {"step": 1e-12, "limits": (-CLIMmcbxfa, CLIMmcbxfa)},
        "acbxh3.r1": {"step": 1e-12, "limits": (-CLIMmcbxfa, CLIMmcbxfa)},
        "acbxv1.l1": {"step": 1e-12, "limits": (-CLIMmcbxfb, CLIMmcbxfb)},
        "acbxv1.r1": {"step": 1e-12, "limits": (-CLIMmcbxfb, CLIMmcbxfb)},
        "acbxv2.l1": {"step": 1e-12, "limits": (-CLIMmcbxfb, CLIMmcbxfb)},
        "acbxv2.r1": {"step": 1e-12, "limits": (-CLIMmcbxfb, CLIMmcbxfb)},
        "acbxv3.l1": {"step": 1e-12, "limits": (-CLIMmcbxfa, CLIMmcbxfa)},
        "acbxv3.r1": {"step": 1e-12, "limits": (-CLIMmcbxfa, CLIMmcbxfa)},
        "acbxh1.l5": {"step": 1e-12, "limits": (-CLIMmcbxfb, CLIMmcbxfb)},
        "acbxh1.r5": {"step": 1e-12, "limits": (-CLIMmcbxfb, CLIMmcbxfb)},
        "acbxh2.l5": {"step": 1e-12, "limits": (-CLIMmcbxfb, CLIMmcbxfb)},
        "acbxh2.r5": {"step": 1e-12, "limits": (-CLIMmcbxfb, CLIMmcbxfb)},
        "acbxh3.l5": {"step": 1e-12, "limits": (-CLIMmcbxfa, CLIMmcbxfa)},
        "acbxh3.r5": {"step": 1e-12, "limits": (-CLIMmcbxfa, CLIMmcbxfa)},
        "acbxv1.l5": {"step": 1e-12, "limits": (-CLIMmcbxfb, CLIMmcbxfb)},
        "acbxv1.r5": {"step": 1e-12, "limits": (-CLIMmcbxfb, CLIMmcbxfb)},
        "acbxv2.l5": {"step": 1e-12, "limits": (-CLIMmcbxfb, CLIMmcbxfb)},
        "acbxv2.r5": {"step": 1e-12, "limits": (-CLIMmcbxfb, CLIMmcbxfb)},
        "acbxv3.l5": {"step": 1e-12, "limits": (-CLIMmcbxfa, CLIMmcbxfa)},
        "acbxv3.r5": {"step": 1e-12, "limits": (-CLIMmcbxfa, CLIMmcbxfa)},
        # MCBRD
        "acbrdh4.l1b1aux": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdh4.l1b2aux": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdh4.r1b1aux": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdh4.r1b2aux": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdv4.l1b1aux": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdv4.l1b2aux": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdv4.r1b1aux": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdv4.r1b2aux": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdh4.l5b1aux": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdh4.l5b2aux": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdh4.r5b1aux": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdh4.r5b2aux": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdv4.l5b1aux": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdv4.l5b2aux": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdv4.r5b1aux": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdv4.r5b2aux": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdh4.l1b1": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdh4.l1b2": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdh4.r1b1": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdh4.r1b2": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdv4.l1b1": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdv4.l1b2": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdv4.r1b1": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdv4.r1b2": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdh4.l5b1": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdh4.l5b2": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdh4.r5b1": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdh4.r5b2": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdv4.l5b1": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdv4.l5b2": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdv4.r5b1": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        "acbrdv4.r5b2": {"step": 1e-12, "limits": (-CLIMmcbrd, CLIMmcbrd)},
        # MCBC
        "acbch5.l1b2": {"step": 1e-12, "limits": (-CLIMmcbc, CLIMmcbc)},
        "acbch5.r1b1": {"step": 1e-12, "limits": (-CLIMmcbc, CLIMmcbc)},
        "acbch6.l1b1": {"step": 1e-12, "limits": (-CLIMmcbc, CLIMmcbc)},
        "acbch6.r1b2": {"step": 1e-12, "limits": (-CLIMmcbc, CLIMmcbc)},
        "acbcv5.l1b1": {"step": 1e-12, "limits": (-CLIMmcbc, CLIMmcbc)},
        "acbcv5.r1b2": {"step": 1e-12, "limits": (-CLIMmcbc, CLIMmcbc)},
        "acbcv6.l1b2": {"step": 1e-12, "limits": (-CLIMmcbc, CLIMmcbc)},
        "acbcv6.r1b1": {"step": 1e-12, "limits": (-CLIMmcbc, CLIMmcbc)},
        "acbch5.l5b2": {"step": 1e-12, "limits": (-CLIMmcbc, CLIMmcbc)},
        "acbch5.r5b1": {"step": 1e-12, "limits": (-CLIMmcbc, CLIMmcbc)},
        "acbch6.l5b1": {"step": 1e-12, "limits": (-CLIMmcbc, CLIMmcbc)},
        "acbch6.r5b2": {"step": 1e-12, "limits": (-CLIMmcbc, CLIMmcbc)},
        "acbcv5.l5b1": {"step": 1e-12, "limits": (-CLIMmcbc, CLIMmcbc)},
        "acbcv5.r5b2": {"step": 1e-12, "limits": (-CLIMmcbc, CLIMmcbc)},
        "acbcv6.l5b2": {"step": 1e-12, "limits": (-CLIMmcbc, CLIMmcbc)},
        "acbcv6.r5b1": {"step": 1e-12, "limits": (-CLIMmcbc, CLIMmcbc)},
        # MCBY
        "acbyhs4.l1b1": {"step": 1e-12, "limits": (-CLIMmcby4, CLIMmcby4)},
        "acbyhs4.l1b2": {"step": 1e-12, "limits": (-CLIMmcby4, CLIMmcby4)},
        "acbyhs4.r1b1": {"step": 1e-12, "limits": (-CLIMmcby4, CLIMmcby4)},
        "acbyhs4.r1b2": {"step": 1e-12, "limits": (-CLIMmcby4, CLIMmcby4)},
        "acbyvs4.l1b1": {"step": 1e-12, "limits": (-CLIMmcby4, CLIMmcby4)},
        "acbyvs4.l1b2": {"step": 1e-12, "limits": (-CLIMmcby4, CLIMmcby4)},
        "acbyvs4.r1b1": {"step": 1e-12, "limits": (-CLIMmcby4, CLIMmcby4)},
        "acbyvs4.r1b2": {"step": 1e-12, "limits": (-CLIMmcby4, CLIMmcby4)},
        "acbyhs4.l5b1": {"step": 1e-12, "limits": (-CLIMmcby4, CLIMmcby4)},
        "acbyhs4.l5b2": {"step": 1e-12, "limits": (-CLIMmcby4, CLIMmcby4)},
        "acbyhs4.r5b1": {"step": 1e-12, "limits": (-CLIMmcby4, CLIMmcby4)},
        "acbyhs4.r5b2": {"step": 1e-12, "limits": (-CLIMmcby4, CLIMmcby4)},
        "acbyvs4.l5b1": {"step": 1e-12, "limits": (-CLIMmcby4, CLIMmcby4)},
        "acbyvs4.l5b2": {"step": 1e-12, "limits": (-CLIMmcby4, CLIMmcby4)},
        "acbyvs4.r5b1": {"step": 1e-12, "limits": (-CLIMmcby4, CLIMmcby4)},
        "acbyvs4.r5b2": {"step": 1e-12, "limits": (-CLIMmcby4, CLIMmcby4)},
    }

    collider.vars.vary_default.update(orbit_correctors_ip15_limits)


kmcb_max = 800e-6


def set_limits_steps_disp_correctors(collider, kmcb_max=kmcb_max):
    # TODO: find good step
    disp_correctors_default = {
        # IP1 Beam1
        "acbh16.r8b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbh14.l1b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbh12.l1b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbh13.r1b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbh15.r1b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbh15.l2b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv15.r8b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv15.l1b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv13.l1b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv12.r1b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv14.r1b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv16.l2b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        # IP1 Beam2
        "acbh15.r8b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbh15.l1b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbh13.l1b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbh12.r1b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbh14.r1b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbh16.l2b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv16.r8b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv14.l1b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv12.l1b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv13.r1b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv15.r1b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv15.l2b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        # IP5 Beam1
        "acbh16.r4b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbh14.l5b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbh12.l5b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbh13.r5b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbh15.r5b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbh15.l6b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv15.r4b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv15.l5b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv13.l5b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv12.r5b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv14.r5b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv16.l6b1": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        # IP5 Beam 2
        "acbh15.r4b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbh15.l5b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbh13.l5b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbh12.r5b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbh14.r5b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbh16.l6b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv16.r4b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv14.l5b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv12.l5b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv13.r5b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv15.r5b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
        "acbv15.l6b2": {"step": 1e-11, "limits": (-kmcb_max, kmcb_max)},
    }
    collider.vars.vary_default.update(disp_correctors_default)


k2max = 0.38


def set_limits_steps_sextupoles_w(collider):
    sextupoles_defaults = {
        # Beam 1
        "ksf1.a81b1": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksf2.a81b1": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksd1.a81b1": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksd2.a81b1": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksf1.a12b1": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksf2.a12b1": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksd1.a12b1": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksd2.a12b1": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksf1.a45b1": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksf2.a45b1": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksd1.a45b1": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksd2.a45b1": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksf1.a56b1": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksf2.a56b1": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksd1.a56b1": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksd2.a56b1": {"step": 1e-4, "limits": (-k2max, k2max)},
        # Beam 2
        "ksf1.a81b2": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksf2.a81b2": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksd1.a81b2": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksd2.a81b2": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksf1.a12b2": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksf2.a12b2": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksd1.a12b2": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksd2.a12b2": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksf1.a45b2": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksf2.a45b2": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksd1.a45b2": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksd2.a45b2": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksf1.a56b2": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksf2.a56b2": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksd1.a56b2": {"step": 1e-4, "limits": (-k2max, k2max)},
        "ksd2.a56b2": {"step": 1e-4, "limits": (-k2max, k2max)},
    }
    collider.vars.vary_default.update(sextupoles_defaults)
