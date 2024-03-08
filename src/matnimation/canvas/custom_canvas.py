from matplotlib import pyplot as plt
from matplotlib.axes import Axes
import numpy as np
from src.matnimation.artist.base_artist import BaseArtist
from src.matnimation.canvas.canvas import Canvas

class CustomCanvas(Canvas):
    def __init__(
            self, 
            figsize: tuple, 
            dpi: int, 
            time_array: np.ndarray[float],
            mosaic: list,
            axes_limits: list,          
            axes_labels: list, 
            shared_x=False,
            shared_y=False,
            width_ratios=None, 
            height_ratios=None,
            gridspec_kw=None
            ):
        """
        Initialize a CustomCanvas instance.

        Parameters
        ----------
        figsize : tuple
            Figure size (width, height) in inches
        dpi : int
            Dots per inch, resolution of canvas
        time_array : np.ndarray
            Array representing time steps in animation
        mosaic : list
            List specifying the layout of subplots, e.g., [['Axes 1', 'Axes 1'], ['Axes 2', 'Axes 3']]
            Here 'Axes 1' spans the entire first row, 'Axes 2' ('Axes 3') is on second row first (second) column 
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
        width_ratios : list, optional
            Width ratios of subplots, by default None
        height_ratios : list, optional
            Height ratios of subplots, by default None
        gridspec_kw : dict, optional
            Additional keyword arguments for specifying the layout, by default None
        """
        super().__init__(figsize, dpi, time_array)
        
        self.mosaic = mosaic
        self.axes_limits = axes_limits
        self.axes_labels = axes_labels

        self.shared_x = shared_x
        self.shared_y = shared_y
        self.width_ratios = width_ratios
        self.height_ratios = height_ratios
        self.gridspec_kw = gridspec_kw

        self.fig, self.axs_dict = plt.subplot_mosaic(
            self.mosaic, 
            width_ratios=self.width_ratios, 
            height_ratios=self.height_ratios,
            sharex=self.shared_x,
            sharey=self.shared_y,
            constrained_layout=True, 
            gridspec_kw=self.gridspec_kw
            )
        
        self.axs_array = np.array(list(self.axs_dict.values()))

        self.set_layout(self.fig, self.axs_array, self.axes_limits, self.axes_labels)

        self.axs_keys = self.axs_dict.keys()
        self.legend_handles_collection = {axis_key:set() for axis_key in self.axs_keys}

    def get_axis(self, axis_key: str) -> Axes:
        """
        Get the Axes object corresponding to a specific subplot.

        Parameters
        ----------
        axis_key : str
            Key representing the desired subplot/Axes

        Returns
        -------
        ax : Axes
            Matplotlib Axes object corresponding to the specified subplot
        """
        ax = self.axs_dict[axis_key]
        return ax 

    def set_axis_properties(self, axis_key: str, **axis_styling):
        """
        Set styling properties for a specific subplot.

        Parameters
        ----------
        axis_key : str
            Key representing the desired subplot/Axes
        **axis_styling : dict
            Keyword arguments for styling the subplot
        """
        ax = self.get_axis(axis_key)
        ax.set(**axis_styling)
    
    def add_artist(self, artist: BaseArtist, axes_key: str, in_legend=False):
        """
        Add an artist to a specific subplot/Axes.

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
            Key representing the desired subplot/Axes
        **legend_styling : dict
            Keyword arguments for styling the legend
        """
        if self.legend_handles_collection[axes_key]:
            legend_handles = self.legend_handles_collection[axes_key]
            axes = self.get_axis(axes_key)
            self.add_legend(axes, legend_handles, **legend_styling)
