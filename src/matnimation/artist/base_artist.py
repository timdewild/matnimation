from abc import ABC, abstractmethod
from matplotlib.artist import Artist as Artist
from matplotlib.axes import Axes

class BaseArtist(ABC): 

    def __init__(self, name: str):
        """
        Initialize a BaseArtist object.

        Parameters
        ----------
        name : str
            Name of the artist
        """
        self.name = name
        self.artist: Artist = None
        self.legend_handle: Artist = None
        
    def set_styling_properties(self, **styling):
        """
        Set styling properties for the artist.

        Parameters
        ----------
        **styling : dict
            Keyword arguments for styling the artist
        """
        self.artist.set(**styling)

    def add_to_axes(self, axes: Axes):
        """
        Add the artist to a specific axes.

        Parameters
        ----------
        axes : Axes
            Axes object to add the artist to
        """
        axes.add_artist(self.artist)

    def get_legend_handle(self):
        """
        Get the legend handle for the artist.

        Returns
        -------
        Artist
            Legend handle for the artist
        """
        return self.legend_handle
    
    @abstractmethod
    def update_timestep(self, time_index: int):
        """
        Abstract method to update the artist for a specific time index.

        This method must be implemented by subclasses.

        Parameters
        ----------
        time_index : int
            Index representing the time step
        """
        pass