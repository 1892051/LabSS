"""
Python code

Simulate a common emitter BJT amplifier that amplifies the input 8 times
Use an alternate signal as input
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Input signal
t = np.linspace(0, 1, 1000)
x = signal.sin(2 * np.pi * 5 * t)


# Simulate the circuit
b = [1, -1]
a = [1, -2, 1]
y = signal.lfilter(b, a, x)

# Plot the input and output
plt.figure(1)
plt.title('BJT Common Emitter Amplifier')
plt.plot(t, x, label='Input')
plt.plot(t, y, label='Output')
plt.xlabel('Time [s]')
plt.ylabel('Voltage [V]')
plt.legend()
plt.show()