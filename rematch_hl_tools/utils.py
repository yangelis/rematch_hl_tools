import numpy as np
import matplotlib.pyplot as plt

configs = {
    "on_0": {
        "cd2q4": 0,
        "on_disp": 0,
        "on_x1": 0,
        "on_x5": 0,
        "on_sep1": 0,
        "on_sep5": 0,
        "phi_ir1": 0,
        "phi_ir5": 90,
        "on_a1": 0,
        "on_a5": 0,
    },
    "on_x1hs": {
        "cd2q4": 0,
        "on_x1": 250,
        "on_x5": 0,
        "on_sep1": 0,
        "phi_ir1": 0,
        "phi_ir5": 90,
    },
    "on_x1hl": {
        "cd2q4": 1,
        "on_x1": 250,
        "on_x5": 0,
        "on_sep1": 0,
        "phi_ir1": 0,
        "phi_ir5": 90,
    },
    "on_x1vs": {
        "cd2q4": 0,
        "on_x1": 250,
        "on_x5": 0,
        "on_sep1": 0,
        "phi_ir1": 90,
        "phi_ir5": 0,
    },
    "on_x1vl": {
        "cd2q4": 1,
        "on_x1": 250,
        "on_x5": 0,
        "on_sep1": 0,
        "phi_ir1": 90,
        "phi_ir5": 0,
    },
    "on_x5hs": {
        "cd2q4": 0,
        "on_x1": 0,
        "on_x5": 250,
        "on_sep1": 0,
        "phi_ir1": 90,
        "phi_ir5": 0,
    },
    "on_x5hl": {
        "cd2q4": 1,
        "on_x1": 0,
        "on_x5": 250,
        "on_sep1": 0,
        "phi_ir1": 90,
        "phi_ir5": 0,
    },
    "on_x5vs": {
        "cd2q4": 0,
        "on_x1": 0,
        "on_x5": 250,
        "on_sep1": 0,
        "phi_ir1": 0,
        "phi_ir5": 90,
    },
    "on_x5vl": {
        "cd2q4": 1,
        "on_x1": 0,
        "on_x5": 250,
        "on_sep1": 0,
        "phi_ir1": 0,
        "phi_ir5": 90,
    },
    "on_x15hvs": {
        "cd2q4": 0,
        "on_x1": 250,
        "on_x5": 250,
        "on_sep1": 0,
        "phi_ir1": 0,
        "phi_ir5": 90,
    },
    "on_x15hvl": {
        "cd2q4": 1,
        "on_x1": 250,
        "on_x5": 250,
        "on_sep1": 0,
        "phi_ir1": 0,
        "phi_ir5": 90,
    },
    "on_sep1v": {"on_sep1": 2, "phi_ir1": 0},
    "on_sep5h": {"on_sep5": 2, "phi_ir5": 90},
    "on_sep1h": {"on_sep1": 2, "phi_ir1": 90},
    "on_sep5v": {"on_sep5": 2, "phi_ir5": 0},
    "on_a1v": {"on_a1": 1},
    "on_a1h": {"on_a1": 1, "phi_ir1": 90},
    "on_a5h": {"on_a5": 1},
    "on_a5v": {"on_a5": 1, "phi_ir5": 0},
}


def set_vars(collider, config):
    print(config)
    for key, val in config.items():
        collider.varval[key] = val


def check_ip(collider, beam="b1"):
    tw = collider[f"lhc{beam}"].twiss()

    res = {}

    res["betx_ip1"] = tw["betx", "ip1"]
    res["bety_ip1"] = tw["bety", "ip1"]
    res["betx_ip5"] = tw["betx", "ip5"]
    res["bety_ip5"] = tw["bety", "ip5"]
    res["betx_ip2"] = tw["betx", "ip2"]
    res["bety_ip2"] = tw["bety", "ip2"]
    res["betx_ip8"] = tw["betx", "ip8"]
    res["bety_ip8"] = tw["bety", "ip8"]

    res["qx"] = tw.qx
    res["qy"] = tw.qy
    res["dqx"] = tw.dqx
    res["dqy"] = tw.dqy

    return res


def connect_octupoles(collider, energy=7000):
    from scipy.constants import c as clight
    collider.vars["brho"] = energy * 1e9 / clight
    # NOTE: Test B1 for now
    v = collider.vars
    v["i_oct_b1"] = 0
    v["kof.a12b1"] = v["kmax_mo"] * v["i_oct_b1"] / v["imax_mo"] / v["brho"]
    v["kof.a23b1"] = v["kmax_mo"] * v["i_oct_b1"] / v["imax_mo"] / v["brho"]
    v["kof.a34b1"] = v["kmax_mo"] * v["i_oct_b1"] / v["imax_mo"] / v["brho"]
    v["kof.a45b1"] = v["kmax_mo"] * v["i_oct_b1"] / v["imax_mo"] / v["brho"]
    v["kof.a56b1"] = v["kmax_mo"] * v["i_oct_b1"] / v["imax_mo"] / v["brho"]
    v["kof.a67b1"] = v["kmax_mo"] * v["i_oct_b1"] / v["imax_mo"] / v["brho"]
    v["kof.a78b1"] = v["kmax_mo"] * v["i_oct_b1"] / v["imax_mo"] / v["brho"]
    v["kof.a81b1"] = v["kmax_mo"] * v["i_oct_b1"] / v["imax_mo"] / v["brho"]
    v["kod.a12b1"] = v["kmax_mo"] * v["i_oct_b1"] / v["imax_mo"] / v["brho"]
    v["kod.a23b1"] = v["kmax_mo"] * v["i_oct_b1"] / v["imax_mo"] / v["brho"]
    v["kod.a34b1"] = v["kmax_mo"] * v["i_oct_b1"] / v["imax_mo"] / v["brho"]
    v["kod.a45b1"] = v["kmax_mo"] * v["i_oct_b1"] / v["imax_mo"] / v["brho"]
    v["kod.a56b1"] = v["kmax_mo"] * v["i_oct_b1"] / v["imax_mo"] / v["brho"]
    v["kod.a67b1"] = v["kmax_mo"] * v["i_oct_b1"] / v["imax_mo"] / v["brho"]
    v["kod.a78b1"] = v["kmax_mo"] * v["i_oct_b1"] / v["imax_mo"] / v["brho"]
    v["kod.a81b1"] = v["kmax_mo"] * v["i_oct_b1"] / v["imax_mo"] / v["brho"]


def crit_phases(collider, cycle=False):
    if cycle:
        collider.lhcb1.cycle("e.ds.l3.b1", inplace=True)
        collider.lhcb2.cycle("e.ds.l3.b2", inplace=True)

    t1 = collider.lhcb1.twiss()
    t2 = collider.lhcb2.twiss()

    if cycle:
        collider.lhcb1.cycle('lhcb1$start', inplace=True)
        collider.lhcb2.cycle('lhcb2$end', inplace=True)

    mux_tcphb1 = t1["mux", "tcp.b6l7.b1"]
    muy_tcpvb1 = t1["muy", "tcp.d6l7.b1"]
    mux_tct5b1 = t1["mux", "tctpxh.4l5.b1"]
    muy_tct5b1 = t1["muy", "tctpxv.4l5.b1"]
    mux_tct1b1 = t1["mux", "tctpxh.4l1.b1"]
    muy_tct1b1 = t1["muy", "tctpxv.4l1.b1"]
    mux_tct8b1 = t1["mux", "tctph.4l8.b1"]
    muy_tct8b1 = t1["muy", "tctpv.4l8.b1"]
    mux_mkdob1 = t1["mux", "mkd.o5l6.b1"]
    mux_mkdab1 = t1["mux", "mkd.a5l6.b1"]
    mux_cchl1b1 = t1["mux", "acfca.4al1.b1"]
    mux_cchr1b1 = t1["mux", "acfca.4ar1.b1"]
    muy_ccvl5b1 = t1["muy", "acfca.4al5.b1"]
    muy_ccvr5b1 = t1["muy", "acfca.4ar5.b1"]

    mux_tcphb2 = t2["mux", "tcp.b6r7.b2"]
    muy_tcpvb2 = t2["muy", "tcp.d6r7.b2"]
    mux_tct5b2 = t2["mux", "tctpxh.4r5.b2"]
    muy_tct5b2 = t2["muy", "tctpxv.4r5.b2"]
    mux_tct1b2 = t2["mux", "tctpxh.4r1.b2"]
    muy_tct1b2 = t2["muy", "tctpxv.4r1.b2"]
    mux_tct8b2 = t2["mux", "tctph.4r8.b2"]
    muy_tct8b2 = t2["muy", "tctpv.4r8.b2"]
    mux_mkdob2 = t2["mux", "mkd.o5r6.b2"]
    mux_mkdab2 = t2["mux", "mkd.a5r6.b2"]
    mux_cchl1b2 = t2["mux", "acfca.4al1.b2"]
    mux_cchr1b2 = t2["mux", "acfca.4ar1.b2"]
    muy_ccvl5b2 = t2["muy", "acfca.4al5.b2"]
    muy_ccvr5b2 = t2["muy", "acfca.4ar5.b2"]

    # NOTE: calulate them
    qx = 62.31
    qy = 60.32
    
    cc_tcp = {
        "CC1H": {
            "B1 Left": mux_tcphb1 + qx - mux_cchl1b1,
            "B1 Right": mux_tcphb1 - mux_cchr1b1,
            "B2 Left": -mux_tcphb2 + mux_cchl1b2,
            "B2 Right": -mux_tcphb2 + mux_cchr1b2 + qx,
        },
        "CC5V": {
            "B1 Left": muy_tcpvb1 - muy_ccvl5b1,
            "B1 Right": muy_tcpvb1 - muy_ccvr5b1,
            "B2 Left": -muy_tcpvb2 + muy_ccvl5b2 + qy,
            "B2 Right": -muy_tcpvb2 + muy_ccvr5b2 + qy,
        },
    }
    mkd_tct = {
        "TCTH1": {
            "B1 MKD.A": mux_tct1b1 - mux_mkdab1,
            "B1 MKD.0": mux_tct1b1 - mux_mkdob1,
            "B2 MKD.A": -mux_tct1b2 + mux_mkdab2,
            "B2 MKD.0": -mux_tct1b2 + mux_mkdob2,
        },
        "TCTH5": {
            "B1 MKD.A": mux_tct5b1 - mux_mkdab1 + qx,
            "B1 MKD.0": mux_tct5b1 - mux_mkdob1 + qx,
            "B2 MKD.A": -mux_tct5b2 + mux_mkdab2,
            "B2 MKD.0": -mux_tct5b2 + mux_mkdob2,
        },
        "TCTH8": {
            "B1 MKD.A": mux_tct8b1 - mux_mkdab1,
            "B1 MKD.0": mux_tct8b1 - mux_mkdob1,
            "B2 MKD.A": -mux_tct8b2 + mux_mkdab2 + qx,
            "B2 MKD.0": -mux_tct8b2 + mux_mkdob2 + qx,
        },
    }

    tcp_tct = {
        "TCT1": {
            "B1 H": mux_tct1b1 - mux_tcphb1,
            "B1 V": muy_tct1b1 - muy_tcpvb1,
            "B2 H": -mux_tct1b2 + mux_tcphb2,
            "B2 V": -muy_tct1b2 + muy_tcpvb2,
        },
        "TCT5": {
            "B1 H": mux_tct5b1 - mux_tcphb1 + qx,
            "B1 V": muy_tct5b1 - muy_tcpvb1 + qy,
            "B2 H": -mux_tct5b2 + mux_tcphb2,
            "B2 V": -muy_tct5b2 + muy_tcpvb2,
        },
        "TCT8": {
            "B1 H": mux_tct8b1 - mux_tcphb1,
            "B1 V": muy_tct8b1 - muy_tcpvb1,
            "B2 H": -mux_tct8b2 + mux_tcphb2 + qx,
            "B2 V": -muy_tct8b2 + muy_tcpvb2 + qy,
        },
    }

    for d in [cc_tcp, mkd_tct, tcp_tct]:
        for k, v in d.items():
            for kk, vv in v.items():
                d[k][kk] = 360 * ( (vv * 2 - round(vv * 2)) / 2)

    return (cc_tcp, mkd_tct, tcp_tct)


def plot_dmu(tw1, tw2):
    # fig, axs = plt.subplots(2, 1, figsize=(14, 10.3), dpi=300, sharex=True)
    fig, axs = plt.subplots(2, 1, sharex=True)

    for i, bim in enumerate(["lhcb1", "lhcb2"]):
        dmux = ((tw2[bim].mux % 1) - (tw1[bim].mux % 1)) % 1
        dmux = np.where(dmux > 0.5, dmux - 1, dmux)
        dmuy = ((tw2[bim].muy % 1) - (tw1[bim].muy % 1)) % 1
        dmuy = np.where(dmuy > 0.5, dmuy - 1, dmuy)

        axs[i].plot(tw2[bim].s, dmux, label=r"$\Delta \mu_{x}$")
        axs[i].plot(tw2[bim].s, dmuy, label=r"$\Delta \mu_{y}$")


    for i in range(2):
        axs_t = axs[i].twiny()
        axs_t.set_xticks(tw1[f"lhcb{i+1}"].rows["ip.*"].s, tw1[f"lhcb{i+1}"].rows["ip.*"].name)
        axs_t.set_xlim(axs[i].get_xlim()[0], axs[i].get_xlim()[1])
        axs[i].grid()
        axs[i].legend()
        axs[i].set_xlabel("s [m]")
        axs[i].set_ylabel(r"$\Delta \mu_{x,y}$")

    plt.show()
