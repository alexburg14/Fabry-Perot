import numpy as np
def Transmission(lam: int, r = 1, optdick = 1):
    lam = lam*10**-9
    delphi = (4*np.pi/lam) * optdick
    F = ((4*r)/(1-r)**2)
    return 1/ (1+(F*(np.sin(delphi/2))**2))

def reflectance(n1,n2):
    return ((n1-n2)/(n1+n2))