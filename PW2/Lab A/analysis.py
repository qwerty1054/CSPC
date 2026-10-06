"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)
data=np.loadtxt('freefall.csv', delimiter=',', skiprows=1)
t=data[:,0]
y=data[:,1]
# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?
v=np.gradient(y, t) 
a=np.gradient(v, t)

mean_acceleration = np.mean(a)
noise = np.std(a)
print(f"mean acceleration: {mean_acceleration:.2f} m/s^2")
print(f"noise: {noise:.2f} m/s^2")
# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)
v_recovered = cumulative_trapezoid(a, t, initial=0) + v[0]
y_recovered = cumulative_trapezoid(v_recovered, t, initial=0) + y[0]
# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png
fig,(ax1,ax2,ax3)=plt.subplots(3,1,sharex=True,figsize=(8,10))

#position
ax1.plot(t,y,label='Measured Position')
ax1.plot(t,y_recovered,label='Recovered Position')
ax1.set_ylabel('Position (m)')
ax1.set_title('Position vs Time')

#velocity
ax2.plot(t,v,label='Measured Velocity')
ax2.plot(t,v_recovered,label='Recovered Velocity')
ax2.set_ylabel('Velocity (m/s)')
ax2.set_title('Velocity vs Time')

#acceleration
ax3.plot(t,a,label='Measured Acceleration')
ax3.axhline(y=-9.81, color='r', label='True Acceleration')
ax3.set_ylabel('Acceleration (m/s^2)')
ax3.set_title('Acceleration vs Time')
ax3.set_xlabel('Time (s)')

plt.tight_layout()
plt.savefig("motion.png", dpi=300)
plt.show()

#trajectory track

traj_data=np.loadtxt("trajectory.csv", delimiter=",", skiprows=1)
t_2d=traj_data[:, 0]
x_2d=traj_data[:, 1]
y_2d=traj_data[:, 2]

vx=np.gradient(x_2d, t_2d)
vy=np.gradient(y_2d, t_2d)
speed=np.sqrt(vx**2 + vy**2)

fig, (ax1, ax2)=plt.subplots(2, 1, figsize=(8, 8))

ax1.plot(x_2d, y_2d, label='Tracked Path')
ax1.set_xlabel('position X (m)')
ax1.set_ylabel('position Y (m)')
ax1.set_title('2D Trajectory')

ax2.plot(t_2d, speed, label='Speed')
ax2.set_xlabel('time (s)')
ax2.set_ylabel('speed (m/s)')
ax2.set_title('speed vs Time')

plt.tight_layout()
plt.savefig("trajectory_2d.png", dpi=300)
plt.show()



