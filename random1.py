import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import scipy.stats as st
import incredible as cr
from pygtc import plotGTC 


dat = np.loadtxt('Exodata/LightCurves/OGLE/2006/blg-109/phot.dat')
print(dat.shape)