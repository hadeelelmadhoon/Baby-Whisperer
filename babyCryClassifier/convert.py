import numpy, scipy, matplotlib.pyplot as plt, sklearn, librosa, urllib, IPython.display
import librosa.display
from matplotlib.colors import NoNorm
# plt.rcParams['figure.figsize'] = (14,4)

plt.gray()

x, fs = librosa.load('data/belly_pain/69BDA5D6-0276-4462-9BF7-951799563728-1436936185-1.1-m-26-bp.wav')
librosa.display.waveplot(x, sr=fs)

mfccs = librosa.feature.mfcc(x, sr=fs)
print(mfccs.shape)
librosa.display.specshow(mfccs, sr=fs, x_axis='time')

plt.imshow(mfccs.T, cmap='gray', origin='lower', aspect='auto', interpolation='nearest', norm=NoNorm())
plt.ylabel('MFCC Coefficient Index')
plt.xlabel('Frame Index')
plt.show()