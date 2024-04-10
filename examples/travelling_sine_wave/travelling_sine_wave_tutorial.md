# Tutorial: Travelling Sine Wave
In this example, we animate a travelling sine wave, described by:
```math
\begin{equation}
    y(x,t) = \sin (kx-\omega t),
\end{equation}
```
where we take the wavenumber $k=2\pi$ and radial frequency $\omega = 4\pi$.

> [!NOTE]
> Before going through this tutorial, we advise you to go through the [oscillating particle](/examples/oscillating_particle/tutorial_oscillating_particle.md) tutorial first. 

https://github.com/timdewild/matnimation/assets/93600756/6388ec0b-f749-44fc-9153-2bec5a076cb2 

### Step 0: Import Dependencies
We start by importing all the dependencies.
```python
import numpy as np
import sys
import os

# to be able to find ~/matnimation directory
sys.path.append(os.path.abspath('matnimation'))

from matnimation.src.matnimation.animation.animation import Animation
from matnimation.src.matnimation.canvas.single_canvas import SingleCanvas
from matnimation.src.matnimation.artist.animated.animated_line import AnimatedLine
from matnimation.src.matnimation.helper.helper_functions import HelperFunctions
```

### Step 1: Generating Data
We have to set the spatial and temporal boundaries of our animation, we take $x\in[0,4]$ and $t\in[0,1]$. Those intervals are descretized by the arrays:
```python
N, M = 1000, 100
x_array = np.linspace(0,4,M)
t_array = np.linspace(0,1,N)
```
The animation should be thought of as a collection of frames, one for each time value in `t_array`, meaning we have a total of 100 frames in this animation. Then we define a function that describes the travelling sine wave:
```python
def wave(x,t):
    """Returns the traveling waveform y(x,t) = sin(kx - wt) with k = 2pi and w = 4pi."""

    y = np.sin(2 * np.pi * (x - 2*t)) 

    return y
```
We will animate the travelling sine wave using the `AnimatedLine` artist, which requires the $y$ coordinates of the line at all timesteps in the animation. That is, we have to find the waveform $y(x,t)$ for all $x$ in `x_array` at all timesteps $t$ in `t_array`. The data must be passed into `AnimatedLine` as a 2D numpy array of shape `(M, N)`, which we will call `ydata` and schematically looks like this:
```math
\begin{equation}
    \textsf{ydata}=\left( 
    \left[\begin{array}{c}
    y(x_1, t_1)\\
    \vdots \\
    y(x_M, t_1)
    \end{array}\right]
    \begin{array}{c}
    \\
    \cdots\\
    \end{array}
    \left[\begin{array}{c}
    y(x_1, t_N) \\
    \vdots \\
    y(x_M, t_N)
    \end{array}\right]
    \right)
\end{equation}
```
This means that `ydata[:,i]` gives the full wavefrom at the $i$-th timestep:
```math
[y(x_1,t_i), \dots, y(x_M,t_i)]. 
```
We use `func_ab_to_grid` from the `HelperFunctions` class to generate the `ydata`.
```python
ydata = HelperFunctions.func_ab_to_grid(
    func = wave,
    a = x_array,
    b = t_array
    )
```

> [!NOTE]
> Given a mathematical function of two parameters $f(a,b)$ called `func(a,b)` and two arrays `a_array` and `b_array`, `func_ab_to_grid` returns a 2D array with entry `[i,j]` corresponding to `func(a_array[i], b_array[j])`.

### Step 2: Define Canvas
Next, we constuct a canvas on which the artists, to be constructed in the next step, live. We make a simple animation with only a single panel, so we use `SingleCanvas`. We set the `figsize` in inches, the resolution `dpi` in dots-per-inch, the `time_array`, the `axis_limits` and the `axis_labels`. Simple mathmetical expressions are passed into the labels via the double dollar syntax `$$`. 

```python
canvas = SingleCanvas(
    figsize = (4,4),
    dpi = 400,
    time_array = t_array,
    axis_limits = [0, 4, -2, 2],
    axis_labels = ['$x$', '$y(x,t)$']
)
```

> [!IMPORTANT]
> The canvas should be thought of as the stage on which animated (and static) objects live over time. Therefore, it takes the `time_array` as argument. The dynamic behavior of all animated artists should be defined for all timesteps in `t_array`. 

### Step 3: Construct Artists
Now we are in the position to construct the artists. In our example we only have one artist, the `AnimatedLine` representing the travelling wave. 

```python
travelling_wave = AnimatedLine(
    name = 'Travelling Wave',
    x_data = x_array,
    y_data = ydata,
)
```

We provide a `name`, the `x_data` which is simply `x_array` and pass the waveform at all timesteps via `ydata`. In this case, only the $y$ coordinates of the animated line change over time and the $x$ coordinates are fixed. This need not be the case, if the latter also change you can pass a 2D array to `x_data` of the same format as `ydata`. Now we add `travelling_wave` to the canvas via:

```python
canvas.add_artist(travelling_wave)
```

In this example we only added one artist to the canvas, but note that in this way you can systematically add as many artists to the canvas as you like. 

### Step 4: Construct and Render Animation
Lastly, we construct an `Animation` object which takes the `canvas` as input, in addition to the `interval` keyword which specifies the time interval between succesive frames in milliseconds (ms). The default is set to 30 ms. We render the animation via the `render` method, which takes the filename (or filepath) as input. The final animation will have a duration of `N * interval` milliseconds. In our case, we have `N=100` timesteps or frames and take the interval to be 20 ms, so that our final animation is 2 seconds. 

```python
animation = Animation(canvas, interval = 20)
animation.render('sine_wave_using_matnimation.mp4')
```