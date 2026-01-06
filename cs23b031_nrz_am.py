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
 
# Plots of message signal , carrier signal and amplitude 
plt.subplots(3, 1, figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(t, nrz_signal)
plt.xlabel('Time (s)')
plt.ylabel('NRZ Signal')
plt.title('NRZ Signal')
plt.grid(True)
plt.subplot(3, 1, 2)
plt.plot(t, carrier_signal)
plt.xlabel('Time (s)')
plt.ylabel('Carrier Signal')
plt.title('Carrier Signal')
plt.grid(True)
plt.subplot(3, 1, 3)
plt.plot(t, modulated_signal)
plt.xlabel('Time (s)')
plt.ylabel('Modulated Signal')
plt.title('Modulated Signal')
plt.grid(True)
plt.tight_layout()
plt.show()
