#!/usr/bin/env python3

import numpy as np
from scipy.io import wavfile
from scipy import ndimage, misc

sampleRate = 44100
frequency = 440
length = 1 #seconde

t = np.linspace(0, length, sampleRate * length)  #  Produces a 5 second Audio-File
y = np.sin(frequency * 2 * np.pi * t)



#y = np.random.normal(0, 2, sampleRate * length)
#y = ndimage.maximum_filter(y, size=20)
#y = ndimage.minimum_filter(y, size=20)
#y = ndimage.gaussian_filter(y, sigma=5)
y = ndimage.median_filter(y, size =20)


wavfile.write('Sine.wav', sampleRate, y)
