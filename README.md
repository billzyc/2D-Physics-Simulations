# 2D Physics Simulations

## set up

** If you are viewing this on a macbook retina display, please navigate to where python 3 is install, click the icon, choose get information and select launch in low resolution more. If this is not done, the simulation will run at a low fps

1) Install python3 at "https://www.python.org/downloads/"

2) In terminal or command prompt type in and enter python3 -m pip install -U pygame --user"

3) In terminal or command prompt type in "git clone https://github.com/billzyc/2D-Physics-Simulations.git"

**see set up and resource information below overview**


## Fluid (Smoothed-particle hydrodynamics) simulation

![fluid gif](https://github.com/billzyc/2D-Physics-Simulations/blob/master/assets/fluid-gif1.gif)

### overview
**work in progress**
Fluid simluation using Smoothed-particle hydrodynamics. 
Click on input boxes to adjust values such as number of particles, gravitational constant, k, etc.
Press restart to restart simulation *you will have to restart simulation to see certain values to take effect such as number of particles

## Electrostatics simulation

![electrostatics gif](https://github.com/billzyc/2D-Physics-Simulations/blob/master/assets/electrostatic-gif1.gif)
### overview
**work in progress**
Place charges and view the electrostatic force on any charge in the grid.
Click anywhere on the grid to place particle and enter value of charge.
Click again on particle to set as target charge and see the electric force on the target charge.

## Kinematics simulation

![kinematics gif](https://github.com/billzyc/2D-Physics-Simulations/blob/master/assets/kinematic-gif1.gif)

### overview
Projectile launch simulation, launch a projectile and view the projectile travel with it's arc.
Click anywhere in window to position a projectile and enter the velocity/angle it is launched at.

## Fluid (Smoothed-particle hydrodynamics) simulation

### set up
1) after cloning the repo enter "cd fluid-flow-simulation" in terminal or command prompt
2) enter "python3 main.py" or "python main.py"


Used resources below to for this project:
https://users.csc.calpoly.edu/~zwood/teaching/csc572/final15/awang/index.html
https://blog.altair.com/basics-of-the-smoothed-particle-hydrodynamics-method/
http://blog.brandonpelfrey.com/?p=303
https://www.cs.cornell.edu/~bindel/class/cs5220-f11/code/sph.pdf

## Electrostatics simulation

### set up
1) after cloning the repo enter "cd electrostatics-simulation" in terminal or command prompt
2) enter "python3 main.py" or "python main.py"

## Kinematics simulation

### set up
1) after cloning the repo enter "cd kinematics-simulation" in terminal or command prompt
2) enter "python3 main.py" or "python main.py"
