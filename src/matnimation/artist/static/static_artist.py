from src.matnimation.artist.base_artist import BaseArtist

class StaticArtist(BaseArtist):

    def __init__(self, name: str):
        """
        Initialize a StaticArtist object.

        Parameters
        ----------
        name : str
            Name of the static artist
        """
        super().__init__(name)

        # set z order
        self.zorder = 2

    def update_timestep(self, time_index: int):
        """
        Update the static artist for a specific time index.

        This method is intended to be overridden by subclasses if needed.

        Parameters
        ----------
        time_index : int
            Index representing the time step
        """
        pass