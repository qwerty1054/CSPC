"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read titration.csv (columns volume_base, pH) into arrays V, pH.
data=np.loadtxt('titration.csv', delimiter=',', skiprows=1)
V=data[:,0]
pH=data[:,1]
# TODO 2: compute the slope of the pH curve with np.gradient(pH, V), and find
#         the volume where that slope is largest (np.argmax). That is the
#         equivalence point. Print it.
slope=np.gradient(pH, V)
equivalence_index=np.argmax(slope)
equivalence_volume=V[equivalence_index]
print(f"equivalence point volume: {equivalence_volume:.6f} ml")
# TODO 3: make two plots side by side: (left) pH vs volume with a line at the
#         equivalence point; (right) the slope vs volume, showing it peaks
#         at the equivalence point. Save as titration.png.
plt.figure(figsize=(12, 5))
# TODO 3: make two plots side by side and save as titration.png
plt.subplot(1, 2, 1)
plt.plot(V, pH, 'b')
plt.axvline(equivalence_volume, color='gray', linestyle='--')
plt.xlabel("Volume (mL)")
plt.ylabel("pH")

plt.subplot(1, 2, 2)
plt.plot(V, slope, 'r')
plt.axvline(equivalence_volume, color='gray', linestyle='--')
plt.xlabel("Volume (mL)")
plt.ylabel("dpH/dV")

plt.tight_layout()
plt.savefig("titration.png")
plt.show()