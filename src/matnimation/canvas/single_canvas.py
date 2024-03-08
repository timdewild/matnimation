import numpy as np
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from src.matnimation.artist.base_artist import BaseArtist
from src.matnimation.canvas.canvas import Canvas

class SingleCanvas(Canvas):
    def __init__(self, figsize: tuple, dpi: int, time_array: np.ndarray[float], axis_limits: list, axis_labels: list):
        """
        Initialize a SingleCanvas instance.

        Parameters
        ----------
        figsize : tuple
            Figure size (width, height) in inches
        dpi : int
            Dots per inch, resolution of canvas
        time_array : np.ndarray
            Array representing time steps in animation
        axis_limits : list
            1D list with axis limits [xmin, xmax, ymin, ymax]
        axis_labels : list
            1D list with axis labels ['xlabel', 'ylabel']
        """
        super().__init__(figsize, dpi, time_array)
        self.axis_limits = [axis_limits]
        self.axis_labels = [axis_labels]

        self.fig, self.axs_array = plt.subplots(figsize=self.figsize, squeeze=False, constrained_layout=True)
        self.ax: Axes = self.axs_array[0, 0]

        self.set_layout(self.fig, self.axs_array, self.axis_limits, self.axis_labels)

        # set that will contains the Artists' legend handles
        self.legend_handles_collection = set([])

    def set_axis_properties(self, **axis_styling):
        """
        Set styling properties for the single canvas.

        Parameters
        ----------
        **axis_styling : dict
            Keyword arguments for styling the canvas
        """
        self.ax.set(**axis_styling)

    def get_axis(self) -> Axes:
        """
        Get the Axes object for the single canvas.

        Returns
        -------
        self.ax : Axes
            Matplotlib Axes object for the canvas
        """
        return self.ax
    
    def add_artist(self, artist: BaseArtist, in_legend=False):
        """
        Add an artist to the single canvas.

        Parameters
        ----------
        artist : BaseArtist
            Artist object to add
        in_legend : bool, optional
            Whether the artist should be included in the canvas's legend, by default False
        """
        axes = self.get_axis()
        artist.add_to_axes(axes)
        self._add_artist(artist)

        # if in_legend = True add legend handle to collection
        if in_legend:
            legend_handle = artist.get_legend_handle()
            self.legend_handles_collection.add(legend_handle)

    def construct_legend(self, **legend_styling):
        """
        Construct legend for the single canvas, if legend handles collection is not empty.

        Parameters
        ----------
        **legend_styling : dict
            Keyword arguments for styling the legend
        """
        # if collection of legend handles is not empty, construct legend
        if self.legend_handles_collection:
            axes = self.get_axis()
            legend_handles = self.legend_handles_collection
            self.add_legend(axes, legend_handles, **legend_styling)