import numpy as np
from src.matnimation.artist.animated.animated_artist import AnimatedArtist
from matplotlib import patches


class AnimatedEllipse(AnimatedArtist):

    def __init__(
            self, 
            name: str, 
            width: float,
            height: float,
            x_data: np.ndarray, 
            y_data: np.ndarray, 
            vis_interval: list[int] = None, 
            width_data: np.ndarray = None, 
            height_data: np.ndarray = None
            ):
        """
        Initialize an Animated Ellipse.

        Parameters
        ----------
        name : str
            Name of the animated ellipse
        width : float
            Width of the ellipse
        height : float
            Height of the ellipse
        x_data : np.ndarray
            Array of x-values representing the center for all timesteps
        y_data : np.ndarray
            Array of y-values representing the center for all timesteps
        vis_interval : list[int], optional
            List with time indices at which visibility must be turned ON and OFF.
        width_data : np.ndarray, optional
            Array of ellipse-width at each timestep (default is None)
        height_data : np.ndarray, optional
            Array of ellipse-height at each timestep (default is None)
        """

        super().__init__(name, vis_interval)
        self.width = width
        self.height = height
        self.x_data = x_data
        self.y_data = y_data
        self.width_data = width_data
        self.height_data = height_data

        self.artist: patches.Ellipse = patches.Ellipse((0, 0), width=self.width, height=self.width)
        self.legend_handle = self.artist

    def update_timestep(self, time_index):
        """
        Update the properties of the ellipse at a specific timestep in the animation.

        Parameters
        ----------
        time_index : int
            Current time index
        """

        self.update_visibility(time_index)

        xy_data = (self.x_data[time_index], self.y_data[time_index])
        self.artist.set_center(xy_data)

        if self.width_data is not None:
            width = self.width_data[time_index]
            self.artist.set_width(width)
        
        if self.height_data is not None:
            height = self.height_data[time_index]
            self.artist.set_height(height)
