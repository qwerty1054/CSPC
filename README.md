# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.
## Setup
Create the environment for a given lab:
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc
---
## PW1 - Lab A: Reproducible Foundations
**What I built:**
- A radioactive decay simulation comparing pure python to numpy, with pytests, in a clean git repository structure with environment specifications
**Speed comparison (loop vs NumPy):**
- loop : 10.4739 s
- numpy : 0.0003 s
- speed-up: 38606.76x faster
**Tests:** all passing? yes
**Conclusion:**
- This pw demonstrates how runtime of python loops differs from vectorized numpy operations and why numpy is essential in scientific computing. i learned how to manage git commands via terminal, setting up environments, understood the importance of .gitignore and environment.yml files, learned structuring the project, making commits and pushing to github. Writing tests with pytest helped me make sure that code matches the actual physical decay law

## PW1 - Lab B: Data, Plotting, and Automation

**observations:** the dataset decay_observed.csv shows the number of measured particles decreasing over time during redioactive decay
**comparison:** observed scatter plot matches the theoretical curve very closely, so experimental dats fits the exponential deca law
**snakemake pipeline:** snakemake automates building figure.png from csv and script files, rerunning plot.py only when there are changes in input files

## PW2 - Lab A: Motion from Tracking Data

**acceleration noise:** while finding derivative of position to find acceleration we are dividing by small numbers which amplifies the error
**recovery by integration** we observe smooth curves, because while integration random positive and negative spikes cancel each other out

**mean acceleration:** -8.58 m/s^2
**noise:** 28.72 m/s^2
the noise in acceleration graph is high but the mean value still stays around -9.81 m/s^2

## PW2 - Lab B: Motion from Tracking Data

    **2A**
Gradient descent result for f: 2.9999963220107015
Newton's method result for f: 3.0
SLSQP result for f: 3.0
    **2B**
with x0=0
1. Gradient Descent: x =-1.300834  starting from x0=0.0
2. Newton's method: x=0.169938, d2g=-5.653451 starting from x0=0.0
3. SLSQP: x=-1.300857 starting from x0=0.0

with x0=2.0
1. Gradient Descent: x =1.130910  starting from x0=2.0
2. Newton's method: x=1.130901, d2g=9.347248 starting from x0=2.0
3. SLSQP: x=-1.300639 starting from x0=2.0

**3 methods compared:** 
in 2A we have a convex function with one global minimum, therefore newton and slsqp are the same, gradient is slightly off due to it being dependant on steps

in 2B the function is complex with multiple curves, therefore the methods dont always agree. 
different starting points give different results. newtons method found the nearest local minimums in each try, which were different.in algotithms with big steps like slsqp it can step out of the valley and "accidentally" find a global minimum like in our situation

the starting point determines which valley gradient decent enters, thats why it affects the results

**fitted rate constant:**0.261761
**titration equivalence point:**50.000000 ml

x (Newton): 0.663848
x (SLSQP): 0.663847
Equilibrium values: H2 = 0.336152, I2 = 0.336152, HI = 1.327695
