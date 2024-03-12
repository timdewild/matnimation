from matplotlib.axes import Axes
from matplotlib.lines import Line2D
from matplotlib.quiver import Quiver
import numpy as np
from src.matnimation.artist.static.static_artist import StaticArtist

class StaticQuiver(StaticArtist):
    def __init__(
            self, 
            name: str, 
            x_data: np.ndarray, 
            y_data: np.ndarray, 
            Fx_data: np.ndarray, 
            Fy_data: np.ndarray, 
            scale: float = 1., 
            scale_units: str = None, 
            width: float = None, 
            color='k'
            ):    
        """
        Initialize a StaticQuiver object.

        Parameters
        ----------
        name : str
            Name of the static quiver
        x_data : np.ndarray
            1D numpy array containing x coordinates of tails of vectors
        y_data : np.ndarray
            1D numpy array containing y coordinates of tails of vectors
        Fx_data : np.ndarray
            1D numpy array containing x-component of vectors
        Fy_data : np.ndarray
            1D numpy array containing y-component of vectors
        scale : float, optional
            Sets scale of vectors, by default 1.
        scale_units : str, optional
            Scale units of the vectors, by default None
        width : float, optional
            Width of the arrow shaft, by default None
        color : str or RGBA seq, optional
            Arrow color, by default 'k'
        """            

        super().__init__(name)

        self.x_data = x_data
        self.y_data = y_data
        self.Fx_data = Fx_data
        self.Fy_data = Fy_data
        self.scale = scale
        self.scale_units = scale_units
        self.width = width
        self.color = color

        self.artist: Quiver = None
    
    def add_to_axes(self, axes: Axes):
        """
        Add the quiver to the given axes.

        Parameters
        ----------
        axes : Axes
            Axes object to which the quiver will be added
        """
        self.artist: Quiver = axes.quiver(self.x_data, self.y_data, self.Fx_data, self.Fy_data, scale=self.scale, zorder=self.zorder, scale_units=self.scale_units, width=self.width, color=self.color)
        self.legend_handle: Line2D = Line2D([], [], marker="$\u279B$", markersize=10, markerfacecolor=self.color, markeredgecolor=self.color, label=self.name, linewidth=0)

    def set_styling_properties(self, **styling):
        """
        Set styling properties of the quiver.

        Raises
        ------
        ValueError
            If the artist has not been added to an axes yet

        Parameters
        ----------
        **styling
            Styling properties to be set on the quiver
        """
        if self.artist is None:
            raise ValueError('For Quivers, the artist must first be added to (an axes on) the canvas before styling properties can be set.')

        self.artist.set(**styling)
