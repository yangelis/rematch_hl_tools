# %%
import xtrack as xt
import rematch_hl_tools
from rematch_hl_tools import qtlim1
import xtrack._temp.lhc_match as lm
from xtrack._temp.lhc_match import (
    get_arc_periodic_solution,
    match_arc_phase_advance,
    ARC_NAMES,
)
from matplotlib import pyplot as plt
import numpy as np

from rematch_hl_tools import save_to_madx


# %%
plt.rcParams.update(
    {
        "figure.figsize": (7, 6),
        # "font.size": 19,
        # "axes.titlesize": 19,
        # "axes.labelsize": 19,
        # "xtick.labelsize": 18,
        # "ytick.labelsize": 18,
        # "legend.fontsize": 19,
        # "figure.titlesize": 12,
        # "lines.linewidth": 1.0,
        "lines.markersize": 4,
        "legend.loc": "best",
        "legend.frameon": True,
    }
)
plt.rcParams["font.family"] = "sans-serif"

# %%
# get_ipython().run_line_magic("matplotlib", "qt5")
# plt.ion()
get_ipython().run_line_magic("matplotlib", "inline")
# %%
hl19_path = "/home/iangelis/Projects/hllhc_optics/hl19"
# %%
env = xt.Environment.from_json("../build_hl/hl19_round_150_1500.json")
# %%
# env.vars.load_madx_optics_file("optics/opt_round_150_newir7_v1_fix.madx")
# %%
# env.vars.load_madx_optics_file(
#     f"{hl19_path}/strengths/round/opt_round_150_1500_optphases.madx"
# )
env.vars.load_madx_optics_file("optics/opt_rount_150_ir7_b12_good3.madx")

# %%
env.lhcb1.cycle("e.ds.l3.b1", inplace=True)
env.lhcb2.cycle("e.ds.l3.b2", inplace=True)

# %%
tw = env.twiss()

# %%
t1 = tw.lhcb1
t2 = tw.lhcb2
# %%

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

# %%
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

# %%
qx = 62.31
qy = 60.32

# %%
# cc_tcp =
# {
#     "B1 Left":{'CC1 H':mux_tcphb1- mux_cchl1b1."CC5 V":} ,
#     "B1 Right":{} ,
#     "B2 Left": ,
#     "B2 Right: ,
# }

# %%

cc_tcp = [
    ["CC-TCP", "B1 Left", "B1 Right", "B2 Left", "B2 Right"],
    [
        "CC1 H",
        mux_tcphb1 + qx - mux_cchl1b1,
        mux_tcphb1 - mux_cchr1b1,
        -mux_tcphb2 + mux_cchl1b2,
        -mux_tcphb2 + mux_cchr1b1 + qx,
    ],
    [
        "CC5 V",
        muy_tcpvb1 - muy_ccvl5b1,
        muy_tcpvb1 - muy_ccvr5b1,
        -muy_tcpvb2 + muy_ccvl5b2 + qy,
        -muy_tcpvb2 + muy_ccvr5b1 + qy,
    ],
]

mkd_tct = [
    ["MKD-TCT", "B1 MKD.A", "B1 MKD.0", "B2 MKD.A", "B2 MKD.0"],
    [
        "TCTH1",
        mux_tct1b1 - mux_mkdab1,
        mux_tct1b1 - mux_mkdob1,
        -mux_tct1b2 + mux_mkdab2,
        -mux_tct1b2 + mux_mkdob2,
    ],
    [
        "TCTH5",
        mux_tct5b1 - mux_mkdab1 + qx,
        mux_tct5b1 - mux_mkdob1 + qx,
        -mux_tct5b2 + mux_mkdab2,
        -mux_tct5b2 + mux_mkdob2,
    ],
    [
        "TCTH8",
        mux_tct8b1 - mux_mkdab1,
        mux_tct8b1 - mux_mkdob1,
        -mux_tct8b2 + mux_mkdab2 + qx,
        -mux_tct8b2 + mux_mkdob2 + qx,
    ],
]

tcp_tct = [
    ["TCP-TCT", "B1 H", "B1 V", "B2 H", "B2 V"],
    [
        "TCT1",
        mux_tct1b1 - mux_tcphb1,
        muy_tct1b1 - muy_tcpvb1,
        -mux_tct1b2 + mux_tcphb2,
        -muy_tct1b2 + muy_tcpvb2,
    ],
    [
        "TCT5",
        mux_tct5b1 - mux_tcphb1 + qx,
        muy_tct5b1 - muy_tcpvb1 + qy,
        -mux_tct5b2 + mux_tcphb2,
        -muy_tct5b2 + muy_tcpvb2,
    ],
    [
        "TCT8",
        mux_tct8b1 - mux_tcphb1,
        muy_tct8b1 - muy_tcpvb1,
        -mux_tct8b2 + mux_tcphb2 + qx,
        -muy_tct8b2 + muy_tcpvb2 + qy,
    ],
]


if False:
    for tab in cc_tcp, mkd_tct, tcp_tct:
        for row in tab:
            for col in row:
                if type(col) is str:
                    print(f'"{col:8}"', end=",")
                else:
                    print(f"{col:10.2f}", end=",")
            print()


print()
for tab in cc_tcp, mkd_tct, tcp_tct:
    for row in tab:
        for col in row:
            if type(col) is str:
                print(f'"{col:8}"', end=",")
            else:
                cc = (col * 2 - round(col * 2)) / 2
                print(f"{cc*360:10.2f}", end=",")
        print()

# %%

cc_tcp = {
    "CC1H": {
        "B1 Left": mux_tcphb1 + qx - mux_cchl1b1,
        "B1 Right": mux_tcphb1 - mux_cchr1b1,
        "B2 Left": -mux_tcphb2 + mux_cchl1b2,
        "B2 Right": -mux_tcphb2 + mux_cchr1b1 + qx,
    },
    "CC5V": {
        "B1 Left": muy_tcpvb1 - muy_ccvl5b1,
        "B1 Right": muy_tcpvb1 - muy_ccvr5b1,
        "B2 Left": -muy_tcpvb2 + muy_ccvl5b2 + qy,
        "B2 Right": -muy_tcpvb2 + muy_ccvr5b1 + qy,
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
