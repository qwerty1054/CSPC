"""
PW1 Lab B -- read observed decay data and compare it to the analytical law.
Produce a 1x2 figure:  left = observed data,  right = analytical N0*exp(-lam*t),
with SHARED axes so the two shapes are directly comparable.

Complete the TODOs below. Run with:  python plot.py
"""

import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3     # decay constant, given

# TODO 1: read decay_observed.csv (columns: time, count; skip the header row)
#         and split it into two arrays: t and observed.

t, observed = np.loadtxt('decay_observed.csv', delimiter=',', skiprows=1, unpack=True)

# TODO 2: set N0 to the FIRST observed value, then build the analytical curve
#         analytical = N0 * exp(-LAMBDA * t)

N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

# TODO 3: make a 1x2 subplot with SHARED x and y axes.

fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(10, 5))

#         left panel : scatter of the observed data, titled "Observed data"
ax1.scatter(t, observed, color='blue', label='Observed Data', s=15)
ax1.set_title('Observed Data')
ax1.set_xlabel('Time (t)')
ax1.set_ylabel('Count (N)')
ax1.grid(True)
ax1.legend()
#         right panel: line plot of the analytical curve, titled "Analytical"
ax2.plot(t, analytical, color='red', label=r'$N_0 e^{-\lambda t}$')
ax2.set_title('Analytical')
ax2.set_xlabel('Time (t)')
ax2.grid(True)
ax2.legend()

plt.tight_layout()
#         label the axes.

# TODO 4: save the figure as figure.png
plt.savefig('figure.png', dpi=300)
plt.close()

print("figure.png generated successfully.")