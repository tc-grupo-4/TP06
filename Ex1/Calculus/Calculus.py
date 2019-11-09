import matplotlib.pyplot as plt
import numpy as np
from math import *
import control as cl

def plotPolesAndZeros(num,den):
    sistema = cl.TransferFunction(num,den)
    cl.pzmap(sistema,Plot=True)
    plt.show()
    return

C = 1e-9
R = 2050
Rt = 540
R3 = 5.4e3
R4 = 2.4e3 +Rt
K=1+R3/R4

num = [C**2 * R**2 * K, 3*C*R*K , K]
den = [C**2 * R**2 , C*R*(2-R3/R4) , 1]
plotPolesAndZeros(num, den)