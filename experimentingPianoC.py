from pylab import*
from scipy.io import wavfile
import matplotlib.pyplot as plt
import pandas as pd
import cmath

print("Hello World")
sampFreq, snd = wavfile.read('C:/Users/raro/Desktop/pianoc.wav')
print snd.shape
print snd.shape[0]
duration=float(snd.shape[0])/float(sampFreq)    #in secs
print(sampFreq, snd, duration)

max_val=max(snd)
min_val=min(snd)
summary_df=pd.DataFrame(snd)
print(summary_df.describe)

timeArray = arange(0, snd.shape[0], 1)
timeArray = timeArray/ float(sampFreq)
timeArray = timeArray * 1000  #scale to milliseconds

plt.plot(timeArray, snd, 'r-')
plt.ylabel('Amplitude')
plt.xlabel('Time (ms)')
plt.show()


p=fft(snd)
n=len(snd)

# One Implementation
# # Calculate the number of unique points
#
# NumUniquePts = ceil((n+1)/2);
# nUniquePts = int(ceil((n+1)/2.0))
#
#
# # FFT is symmetric, throw away second half
# p = p[0:nUniquePts]
#
# #  fourier transform of the tone returned by the fft function contains
# # both magnitude and phase information and is given in a complex
# # representation (i.e. returns complex numbers). By taking the absolute
# # value of the fourier transform we get the information about the magnitude
# # of the frequency components.
#
# p = abs(p)  #Calculate power(magnitude)
#
#
# #p = p / float(n) # scale by the number of points so that
#                  # the magnitude does not depend on the length
#                  # of the signal or on its sampling frequency
# p = p**2  # square it to get the power
#
# # multiply by two (see technical document for details)
# # odd nfft excludes Nyquist point
# if n % 2 > 0: # we've got odd number of points fft
#     p[1:len(p)] = p[1:len(p)] * 2
# else:
#     p[1:len(p) -1] = p[1:len(p) - 1] * 2 # we've got even number of points fft
#
# freqArray = arange(0, nUniquePts, 1.0) * (sampFreq / n);
# plt.plot(freqArray/1000, 10*log10(p), 'r.')
# plt.xlabel('Frequency (kHz)')
# plt.ylabel('Power (dB)')
# plt.show()


p_abs=abs(p)
p_phase=cmath.phase(p)