from src.matnimation.artist.static.static_artist import StaticArtist
from matplotlib.collections import LineCollection
from matplotlib.axes import Axes
import numpy as np

class StaticVlines(StaticArtist):
    def __init__(self, name: str, x_data: np.ndarray, y_min: float, y_max: float):    
        """
        Initialize a StaticVlines object.

        Parameters
        ----------
        name : str
            Name of the static vlines
        x_data : np.ndarray
            1D numpy array containing x values of vlines
        y_min : float
            y-value of start of vlines
        y_max : float
            y-value of end of vlines
        """            

        super().__init__(name)

        self.x_data = x_data
        self.y_min = y_min
        self.y_max = y_max

        self.artist: LineCollection = None
        self.legend_handle = None

    def add_to_axes(self, axes: Axes):
        """
        Add the static vlines to the specified axes.

        Parameters
        ----------
        axes : Axes
            The axes to which the vlines will be added
        """
        self.artist: LineCollection = axes.vlines(self.x_data, self.y_min, self.y_max)

    def set_styling_properties(self, **styling):
        """
        Set styling properties of the static vlines.

        Raises
        ------
        ValueError
            If the artist has not been added to an axes yet

        Parameters
        ----------
        **styling
            Keyword arguments representing styling properties
        """
        if self.artist is None:
            raise ValueError('For Vlines, the artist must first be added to an axes on the canvas before styling properties can be set.')

        self.artist.set(**styling)
