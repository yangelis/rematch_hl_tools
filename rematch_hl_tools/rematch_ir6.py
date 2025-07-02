import numpy as np
import xtrack as xt
from xtrack._temp.lhc_match import get_arc_periodic_solution


# nominal injection/collision parameter at the ip
fixed_ip_params = {
    "b1": {
        "mux": 2.0000,
        "betx": 187.297499,
        "alfx": -0.541994,
        "muy": 2.0300,
        "bety": 168.122917,
        "alfy": 0.605891,
        "dx": 0.00,
        "dpx": 0,
    },
    "b2": {
        "mux": 2.0000,
        "betx": 187.749224,
        "alfx": 0.551968,
        "muy": 2.0300,
        "bety": 178.368556,
        "alfy": -0.607183,
        "dx": 0.00,
        "dpx": 0,
    },
}


class Action_ir6(xt.Action):
    def __init__(self, collider, bim):
        self.collider = collider
        self.bim = bim

    def run(self, allow_failure=False):
        try:
            tw = self.collider[f"lhc{self.bim}"].twiss()
            beta0 = tw.get_twiss_init(f"s.ds.l6.{self.bim}")
            beta0.mux = 0
            beta0.muy = 0
            tw_ir6 = self.collider[f"lhc{self.bim}"].twiss(
                start=f"s.ds.l6.{self.bim}", end=f"e.ds.r6.{self.bim}", init=beta0
            )
        except ValueError:
            # Twiss failed
            return {
                "betxip6": 1e100,
                "alfxip6": 1e100,
                "betyip6": 1e100,
                "alfyip6": 1e100,
                "dxip6": 1e100,
                "dpxip6": 1e100,
                "dmuxkick_tcsg": 1e100,
                "dmuxkick_tcdqc": 1e100,
                "dmuxkick_tcdqb": 1e100,
                "dmuxkick_tcdqa": 1e100,
                "dmuxkick": 1e100,
                "dxq5": 1e100,
                "dxq4": 1e100,
                "dxtcdq": 1e100,
                "betxtcdq": 1e100,
                "betytcdq": 1e100,
                "betxtcds": 1e100,
                "betytcds": 1e100,
                "betxtcsg": 1e100,
                "betytcsg": 1e100,
                "betxmkd": 1e100,
                "betymkd": 1e100,
                "bxdump": 1e100,
                "bydump": 1e100,
                "bdump": 1e100,
                "dmuxkick_bds": 1e100,
                "dmuxkick_bdsa": 1e100,
                # "dmuxkick_eds": 1e100,
                **({"dmuxkick_eds": 1e100} if self.bim == "b1" else {}),
                "tcdqmingap": 1e100,
                "tcdqgap": 1e100,
            }

        # constants needed for calculation of the constraint 6 (2017) from chiara 8/6/17
        chi6_nsig = 10.1
        chi6_dpoverp = 2e-4
        chi6_emitx = 2.5e-6 / (7000 / 0.9382720814)
        chi6_maxorbitdrift = 0.6e-3
        al_dump = 761

        betxip6 = tw_ir6["betx", "ip6"]
        alfxip6 = tw_ir6["alfx", "ip6"]
        betyip6 = tw_ir6["bety", "ip6"]
        alfyip6 = tw_ir6["alfy", "ip6"]
        dxip6 = tw_ir6["dx", "ip6"]
        dpxip6 = tw_ir6["dpx", "ip6"]

        if self.bim == "b1":
            dmuxkick_tcsg = tw_ir6["mux", "tcsp.a4r6.b1"] - tw_ir6["mux", "mkd.h5l6.b1"]
            dmuxkick_tcdqc = (
                tw_ir6["mux", "tcdqa.c4r6.b1"] - tw_ir6["mux", "mkd.h5l6.b1"]
            )
            dmuxkick_tcdqb = (
                tw_ir6["mux", "tcdqa.b4r6.b1"] - tw_ir6["mux", "mkd.h5l6.b1"]
            )
            dmuxkick_tcdqa = (
                tw_ir6["mux", "tcdqa.a4r6.b1"] - tw_ir6["mux", "mkd.h5l6.b1"]
            )
            dmuxkick = dmuxkick_tcdqc

            if np.abs(dmuxkick_tcdqa - 0.25) > np.abs(dmuxkick - 0.25):
                dmuxkick = dmuxkick_tcdqa

            if np.abs(dmuxkick_tcdqb - 0.25) > np.abs(dmuxkick - 0.25):
                dmuxkick = dmuxkick_tcdqb

            dxq5 = np.abs(tw_ir6["dx", "mqy.5l6.b1"])
            dxq4 = np.abs(tw_ir6["dx", "mqy.4r6.b1"])

            dxtcdq = tw_ir6["dx", "tcdqa.a4r6.b1"]
            betxtcdq = tw_ir6["betx", "tcdqa.a4r6.b1"]
            betytcdq = tw_ir6["bety", "tcdqa.a4r6.b1"]
            betxtcds = tw_ir6["betx", "tcdsa.4l6.b1"]
            betytcds = tw_ir6["bety", "tcdsa.4l6.b1"]
            betxtcsg = tw_ir6["betx", "tcsp.a4r6.b1"]
            betytcsg = tw_ir6["bety", "tcsp.a4r6.b1"]
            betxmkd = tw_ir6["betx", "mkd.h5l6.b1"]
            betymkd = tw_ir6["bety", "mkd.h5l6.b1"]

            bxdump = (
                betxip6
                - 2 * al_dump * alfxip6
                + al_dump**2 * (1 + alfxip6**2) / betxip6
            )
            bydump = (
                betyip6
                - 2 * al_dump * alfyip6
                + al_dump**2 * (1 + alfyip6**2) / betyip6
            )
            bdump = np.sqrt(bxdump * bydump)

            dmuxkick_bds = tw_ir6["mux", "mkd.o5l6.b1"]
            dmuxkick_bdsa = tw_ir6["mux", "mkd.a5l6.b1"]
            dmuxkick_eds = tw_ir6["mux", "e.ds.r6.b1"] - tw_ir6["mux", "mkd.o5l6.b1"]

            tcdqmingap = (
                chi6_nsig * np.sqrt(chi6_emitx * betxtcdq)
                - 3e-4
                - np.abs(dxtcdq * chi6_dpoverp)
                - chi6_maxorbitdrift
            )

            tcdqgap = chi6_nsig * np.sqrt(chi6_emitx * betxtcdq)
        else:
            dmuxkick_tcsg = tw_ir6["mux", "mkd.h5r6.b2"] - tw_ir6["mux", "tcsp.a4l6.b2"]
            dmuxkick_tcdqc = (
                tw_ir6["mux", "mkd.h5r6.b2"] - tw_ir6["mux", "tcdqa.c4l6.b2"]
            )
            dmuxkick_tcdqb = (
                tw_ir6["mux", "mkd.h5r6.b2"] - tw_ir6["mux", "tcdqa.b4l6.b2"]
            )
            dmuxkick_tcdqa = (
                tw_ir6["mux", "mkd.h5r6.b2"] - tw_ir6["mux", "tcdqa.a4l6.b2"]
            )
            dmuxkick = dmuxkick_tcdqc

            if np.abs(dmuxkick_tcdqa - 0.25) > np.abs(dmuxkick - 0.25):
                dmuxkick = dmuxkick_tcdqa

            if np.abs(dmuxkick_tcdqb - 0.25) > np.abs(dmuxkick - 0.25):
                dmuxkick = dmuxkick_tcdqb

            dxq5 = np.abs(tw_ir6["dx", "mqy.5r6.b2"])
            dxq4 = np.abs(tw_ir6["dx", "mqy.4l6.b2"])

            dxtcdq = tw_ir6["dx", "tcdqa.a4l6.b2"]
            betxtcdq = tw_ir6["betx", "tcdqa.a4l6.b2"]
            betytcdq = tw_ir6["bety", "tcdqa.a4l6.b2"]
            betxtcds = tw_ir6["betx", "tcdsa.4r6.b2"]
            betytcds = tw_ir6["bety", "tcdsa.4r6.b2"]
            betxtcsg = tw_ir6["betx", "tcsp.a4l6.b2"]
            betytcsg = tw_ir6["bety", "tcsp.a4l6.b2"]
            betxmkd = tw_ir6["betx", "mkd.h5r6.b2"]
            betymkd = tw_ir6["bety", "mkd.h5r6.b2"]

            bxdump = (
                betxip6
                + 2 * al_dump * alfxip6
                + al_dump**2 * (1 + alfxip6**2) / betxip6
            )
            bydump = (
                betyip6
                + 2 * al_dump * alfyip6
                + al_dump**2 * (1 + alfyip6**2) / betyip6
            )
            bdump = np.sqrt(bxdump * bydump)

            dmuxkick_bds = tw_ir6["mux", "mkd.o5r6.b2"]
            dmuxkick_bdsa = tw_ir6["mux", "mkd.a5r6.b2"]
            # dmuxkick_eds = ??

            tcdqmingap = (
                chi6_nsig * np.sqrt(chi6_emitx * betxtcdq)
                - 3e-4
                - np.abs(dxtcdq * chi6_dpoverp)
                - chi6_maxorbitdrift
            )

            tcdqgap = chi6_nsig * np.sqrt(chi6_emitx * betxtcdq)

        return {
            "betxip6": betxip6,
            "alfxip6": alfxip6,
            "betyip6": betyip6,
            "alfyip6": alfyip6,
            "dxip6": dxip6,
            "dpxip6": dpxip6,
            "dmuxkick_tcsg": dmuxkick_tcsg,
            "dmuxkick_tcdqc": dmuxkick_tcdqc,
            "dmuxkick_tcdqb": dmuxkick_tcdqb,
            "dmuxkick_tcdqa": dmuxkick_tcdqa,
            "dmuxkick": dmuxkick,
            "dxq5": dxq5,
            "dxq4": dxq4,
            "dxtcdq": dxtcdq,
            "betxtcdq": betxtcdq,
            "betytcdq": betytcdq,
            "betxtcds": betxtcds,
            "betytcds": betytcds,
            "betxtcsg": betxtcsg,
            "betytcsg": betytcsg,
            "betxmkd": betxmkd,
            "betymkd": betymkd,
            "bxdump": bxdump,
            "bydump": bydump,
            "bdump": bdump,
            "dmuxkick_bds": dmuxkick_bds,
            "dmuxkick_bdsa": dmuxkick_bdsa,
            # "dmuxkick_eds": dmuxkick_eds,
            **({"dmuxkick_eds": dmuxkick_eds} if self.bim == "b1" else {}),
            "tcdqmingap": tcdqmingap,
            "tcdqgap": tcdqgap,
        }

class Action_dump(xt.Action):
    def __init__(self, collider, bim):
        self.collider = collider
        self.bim = bim

    def run(self, allow_failure=False):
        try:
            tw = self.collider[f"lhc{self.bim}"].twiss()
            beta0 = tw.get_twiss_init(f"s.ds.l6.{self.bim}")
            beta0.mux = 0
            beta0.muy = 0
            tw_ir6 = self.collider[f"lhc{self.bim}"].twiss(
                start=f"s.ds.l6.{self.bim}", end=f"e.ds.r6.{self.bim}", init=beta0
            )
        except ValueError:
            # Twiss failed
            return {"bxdump": 1e100, "bydump": 1e100, "bdump": 1e100}

        al_dump = 761

        betxip6 = tw_ir6["betx", "ip6"]
        alfxip6 = tw_ir6["alfx", "ip6"]
        betyip6 = tw_ir6["bety", "ip6"]
        alfyip6 = tw_ir6["alfy", "ip6"]

        if self.bim == "b1":
            bxdump = (
                betxip6
                - 2 * al_dump * alfxip6
                + al_dump**2 * (1 + alfxip6**2) / betxip6
            )
            bydump = (
                betyip6
                - 2 * al_dump * alfyip6
                + al_dump**2 * (1 + alfyip6**2) / betyip6
            )
            bdump = np.sqrt(bxdump * bydump)      
        else:
            bxdump = (
                betxip6
                + 2 * al_dump * alfxip6
                + al_dump**2 * (1 + alfxip6**2) / betxip6
            )
            bydump = (
                betyip6
                + 2 * al_dump * alfyip6
                + al_dump**2 * (1 + alfyip6**2) / betyip6
            )
            bdump = np.sqrt(bxdump * bydump)

        return {"bxdump": bxdump, "bydump": bydump, "bdump": bdump}



def rematch_ir6m(
    collider,
    line_name,
    boundary_conditions_left,
    boundary_conditions_right,
    mux_ir6,
    muy_ir6,
    alfx_ip6,
    alfy_ip6,
    betx_ip6,
    bety_ip6,
    dx_ip6,
    dpx_ip6,
    match_dx=False,
    match_dpx=False,
    fixedip=False,
    solve=True,
    restore=True,
    assert_within_tol=True,
    default_tol=None,
    betxtcdq=None,
    betytcdq=None,
    betytcds=None,
    bxdump=None,
    bydump=None,
    betir=None,
):

    assert line_name in ["lhcb1", "lhcb2"]
    bn = line_name[-2:]

    if fixedip:
        alfx_ip6 = fixed_ip_params[bn]["alfx"]
        alfy_ip6 = fixed_ip_params[bn]["alfy"]
        betx_ip6 = fixed_ip_params[bn]["betx"]
        bety_ip6 = fixed_ip_params[bn]["bety"]
        dx_ip6 = fixed_ip_params[bn]["dx"]
        dpx_ip6 = fixed_ip_params[bn]["dpx"]

    # action_ir6 = Action_ir6(collider, bn)
    action_dump = Action_dump(collider, bn)

    q4 = "mqy.4r6.b1" if bn == 'b1' else "mqy.4l6.b2"
    q5 = "mqy.5l6.b1" if bn == 'b1' else "mqy.5r6.b2"
    tcdqa = "tcdqa.a4r6.b1" if bn == 'b1' else "tcdqa.a4l6.b2"
    tcds = "tcdsa.4l6.b1" if bn == 'b1' else "tcdsa.4r6.b2"

    ref_tcdqa_betxy = {'b1': {'betx': 470.0, 'bety': 145.0}, 'b2': {'betx': 470.0, 'bety': 145.0}} # 145 or 170?

    extra_targets = []
    if betxtcdq is None:
        betxtcdq = ref_tcdqa_betxy[bn]['betx']

    if betytcdq is None:
        betytcdq = ref_tcdqa_betxy[bn]['bety']
             
    if betytcds is None:
        betytcds = 200.0

    targets_dump = []
    if bxdump is None and bydump is None:
        extra_targets.append(action_dump.target("bxdump", xt.GreaterThan(4000)))
        extra_targets.append(action_dump.target("bydump", xt.GreaterThan(3200)))
        extra_targets.append(action_dump.target("bdump", xt.GreaterThan(4500)))
    else:
        extra_targets.append(action_dump.target("bxdump", bxdump))
        extra_targets.append(action_dump.target("bydump", bydump))


     # extra_targets.append(xt.Target(at=tcds, tar='bety', value=xt.GreaterThan(170))) 


    targets_betir = []
    if betir is not None:
        if bn == 'b1':
            targets_betir = [
                xt.Target(at="mqy.4l6.b1", tar='bety', value=xt.LessThan(betir)),
                xt.Target(at="mqy.5l6.b1", tar='betx', value=xt.LessThan(betir)),
                xt.Target(at="mqy.4r6.b1", tar='betx', value=xt.LessThan(betir)),
                xt.Target(at="mqy.5r6.b1", tar='bety', value=xt.LessThan(betir)),
                xt.Target(at="mqml.10l6.b1", tar='bety', value=xt.LessThan(betir)),
                xt.Target(at="mqm.9l6.b1", tar='betx', value=xt.LessThan(betir)),
            
        ]
        elif bn == 'b2':
            targets_betir = [
                xt.Target(at="mqy.4l6.b2", tar='betx', value=xt.LessThan(betir)),
                xt.Target(at="mqy.4r6.b2", tar='bety', value=xt.LessThan(betir)),
                xt.Target(at="mqy.5r6.b2", tar='betx', value=xt.LessThan(betir)),
                xt.Target(at='mqml.8l6.b2', tar='betx', value=xt.LessThan(betir)),
                xt.Target(at='mqml.8r6.b2', tar='bety', value=xt.LessThan(betir)),
                xt.Target(at='mqm.9l6.b2', tar='bety', value=xt.LessThan(betir)),
                xt.Target(at='mqm.9r6.b2', tar='betx', value=xt.LessThan(betir)),
                xt.Target(at='mqml.10l6.b2', tar='betx', value=xt.LessThan(betir)),
                xt.Target(at='mqml.10r6.b2', tar='bety', value=xt.LessThan(betir)),
        ]

    opt = collider[f"lhc{bn}"].match(
        solve=False,
        restore_if_fail=restore,
        assert_within_tol=assert_within_tol,
        default_tol=default_tol,
        start=f"s.ds.l6.{bn}",
        end=f"e.ds.r6.{bn}",
        # Left boundary
        init=boundary_conditions_left,
        init_at=xt.START,
        targets=[
            xt.TargetSet(
                at="ip6",
                alfx=alfx_ip6,
                alfy=alfy_ip6,
                betx=betx_ip6,
                bety=bety_ip6,
                tag="stage1",
            ),
            xt.Target(at="ip6", dx=dx_ip6, tag="dx_ip6"),
            xt.Target(at="ip6", dpx=dpx_ip6, tag="dpx_ip6"),
            xt.TargetSet(
                at=xt.END,
                tars=("betx", "bety", "alfx", "alfy", "dx", "dpx"),
                value=boundary_conditions_right,
            ),
            xt.TargetRelPhaseAdvance("mux", mux_ir6),
            xt.TargetRelPhaseAdvance("muy", muy_ir6),
            xt.Target(tag="dxq4", tar=lambda tw: np.abs(tw['dx', q4]), value=xt.LessThan(1.2) if bn == "b1" else xt.LessThan(0.7)),
            xt.Target(tag="dxq5", tar=lambda tw: np.abs(tw['dx', q5]), value=xt.LessThan(1.2) if bn == "b1" else xt.LessThan(0.7)),
            xt.Target(tag="dxtcdq", tar=lambda tw: np.abs(tw['dx', tcdqa]), value=xt.LessThan(0.5)),
            xt.Target(tag="tcdqa_betx", at=tcdqa, tar='betx', value=xt.GreaterThan(betxtcdq)),
            xt.Target(tag="tcdqa_bety", at=tcdqa, tar='bety', value=xt.GreaterThan(betytcdq)),
            xt.Target(tag="tcds_bety", at=tcds, tar='bety', value=xt.GreaterThan(betytcds)),
            # xt.Target(tag="tcds_bety", at=tcds, tar="bety", value=xt.GreaterThan(170)), # NOTE: WHY this is there in madx files
          
        ] + targets_betir,
        vary=(
            [
                xt.VaryList(
                    [
                        f"kqt13.l6{bn}",
                        f"kqt12.l6{bn}",
                        f"kqtl11.l6{bn}",
                        f"kq10.l6{bn}",
                        f"kq9.l6{bn}",
                        f"kq8.l6{bn}",
                        f"kq5.l6{bn}",
                        f"kq5.r6{bn}",
                        f"kq8.r6{bn}",
                        f"kq9.r6{bn}",
                        f"kq10.r6{bn}",
                        f"kqtl11.r6{bn}",
                        f"kqt12.r6{bn}",
                        f"kqt13.r6{bn}",
                    ]
                )
            ]
            + [xt.Vary((f"kq4.r6{bn}" if bn == "b1" else f"kq4.l6{bn}"))]
        ),
    )

    if not match_dx:
        opt.disable(target="dx_ip6")

    if not match_dpx:
        opt.disable(target="dpx_ip6")

    # No staged match for IR6
    if solve:
        opt.solve()

    return opt
