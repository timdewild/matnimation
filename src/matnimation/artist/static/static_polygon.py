from src.matnimation.artist.static.static_artist import StaticArtist
import numpy as np
from matplotlib import patches

class StaticPolygon(StaticArtist):
    def __init__(self, name: str, x_data: np.ndarray, y_data: np.ndarray):
        """
        Initialize a StaticPolygon object.

        Parameters
        ----------
        name : str
            Name of the static polygon
        x_data : np.ndarray
            1D numpy array containing x values of the polygon
        y_data : np.ndarray
            1D numpy array containing y values of the polygon
        """
        super().__init__(name)
        self.x_data = x_data
        self.y_data = y_data

        self.artist: patches.Polygon = patches.Polygon(np.column_stack([self.x_data, self.y_data]), zorder=self.zorder, closed=True, label=self.name)
        self.legend_handle = self.artist
