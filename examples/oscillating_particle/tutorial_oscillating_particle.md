# Tutorial: Oscillating Particle Animation
In this tutorial, we show how to use `matnimation` to make a simple animation of a particle moving along an oscillating trajectory. This trajectory is given by the parametric equations:
```math
\begin{align*}
x(t) &= t \\
y(t) &= \sin t
\end{align*}
```
for $t\in [0,2\pi]$. We will go through the [code](/examples/oscillating_particle/oscillating_particle.py) for this animation step by step. 

## General Workflow
We start by describing the general workflow to make animations. The animations are build using three base classes/objects: 
1. `Canvas`: The canvas object should be thought of as the stage on which the animations take place. The canvas defines the figure with (possibly) multiple axes on which `BaseArtist` objects live. 
2. `BaseArtist`: Artists that live on the canvas. Examples are a e.g. a line, circle, vector field or image, but also a textbox is considered an artist. Artists can be _static_ or _animated_, as implemented via the `StaticArtist` and `AnimatedArtist` subclasses. As the name suggests, static artists do not change during the animation. Animated artists change in some way or another during the animation. 

[!TIP]
> For example, a line can change its shape during the animation, just as the text string in a textbox can change over time. 

 