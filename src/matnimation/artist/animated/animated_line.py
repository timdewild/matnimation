from matplotlib.axes import Axes
from matplotlib.lines import Line2D
import numpy as np
from src.matnimation.artist.animated.animated_artist import AnimatedArtist

class AnimatedLine(AnimatedArtist):

    def __init__(self, name: str, x_data: np.ndarray, y_data: np.ndarray, vis_interval: list[int] = None):
        """
        Initialize an Animated Line.

        Parameters
        ----------
        name : str
            Name of the animated line
        x_data : np.ndarray
            x values of line (1D if they dont change over time, 2D if they do)
        y_data : np.ndarray
            y values of line (rows) for all timesteps (cols)
        vis_interval : list[int], optional
            List with time indices at which visibility must be turned ON and OFF
        """

        super().__init__(name, vis_interval)
        self.x_data = x_data
        self.y_data = y_data

        self.artist: Line2D = Line2D([], [], zorder=self.zorder, label=self.name)
        self.legend_handle = self.artist

    def update_timestep(self, time_index):
        """
        Update the line data at a specific timestep in the animation.

        Parameters
        ----------
        time_index : int
            Current time index
        """

        self.update_visibility(time_index)

        if self.x_data.ndim == 1:
            self.artist.set_data(self.x_data, self.y_data[:, time_index])

        if self.x_data.ndim == 2:
            self.artist.set_data(self.x_data[:, time_index], self.y_data[:, time_index])
