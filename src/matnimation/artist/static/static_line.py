from matplotlib.axes import Axes
from matplotlib.lines import Line2D
import numpy as np
from src.matnimation.artist.static.static_artist import StaticArtist

class StaticLine(StaticArtist):
    def __init__(self, name: str, x_data: np.ndarray, y_data: np.ndarray):
        """
        Initialize a StaticLine object.

        Parameters
        ----------
        name : str
            Name of the static line
        x_data : np.ndarray
            1D numpy array containing x values of the line
        y_data : np.ndarray
            1D numpy array containing y values of the line
        """
        super().__init__(name)

        self.x_data = x_data
        self.y_data = y_data

        self.artist: Line2D = Line2D(x_data, y_data, zorder=self.zorder, label=self.name)
        self.legend_handle = self.artist
