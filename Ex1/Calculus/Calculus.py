import matplotlib.pyplot as plt
import numpy as np
from math import *


Rt = 0
R4 = 2.4e3+Rt
R3 = 5.4e3
wp = 10
Av = 100e3


pol = (Av*wp)/(1+R3/R4) - 1

mod = (pol**2)**0.5
pha = atan(np.imag(pol)/np.real(pol))+3.142

plt.polar(pha,mod,marker='x', color='black')
plt.title("Diagrama de polos y ceros")
plt.show()