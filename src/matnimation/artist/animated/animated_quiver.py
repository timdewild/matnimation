from matplotlib.axes import Axes
from matplotlib.lines import Line2D
from matplotlib.quiver import Quiver
import numpy as np
from src.matnimation.artist.animated.animated_artist import AnimatedArtist

class AnimatedQuiver(AnimatedArtist):
    def __init__(self, name: str, x_data: np.ndarray, y_data: np.ndarray, Fx_data: np.ndarray, Fy_data: np.ndarray, scale: float = 1., scale_units: str = None, width: float = None, color='k', vis_interval: list[int] = None):
        """
        Initialize an Animated Quiver.

        Parameters
        ----------
        name : str
            Name of the animated quiver
        x_data : np.ndarray
            x coordinates of tails of vectors
        y_data : np.ndarray
            y coordinates of tails of vectors
        Fx_data : np.ndarray
            x-component of vectors (rows) at all timesteps (cols)
        Fy_data : np.ndarray
            y-component of vectors (rows) at all timesteps (cols)
        scale : float, optional
            Sets scale of vectors, by default 1.
        scale_units : str, optional
            Units of the scale, by default None
        width : float, optional
            Width of arrow shaft, by default None
        color : str or RGBA seq, optional
            Arrow color, by default 'k'
        vis_interval : list[int], optional
            List with time indices at which visibility must be turned ON and OFF, by default None
        """

        super().__init__(name, vis_interval)
        self.x_data = x_data
        self.y_data = y_data
        self.Fx_data = Fx_data
        self.Fy_data = Fy_data
        self.scale = scale
        self.scale_units = scale_units
        self.width = width
        self.color = color

        self.artist: Quiver = None
    
    def add_to_axes(self, axes: Axes):
        """
        Add the quiver to the given axes.

        Parameters
        ----------
        axes : Axes
            Axes object to which the quiver will be added
        """
        self.artist: Quiver = axes.quiver(self.x_data, self.y_data, np.zeros_like(self.x_data), np.zeros_like(self.y_data), scale=self.scale, zorder=self.zorder, scale_units=self.scale_units, width=self.width, color=self.color)
        self.legend_handle: Line2D = Line2D([], [], marker="$\u279B$", markersize=10, markerfacecolor=self.color, markeredgecolor=self.color, label=self.name, linewidth=0)
        
    def set_styling_properties(self, **styling):
        """
        Set styling properties for the quiver.

        Raises
        ------
        ValueError
            If the artist has not been added to an axes yet

        Parameters
        ----------
        **styling : dict
            Styling properties to be set
        """
        if self.artist is None:
            raise ValueError('For Quivers, the artist must first be added to an axes on the canvas before styling properties can be set.')
        self.artist.set(**styling)

    def update_timestep(self, time_index: int):
        """
        Update the quiver vector data at a specific timestep in the animation.

        Parameters
        ----------
        time_index : int
            Current time index
        """
        self.update_visibility(time_index)
        self.artist.set_UVC(self.Fx_data[:, time_index], self.Fy_data[:, time_index])
