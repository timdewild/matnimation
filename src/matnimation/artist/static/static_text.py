from src.matnimation.artist.static.static_artist import StaticArtist
from matplotlib.text import Text

class StaticText(StaticArtist):

    def __init__(self, name: str, xy_center: tuple[float]):
        """
        Initialize a StaticText object.

        Parameters
        ----------
        name : str
            Name of the static text
        xy_center : tuple[float]
            Tuple containing (x, y) coordinates of text location
        """

        super().__init__(name)
        self.xy_center = xy_center

        self.x, self.y = self.xy_center

        self.artist = Text(
            x=self.x,
            y=self.y,
            text=self.name
        )


        
