import xtrack as xt


def rematch_ir6(
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
    solve=True,
    restore=True,
    assert_within_tol=True,
    default_tol=None,
):

    assert line_name in ["lhcb1", "lhcb2"]
    bn = line_name[-2:]

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
                # dx=dx_ip6,
                # dpx=dpx_ip6,
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
        ],
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
