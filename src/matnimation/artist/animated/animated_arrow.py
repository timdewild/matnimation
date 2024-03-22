from matplotlib.axes import Axes
import numpy as np
from src.matnimation.artist.animated.animated_artist import AnimatedArtist
from matplotlib import patches


class AnimatedArrow(AnimatedArtist):

    def __init__(
            self, 
            name: str, 
            x_tail_data: np.ndarray, 
            y_tail_data: np.ndarray, 
            x_tip_data: np.ndarray,
            y_tip_data: np.ndarray,
            vis_interval: list[int] = None,
            width: float = 0.001,
            head_width: float = None,
            head_length: float = None,
            overhang: float = 0
            ):
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
        self.x_tail_data = x_tail_data
        self.y_tail_data = y_tail_data
        self.x_tip_data = x_tip_data
        self.y_tip_data = y_tip_data
        self.width = width
        self.head_width = head_width
        self.head_length = head_length
        self.overhang = overhang

        self.dx_data = self.x_tip_data - self.x_tail_data
        self.dy_data = self.y_tip_data - self.y_tail_data

        self.artist: patches.FancyArrow = patches.FancyArrow(
            x = 0,
            y = 0,
            dx = 0,
            dy = 0,
            width = self.width,
            length_includes_head = True,
            head_width = self.head_width,
            head_length = self.head_length,
            zorder=self.zorder
            )
        
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
        self.artist.set_data(
            x = self.x_tail_data[time_index],
            y = self.y_tail_data[time_index],
            dx = self.dx_data[time_index],
            dy = self.dy_data[time_index]
        )
