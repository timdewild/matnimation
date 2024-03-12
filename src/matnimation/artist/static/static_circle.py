from matplotlib import patches
from matplotlib.axes import Axes
from src.matnimation.artist.static.static_artist import StaticArtist

class StaticCircle(StaticArtist):

    def __init__(self, name: str, radius: float, xy_center: tuple[float]):
        """
        Initialize a StaticCircle object.

        Parameters
        ----------
        name : str
            Name of the static circle
        radius : float
            Radius of the circle
        xy_center : tuple[float]
            (x, y) coordinates of the center of the circle
        """
        super().__init__(name)
        self.radius = radius
        self.xy_center = xy_center

        self.artist = patches.Circle(xy_center, radius=self.radius, zorder=self.zorder, label=self.name)
        self.legend_handle = self.artist

    