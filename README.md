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

For both options, there should now be a subfolder in `my_animation_project` called `matnimation` that contains (a version of) its source code. Let `animation.py` be the file in which you build the animation. The structure of your project then looks like:

```
my_animation_project
└── matnination/
└── animation.py
```



# Examples
Examples are given in the folder `examples`. They are also listed in [this](./examples/examples.md) overview. 
