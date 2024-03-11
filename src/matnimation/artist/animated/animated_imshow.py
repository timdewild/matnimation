from matplotlib.axes import Axes
from matplotlib.image import AxesImage
import numpy as np
from src.matnimation.artist.animated.animated_artist import AnimatedArtist



class AnimatedImshow(AnimatedArtist):
    def __init__(self, name: str, image_data: np.ndarray, extent: list, cmap = 'viridis', vmin: float = None, vmax: float = None, vis_interval: list[int] = None):    
        """
        Arguments:
        image_data      (list of 2D numpy arrays)    function values f(x,y) on grid for all timesteps len(image_data) = len(time_array)
 

        """            

        super().__init__(name, vis_interval)

        self.image_data = image_data
        self.extent = extent

        # color scheme, set to 'viridis' by default
        self.cmap = cmap

        # vmin and vmax are by default set to the min and maximum value in the first image of the animation
        self.vmin = self.image_data[0].min() 
        self.vmax = self.image_data[0].max()

        # they can be set explicitly by the user
        if vmin is not None and vmax is not None:
            self.vmin = vmin
            self.vmax = vmax

        self.artist: AxesImage = None
        self.legend_handle = None
    
    def add_to_axes(self, axes: Axes):
        self.artist: AxesImage = axes.imshow(
            self.image_data[0], 
            origin = 'lower', 
            extent = self.extent, 
            cmap = self.cmap,
            vmin = self.vmin, 
            vmax = self.vmax, 
            zorder = self.zorder
            )
                
    def set_styling_properties(self, **styling):
        if self.artist == None:
            ValueError('For Imshows, the artist must first be added to an axes on the canvas before styling properties can be set.')

        self.artist.set(**styling)

    def update_timestep(self, time_index: int):
        """Set imshow image_data at specific timestep in animation."""

        self.update_visibility(time_index)
        self.artist.set_data(self.image_data[time_index])                         