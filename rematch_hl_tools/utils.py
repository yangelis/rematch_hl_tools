import numpy as np
import matplotlib.pyplot as plt


ARC_NAMES = ["12", "23", "34", "45", "56", "67", "78", "81"]

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
    "on_nom": {
        "on_x1": 250,
        "on_sep1": 0,
        "on_x2": -170,
        "on_sep2": 0.138,
        "on_x5": 250,
        "on_sep5": 0,
        "on_x8h": 0.0,
        "on_x8v": 170,
        "on_sep8h": -0.01,
        "on_sep8v": 0.01,
        "on_a1": 0,
        "on_o1": 0,
        "on_a2": 0,
        "on_o2": 0,
        "on_a5": 0,
        "on_o5": 0,
        "on_a8": 0,
        "on_o8": 0,
        "on_disp": 1,
    },
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
        collider.lhcb1.cycle("lhcb1$start", inplace=True)
        collider.lhcb2.cycle("lhcb2$end", inplace=True)

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
    mux_cchl1b1 = t1["mux", "acfcah.a4l1.b1"]
    mux_cchr1b1 = t1["mux", "acfcah.a4r1.b1"]
    muy_ccvl5b1 = t1["muy", "acfcav.a4l5.b1"]
    muy_ccvr5b1 = t1["muy", "acfcav.a4r5.b1"]

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
    mux_cchl1b2 = t2["mux", "acfcah.a4l1.b2"]
    mux_cchr1b2 = t2["mux", "acfcah.a4r1.b2"]
    muy_ccvl5b2 = t2["muy", "acfcav.a4l5.b2"]
    muy_ccvr5b2 = t2["muy", "acfcav.a4r5.b2"]

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
                d[k][kk] = 360 * ((vv * 2 - round(vv * 2)) / 2)

    return (cc_tcp, mkd_tct, tcp_tct)


def plot_dmu(tw1, tw2, fig=None, axs=None):
    # fig, axs = plt.subplots(2, 1, figsize=(14, 10.3), dpi=300, sharex=True)
    if fig is None:
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
        axs_t.set_xticks(
            tw1[f"lhcb{i + 1}"].rows["ip.*"].s, tw1[f"lhcb{i + 1}"].rows["ip.*"].name
        )
        axs_t.set_xlim(axs[i].get_xlim()[0], axs[i].get_xlim()[1])
        axs[i].grid()
        axs[i].legend()
        axs[i].set_xlabel("s [m]")
        axs[i].set_ylabel(r"$\Delta \mu_{x,y}$")


import pandas as pd


def phases_table(env, table=None):
    if table is None:
        table = crit_phases(env)
    print(pd.DataFrame(table[0]).transpose().to_markdown())
    print(pd.DataFrame(table[1]).transpose().to_markdown())
    print(pd.DataFrame(table[2]).transpose().to_markdown())
    print("\n\n\n")


from scipy.interpolate import interp1d


def get_strengths_triplet(collider, ip):
    kqs = {}
    names = "kqx.lip ktqx1.lip ktqx2.lip kqx.rip ktqx1.rip ktqx2.rip"

    for n in names.split():
        tn = n.replace("ip", str(ip))
        kqs[tn] = collider.varval[tn]
    return kqs


def get_strengths_triplethl(collider, ip):
    kqs = {}
    names = (
        "kqx1.lip kqx2a.lip kqx2b.lip kqx3.lip kqx1.rip kqx2a.rip kqx2b.rip kqx3.rip"
    )
    for n in names.split():
        tn = n.replace("ip", str(ip))
        kqs[tn] = collider.varval[tn]
    return kqs


def get_strengths_quad(collider, qtype, nquad, ip):
    kqs = {}
    names = "kQN.lipb1 kQN.ripb1 kQN.lipb2 kQN.ripb2"
    for n in names.split():
        tn = n.replace("Q", qtype).replace("N", str(nquad)).replace("ip", str(ip))
        kqs[tn] = collider.varval[tn]
    return kqs


def get_strengths_ms(collider, ip):
    kq4 = get_strengths_quad(collider, "q", 4, ip)
    kq5 = get_strengths_quad(collider, "q", 5, ip)
    kq6 = get_strengths_quad(collider, "q", 6, ip)
    return kq4 | kq5 | kq6


def get_strengths_ds(collider, ip):
    kqs = {}
    if ip != 6:
        kq7 = get_strengths_quad(collider, "q", 7, ip)
        kqs = kqs | kq7

    kq8 = get_strengths_quad(collider, "q", 8, ip)
    kq9 = get_strengths_quad(collider, "q", 9, ip)
    kq10 = get_strengths_quad(collider, "q", 10, ip)
    kqtl11 = get_strengths_quad(collider, "qtl", 11, ip)
    kqt12 = get_strengths_quad(collider, "qt", 12, ip)
    kqt13 = get_strengths_quad(collider, "qt", 13, ip)

    kqs = kqs | kq8 | kq9 | kq10 | kqtl11 | kqt12 | kqt13

    return kqs


class IR15:
    def __init__(self, lhc, N: int, ir: int = 1, mode='hllhc') -> None:
        self.ir = ir
        self.mode = mode
        self.triplet_quads = {}
        self.ms_quads = {}
        self.ds_quads = {}

        self._quads = {}

        if self.mode == 'hllhc':
            k_triplet = get_strengths_triplethl(lhc, self.ir)
        else:
            k_triplet = get_strengths_triplet(lhc, self.ir)
        k_ms = get_strengths_ms(lhc, self.ir)
        k_ds = get_strengths_ds(lhc, self.ir)
        for kn in k_triplet.keys():
            self.triplet_quads[kn] = np.zeros(N)
        for kn in k_ms.keys():
            self.ms_quads[kn] = np.zeros(N)
        for kn in k_ds.keys():
            self.ds_quads[kn] = np.zeros(N)

        self.betas = np.zeros(N)

    def fill_cycle(self, i, lhc):
        self.betas[i] = lhc.varval[f"betx_ip{self.ir}"]

        if self.mode == 'hllhc':
            _k_triplet = get_strengths_triplethl(lhc, self.ir)
        else:
            _k_triplet = get_strengths_triplet(lhc, self.ir)
        _k_ms = get_strengths_ms(lhc, self.ir)
        _k_ds = get_strengths_ds(lhc, self.ir)
        for qname, val in _k_triplet.items():
            self.triplet_quads[qname][i] = val
        for qname, val in _k_ms.items():
            self.ms_quads[qname][i] = val
        for qname, val in _k_ds.items():
            self.ds_quads[qname][i] = val

    def add_beta(self, x, ys):
        self.betas = np.append(self.betas, x)
        for q, kq in self.triplet_quads.items():
            self.triplet_quads[q] = np.append(kq, ys[q])

        for q, kq in self.ms_quads.items():
            self.ms_quads[q] = np.append(kq, ys[q])

        for q, kq in self.ds_quads.items():
            self.ds_quads[q] = np.append(kq, ys[q])

        sort_idx = np.argsort(self.betas)
        self.betas = self.betas[sort_idx]

        for q, kq in self.triplet_quads.items():
            self.triplet_quads[q] = kq[sort_idx]
        for q, kq in self.ms_quads.items():
            self.ms_quads[q] = kq[sort_idx]
        for q, kq in self.ds_quads.items():
            self.ds_quads[q] = kq[sort_idx]

class IR8:
    def __init__(self, N: int, bn="b1") -> None:
        self.beam = bn
        self.quads = {}
        self.quad_names = [
            f"kq6.l8{bn}",
            f"kq7.l8{bn}",
            f"kq8.l8{bn}",
            f"kq9.l8{bn}",
            f"kq10.l8{bn}",
            f"kqtl11.l8{bn}",
            f"kqt12.l8{bn}",
            f"kqt13.l8{bn}",
            f"kq4.l8{bn}",
            f"kq5.l8{bn}",
            f"kq4.r8{bn}",
            f"kq5.r8{bn}",
            f"kq6.r8{bn}",
            f"kq7.r8{bn}",
            f"kq8.r8{bn}",
            f"kq9.r8{bn}",
            f"kq10.r8{bn}",
            f"kqtl11.r8{bn}",
            f"kqt12.r8{bn}",
            f"kqt13.r8{bn}",
        ]

        self.betas = np.zeros(N)
        for q in self.quad_names:
            self.quads[q] = np.zeros(N)

    def fill_cycle(self, i, lhc):
        self.betas[i] = lhc.varval[f"betxip8{self.beam}"]
        for q in self.quad_names:
            self.quads[q][i] = lhc.varval[q]


class OpticsTable:
    def __init__(self, lhc, optics_name=[], mode='hllhc') -> None:
        self.time = None
        N = len(optics_name)
        self.lhc = lhc
        self.mode = mode
        self.mux_arcs = {"b1": {}, "b2": {}}
        self.muy_arcs = {"b1": {}, "b2": {}}

        self.IR8b1 = IR8(N, "b1")
        self.IR8b2 = IR8(N, "b2")

        self.IR1 = IR15(self.lhc, N, 1, self.mode)
        self.IR5 = IR15(self.lhc, N, 5, self.mode)

        for i in ARC_NAMES:
            self.mux_arcs["b1"][i] = np.zeros(N)
            self.muy_arcs["b1"][i] = np.zeros(N)
            self.mux_arcs["b2"][i] = np.zeros(N)
            self.muy_arcs["b2"][i] = np.zeros(N)

        self.betas = np.zeros(N)
        for i in range(N):
            self.lhc.vars.load_madx_optics_file(optics_name[i])
            self.betas[i] = self.lhc.varval["betx_ip5"]

            if self.mode == 'hllhc':
                for j in ARC_NAMES:
                    self.mux_arcs["b1"][j][i] = lhc.varval[f"mux{j}b1"]
                    self.muy_arcs["b1"][j][i] = lhc.varval[f"muy{j}b1"]
                    self.mux_arcs["b2"][j][i] = lhc.varval[f"mux{j}b2"]
                    self.muy_arcs["b2"][j][i] = lhc.varval[f"muy{j}b2"]
            else:
                for j in ARC_NAMES:
                    self.mux_arcs["b1"][j][i] = lhc.varval[f"muxa{j}b1"]
                    self.muy_arcs["b1"][j][i] = lhc.varval[f"muya{j}b1"]
                    self.mux_arcs["b2"][j][i] = lhc.varval[f"muxa{j}b2"]
                    self.muy_arcs["b2"][j][i] = lhc.varval[f"muya{j}b2"]

            self.IR8b1.fill_cycle(i, self.lhc)
            self.IR8b2.fill_cycle(i, self.lhc)
            
            self.IR1.fill_cycle(i, self.lhc)
            self.IR5.fill_cycle(i, self.lhc)

        self.quads = {}

        self.IR5_quads = self.IR5.triplet_quads | self.IR5.ms_quads | self.IR5.ds_quads

        self._interpolate = {}
        for q, kq in self.IR5_quads.items():
            self._interpolate[q] = self._build_interpolator(kq)

        # for q, kq in self.IR8b1.quads.items():
        #     self._interpolate[q] = self._build_interpolator(kq)
        # for q, kq in self.IR8b2.quads.items():
        #     self._interpolate[q] = self._build_interpolator(kq)


    def _build_interpolator(self, quad):
        self._interp = interp1d(
            self.betas,
            quad,
            kind="linear",
            fill_value="extrapolate",
            bounds_error=False,
        )
        return self._interp

    def interpolate(self, q, x_val):
        return self._interpolate[q](x_val)

    def add_beta(self, x, ys):
        self.betas = np.append(self.betas, x)
        for q, kq in self.quads.items():
            self.quads[q] = np.append(kq, ys[q])
        sort_idx = np.argsort(self.betas)
        self.betas = self.betas[sort_idx]
        for q, kq in self.quads.items():
            self.quads[q] = kq[sort_idx]