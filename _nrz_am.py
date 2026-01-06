#NRZ-coding
import numpy as np  
import matplotlib.pyplot as plt                                                        
data_sequence = [1, 0, 1, 0, 1, 1, 0]
bits_per_sample = 200
nrz_signal = []
for bit in data_sequence:
  if bit == 1:
    nrz_signal.extend([1] * bits_per_sample)
  else:
    nrz_signal.extend([-1] * bits_per_sample)
nrz_signal = np.array(nrz_signal)
plt.plot(nrz_signal)
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.show()

#Sinusoidal wave - 20 Hz
fc = 20 
fs = bits_per_sample 

T = len(nrz_signal) / fs
t = np.linspace(0,T, len(nrz_signal), endpoint=False)

carrier_signal = np.sin(2 * np.pi * fc * t)
plt.plot(carrier_signal)

#Amplitude Modulation 
modulated_signal = nrz_signal * carrier_signal
plt.plot(modulated_signal)
 
