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
qtlim6 = 90.0 / scale

scale_cor = 23348.89927 / 2
CLIMmcbxfb = 2.5 / scale_cor
CLIMmcbxfa = 4.5 / scale_cor
CLIMmcbrd = 5.0 / scale_cor
CLIMmcby4 = 2.25 / scale_cor
CLIMmcbc = 2.1 / scale_cor

limitmcbx = 67.0164e-6
limitmcby = 96.3000e-6
limitmcbc = 89.8700e-6


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


def set_var_limits_and_steps_correctors_on_o(collider):
    brho = 23348.89927
    limitMCBXH1 = 2.5 / brho * 0.40
    limitMCBXH2 = 2.5 / brho * 0.15
    limitMCBXH3 = 4.5 / brho * 0.05
    limitMCBY = 2.8 / brho * 0.33
    limitMCBC = 2.1 / brho * 0.33

    step_mcbx = 1e-15
    step_mcby = 1e-12
    step_mcbc = 1e-12

    orbit_correctors_on_o15hv = {
        # MCBX
        "acbxh1.l1": {"step": step_mcbx, "limits": (-limitMCBXH1, limitMCBXH1)},
        "acbxh1.r1": {"step": step_mcbx, "limits": (-limitMCBXH1, limitMCBXH1)},
        "acbxh2.l1": {"step": step_mcbx, "limits": (-limitMCBXH2, limitMCBXH2)},
        "acbxh2.r1": {"step": step_mcbx, "limits": (-limitMCBXH2, limitMCBXH2)},
        "acbxh3.l1": {"step": step_mcbx, "limits": (-limitMCBXH3, limitMCBXH3)},
        "acbxh3.r1": {"step": step_mcbx, "limits": (-limitMCBXH3, limitMCBXH3)},
        "acbxv1.l1": {"step": step_mcbx, "limits": (-limitMCBXH1, limitMCBXH1)},
        "acbxv1.r1": {"step": step_mcbx, "limits": (-limitMCBXH1, limitMCBXH1)},
        "acbxv2.l1": {"step": step_mcbx, "limits": (-limitMCBXH2, limitMCBXH2)},
        "acbxv2.r1": {"step": step_mcbx, "limits": (-limitMCBXH2, limitMCBXH2)},
        "acbxv3.l1": {"step": step_mcbx, "limits": (-limitMCBXH3, limitMCBXH3)},
        "acbxv3.r1": {"step": step_mcbx, "limits": (-limitMCBXH3, limitMCBXH3)},
        "acbxh1.l5": {"step": step_mcbx, "limits": (-limitMCBXH1, limitMCBXH1)},
        "acbxh1.r5": {"step": step_mcbx, "limits": (-limitMCBXH1, limitMCBXH1)},
        "acbxh2.l5": {"step": step_mcbx, "limits": (-limitMCBXH2, limitMCBXH2)},
        "acbxh2.r5": {"step": step_mcbx, "limits": (-limitMCBXH2, limitMCBXH2)},
        "acbxh3.l5": {"step": step_mcbx, "limits": (-limitMCBXH3, limitMCBXH3)},
        "acbxh3.r5": {"step": step_mcbx, "limits": (-limitMCBXH3, limitMCBXH3)},
        "acbxv1.l5": {"step": step_mcbx, "limits": (-limitMCBXH1, limitMCBXH1)},
        "acbxv1.r5": {"step": step_mcbx, "limits": (-limitMCBXH1, limitMCBXH1)},
        "acbxv2.l5": {"step": step_mcbx, "limits": (-limitMCBXH2, limitMCBXH2)},
        "acbxv2.r5": {"step": step_mcbx, "limits": (-limitMCBXH2, limitMCBXH2)},
        "acbxv3.l5": {"step": step_mcbx, "limits": (-limitMCBXH3, limitMCBXH3)},
        "acbxv3.r5": {"step": step_mcbx, "limits": (-limitMCBXH3, limitMCBXH3)},
        # MCBY
        "acbyhs4.l1b1": {"step": step_mcby, "limits": (-limitMCBY, limitMCBY)},
        "acbyhs4.l1b2": {"step": step_mcby, "limits": (-limitMCBY, limitMCBY)},
        "acbyhs4.r1b1": {"step": step_mcby, "limits": (-limitMCBY, limitMCBY)},
        "acbyhs4.r1b2": {"step": step_mcby, "limits": (-limitMCBY, limitMCBY)},
        "acbyvs4.l1b1": {"step": step_mcby, "limits": (-limitMCBY, limitMCBY)},
        "acbyvs4.l1b2": {"step": step_mcby, "limits": (-limitMCBY, limitMCBY)},
        "acbyvs4.r1b1": {"step": step_mcby, "limits": (-limitMCBY, limitMCBY)},
        "acbyvs4.r1b2": {"step": step_mcby, "limits": (-limitMCBY, limitMCBY)},
        "acbyhs4.l5b1": {"step": step_mcby, "limits": (-limitMCBY, limitMCBY)},
        "acbyhs4.l5b2": {"step": step_mcby, "limits": (-limitMCBY, limitMCBY)},
        "acbyhs4.r5b1": {"step": step_mcby, "limits": (-limitMCBY, limitMCBY)},
        "acbyhs4.r5b2": {"step": step_mcby, "limits": (-limitMCBY, limitMCBY)},
        "acbyvs4.l5b1": {"step": step_mcby, "limits": (-limitMCBY, limitMCBY)},
        "acbyvs4.l5b2": {"step": step_mcby, "limits": (-limitMCBY, limitMCBY)},
        "acbyvs4.r5b1": {"step": step_mcby, "limits": (-limitMCBY, limitMCBY)},
        "acbyvs4.r5b2": {"step": step_mcby, "limits": (-limitMCBY, limitMCBY)},
        # MCBC
        "acbch5.l1b2": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbch5.r1b1": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbch6.l1b1": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbch6.r1b2": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbcv5.l1b1": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbcv5.r1b2": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbcv6.l1b2": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbcv6.r1b1": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbch5.l5b2": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbch5.r5b1": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbch6.l5b1": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbch6.r5b2": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbcv5.l5b1": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbcv5.r5b2": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbcv6.l5b2": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbcv6.r5b1": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbch7.l1b2": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbch7.r1b1": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbcv7.l1b1": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbcv7.r1b2": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbch7.l5b2": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbch7.r5b1": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbcv7.l5b1": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
        "acbcv7.r5b2": {"step": step_mcbc, "limits": (-limitMCBC, limitMCBC)},
    }

    collider.vars.vary_default.update(orbit_correctors_on_o15hv)


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


def set_limits_steps_sextupoles_w(collider, step=1e-4):
    sextupoles_defaults = {
        # Beam 1
        "ksf1.a81b1": {"step": step, "limits": (-k2max, k2max)},
        "ksf2.a81b1": {"step": step, "limits": (-k2max, k2max)},
        "ksd1.a81b1": {"step": step, "limits": (-k2max, k2max)},
        "ksd2.a81b1": {"step": step, "limits": (-k2max, k2max)},
        "ksf1.a12b1": {"step": step, "limits": (-k2max, k2max)},
        "ksf2.a12b1": {"step": step, "limits": (-k2max, k2max)},
        "ksd1.a12b1": {"step": step, "limits": (-k2max, k2max)},
        "ksd2.a12b1": {"step": step, "limits": (-k2max, k2max)},
        "ksf1.a45b1": {"step": step, "limits": (-k2max, k2max)},
        "ksf2.a45b1": {"step": step, "limits": (-k2max, k2max)},
        "ksd1.a45b1": {"step": step, "limits": (-k2max, k2max)},
        "ksd2.a45b1": {"step": step, "limits": (-k2max, k2max)},
        "ksf1.a56b1": {"step": step, "limits": (-k2max, k2max)},
        "ksf2.a56b1": {"step": step, "limits": (-k2max, k2max)},
        "ksd1.a56b1": {"step": step, "limits": (-k2max, k2max)},
        "ksd2.a56b1": {"step": step, "limits": (-k2max, k2max)},
        # Beam 2
        "ksf1.a81b2": {"step": step, "limits": (-k2max, k2max)},
        "ksf2.a81b2": {"step": step, "limits": (-k2max, k2max)},
        "ksd1.a81b2": {"step": step, "limits": (-k2max, k2max)},
        "ksd2.a81b2": {"step": step, "limits": (-k2max, k2max)},
        "ksf1.a12b2": {"step": step, "limits": (-k2max, k2max)},
        "ksf2.a12b2": {"step": step, "limits": (-k2max, k2max)},
        "ksd1.a12b2": {"step": step, "limits": (-k2max, k2max)},
        "ksd2.a12b2": {"step": step, "limits": (-k2max, k2max)},
        "ksf1.a45b2": {"step": step, "limits": (-k2max, k2max)},
        "ksf2.a45b2": {"step": step, "limits": (-k2max, k2max)},
        "ksd1.a45b2": {"step": step, "limits": (-k2max, k2max)},
        "ksd2.a45b2": {"step": step, "limits": (-k2max, k2max)},
        "ksf1.a56b2": {"step": step, "limits": (-k2max, k2max)},
        "ksf2.a56b2": {"step": step, "limits": (-k2max, k2max)},
        "ksd1.a56b2": {"step": step, "limits": (-k2max, k2max)},
        "ksd2.a56b2": {"step": step, "limits": (-k2max, k2max)},
    }
    collider.vars.vary_default.update(sextupoles_defaults)


def set_limits_steps_ahvcrab(collider, step=1e-10):
    ahvcrab_default = {
        "ahcrab_l1b1": {"step": step, "limits": None},
        "ahcrab_r1b1": {"step": step, "limits": None},
        "ahcrab_l1b2": {"step": step, "limits": None},
        "ahcrab_r1b2": {"step": step, "limits": None},
        "ahcrab_l5b1": {"step": step, "limits": None},
        "ahcrab_r5b1": {"step": step, "limits": None},
        "ahcrab_l5b2": {"step": step, "limits": None},
        "ahcrab_r5b2": {"step": step, "limits": None},
        "avcrab_l1b1": {"step": step, "limits": None},
        "avcrab_r1b1": {"step": step, "limits": None},
        "avcrab_l1b2": {"step": step, "limits": None},
        "avcrab_r1b2": {"step": step, "limits": None},
        "avcrab_l5b1": {"step": step, "limits": None},
        "avcrab_r5b1": {"step": step, "limits": None},
        "avcrab_l5b2": {"step": step, "limits": None},
        "avcrab_r5b2": {"step": step, "limits": None},
    }
    collider.vars.vary_default.update(ahvcrab_default)


def set_limits_steps_main(collider):
    mqt_defaults = {
        "kqtf.a12b1": {"step": 1e-8, "limits": None},
        "kqtf.a12b2": {"step": 1e-8, "limits": None},
        "kqtd.a12b1": {"step": 1e-8, "limits": None},
        "kqtd.a12b2": {"step": 1e-8, "limits": None},
        "kqtf.a23b1": {"step": 1e-8, "limits": None},
        "kqtf.a23b2": {"step": 1e-8, "limits": None},
        "kqtd.a23b1": {"step": 1e-8, "limits": None},
        "kqtd.a23b2": {"step": 1e-8, "limits": None},
        "kqtf.a34b1": {"step": 1e-8, "limits": None},
        "kqtf.a34b2": {"step": 1e-8, "limits": None},
        "kqtd.a34b1": {"step": 1e-8, "limits": None},
        "kqtd.a34b2": {"step": 1e-8, "limits": None},
        "kqtf.a45b1": {"step": 1e-8, "limits": None},
        "kqtf.a45b2": {"step": 1e-8, "limits": None},
        "kqtd.a45b1": {"step": 1e-8, "limits": None},
        "kqtd.a45b2": {"step": 1e-8, "limits": None},
        "kqtf.a56b1": {"step": 1e-8, "limits": None},
        "kqtf.a56b2": {"step": 1e-8, "limits": None},
        "kqtd.a56b1": {"step": 1e-8, "limits": None},
        "kqtd.a56b2": {"step": 1e-8, "limits": None},
        "kqtf.a67b1": {"step": 1e-8, "limits": None},
        "kqtf.a67b2": {"step": 1e-8, "limits": None},
        "kqtd.a67b1": {"step": 1e-8, "limits": None},
        "kqtd.a67b2": {"step": 1e-8, "limits": None},
        "kqtf.a78b1": {"step": 1e-8, "limits": None},
        "kqtf.a78b2": {"step": 1e-8, "limits": None},
        "kqtd.a78b1": {"step": 1e-8, "limits": None},
        "kqtd.a78b2": {"step": 1e-8, "limits": None},
        "kqtf.a81b1": {"step": 1e-8, "limits": None},
        "kqtf.a81b2": {"step": 1e-8, "limits": None},
        "kqtd.a81b1": {"step": 1e-8, "limits": None},
        "kqtd.a81b2": {"step": 1e-8, "limits": None},
    }
    mq_defaults = {
        "kqf.a12": {"step": 1e-10, "limits": None},
        "kqd.a12": {"step": 1e-10, "limits": None},
        "kqf.a23": {"step": 1e-10, "limits": None},
        "kqd.a23": {"step": 1e-10, "limits": None},
        "kqf.a34": {"step": 1e-10, "limits": None},
        "kqd.a34": {"step": 1e-10, "limits": None},
        "kqf.a45": {"step": 1e-10, "limits": None},
        "kqd.a45": {"step": 1e-10, "limits": None},
        "kqf.a56": {"step": 1e-10, "limits": None},
        "kqd.a56": {"step": 1e-10, "limits": None},
        "kqf.a67": {"step": 1e-10, "limits": None},
        "kqd.a67": {"step": 1e-10, "limits": None},
        "kqf.a78": {"step": 1e-10, "limits": None},
        "kqd.a78": {"step": 1e-10, "limits": None},
        "kqf.a81": {"step": 1e-10, "limits": None},
        "kqd.a81": {"step": 1e-10, "limits": None},
    }

    collider.vars.vary_default.update(mqt_defaults)
    collider.vars.vary_default.update(mq_defaults)


def set_limits_steps_ir2(collider, nrj=7000):
    scmin = 0.03 * 7000.0 / nrj
    ir2_defaults = {
        "kq5.l2b1": {"step": 1.0e-6, "limits": (qtlim2 * scmin, qtlim2)},
        "kq4.l2b1": {"step": 1.0e-6, "limits": (-qtlim2, -qtlim2 * scmin)},
        "kq6.l2b1": {"step": 1.0e-6, "limits": (-qtlim2, -qtlim2 * scmin)},
        "kq7.l2b1": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq8.l2b1": {"step": 1.0e-6, "limits": (-qtlim3, -qtlim3 * scmin * 0.9)},
        "kq9.l2b1": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq10.l2b1": {"step": 1.0e-6, "limits": (-qtlim3, -qtlim3 * scmin)},
        "kqtl11.l2b1": {"step": 1.0e-6, "limits": (-qtlim4, qtlim4)},
        "kqt12.l2b1": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqt13.l2b1": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kq4.r2b1": {"step": 1.0e-6, "limits": (qtlim2 * scmin, qtlim2)},
        "kq5.r2b1": {"step": 1.0e-6, "limits": (-qtlim2, -qtlim2 * scmin)},
        "kq6.r2b1": {"step": 1.0e-6, "limits": (qtlim2 * scmin, qtlim2)},
        "kq7.r2b1": {"step": 1.0e-6, "limits": (-qtlim3, -qtlim3 * scmin)},
        "kq8.r2b1": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq9.r2b1": {"step": 1.0e-6, "limits": (-qtlim3, -qtlim3 * scmin)},
        "kq10.r2b1": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kqtl11.r2b1": {"step": 1.0e-6, "limits": (-qtlim4, qtlim4)},
        "kqt12.r2b1": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqt13.r2b1": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqt13.l2b2": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqt12.l2b2": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqtl11.l2b2": {"step": 1.0e-6, "limits": (-qtlim4, qtlim4)},
        "kq10.l2b2": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq9.l2b2": {"step": 1.0e-6, "limits": (-qtlim3, -qtlim3 * scmin)},
        "kq8.l2b2": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq7.l2b2": {"step": 1.0e-6, "limits": (-qtlim3, -qtlim3 * scmin)},
        "kq6.l2b2": {"step": 1.0e-6, "limits": (qtlim2 * scmin, qtlim2)},
        "kq5.l2b2": {"step": 1.0e-6, "limits": (-qtlim2, -qtlim2 * scmin)},
        "kq4.l2b2": {"step": 1.0e-6, "limits": (qtlim2 * scmin, qtlim2)},
        "kq4.r2b2": {"step": 1.0e-6, "limits": (-qtlim2, -qtlim2 * scmin)},
        "kq5.r2b2": {"step": 1.0e-6, "limits": (qtlim2 * scmin, qtlim2)},
        "kq6.r2b2": {"step": 1.0e-6, "limits": (-qtlim2, -qtlim2 * scmin)},
        "kq7.r2b2": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq8.r2b2": {"step": 1.0e-6, "limits": (-qtlim3, -qtlim3 * scmin)},
        "kq9.r2b2": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq10.r2b2": {"step": 1.0e-6, "limits": (-qtlim3, -qtlim3 * scmin)},
        "kqtl11.r2b2": {"step": 1.0e-6, "limits": (-qtlim4, qtlim4)},
        "kqt12.r2b2": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqt13.r2b2": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
    }
    collider.vars.vary_default.update(ir2_defaults)


def set_limits_steps_ir3(collider, nrj=7000):
    scmin = 0.03 * 7000.0 / nrj
    ir3_defaults = {
        "kqt13.l3b1": {"step": 1.0e-9, "limits": (-qtlim5, qtlim5)},
        "kqt12.l3b1": {"step": 1.0e-9, "limits": (-qtlim5, qtlim5)},
        "kqtl11.l3b1": {
            "step": 1.0e-9,
            "limits": (-qtlim4 * 400.0 / 550.0, qtlim4 * 400.0 / 550.0),
        },
        "kqtl10.l3b1": {"step": 1.0e-9, "limits": (-qtlim4, qtlim4)},
        "kqtl9.l3b1": {"step": 1.0e-9, "limits": (-qtlim4, qtlim4)},
        "kqtl8.l3b1": {
            "step": 1.0e-9,
            "limits": (-qtlim4 * 450.0 / 550.0, qtlim4 * 450.0 / 550.0),
        },
        "kqtl7.l3b1": {"step": 1.0e-9, "limits": (-qtlim4, qtlim4)},
        "kq6.l3b1": {"step": 1.0e-9, "limits": (-qtlim6, qtlim6)},
        "kq6.r3b1": {"step": 1.0e-9, "limits": (-qtlim6, qtlim6)},
        "kqtl7.r3b1": {"step": 1.0e-9, "limits": (-qtlim4, qtlim4)},
        "kqtl8.r3b1": {"step": 1.0e-9, "limits": (-qtlim4, qtlim4)},
        "kqtl9.r3b1": {
            "step": 1.0e-9,
            "limits": (-qtlim4 * 500.0 / 550.0, qtlim4 * 500.0 / 550.0),
        },
        "kqtl10.r3b1": {
            "step": 1.0e-9,
            "limits": (-qtlim4 * 450.0 / 550.0, qtlim4 * 450.0 / 550.0),
        },
        "kqtl11.r3b1": {
            "step": 1.0e-9,
            "limits": (-qtlim4 * 520.0 / 550.0, qtlim4 * 520.0 / 550.0),
        },
        "kqt12.r3b1": {"step": 1.0e-9, "limits": (-qtlim5, qtlim5)},
        "kqt13.r3b1": {"step": 1.0e-9, "limits": (-qtlim5, qtlim5)},
        "kqt13.l3b2": {"step": 1.0e-9, "limits": (-qtlim5, qtlim5)},
        "kqt12.l3b2": {"step": 1.0e-9, "limits": (-qtlim5, qtlim5)},
        "kqtl11.l3b2": {
            "step": 1.0e-9,
            "limits": (-qtlim4 * 400.0 / 550.0, qtlim4 * 400.0 / 550.0),
        },
        "kqtl10.l3b2": {"step": 1.0e-9, "limits": (-qtlim4, qtlim4)},
        "kqtl9.l3b2": {"step": 1.0e-9, "limits": (-qtlim4, qtlim4)},
        "kqtl8.l3b2": {
            "step": 1.0e-9,
            "limits": (-qtlim4 * 450.0 / 550.0, qtlim4 * 450.0 / 550.0),
        },
        "kqtl7.l3b2": {"step": 1.0e-9, "limits": (-qtlim4, qtlim4)},
        "kq6.l3b2": {"step": 1.0e-9, "limits": (-qtlim6, qtlim6)},
        "kq6.r3b2": {"step": 1.0e-9, "limits": (-qtlim6, qtlim6)},
        "kqtl7.r3b2": {"step": 1.0e-9, "limits": (-qtlim4, qtlim4)},
        "kqtl8.r3b2": {"step": 1.0e-9, "limits": (-qtlim4, qtlim4)},
        "kqtl9.r3b2": {
            "step": 1.0e-9,
            "limits": (-qtlim4 * 500.0 / 550.0, qtlim4 * 500.0 / 550.0),
        },
        "kqtl10.r3b2": {
            "step": 1.0e-9,
            "limits": (-qtlim4 * 450.0 / 550.0, qtlim4 * 450.0 / 550.0),
        },
        "kqtl11.r3b2": {
            "step": 1.0e-9,
            "limits": (-qtlim4 * 520.0 / 550.0, qtlim4 * 520.0 / 550.0),
        },
        "kqt12.r3b2": {"step": 1.0e-9, "limits": (-qtlim5, qtlim5)},
        "kqt13.r3b2": {"step": 1.0e-9, "limits": (-qtlim5, qtlim5)},
    }
    collider.vars.vary_default.update(ir3_defaults)


def set_limits_steps_ir4(collider, nrj=7000):
    scmin = 0.03 * 7000.0 / nrj
    ir4_defaults = {
        "kqt13.l4b1": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqt12.l4b1": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqtl11.l4b1": {"step": 1.0e-6, "limits": (-qtlim4, qtlim4)},
        "kq10.l4b1": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kq9.l4b1": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq8.l4b1": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kq7.l4b1": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq6.l4b1": {"step": 1.0e-6, "limits": (-qtlim2, qtlim2 * scmin)},
        "kq5.l4b1": {"step": 1.0e-6, "limits": (qtlim2 * scmin, qtlim2)},
        "kq5.r4b1": {"step": 1.0e-6, "limits": (-qtlim2, qtlim2 * scmin)},
        "kq6.r4b1": {"step": 1.0e-6, "limits": (qtlim2 * scmin, qtlim2)},
        "kq7.r4b1": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kq8.r4b1": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq9.r4b1": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kq10.r4b1": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kqtl11.r4b1": {"step": 1.0e-6, "limits": (-qtlim4, qtlim4)},
        "kqt12.r4b1": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqt13.r4b1": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqt13.l4b2": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqt12.l4b2": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqtl11.l4b2": {"step": 1.0e-6, "limits": (-qtlim4, qtlim4)},
        "kq10.l4b2": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq9.l4b2": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kq8.l4b2": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq7.l4b2": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kq6.l4b2": {"step": 1.0e-6, "limits": (qtlim2 * scmin, qtlim2)},
        "kq5.l4b2": {"step": 1.0e-6, "limits": (-qtlim2, qtlim2 * scmin)},
        "kq5.r4b2": {"step": 1.0e-6, "limits": (qtlim2 * scmin, qtlim2)},
        "kq6.r4b2": {"step": 1.0e-6, "limits": (-qtlim2, qtlim2 * scmin)},
        "kq7.r4b2": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq8.r4b2": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kq9.r4b2": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq10.r4b2": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kqtl11.r4b2": {"step": 1.0e-6, "limits": (-qtlim4, qtlim4)},
        "kqt12.r4b2": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqt13.r4b2": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
    }
    collider.vars.vary_default.update(ir4_defaults)


def set_limits_steps_ir6(collider, nrj=7000):
    scmin = 0.03 * 7000.0 / nrj
    ir6_defaults = {
        "kqt13.l6b1": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqt12.l6b1": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqtl11.l6b1": {
            "step": 1.0e-6,
            "limits": (-qtlim4 * 400.0 / 550.0, qtlim4 * 400.0 / 550.0),
        },
        "kq10.l6b1": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kq9.l6b1": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq8.l6b1": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kq5.l6b1": {"step": 1.0e-6, "limits": (qtlim2 * scmin, qtlim2)},
        "kq4.l6b1": {"step": 1.0e-6, "limits": (-qtlim2, qtlim2 * scmin)},
        "kq4.r6b1": {"step": 1.0e-6, "limits": (qtlim2 * scmin, qtlim2)},
        "kq5.r6b1": {"step": 1.0e-6, "limits": (-qtlim2, qtlim2 * scmin)},
        "kq8.r6b1": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq9.r6b1": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kq10.r6b1": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kqtl11.r6b1": {
            "step": 1.0e-6,
            "limits": (-qtlim4 * 300.0 / 550.0, qtlim4 * 300.0 / 550.0),
        },
        "kqt12.r6b1": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqt13.r6b1": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqt13.l6b2": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqt12.l6b2": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqtl11.l6b2": {
            "step": 1.0e-6,
            "limits": (-qtlim4 * 400.0 / 550.0, qtlim4 * 400.0 / 550.0),
        },
        "kq10.l6b2": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq9.l6b2": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kq8.l6b2": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq5.l6b2": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kq4.l6b2": {"step": 1.0e-6, "limits": (qtlim2 * scmin, qtlim2)},
        "kq4.r6b2": {"step": 1.0e-6, "limits": (-qtlim2, qtlim2 * scmin)},
        "kq5.r6b2": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq8.r6b2": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kq9.r6b2": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq10.r6b2": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kqtl11.r6b2": {
            "step": 1.0e-6,
            "limits": (-qtlim4 * 300.0 / 550.0, qtlim4 * 300.0 / 550.0),
        },
        "kqt12.r6b2": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqt13.r6b2": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
    }
    collider.vars.vary_default.update(ir6_defaults)


def set_limits_steps_ir7(collider, nrj=7000):
    scmin = 0.03 * 7000.0 / nrj
    ir7_defaults = {
        "kqt13.l7b1": {"step": 1.0e-9, "limits": (-qtlim5, qtlim5)},
        "kqt12.l7b1": {"step": 1.0e-9, "limits": (-qtlim5, qtlim5)},
        "kqtl11.l7b1": {
            "step": 1.0e-9,
            "limits": (-qtlim4 * 300.0 / 550.0, qtlim4 * 300.0 / 550.0),
        },
        "kqtl10.l7b1": {
            "step": 1.0e-9,
            "limits": (-qtlim4 * 500.0 / 550.0, qtlim4 * 500.0 / 550.0),
        },
        "kqtl9.l7b1": {
            "step": 1.0e-9,
            "limits": (-qtlim4 * 400.0 / 550.0, qtlim4 * 400.0 / 550.0),
        },
        "kqtl8.l7b1": {
            "step": 1.0e-9,
            "limits": (-qtlim4 * 300.0 / 550.0, qtlim4 * 300.0 / 550.0),
        },
        "kqtl7.l7b1": {"step": 1.0e-9, "limits": (-qtlim4, qtlim4)},
        "kq6.l7b1": {"step": 1.0e-9, "limits": (-qtlim6, qtlim6)},
        "kq6.r7b1": {"step": 1.0e-9, "limits": (-qtlim6, qtlim6)},
        "kqtl7.r7b1": {"step": 1.0e-9, "limits": (-qtlim4, qtlim4)},
        "kqtl8.r7b1": {
            "step": 1.0e-9,
            "limits": (-qtlim4 * 550.0 / 550.0, qtlim4 * 550.0 / 550.0),
        },
        "kqtl9.r7b1": {
            "step": 1.0e-9,
            "limits": (-qtlim4 * 500.0 / 550.0, qtlim4 * 500.0 / 550.0),
        },
        "kqtl10.r7b1": {"step": 1.0e-9, "limits": (-qtlim4, qtlim4)},
        "kqtl11.r7b1": {"step": 1.0e-9, "limits": (-qtlim4, qtlim4)},
        "kqt12.r7b1": {"step": 1.0e-9, "limits": (-qtlim5, qtlim5)},
        "kqt13.r7b1": {"step": 1.0e-9, "limits": (-qtlim5, qtlim5)},
        "kqt13.l7b2": {"step": 1.0e-9, "limits": (-qtlim5, qtlim5)},
        "kqt12.l7b2": {"step": 1.0e-9, "limits": (-qtlim5, qtlim5)},
        "kqtl11.l7b2": {
            "step": 1.0e-9,
            "limits": (-qtlim4 * 300.0 / 550.0, qtlim4 * 300.0 / 550.0),
        },
        "kqtl10.l7b2": {
            "step": 1.0e-9,
            "limits": (-qtlim4 * 500.0 / 550.0, qtlim4 * 500.0 / 550.0),
        },
        "kqtl9.l7b2": {
            "step": 1.0e-9,
            "limits": (-qtlim4 * 400.0 / 550.0, qtlim4 * 400.0 / 550.0),
        },
        "kqtl8.l7b2": {
            "step": 1.0e-9,
            "limits": (-qtlim4 * 300.0 / 550.0, qtlim4 * 300.0 / 550.0),
        },
        "kqtl7.l7b2": {"step": 1.0e-9, "limits": (-qtlim4, qtlim4)},
        "kq6.l7b2": {"step": 1.0e-9, "limits": (-qtlim6, qtlim6)},
        "kq6.r7b2": {"step": 1.0e-9, "limits": (-qtlim6, qtlim6)},
        "kqtl7.r7b2": {"step": 1.0e-9, "limits": (-qtlim4, qtlim4)},
        "kqtl8.r7b2": {
            "step": 1.0e-9,
            "limits": (-qtlim4 * 550.0 / 550.0, qtlim4 * 550.0 / 550.0),
        },
        "kqtl9.r7b2": {
            "step": 1.0e-9,
            "limits": (-qtlim4 * 500.0 / 550.0, qtlim4 * 500.0 / 550.0),
        },
        "kqtl10.r7b2": {"step": 1.0e-9, "limits": (-qtlim4, qtlim4)},
        "kqtl11.r7b2": {"step": 1.0e-9, "limits": (-qtlim4, qtlim4)},
        "kqt12.r7b2": {"step": 1.0e-9, "limits": (-qtlim5, qtlim5)},
        "kqt13.r7b2": {"step": 1.0e-9, "limits": (-qtlim5, qtlim5)},
    }
    collider.vars.vary_default.update(ir7_defaults)


def set_limits_steps_ir8(collider, nrj=7000):
    scmin = 0.03 * 7000.0 / nrj
    ir8_defaults = {
        "kq4.r8b1": {"step": 1.0e-6, "limits": (qtlim2 * scmin, qtlim2)},
        "kq5.r8b1": {"step": 1.0e-6, "limits": (-qtlim2, qtlim2 * scmin)},
        "kq6.r8b1": {"step": 1.0e-6, "limits": (qtlim2 * scmin, qtlim2)},
        "kq7.r8b1": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kq8.r8b1": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq9.r8b1": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kq10.r8b1": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kqtl11.r8b1": {"step": 1.0e-6, "limits": (-qtlim4, qtlim4)},
        "kqt12.r8b1": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqt13.r8b1": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kq4.l8b1": {"step": 1.0e-6, "limits": (-qtlim2, qtlim2 * scmin)},
        "kq5.l8b1": {"step": 1.0e-6, "limits": (qtlim2 * scmin, qtlim2)},
        "kq6.l8b1": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kq7.l8b1": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq8.l8b1": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kq9.l8b1": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq10.l8b1": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kqtl11.l8b1": {"step": 1.0e-6, "limits": (-qtlim4, qtlim4)},
        "kqt12.l8b1": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqt13.l8b1": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kq4.r8b2": {"step": 1.0e-6, "limits": (-qtlim2, qtlim2 * scmin)},
        "kq5.r8b2": {"step": 1.0e-6, "limits": (qtlim2 * scmin, qtlim2)},
        "kq6.r8b2": {"step": 1.0e-6, "limits": (-qtlim2, qtlim2 * scmin)},
        "kq7.r8b2": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq8.r8b2": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kq9.r8b2": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq10.r8b2": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kqtl11.r8b2": {"step": 1.0e-6, "limits": (-qtlim4, qtlim4)},
        "kqt12.r8b2": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqt13.r8b2": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kq5.l8b2": {"step": 1.0e-6, "limits": (-qtlim2, qtlim2 * scmin)},
        "kq4.l8b2": {"step": 1.0e-6, "limits": (qtlim2 * scmin, qtlim2)},
        "kq6.l8b2": {"step": 1.0e-6, "limits": (qtlim2 * scmin, qtlim2)},
        "kq7.l8b2": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kq8.l8b2": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kq9.l8b2": {"step": 1.0e-6, "limits": (-qtlim3, qtlim3 * scmin)},
        "kq10.l8b2": {"step": 1.0e-6, "limits": (qtlim3 * scmin, qtlim3)},
        "kqtl11.l8b2": {"step": 1.0e-6, "limits": (-qtlim4, qtlim4)},
        "kqt12.l8b2": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
        "kqt13.l8b2": {"step": 1.0e-6, "limits": (-qtlim5, qtlim5)},
    }
    collider.vars.vary_default.update(ir8_defaults)


def set_limits_steps_ir2_orbit(collider):
    # Single beam correctors at IR2 (Q4 and Q5, H and V)
    collider.vars.vary_default.update(
        {
            "acbyvs4.l2b1": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbyvs4.r2b2": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbyvs4.l2b2": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbyvs4.r2b1": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbyvs5.l2b2": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbyvs5.l2b1": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbcvs5.r2b1": {"step": 1.0e-15, "limits": (-limitmcbc, limitmcbc)},
            "acbcvs5.r2b2": {"step": 1.0e-15, "limits": (-limitmcbc, limitmcbc)},
            "acbyhs4.l8b1": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbyhs4.r8b2": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbyhs4.l8b2": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbyhs4.r8b1": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbchs5.l8b2": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbchs5.l8b1": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbyhs5.r8b1": {"step": 1.0e-15, "limits": (-limitmcbc, limitmcbc)},
            "acbyhs5.r8b2": {"step": 1.0e-15, "limits": (-limitmcbc, limitmcbc)},
        }
    )


def set_limits_steps_ir8_orbit(collider):
    # Correctors in IR8 (Q4 and Q5, and triplet)
    collider.vars.vary_default.update(
        {
            "acbyhs4.l8b1": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbyhs4.r8b2": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbyhs4.l8b2": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbyhs4.r8b1": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbchs5.l8b2": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbchs5.l8b1": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbyhs5.r8b1": {"step": 1.0e-15, "limits": (-limitmcbc, limitmcbc)},
            "acbyhs5.r8b2": {"step": 1.0e-15, "limits": (-limitmcbc, limitmcbc)},
            "acbxh1.l8": {"step": 1.0e-15, "limits": (-limitmcbx, limitmcbx)},
            "acbxh2.l8": {"step": 1.0e-15, "limits": (-limitmcbx, limitmcbx)},
            "acbxh3.l8": {"step": 1.0e-15, "limits": (-limitmcbx, limitmcbx)},
            "acbxh1.r8": {"step": 1.0e-15, "limits": (-limitmcbx, limitmcbx)},
            "acbxh2.r8": {"step": 1.0e-15, "limits": (-limitmcbx, limitmcbx)},
            "acbxh3.r8": {"step": 1.0e-15, "limits": (-limitmcbx, limitmcbx)},
            "acbyvs4.l8b1": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbcvs5.l8b1": {"step": 1.0e-15, "limits": (-limitmcbc, limitmcbc)},
            "acbyvs4.r8b1": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbyvs5.r8b1": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbyvs4.l8b2": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbcvs5.l8b2": {"step": 1.0e-15, "limits": (-limitmcbc, limitmcbc)},
            "acbyvs4.r8b2": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbyvs5.r8b2": {"step": 1.0e-15, "limits": (-limitmcby, limitmcby)},
            "acbxv1.l8": {"step": 1.0e-15, "limits": (-limitmcbx, limitmcbx)},
            "acbxv2.l8": {"step": 1.0e-15, "limits": (-limitmcbx, limitmcbx)},
            "acbxv3.l8": {"step": 1.0e-15, "limits": (-limitmcbx, limitmcbx)},
            "acbxv1.r8": {"step": 1.0e-15, "limits": (-limitmcbx, limitmcbx)},
            "acbxv2.r8": {"step": 1.0e-15, "limits": (-limitmcbx, limitmcbx)},
            "acbxv3.r8": {"step": 1.0e-15, "limits": (-limitmcbx, limitmcbx)},
        }
    )


def set_limits_steps_ir234678(collider, nrj=7000):
    set_limits_steps_ir2(collider, nrj)
    set_limits_steps_ir3(collider, nrj)
    set_limits_steps_ir4(collider, nrj)
    set_limits_steps_ir6(collider, nrj)
    set_limits_steps_ir7(collider, nrj)
    set_limits_steps_ir8(collider, nrj)

    set_limits_steps_ir2_orbit(collider)
    set_limits_steps_ir8_orbit(collider)
