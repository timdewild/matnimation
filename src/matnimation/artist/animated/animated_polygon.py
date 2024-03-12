from src.matnimation.artist.animated.animated_artist import AnimatedArtist
import numpy as np
from matplotlib import patches

class AnimatedPolygon(AnimatedArtist):

    def __init__(self, name: str, x_data: np.ndarray, y_data: np.ndarray, vis_interval: list[int] = None):
        """
        Initialize an Animated Polygon.

        Parameters
        ----------
        name : str
            Name of the animated polygon
        x_data : np.ndarray
            x values of polygon (rows) for all timesteps (cols)
        y_data : np.ndarray
            y values of polygon (rows) for all timesteps (cols)
        vis_interval : list[int], optional
            List with time indices at which visibility must be turned ON and OFF
        """

        super().__init__(name, vis_interval)
        self.x_data = x_data
        self.y_data = y_data

        self.artist: patches.Polygon = patches.Polygon(np.array([[0, 0], [1, 0], [1, 1], [0, 1]]), zorder=self.zorder, closed=True, label=self.name)
        self.legend_handle = self.artist

    def update_timestep(self, time_index):
        """
        Update the polygon coordinates at a specific timestep in the animation.

        Parameters
        ----------
        time_index : int
            Current time index
        """
        self.update_visibility(time_index)
        xy_data = np.column_stack([self.x_data[:, time_index], self.y_data[:, time_index]])
        self.artist.set_xy(xy_data)
