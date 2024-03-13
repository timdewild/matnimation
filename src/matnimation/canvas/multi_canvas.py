import numpy as np
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from src.matnimation.artist.base_artist import BaseArtist
from src.matnimation.canvas.canvas import Canvas

class MultiCanvas(Canvas):
    """
    A canvas for creating multi-axis plots with a grid layout.
    This class extends the functionality of the base `Canvas` class and allows for creating a grid of subplots.
    """

    def __init__(
            self, 
            figsize: tuple, 
            dpi: int, 
            time_array: np.ndarray[float],
            nrows: int, 
            ncols: int, 
            axes_limits: list,          
            axes_labels: list,  
            shared_x=False,
            shared_y=False,
            height_ratios: list = None,
            width_ratios: list = None
            ):
        """
        Initialize a MultiCanvas instance.

        Parameters
        ----------
        figsize : tuple
            Figure size (width, height) in inches
        dpi : int
            Dots per inch, resolution of canvas
        time_array : np.ndarray
            Array representing time steps in animation
        nrows : int
            Number of rows in the grid of subplots
        ncols : int
            Number of columns in the grid of subplots
        axes_limits : list
            2D list with axes limits [[xmin, xmax, ymin, ymax], ...]
            Order of subplots in list is left-to-right then top-to-bottom. 
        axes_labels : list
            2D list with axes labels [['xlabel', 'ylabel'], ...]
            Order of subplots in list is left-to-right then top-to-bottom. 
        shared_x : bool, optional
            Whether x-axis of subplots is shared, by default False
        shared_y : bool, optional
            Whether y-axis of subplots is shared, by default False
        height_ratios : list, optional
            Ratio of heights of different subplots
        width_ratios : list, optional
            Ratio of widths of different subplots
        """
        super().__init__(figsize, dpi, time_array)

        self.nrows = nrows
        self.ncols = ncols
        self.axes_limits = axes_limits
        self.axes_labels = axes_labels
        self.shared_x = shared_x
        self.shared_y = shared_y
        self.height_ratios = height_ratios
        self.width_ratios = width_ratios

        if (self.nrows == 1) and (self.ncols == 1):
            raise ValueError('You specified a canvas with only one plot (ncols = nrows = 1), use SingleCanvas instead.')  
        
        self.fig, self.axs_array = plt.subplots(
            figsize=self.figsize,
            nrows=self.nrows, 
            ncols=self.ncols, 
            constrained_layout=True, 
            squeeze=False, 
            sharex=self.shared_x, 
            sharey=self.shared_y,
            height_ratios=self.height_ratios,
            width_ratios=self.width_ratios
            )
        
        self.set_layout(self.fig, self.axs_array, self.axes_limits, self.axes_labels)

        # 2D list (nrows, ncols) that contains sets for legend_handles for all subplots
        self.legend_handles_collection = [[set() for j in range(self.ncols)] for i in range(self.nrows)]

    def set_axis_properties(self, row: int, col: int, **axis_styling):
        """
        Set styling properties for a specific subplot.

        Parameters
        ----------
        row : int
            Row index of the subplot in the grid
        col : int
            Column index of the subplot in the grid
        **axis_styling : dict
            Keyword arguments for styling the subplot
        """

        ax = self.get_axis(row, col)
        ax.set(**axis_styling)

    def get_axis(self, row: int, col: int) -> Axes:
        """
        Get the Axes object corresponding to a specific subplot.

        Parameters
        ----------
        row : int
            Row index of the subplot in the grid
        col : int
            Column index of the subplot in the grid

        Returns
        -------
        ax : Axes
            Matplotlib Axes object corresponding to the specified subplot
        """
        
        ax = self.axs_array[row, col]
        return ax
    
    def add_artist(self, artist: BaseArtist, row: int, col: int, in_legend=False):
        """
        Add an artist to a specific subplot.

        Parameters
        ----------
        artist : BaseArtist
            Artist object to add
        row : int
            Row index of the subplot in the grid
        col : int
            Column index of the subplot in the grid
        in_legend : bool, optional
            Whether the artist should be included in the subplot's legend, by default False
        """

        axes = self.get_axis(row, col)
        artist.add_to_axes(axes)
        self._add_artist(artist)

        if in_legend:
            legend_handle = artist.get_legend_handle()
            self.legend_handles_collection[row][col].add(legend_handle)

    def construct_legend(self, row: int, col: int,  **legend_styling):
        """
        Construct a legend for a specific subplot, if legend handles are available.

        Parameters
        ----------
        row : int
            Row index of the subplot in the grid
        col : int
            Column index of the subplot in the grid
        **legend_styling : dict
            Keyword arguments for styling the legend
        """

        if self.legend_handles_collection[row][col]:
            legend_handles = self.legend_handles_collection[row][col]
            axes = self.get_axis(row, col)
            self.add_legend(axes, legend_handles, **legend_styling)
