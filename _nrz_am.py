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
