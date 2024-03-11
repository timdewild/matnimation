from matplotlib.axes import Axes
from matplotlib.image import AxesImage
import numpy as np
from src.matnimation.artist.static.static_artist import StaticArtist



class StaticImshow(StaticArtist):
    def __init__(self, name: str, image_data: np.ndarray, extent: list, cmap = 'viridis', vmin: float = None, vmax: float = None):    
        """
        Arguments:
        image_data      (2D numpy array)    function values f(x,y) on grid 
        extent          (list of length 4)  extent over which image must be plotted in figure [xmin, xmax, ymin, ymax]
        cmap            (str)               colormap to be used
        """            

        super().__init__(name)

        self.image_data = image_data
        self.extent = extent
        self.cmap = cmap

        # vmin and vmax are by default set to the min and maximum value in the first image of the animation
        self.vmin, _ = self.image_data.min()
        self.vmax, _ = self.image_data.max()

        # they can be set explicitly by the user
        if vmin is not None and vmax is not None:
            self.vmin = vmin
            self.vmax = vmax

        self.artist: AxesImage = None
        self.legend_handle = None
    
    def add_to_axes(self, axes: Axes):
        self.artist: AxesImage = axes.imshow(
            self.image_data, 
            origin = 'lower', 
            extent = self.extent, 
            vmin = self.vmin, 
            vmax = self.vmax, 
            cmap = self.cmap)
        #self.legend_handle: Line2D = Line2D([], [], marker="$\u279B$", markersize = 10, markerfacecolor = self.color, markeredgecolor = self.color, label = self.name, linewidth = 0)
        
    def set_styling_properties(self, **styling):
        if self.artist == None:
            ValueError('For Imshows, the artist must first be added to an axes on the canvas before styling properties can be set.')

        self.artist.set(**styling)

    # def update_timestep(self, time_index: int):
    #     """Set imshow image_data at specific timestep in animation."""

    #     self.update_visibility(time_index)
    #     self.artist.set_data(self.image_data[time_index])                         