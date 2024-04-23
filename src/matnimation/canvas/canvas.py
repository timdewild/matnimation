from typing import Any
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import numpy as np
from src.matnimation.artist.base_artist import BaseArtist

class Canvas:
    def __init__(self, figsize: tuple, dpi: int, time_array: np.ndarray[float]):
        """
        Initialize Canvas.

        Parameters
        ----------
        figsize : tuple
            Figure size (width, height) in inches
        dpi : int
            Dots per inch, resolution of canvas
        time_array : np.ndarray
            Array representing time steps in animation
        """

        self.figsize = figsize
        self.dpi = dpi
        self.time_array = time_array

        # Define a set to contain all artists living on the canvas
        self.artists: set[BaseArtist] = set(())
        self.fig: Figure = None
        self.axs_array = np.ndarray[Axes]

    def update_frame(self, time_index: int):
        """
        Update the canvas for a given time index.

        Parameters
        ----------
        time_index : int
            Index representing time
        """

        for artist in self.artists:
            artist.update_timestep(time_index)

    def _add_artist(self, artist: BaseArtist):
        """
        Add an artist to the canvas.

        Parameters
        ----------
        artist : BaseArtist
            Artist object to add
        """

        self.artists.add(artist)

    def set_figure_properties(self, **figure_styling):
        """
        Set styling properties of the canvas figure.

        Parameters
        ----------
        **figure_styling : dict
            Styling keyword arguments for Matplotlib Figure object
        """

        self.fig.set(**figure_styling)

    def get_figure(self) -> Figure:
        """
        Get the canvas figure.

        Returns
        -------
        self.fig : Figure
            The canvas figure
        """

        return self.fig

    def save_canvas(self, filename: str):
        """
        Save the canvas figure to a file.

        Parameters
        ----------
        filename : str
            Name of the file to save as
        """

        fig = self.get_figure()
        fig.savefig(filename, dpi=self.dpi)

    def set_layout(self, fig: Figure, axs_array: np.ndarray[Axes], axes_limits: list[float], axes_labels: list[str]):
        """
        Set the layout of the canvas.

        Parameters
        ----------
        fig : Figure
            Matplotlib Figure object
        axs_array : np.ndarray
            Array of Axes objects
        axes_limits : list[float]
            List of axis limits in the form [[xmin, xmax, ymin, ymax], ...]
        axes_labels : list[str]
            List of axis labels in the form [[xlabel, ylabel], ...]

        Note
        ----
        In axes_limits and axes_labels, first sublist corresponds to first Axes object in axs_array.
        Order is left-right then top-bottom through possible subplots.
        """

        fig.set_dpi(self.dpi)

        ax: Axes
        for i, ax in enumerate(axs_array.flatten()):
            ax.axis(axes_limits[i])
            ax.set_xlabel(axes_labels[i][0])
            ax.set_ylabel(axes_labels[i][1])
            ax.grid(True, color=u'white', lw=1.5, zorder=0)
            ax.set_facecolor('#EEEEEE')

    def get_axs_array(self):
        """
        Get the array of Axes objects.

        Returns
        -------
        self.axs_array : np.ndarray
            Array of Axes objects
        """

        return self.axs_array

    def add_legend(self, axes: Axes, legend_handles: set, **legend_styling):
        """
        Add a legend to the canvas.

        Parameters
        ----------
        axes : Axes
            Matplotlib Axes object to add legend to
        legend_handles : set
            Set of legend handles
        **legend_styling : dict
            Keyword arguments for styling the legend, all kwargs ('Other Parameters') of Matplotlib's Axes.legend() may be passed here. 
        """

        axes.legend(handles=legend_handles, **legend_styling)