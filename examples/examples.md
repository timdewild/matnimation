
# Examples
- [Oscillating Particle](#oscillating-particle)
- [Travelling Waves](#travelling-waves)
- [Rotating Vectors](#rotating-vectors)
- [Lissajous Curves](#lissajous-curves)

> [!WARNING]
> In the examples animations shown below, links to the corresponding code files are given. For those links to work, explicitly open the `README.md` file. In preview mode on the start page of the repository, the links **do not work**.

## Oscillating Particle
Animation of a particle that moves along a trajectory using the `AnimatedSingleScatter` artist. The trajectory is given by:
```math
\begin{align}
x(t) &= t \\
y(t) &= \sin(t)
\end{align}
```
over the time interval $t\in [0,2\pi]$. Go to the [code](./examples/oscillating_particle/oscillating_particle.py) or [tutorial](examples/oscillating_particle/tutorial_oscillating_particle.md). 

https://github.com/timdewild/matnimation/assets/93600756/d51b1a3f-6b0b-476b-8277-93d33d578183

## Travelling Waves
Animation of travelling waves using the `AnimatedLine` artist. The waves are of the form:
```math
\begin{equation}
\Psi(x,t) = A\sin(kx-\omega t),
\end{equation}
```
where $\omega$ is the angular frequency and $k$ is the wavenumber. Go to the [code](examples/travelling_waves/travelling_waves.py). 

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
Note that in this case the components ($F_{x,y}$) only depend on time and not on $x$ and $y$, but `AnimatedQuiver` does allow for this possibility. Go to the [code](examples/rotating_vectors/rotating_vectors.py). 

https://github.com/timdewild/matnimation/assets/93600756/b691ea55-d7cb-4104-86cc-14cd340c227a

## Lissajous Curves
In this example, we use `MultiCanvas` to generate a canvas with a grid of 1 by 3 subplots, each showing a different Lissajous curve. These curves correspond to the parametric equations:
```math
\begin{aling}
x(t) &= A\sin(at+\delta),\\
y(t) &= B\sin(bt),
\end{align}
```
where $t\in[0,2\pi]$. In the animated curves, we fix the overall amplitudes $A=B\equiv 1$ and vary only $a,b$ and $\delta$. We also illustrate the use of the animated artist `AnimatedText` to show the time value $t$ during the animation in the left subplot. 