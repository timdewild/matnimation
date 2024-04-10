# Contents
We provide tutorials, with detailed steps on the `matnimation` workflow, and examples with source code. 

#### Tutorials
- [Oscillating Particle](#oscillating-particle)
- [Travelling Sine Wave](#travelling-sine-wave)

#### Examples
- [Travelling Waves](#travelling-waves)
- [Rotating Vectors](#rotating-vectors)
- [Lissajous Curves](#lissajous-curves)
- [Decaying 2D Gaussian](#decaying-2d-gaussian)

# Tutorials
## Oscillating Particle
Animation of a particle that moves along a trajectory using the `AnimatedSingleScatter` artist. The trajectory is given by:
```math
\begin{align}
x(t) &= t \\
y(t) &= \sin(t)
\end{align}
```
over the time interval $t\in [0,2\pi]$. Go to the [code](oscillating_particle/oscillating_particle.py) or [tutorial](oscillating_particle/tutorial_oscillating_particle.md). 

https://github.com/timdewild/matnimation/assets/93600756/d51b1a3f-6b0b-476b-8277-93d33d578183

# Travelling Sine Wave
Animation of a travelling sine wave using the `AnimatedLine` artist. The wave profile $y(x,t)$ is given by:
```math
\begin{equation}
    y(x,t) = \sin (kx-\omega t),
\end{equation}
```
where we take the wavenumber $k=2\pi$ and radial frequency $\omega = 4\pi$. Go to the [code](travelling_sine_wave/travelling_sine_wave.py) or the [tutorial](travelling_sine_wave/travelling_sine_wave_tutorial.py). 

https://github.com/timdewild/matnimation/assets/93600756/6388ec0b-f749-44fc-9153-2bec5a076cb2

# Examples
## Travelling Waves
Animation of travelling waves using the `AnimatedLine` artist, this is an extension of the [Travelling Sine Wave](#travelling-sine-wave) tutorial. The waves are of the form:
```math
\begin{equation}
\Psi(x,t) = A\sin(kx-\omega t),
\end{equation}
```
where $\omega$ is the angular frequency and $k$ is the wavenumber. Go to the [code](travelling_waves/travelling_waves.py). 

https://github.com/timdewild/matnimation/assets/93600756/3614890c-66ae-4fa0-8537-be5d13f5e111

## Rotating Vectors
Using the `AnimatedQuiver` artist, vector fields of the form:
```math
\begin{equation}
\vec{F}(x,y,t) = F_x(x,y,t)\hat{x} + F_y(x,y,t)\hat{y},
\end{equation}
```
can be animated on a grid. In this example, the considered vector field is:
```math
\begin{equation}
\vec{F}(x,y,t) = \cos(t)\hat{x} + \sin(t)\hat{y}.
\end{equation}
```
These are vectors with constant length rotating counterclockwise in the $(x,y)$ plane with period $T=2\pi$. 
Note that in this case the components ($F_{x,y}$) only depend on time and not on $x$ and $y$, but `AnimatedQuiver` does allow for this possibility. Go to the [code](rotating_vectors/rotating_vectors.py). 

https://github.com/timdewild/matnimation/assets/93600756/b691ea55-d7cb-4104-86cc-14cd340c227a

## Lissajous Curves
In this example, we use `MultiCanvas` to generate a canvas with a grid of 1 by 3 subplots, each showing a different Lissajous curve. These curves correspond to the parametric equations:
```math
\begin{align}
x(t) &= A\sin(at+\delta),\\
y(t) &= B\sin(bt),
\end{align}
```
where $t\in[0,2\pi]$. In the animated curves, we fix the overall amplitudes $A=B\equiv 1$ and vary only $a,b$ and $\delta$. We also illustrate the use of the animated artist `AnimatedText` to show the time value $t$ during the animation in the left subplot. Go to the [code](lissajous_figures/lissajous_figures.py). 

https://github.com/timdewild/matnimation/assets/93600756/79bf4e87-c909-4b6f-aec9-13f561e28727

## Decaying 2D Gaussian
In this example, we demonstrate the use of the artist `AnimatedImshow` and the `StaticColorBar`. `AnimatedImshow` is based on Matplotlib's `AxesImage`, and allows to animate a density or heat plot. The function we will plot is the (unnormalized) 2D Gaussian that decays over time:
```math
\begin{equation}
    \varphi(x,y,t) = e^{-r^2 - t/\tau},
\end{equation}
```
where $r^2\equiv x^2+y^2$. The decay constant $\tau$ determines how fast the Gaussian decays over time. Go to the [code](decaying_2D_gaussian/decaying_2D_gaussian.py). 

https://github.com/timdewild/matnimation/assets/93600756/8d384f76-f405-4b52-be01-5c69a3162e52





