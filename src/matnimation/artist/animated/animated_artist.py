from abc import ABC
from src.matnimation.artist.base_artist import BaseArtist


class AnimatedArtist(BaseArtist, ABC):
    """Animated Artist (line, circle, arrow etc) to be placed on a specific axis of a defined canvas."""

    def __init__(self, name: str, vis_interval: list[int] = None):
        """
        Initialize an Animated Artist.

        Parameters
        ----------
        name : str
            Name of the animated artist
        vis_interval : list[int], optional
            List with time indices at which visibility must be turned ON and OFF. 
            If vis_interval = [1, 10], visibility will be turned ON at time index 1 and turned OFF at time index 10.
        """
        super().__init__(name)

        # Set z order of animated artist
        self.zorder = 3

        self.vis_interval = vis_interval  

    def set_styling_properties(self, **styling):
        """
        Set styling properties of the animated artist.

        Parameters
        ----------
        **styling
            Keyword arguments representing styling properties
        """
        return super().set_styling_properties(**styling)

    def update_visibility(self, time_index: int):
        """
        Update the visibility of the animated artist based on the current time index.

        Parameters
        ----------
        time_index : int
            Current time index
        """
        if self.vis_interval:
            ti_appear = self.vis_interval[0]
            ti_disappear = self.vis_interval[1]

            self.artist.set_visible(False)

            if time_index in range(ti_appear, ti_disappear + 1):
                self.artist.set_visible(True)


        




