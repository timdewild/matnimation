# matnimation

A wrapper to quickly make Matplotlib animations. 

> [!WARNING]
> This README file is not complete yet, but will be updated soon! Take a sneak peak at the [examples](./examples/examples.md)!

# Installation
`matnimation` is not an official python package that can be installed locally. Instead, you have two options to use `matnimation` yourself. 

### Option 1: Cloning Repository
The first, and simplest way, is to clone its Github repository inside your project folder. Suppose your project folder is called `my_animation_project`, open your terminal and change directory to that folder. Then use:
```python
git clone git@github.com:timdewild/matnimation.git
``` 
for SSH-cloning using or 
```python
git clone https://github.com/timdewild/matnimation.git
```
for https-cloning. In case new features are added to `matnimation` and you want to use them, you have to clone again. 

### Option 2: Git Submodules
A more versatile way of using `matnimation` in your animation project is to add it as a submodule to your project's repository. For this to work your folder `my_animation_project` must be a git repository. To add `matnimation` as a submodule, use the command:
```python
git add submodule https://github.com/timdewild/matnimation.git
```
This will only stage the submodule, you still need to commit the submodule:
```python
git commit -m "Added the submodule to the project."
git push
```
A submodule always refers to a specific commit, so if you commit changes to `matnimation`, those are not automatically implemented in the submodule. To update the submodule to refer to the newest commit, you run:
```python
git submodule update
```
For more details on git submodules, see the [documentation](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

### Importing the Modules
For both options, there should now be a subfolder in `my_animation_project` called `matnimation` that contains (a version of) its source code. Let `animation.py` be the file in which you build the animation. The structure of your project then looks like:
```
my_animation_project
└── matnination
└── animation.py
```
Now, we wish to import the modules in `matnimation` in our `animation.py` file. To do so, we have to tell python were to look for these modules: inside the `matnimation` folder. We do this by adding the path to the `matnimation` folder at the top of the file:

```python
# file: animation.py

import sys
import os

sys.path.append(os.path.abspath('matnimation'))
```

This is the simplest setup, if your project contains multiple subfolders with `.py` files that import `matnimation`, the correct paths should be included in each of these files. For an example on how this works, see e.g. [this](https://github.com/timdewild/fourier-series-epicycles) repo. 

# Methodology and Usage
Before we give a detailed example of how you can use `matnimation` to easily make Matplotlib animations, we will first give an overview of its working principle and main building principle. After that, we will give an example and explicitly compare `matnimation`'s to how the same animation would be constructed in the conventional way (as described in Matplotlib's [documentation](https://matplotlib.org/stable/users/explain/animations/animations.html)).

## Three Building Blocks: Canvas, Artists and Animation
The working principle of `matnimation` revolves around three fundamental objects/classes:
* `Canvas`

    The canvas object should be thought of as the stage on which the animations take place. The canvas defines the figure with (possibly multiple) axes on which `BaseArtist` objects live. 

    > **Note** The `Canvas` class has multiple subclasses such as `SingleCanvas` for a single pair of axes or `MultiCanvas` for multiple pairs of axes.   

* `BaseArtist`

    An artist that lives on the canvas. Examples are e.g. a line, circle, vector field or image, but also a textbox is considered an artist. Artists can be _static_ or _animated_, as implemented via the `StaticArtist` and `AnimatedArtist` subclasses. As the name suggests, static artists do not change during the animation. Animated artists change in some way or another during the animation. 

    > **Example** A line can change its shape during the animation, just as the text string in a textbox can change over time. 

* `Animation`

    The canvas and (collection of) artists are rendered into an actual animation (video) using the `Animation` class. This class runs Matplotlib's `animation.FuncAnimation` under it's hood ([docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation)). 
























# Examples
Examples are given in the folder `examples`. They are also listed in [this](./examples/examples.md) overview. 
