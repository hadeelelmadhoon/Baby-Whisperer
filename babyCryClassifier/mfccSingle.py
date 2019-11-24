import os
import numpy as np
import matplotlib.pyplot as plt
import glob
import scipy.io.wavfile as wav
from python_speech_features import mfcc, logfbank
from matplotlib import cm

def mfccSingle(wavFileName):

    newArray = np.empty((1, 124, 13))

    # x data

    # Read the input audio file
    (rate,sig) = wav.read(wavFileName)
    # Take the first 10,000 samples for analysis
    sig = sig[:10000]

    features_mfcc = mfcc(sig, rate)
    features_mfcc = np.resize(features_mfcc, (1, 124, 13))
    newArray = np.append(newArray, features_mfcc, axis=0)

    newArray = newArray[1:]
    newArray = np.resize(newArray, (1, 124, 13, 1))
    return newArray

