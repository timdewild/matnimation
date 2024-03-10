from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from matplotlib.text import Text

fig, ax = plt.subplots(1,3)
fig.set_figheight(4)
fig.set_figwidth(12)
for axis in ax.flatten():
    axis.set_xlim(-1,1)
    axis.set_ylim(-1,1)
    axis.set_aspect = 'equal'





fig.savefig('src/matnimation/artist/animated/test.jpg')