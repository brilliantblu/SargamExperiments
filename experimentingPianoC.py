#from pylab import*
from pylab import arange
from scipy.io import wavfile
import matplotlib.pyplot as plt
import pandas as pd
import cmath
import numpy as np

print("Hello World")
# sampling frequency (or sample rate) is the number of samples per second in a Sound. For example: if the sampling frequency is 44100 hertz, a recording with a duration of 2 seconds will contain 88200 samples.
sampFreq, signal = wavfile.read('pianoc.wav')
print signal.shape
duration= float(signal.shape[0]) / float(sampFreq)    #in secs
print(sampFreq, signal, duration)

#Part 1: Display the signal
timeArray = arange(0, signal.shape[0], 1)
timeArray = timeArray/ float(sampFreq) * 1000  #scale to milliseconds

plt.plot(timeArray, signal, 'r-')
plt.ylabel('Amplitude')
plt.xlabel('Time (ms)')
plt.title("Signal: Piano C note")
plt.show()

p=np.fft.fft(signal)
n=len(signal)

#p=p[range(n/2)]
p_abs=abs(p)
p_phase=np.zeros(len(p))
for p_single in range(len(p)):
    p_phase[p_single]=cmath.phase(p[p_single])
print p_phase
print p_abs

n = len(signal) # length of the signal
k = np.arange(n)
T = n/sampFreq
frq = k/T # two sides frequency range
#frq = frq[range(n/2)] # one side frequency range


#Plot all the results
fig = plt.figure()

fig_1 = fig.add_subplot(311)
fig_1.plot(timeArray, signal, 'r-')
plt.ylabel('Amplitude')
plt.xlabel('Time')

fig_2 = fig.add_subplot(312)
fig_2.plot(frq, p_phase, 'r.')
plt.ylabel('Phase')
plt.xlabel('Freq(Hz)')


fig_3 = fig.add_subplot(313)
fig_3.plot(frq, p_abs, 'r.')
plt.ylabel('|Freq(Hz)|')
plt.xlabel('Freq(Hz)')

plt.title("Extracted a, p, f")

plt.show()

low_values=p_abs<0.1*max(p_abs)
new_p_abs = p_abs
new_p_abs[low_values]=0
new_p_phase=p_phase
new_p_phase[low_values]=0
new_p=p
new_p[low_values]=0+0j


#Plot all the results
fig = plt.figure()

fig_1 = fig.add_subplot(311)
fig_1.plot(timeArray, signal, 'r-')
plt.ylabel('Amplitude')
plt.xlabel('Time')

fig_2 = fig.add_subplot(312)
fig_2.plot(frq, new_p_phase, 'r.')
plt.ylabel('Phase')
plt.xlabel('Freq(Hz)')


fig_3 = fig.add_subplot(313)
fig_3.plot(frq, new_p_abs, 'r.')
plt.ylabel('|Freq(Hz)|')
plt.xlabel('Freq(Hz)')

plt.title("Modified a, p, f")

plt.show()

major_frq_indices=np.nonzero(new_p_abs)
print major_frq_indices

# eqns=[]
# for i in major_frq_indices:
#     eqns.append((p_phase[i], p_abs[i], i))   #Phase, Amplitude, Frequency

new_signal=np.fft.ifftshift(new_p)
plt.plot(timeArray, new_signal, 'r-')
plt.ylabel('Amplitude')
plt.xlabel('Time (ms)')
plt.title("New Signal: Piano C note")
plt.show()
