from matplotlib.axes import Axes
from matplotlib.collections import LineCollection
import numpy as np
from src.matnimation.artist.static.static_artist import StaticArtist

class StaticHlines(StaticArtist):
    def __init__(self, name: str, y_data: np.ndarray, x_min: float, x_max: float):
        """
        Initialize a StaticHlines object.

        Parameters
        ----------
        name : str
            Name of the hlines object
        y_data : np.ndarray
            1D numpy array containing y values of hlines
        x_min : float
            x-value of start of hlines
        x_max : float
            x-value of end of hlines
        """
        super().__init__(name)

        self.y_data = y_data
        self.x_min = x_min
        self.x_max = x_max

        self.artist: LineCollection = None
        self.legend_handle = None

    def add_to_axes(self, axes: Axes):
        """
        Add the hlines to the specified axes.

        Parameters
        ----------
        axes : Axes
            Axes object to add the hlines to
        """
        self.artist: LineCollection = axes.hlines(self.y_data, self.x_min, self.x_max)

    def set_styling_properties(self, **styling):
        """
        Set styling properties for the hlines.

        Raises
        ------
        ValueError
            If the artist has not been added to an axes yet

        Parameters
        ----------
        **styling : dict
            Keyword arguments for styling the hlines
        """
        if self.artist is None:
            raise ValueError('For Hlines, the artist must first be added to an axes on the canvas before styling properties can be set.')

        self.artist.set(**styling)