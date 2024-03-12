from matplotlib.lines import Line2D
from src.matnimation.artist.animated.animated_artist import AnimatedArtist
import numpy as np

class AnimatedScatter(AnimatedArtist):

    def __init__(self, name: str, x_data: np.ndarray, y_data: np.ndarray, vis_interval: list[int] = None):
        """
        Initialize an Animated Scatter.

        Scatter is interpreted here as a matplotlib Line2D object with no line (linewidth = 0) but with specified markers (marker = '.') at all data points. 

        Parameters
        ----------
        name : str
            Name of the animated scatter
        x_data : np.ndarray
            1D array with x coodinations of scatter points (assuming x coordinates are time-INDEPENDENT)
            or 2D array wtih x coordinates (rows) of scatter points at all timesteps (cols)
        y_data : np.ndarray
            1D array with y coodinations of scatter points (assuming y coordinates are time-INDEPENDENT)
            or 2D array wtih y coordinates (rows) of scatter points at all timesteps (cols)
        vis_interval : list[int], optional
            List with time indices at which visibility must be turned ON and OFF, by default None
        """
        super().__init__(name, vis_interval)

        if x_data.ndim == 1 and y_data.ndim == 1:
            raise ValueError('x_data and y_data are both 1D arrays, corresponding to a static scatter plot (use StaticScatter instead) or a single animated scatter (use AnimatedSingleScatter instead).')

        self.x_data = x_data
        self.y_data = y_data

        # Here scatter is a line with no linewidth and dots as markers at vertices
        self.artist: Line2D = Line2D([], [], linewidth=0, marker='.', markersize=10, label=self.name) 
        self.legend_handle = self.artist
        
    def update_timestep(self, time_index: int):
        """
        Update the coordinates of scatters at specific timestep in animation.

        Parameters
        ----------
        time_index : int
            Current time index
        """
        self.update_visibility(time_index)

        if self.x_data.ndim == 1:
            # only y data of scatters changes over time
            self.artist.set_data(self.x_data, self.y_data[:, time_index])

        elif self.y_data.ndim == 1:
            # only x data of scatters changes over time
            self.artist.set_data(self.x_data[:, time_index], self.y_data)

        else:
            # both x and y data of scatters change over time
            self.artist.set_data(self.x_data[:, time_index], self.y_data[:, time_index])
