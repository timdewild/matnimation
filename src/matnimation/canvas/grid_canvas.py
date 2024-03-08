import numpy as np
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from src.matnimation.artist.base_artist import BaseArtist
from src.matnimation.canvas.canvas import Canvas

class GridCanvas(Canvas):
    def __init__(
            self, 
            figsize: tuple, 
            dpi: int, 
            time_array: np.ndarray[float],
            nrows: int,
            ncols: int,
            spans: list[list],
            axes_keys: list[str],
            axes_limits: list,          
            axes_labels: list, 
            width_ratios=None, 
            height_ratios=None,
            ):
        """
        Initialize a GridCanvas instance.

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
        spans : list[list]
            List indicating the span of each subplot
            Each sublist [span_row, span_col] defines the span of a subplot, span_row and span_col can be either an int or list of length 2. 

            Example: 
            Suppose that nrows = 2, ncols = 2 and spans = [[0, [0,1]], [1,0], [1,1]]
            Here the first subplot spans the entire first row, the second spans row 1, col 0 and the third spans row 1, col 1. 
        axes_keys : list[str]
            List of keys identifying each subplot, order of subplots is the same as in spans. Lenght must be equal to spans as well.
        axes_limits : list
            2D list with axes limits [[xmin, xmax, ymin, ymax], ...], order of subplots is the same as in spans. Lenght must be equal to spans as well.
        axes_labels : list
            2D list with axes labels [['xlabel', 'ylabel'], ...], order of subplots is the same as in spans. Lenght must be equal to spans as well.
        width_ratios : list, optional
            Width ratios of subplots, by default None
        height_ratios : list, optional
            Height ratios of subplots, by default None
        """
        super().__init__(figsize, dpi, time_array)

        self.nrows = nrows
        self.ncols = ncols
        self.spans = spans                          
        self.axes_limits = axes_limits
        self.axes_labels = axes_labels
        self.width_ratios = width_ratios
        self.height_ratios = height_ratios

        self.fig = plt.figure(figsize=self.figsize, constrained_layout=True, animated=False)

        self.grid = plt.GridSpec(
            self.nrows, 
            self.ncols, 
            figure=self.fig, 
            height_ratios=self.height_ratios,
            width_ratios=self.width_ratios
            )
        
        self.axs_array = np.empty(len(self.spans), dtype=Axes)

        for i, span in enumerate(self.spans):
            span_row, span_col = span[0], span[1]

            if isinstance(span_row, list):
                span_row = slice(span_row[0], span_row[1] + 1)

            if isinstance(span_col, list):
                span_col = slice(span_col[0], span_col[1] + 1)

            ax = self.fig.add_subplot(self.grid[span_row, span_col])
            ax.set_animated(False)
            self.axs_array[i] = ax

        self.axs_dict = dict(zip(self.axes_keys, self.axs_array))

        self.set_layout(self.fig, self.axs_array, self.axes_limits, self.axes_labels)
        
        self.legend_handles_collection = {axis_key: set() for axis_key in self.axes_keys}

    def get_axis(self, axes_key: str):
        """
        Get the Axes object corresponding to a specific subplot.

        Parameters
        ----------
        axes_key : str
            Key representing the desired subplot

        Returns
        -------
        ax : Axes
            Matplotlib Axes object corresponding to the specified subplot
        """
        ax = self.axs_dict[axes_key]
        return ax

    def set_axis_properties(self, axes_key: str, **axis_styling):
        """
        Set styling properties for a specific subplot.

        Parameters
        ----------
        axes_key : str
            Key representing the desired subplot
        **axis_styling : dict
            Keyword arguments for styling the subplot
        """
        ax = self.get_axis(axes_key)
        ax.set(**axis_styling)

    def add_artist(self, artist: BaseArtist, axes_key: str, in_legend=False):
        """
        Add an artist to a specific subplot.

        Parameters
        ----------
        artist : BaseArtist
            Artist object to add
        axes_key : str
            Key representing the desired subplot
        in_legend : bool, optional
            Whether the artist should be included in the subplot's legend, by default False
        """
        axes = self.get_axis(axes_key)
        artist.add_to_axes(axes)
        self._add_artist(artist)

        if in_legend:
            legend_handle = artist.get_legend_handle()
            self.legend_handles_collection[axes_key].add(legend_handle)

    def construct_legend(self, axes_key: str, **legend_styling):
        """
        Construct a legend for a specific subplot, if legend handles are available.

        Parameters
        ----------
        axes_key : str
            Key representing the desired subplot
        **legend_styling : dict
            Keyword arguments for styling the legend
        """
        if self.legend_handles_collection[axes_key]:
            legend_handles = self.legend_handles_collection[axes_key]
            axes = self.get_axis(axes_key)
            self.add_legend(axes, legend_handles, **legend_styling)