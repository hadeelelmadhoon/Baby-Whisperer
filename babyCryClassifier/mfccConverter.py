import os
import numpy as np
import matplotlib.pyplot as plt
import glob
import scipy.io.wavfile as wav
from python_speech_features import mfcc, logfbank
from matplotlib import cm

# Read the input audio file
#(rate,sig) = wav.read('data/belly_pain/69BDA5D6-0276-4462-9BF7-951799563728-1436936185-1.1-m-26-bp.wav')

newArray = np.empty((1, 124, 13))

# x data
for f in glob.iglob(r'data/**/*.wav', recursive=True):
    (rate,sig) = wav.read(f)

    # Take the first 10,000 samples for analysis
    sig = sig[:10000]

    features_mfcc = mfcc(sig, rate)
    features_mfcc = np.resize(features_mfcc, (1, 124, 13))
    newArray = np.append(newArray, features_mfcc, axis=0)

newArray = newArray[1:]


#  y data

labels = []

cryTypes = ['belly_pain', 'discomfort', 'burping', 'hungry', 'tired']
i = 0

for types in cryTypes:
    for idx, f in enumerate(glob.iglob(r'data/'+types+'/*.wav', recursive=True)):
        labels.append(i)
    i=i+1

yData = labels
