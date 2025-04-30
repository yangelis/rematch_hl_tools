
def rename_knobs_ir28(collider):
    v = collider.vars
    f = collider.functions

    knobs_mcbx = "acbxhv1.lrirn acbxhv3.lrirn"
    for lr in ["l", "r"]:
        for irn in ["2", "8"]:
            for hv in ["h", "v"]:
                for kk in knobs_mcbx.split():
                    kn = kk.replace("lr", lr).replace("irn", irn).replace("hv", hv)
                    v[kn] = v[f"{kn}_from_on_x{irn}{hv}"]._expr + v[f"{kn}_from_on_sep{irn}{hv}"]._expr

                    kn2 = kk.replace("hv1", "hv2").replace("lr", lr).replace("irn", irn).replace("hv", hv)
                    v[kn2] = v[f"{kn}_from_on_x{irn}{hv}"]._expr + v[f"{kn}_from_on_sep{irn}{hv}"]._expr   

    knobs_mcbys_hv = ["acbyhvs4.lrirnbim", "acbyhvs5.lrirnbim"]
    for bim in ['b1', 'b2']:
        for lr in ["l", "r"]:
            for irn in ["2", "8"]:
                for hv in ["h", "v"]:
                    kn1 = knobs_mcbys_hv[0].replace("lr", lr).replace("hv", hv).replace("irn", irn).replace('bim', bim)
                    v[kn1] = (
                        v[f"{kn1}_from_on_x{irn}{hv}"]._expr 
                        + v[f"{kn1}_from_on_sep{irn}{hv}"]._expr 
                        + v[f"{kn1}_from_on_o{irn}{hv}"]._expr 
                        + v[f"{kn1}_from_on_a{irn}{hv}"]._expr
                    )

    knobs_mcby5_ir2 = {'h': ['acbyhs5.l2b1', 'acbchs5.r2b1', 'acbyhs5.l2b2', 'acbchs5.r2b2'],
                       'v': ['acbyvs5.l2b1', 'acbcvs5.r2b1', 'acbyvs5.l2b2', 'acbcvs5.r2b2']
    }
    
    for hv, kns in knobs_mcby5_ir2.items():
        for kn in kns:
            v[kn] = (
                v[f"{kn}_from_on_x2{hv}"]._expr 
                + v[f"{kn}_from_on_sep2{hv}"]._expr 
                + v[f"{kn}_from_on_o2{hv}"]._expr 
                + v[f"{kn}_from_on_a2{hv}"]._expr
            )
    
    knobs_mcby5_ir8 = {'h': ['acbyhs5.r8b1', 'acbchs5.l8b1', 'acbyhs5.r8b2', 'acbchs5.l8b2'],
                       'v': ['acbyvs5.r8b1', 'acbcvs5.l8b1', 'acbyvs5.r8b2', 'acbcvs5.l8b2']
    }
    for hv, kns in knobs_mcby5_ir8.items():
        for kn in kns:
            v[kn] = (
                v[f"{kn}_from_on_x8{hv}"]._expr 
                + v[f"{kn}_from_on_sep8{hv}"]._expr 
                + v[f"{kn}_from_on_o8{hv}"]._expr 
                + v[f"{kn}_from_on_a8{hv}"]._expr
            )


def redefine_xing_knobs_ir28(collider):
    v = collider.vars
    f = collider.functions
    v['phi_ir2'] = 90.
    v['phi_ir8'] = 0.
    for irn in ['2', '8']:
        v[f'cphi_ir{irn}'] = f.cos(v[f'phi_ir{irn}'] * v['pi'] / 180.)
        v[f'sphi_ir{irn}'] = f.sin(v[f'phi_ir{irn}'] * v['pi'] / 180.)
        v[f'on_x{irn}h']   =  v[f'on_x{irn}'] * v[f'cphi_ir{irn}']
        v[f'on_x{irn}v']   =  v[f'on_x{irn}'] * v[f'sphi_ir{irn}']
        v[f'on_sep{irn}h'] = -v[f'on_sep{irn}'] * v[f'sphi_ir{irn}']
        v[f'on_sep{irn}v'] =  v[f'on_sep{irn}'] * v[f'cphi_ir{irn}']
        v[f'on_o{irn}h']   =  v[f'on_o{irn}'] * v[f'cphi_ir{irn}']
        v[f'on_o{irn}v']   =  v[f'on_o{irn}'] * v[f'sphi_ir{irn}']
        v[f'on_a{irn}h']   = -v[f'on_a{irn}'] * v[f'sphi_ir{irn}']
        v[f'on_a{irn}v']   =  v[f'on_a{irn}'] * v[f'cphi_ir{irn}']

        v[f'xip{irn}b1']  =   1e-3*v[f'on_sep{irn}h'] + 1e-3*v[f'on_o{irn}h']
        v[f'xip{irn}b2']  = - 1e-3*v[f'on_sep{irn}h'] + 1e-3*v[f'on_o{irn}h']
        v[f'yip{irn}b1']  =   1e-3*v[f'on_sep{irn}v'] + 1e-3*v[f'on_o{irn}v']
        v[f'yip{irn}b2']  = - 1e-3*v[f'on_sep{irn}v'] + 1e-3*v[f'on_o{irn}v']

        v[f'pxip{irn}b1'] =   1e-6*v[f'on_x{irn}h'] + 1e-6*v[f'on_a{irn}h']
        v[f'pxip{irn}b2'] = - 1e-6*v[f'on_x{irn}h'] + 1e-6*v[f'on_a{irn}h']
        v[f'pyip{irn}b1'] =   1e-6*v[f'on_x{irn}v'] + 1e-6*v[f'on_a{irn}v']
        v[f'pyip{irn}b2'] = - 1e-6*v[f'on_x{irn}v'] + 1e-6*v[f'on_a{irn}v']
