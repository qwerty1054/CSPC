"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
#         It equals zero exactly at equilibrium.
def k_imbalance(x):
    return (2*x)**2 / ((a-x)*(b-x)) - K
# TODO 2 (method 1): use scipy.optimize.newton to find the root of k_imbalance
#         (start x0=0.5). This is root-finding.
x_newton = newton(k_imbalance, x0=0.5)
# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
#         (method "SLSQP", bounds [(0, 0.999)], x0=[0.5]). Print both answers
#         and confirm they agree.
result = minimize(lambda x: k_imbalance(x[0])**2, x0=[0.5], method="SLSQP", bounds=[(0, 0.999)])
x_minimize = result.x[0]
print(f"x (Newton): {x_newton:.6f}")
print(f"x (SLSQP): {x_minimize:.6f}")
# TODO 4: report the equilibrium amounts (H2, I2, HI), and plot how the three
#         amounts change with the extent x, marking the equilibrium. Save
#         equilibrium.png.
nH2_eq = a- x_newton
nI2_eq = b-x_newton
nHI_eq = 2*x_newton
print(f"equilibrium values: H2 = {nH2_eq:.6f}, I2 = {nI2_eq:.6f}, HI = {nHI_eq:.6f}")

plot_x = np.linspace(0, 0.99, 200)
plt.plot(plot_x, a - plot_x, label="H2")
plt.plot(plot_x, b - plot_x, label="I2")
plt.plot(plot_x, 2 * plot_x, label="HI")
plt.axvline(x=x_newton, color='gray', linestyle=':', label=f"Equilibrium (x ≈ {x_newton:.2f})")

plt.xlabel("reaction Extent (x)")
plt.ylabel("Amount (mol)")
plt.legend()
plt.savefig("equilibrium.png")
plt.show()