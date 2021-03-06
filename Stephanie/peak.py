from __future__ import division
import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn
from scipy.signal import argrelextrema
from scipy.interpolate import interp1d
import abjad
import re


WAV = 'scale.wav'
#WAV = 'longscale.wav'

rate, data = wavfile.read(WAV)
time = np.arange(len(data[:,0]))*1.0/rate

globalMax = []
maxx = 0
for i in data[:,0]:
    if maxx<i:
        maxx = i

globalMax.append(maxx)

ind = np.where(data[:,0]==maxx)[0][0]

maxx = 0
for i in data[:,0][:ind]:
    if maxx<i:
        maxx = i

globalMax.append(maxx)
ind = np.where(data[:,0]==maxx)[0][0]

ind = np.where(data[:,0]==globalMax[-1])[0][0]
plt.plot(time,data[:,0])
plt.plot(time[ind],globalMax[-1], 'ro')
plt.show()
