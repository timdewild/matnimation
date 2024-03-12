from matplotlib.axes import Axes
from matplotlib.image import AxesImage
import numpy as np
from src.matnimation.artist.static.static_artist import StaticArtist

class StaticImshow(StaticArtist):
    def __init__(self, name: str, image_data: np.ndarray, extent: list, cmap='viridis', vmin: float = None, vmax: float = None):
        """
        Initialize a StaticImshow object.

        Parameters
        ----------
        name : str
            Name of the static imshow
        image_data : np.ndarray
            2D numpy array containing function values f(x,y) on grid, format like np.meshgrid
        extent : list
            Extent over which image must be plotted in figure [xmin, xmax, ymin, ymax]
        cmap : str, optional
            Colormap style to be used, by default 'viridis'
        vmin : float, optional
            Minimum value in data range covered by colormap, by default None
        vmax : float, optional
            Maximum value in data range covered by colormap, by default None
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
        """
        Add the imshow to the specified axes.

        Parameters
        ----------
        axes : Axes
            Axes object to add the imshow to
        """
        self.artist: AxesImage = axes.imshow(
            self.image_data, 
            origin='lower', 
            extent=self.extent, 
            vmin=self.vmin, 
            vmax=self.vmax, 
            cmap=self.cmap
            )
        
    def set_styling_properties(self, **styling):
        """
        Set styling properties for the imshow.

        Raises
        ------
        ValueError
            If the artist has not been added to an axes yet

        Parameters
        ----------
        **styling : dict
            Keyword arguments for styling the imshow
        """
        if self.artist is None:
            raise ValueError('For Imshows, the artist must first be added to an axes on the canvas before styling properties can be set.')

        self.artist.set(**styling)
