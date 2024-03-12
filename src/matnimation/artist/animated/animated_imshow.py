from matplotlib.axes import Axes
from matplotlib.image import AxesImage
import numpy as np
from src.matnimation.artist.animated.animated_artist import AnimatedArtist

class AnimatedImshow(AnimatedArtist):
    def __init__(
            self, 
            name: str, 
            image_data: np.ndarray, 
            extent: list, 
            cmap='viridis', 
            vmin: float = None, 
            vmax: float = None, 
            vis_interval: list[int] = None
            ):    
        """
        Initialize an AnimatedImshow object.

        Parameters
        ----------
        name : str
            Name of the animated imshow
        image_data : list of 2D numpy arrays
            Function values f(x,y) on grid for all timesteps. len(image_data) = len(time_array)
        extent : list
            Extent over which image must be plotted in figure [xmin, xmax, ymin, ymax]
        cmap : str, optional
            Colormap style to be used (default is 'viridis')
        vmin : float, optional
            Minimum value in data range covered by colormap (None by default)
            If None, value will be set the to minimum value in the image_data of the initial timestep
        vmax : float, optional
            Maximum value in data range covered by colormap (None by default)
            If None, value will be set the to minimum value in the image_data of the initial timestep
        vis_interval : list[int], optional
            List with time indices at which visibility must be turned ON and OFF

        """            

        super().__init__(name, vis_interval)

        self.image_data = image_data
        self.extent = extent
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
        """
        Add the artist to the specified axes.

        Parameters
        ----------
        axes : Axes
            Matplotlib axes object
        """
        self.artist: AxesImage = axes.imshow(
            self.image_data[0], 
            origin='lower', 
            extent=self.extent, 
            cmap=self.cmap,
            vmin=self.vmin, 
            vmax=self.vmax, 
            zorder=self.zorder
            )
                
    def set_styling_properties(self, **styling):
        """
        Set styling properties for the artist.

        Raises
        ------
        ValueError
            If the artist has not been added to an axes yet

        Parameters
        ----------
        **styling
            Keyword arguments for styling properties
        """
        if self.artist is None:
            raise ValueError('For Imshows, the artist must first be added to an axes on the canvas before styling properties can be set.')

        self.artist.set(**styling)

    def update_timestep(self, time_index: int):
        """
        Update the imshow data at a specific timestep in the animation.

        Parameters
        ----------
        time_index : int
            Current time index
        """
        self.update_visibility(time_index)
        self.artist.set_data(self.image_data[time_index])
