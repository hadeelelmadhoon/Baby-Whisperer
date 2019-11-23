import os
import numpy as np
import matplotlib.pyplot as plt
import glob
import scipy.io.wavfile as wav
from python_speech_features import mfcc, logfbank
from matplotlib import cm

# Read the input audio file
#(rate,sig) = wav.read('data/belly_pain/69BDA5D6-0276-4462-9BF7-951799563728-1436936185-1.1-m-26-bp.wav')

# newArray = np.empty((124, 13, 1))
# imageArr = []

# # x data
# for f in glob.iglob(r'data/**/*.wav', recursive=True):
#     (rate,sig) = wav.read(f)
#
#     # Take the first 10,000 samples for analysis
#     sig = sig[:10000]
#     features_mfcc = mfcc(sig,rate)
#
#     # print(np.shape(features_mfcc))
#     # print(features_mfcc.shape)
#     # print(type(features_mfcc))
#     # features_mfcc = np.resize(features_mfcc, (124, 13, 1))
#     # fig, ax = plt.subplot()
#     # features_mfcc = np.swapaxes(features_mfcc, 0 , 1)
#     # cax = ax.imshow(features_mfcc, interpolation='nearest', cmap='gray', origin='lower', aspect='auto')
#     # plt.show()
#     # plt.plot(features_mfcc)
#     # plt.show()
#     # Print the parameters for MFCC
#     # print('\nMFCC:\nNumber of windows =', features_mfcc.shape[0])
#     # print('Length of each feature =', features_mfcc.shape[1])
#     # print(features_mfcc)
#     # print(type(features_mfcc))
#
#     # newArray = np.append(newArray, features_mfcc, axis=2)
#     # print(type(newArray))
#
#     # Plot the features
#     # features_mfcc = features_mfcc.T
#     imageArr.append(features_mfcc)
#     # plt.matshow(features_mfcc)
#     # plt.title('MFCC')
#     plt.imshow(features_mfcc, cmap='gray', vmin=0, vmax=255)
#     plt.show()
#
#     # Extract the Filter Bank features
#     features_fb = logfbank(sig, rate)
#
#     # Print the parameters for Filter Bank
#     # print('\nFilter bank:\nNumber of windows =', features_fb.shape[0])
#     # print('Length of each feature =', features_fb.shape[1])
#
#     # Plot the features
#     # features_fb = features_fb.T
#     # plt.matshow(features_fb)
#     # plt.title('Filter bank')
#     #
#     # plt.show()
#
#     # print(newArray.shape)
#     # print(newArray.shape[1])
#     # print(newArray.shape[2])
# print(len(newArray[1]))

# plt.title('MFCC')

# np.subtract(imageArr[400], np.mean(imageArr[400]))
# print(np.subtract(imageArr[400], np.mean(imageArr[400])))

# (rate,sig) = wav.read('data/belly_pain/69BDA5D6-0276-4462-9BF7-951799563728-1436936185-1.1-m-26-bp.wav')
# features_mfcc = mfcc(sig,rate)
#
# # features_mfcc = np.resize(features_mfcc, (124, 13, 1))
# fig, ax = plt.subplots()
# features_mfcc = np.swapaxes(features_mfcc, 0 , 1)
# cax = ax.imshow(features_mfcc, interpolation='nearest', cmap=cm.coolwarm, origin='lower', aspect='auto')
# plt.show()
# plt.plot(features_mfcc)
# plt.show()
#
# #  y data
#
# labels = []
#
# cryTypes = ['belly_pain', 'burping', 'discomfort', 'hungry', 'tired']
# i = 0
#
# for types in cryTypes:
#     for idx, f in enumerate(glob.iglob(r'data/'+types+'/*.wav', recursive=True)):
#         labels.append(i)
#     i=i+1
#
# yData = labels
# print(len(yData))






newArray = np.empty((1, 124, 13))

# x data
for f in glob.iglob(r'data/**/*.wav', recursive=True):
    (rate,sig) = wav.read(f)

    # Take the first 10,000 samples for analysis
    sig = sig[:10000]

    features_mfcc = mfcc(sig, rate)
    print(features_mfcc.shape)
    features_mfcc = np.resize(features_mfcc, (1, 124, 13))
    newArray = np.append(newArray, features_mfcc, axis=0)
    print(features_mfcc.shape)

newArray = newArray[1:]


#  y data

labels = []

cryTypes = ['belly_pain', 'burping', 'discomfort', 'hungry', 'tired']
i = 0

for types in cryTypes:
    for idx, f in enumerate(glob.iglob(r'data/'+types+'/*.wav', recursive=True)):
        labels.append(i)
    i=i+1

yData = labels
# print(yData)
