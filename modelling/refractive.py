import numpy as np
import matplotlib.pyplot as plt

def Gallium(x):
    return (1+2.60+1.75/(1-(0.256/x)**2)+4.1/(1-(17.86/x)**2))**.5
