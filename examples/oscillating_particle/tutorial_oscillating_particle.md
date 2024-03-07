# Tutorial: Oscillating Particle Animation
In this tutorial, we show how to use `matnimation` to make a simple animation of a particle moving along an oscillating trajectory. This trajectory is given by the parametric equations:
```math
\begin{align*}
x(t) = t
y(t) = \sin t
\end{align*}
```
for $t\in [0,2\pi]$. We will go through the [code](/examples/oscillating_particle/oscillating_particle.py) for this animation step by step. 

## General Workflow
We start by describing the general workflow to make animations. The animations are build using three base classes/objects: 
1. `Canvas`: The canvas object should be thought of as the stage on which the animations take place. The canvas defines the figure with (possibly) multiple axes on which `Artist` objects live. 
2. `Artist`: Objects that live on the canvas. 