# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, impulse, step, freqresp

# Transfer function coefficients
num = [13, 9]  # Numerator coefficients
den = [1, 5, 17, 11]  # Denominator coefficients

# Create the transfer function
sys_tf = TransferFunction(num, den)

# Impulse Response
t_impulse, resp_impulse = impulse(sys_tf)
plt.figure()
plt.plot(t_impulse, resp_impulse)
plt.title('Impulse Response')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# Step Response
t_step, resp_step = step(sys_tf)
plt.figure()
plt.plot(t_step, resp_step)
plt.title('Step Response')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# Pole-Zero Map
poles, zeros = sys_tf.poles, sys_tf.zeros
plt.figure()
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', label='Zeros')
plt.scatter(np.real(poles), np.imag(poles), marker='x', label='Poles')
plt.axhline(y=0, color='k', lw=0.5)
plt.axvline(x=0, color='k', lw=0.5)
plt.title('Pole-Zero Map')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.legend()
plt.grid()
plt.show()

# Bode Plot
w, H = freqresp(sys_tf)
magnitude = 20 * np.log10(abs(H))
phase = np.angle(H, deg=True)

plt.figure(figsize=(8, 6))
plt.subplot(211)
plt.semilogx(w, magnitude)
plt.title('Bode Plot')
plt.ylabel('Magnitude (dB)')
plt.grid(True, which='both', ls='-', lw=0.5)

plt.subplot(212)
plt.semilogx(w, phase)
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Phase (°)')
plt.grid(True, which='both', ls='-', lw=0.5)

plt.tight_layout()
plt.show()
