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