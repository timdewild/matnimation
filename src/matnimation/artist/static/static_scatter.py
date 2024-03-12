from src.matnimation.artist.static.static_artist import StaticArtist
from matplotlib.lines import Line2D
import numpy as np

class StaticScatter(StaticArtist):
    def __init__(self, name: str, x_data: np.ndarray, y_data: np.ndarray):    
        """
        Initialize a StaticScatter object.

        Parameters
        ----------
        name : str
            Name of the static scatter
        x_data : np.ndarray
            1D numpy array containing x values of scatters
        y_data : np.ndarray
            1D numpy array containing y values of scatters
        """            

        super().__init__(name)

        self.x_data = x_data
        self.y_data = y_data

        self.artist: Line2D = Line2D(self.x_data, self.y_data, linewidth=0, marker='.', markersize=10, label=self.name) 
        self.legend_handle = self.artist

    




   