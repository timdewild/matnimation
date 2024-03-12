from matplotlib.lines import Line2D
from src.matnimation.artist.animated.animated_artist import AnimatedArtist
import numpy as np

class AnimatedSingleScatter(AnimatedArtist):

    def __init__(self, name: str, x_data: np.ndarray, y_data: np.ndarray, vis_interval: list[int] = None):
        """
        Initialize an Animated Single Scatter.

        Scatter is interpreted here as a matplotlib Line2D object with no line (linewidth = 0) but with specified markers (marker = '.') at all data points. 

        Parameters
        ----------
        name : str
            Name of the animated scatter
        x_data : np.ndarray
            Array with x coordinate of single scatter at all timesteps
        y_data : np.ndarray
            Array with y coordinate of single scatter at all timesteps
        vis_interval : list[int], optional
            List with time indices at which visibility must be turned ON and OFF, by default None
        """
        super().__init__(name, vis_interval)

        # check if x_data and y_data correspond to a single scatter point
        if x_data.ndim != 1 or y_data.ndim != 1:
            raise ValueError('Both x_data and y_data should be 1D arrays for a single scatter.')

        self.x_data = x_data
        self.y_data = y_data

        # Here scatter is a line with no linewidth and dots as markers at vertices
        self.artist: Line2D = Line2D([], [], linewidth=0, marker='.', markersize=10, label=self.name) 

        # Create handle for legend
        self.legend_handle = self.artist

    def set_styling_properties(self, **styling):
        """
        Set styling properties for the scatter.

        Only supports styling properties related to the marker.

        Parameters
        ----------
        **styling : dict
            Styling properties for the scatter
        """
        args_dict: dict = locals()
        styling_dict: dict = args_dict['styling']
        marker_stylings = ['marker', 'markerfacecolor', 'markeredgecolor', 'markeredgewidth', 'markersize']

        for styling_option in styling_dict.copy():
            if styling_option not in marker_stylings:
                styling_dict.pop(styling_option)
                print(
                    f"Keyword {styling_option} is discarded because it is not a valid keyword. Allowed keywords are 'marker', 'markerfacecolor', 'markeredgecolor', 'markeredgewidth', 'markersize'."
                    )

        self.artist.set(**styling_dict)
                
    def update_timestep(self, time_index: int):
        """
        Set coordinates of scatter at specific timestep in animation.

        Parameters
        ----------
        time_index : int
            Current time index
        """
        self.update_visibility(time_index)
        self.artist.set_data(self.x_data[time_index], self.y_data[time_index])
