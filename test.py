import matplotlib.pyplot as plt
import numpy as np


def Transmission(lam, r = 1, d = 1, n = 1):
    lam = lam*10**-9
    delphi = (4*np.pi/lam) * n * d
    F = ((4*r)/(1-r)**2)
    return 1/ (1+(F*(np.sin(delphi/2))**2))



x = np.arange(1200,1700,0.1)
T = Transmission(x, r = 0.4*0.259 , d = 3.5*10**(-6), n = 2.3)
"""for i in range(5):
    T = T * Transmission(x, r = 0.2 , d = 2*10**(-6), n = 1.5) 
for i in range(5):
    T = T * Transmission(x, r = 0.2 , d = 2*10**(-6), n = 2)"""