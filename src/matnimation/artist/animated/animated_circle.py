from matplotlib.axes import Axes
import numpy as np
from src.matnimation.artist.animated.animated_artist import AnimatedArtist
from matplotlib import patches


class AnimatedCircle(AnimatedArtist):

    def __init__(self, name: str, radius: float, x_data: np.ndarray, y_data: np.ndarray, vis_interval: list[int] = None):
        """
        Initialize an Animated Circle.

        Parameters
        ----------
        name : str
            Name of the animated circle
        radius : float
            Radius of the circle
        x_data : np.ndarray
            Array of x-values representing the center for all timesteps
        y_data : np.ndarray
            Array of y-values representing the center for all timesteps
        vis_interval : list[int], optional
            List with time indices at which visibility must be turned ON and OFF.
        """

        super().__init__(name, vis_interval)
        self.radius = radius
        self.x_data = x_data
        self.y_data = y_data

        self.artist: patches.Circle = patches.Circle((0, 0), radius=self.radius, zorder=self.zorder)
        self.legend_handle = self.artist

    def update_timestep(self, time_index):
        """
        Update the center coordinates of the circle at a specific timestep in the animation.

        Parameters
        ----------
        time_index : int
            Current time index
        """

        self.update_visibility(time_index)
        xy_data = (self.x_data[time_index], self.y_data[time_index])
        self.artist.set_center(xy_data)
