from typing import Union
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.cm import ScalarMappable
from matplotlib.colorbar import Colorbar
from src.matnimation.artist.static.static_artist import StaticArtist
from src.matnimation.artist.static.static_imshow import StaticImshow
from src.matnimation.artist.animated.animated_imshow import AnimatedImshow



class StaticColorBar(StaticArtist):

    def __init__(self, name: str, imshow: Union[StaticImshow, AnimatedImshow], styling_dict: dict = None):       #boundaries: list[float, float] = None
        """
        StaticColorBar corresponding to Artist, which can be either a StaticImshow or a AnimatedImshow

        Arguments:
        name            (str)  radius of circle
        imshow          (Artist) 
        styling_dict    (dict) sytling dictionary, all 'Other Parameters' of matplotlib.figure.Figure.colorbar can be passed here.  
        """

        super().__init__(name)
        self.imshow = imshow
        self.imshow_artist = self.imshow.artist
        self.styling_dict = styling_dict

        self.artist = None
        self.legend_handle = None

    def add_to_axes(self, axes: Axes):

        # extract figure belonging to axes
        fig: Figure = axes.get_figure()

        # define ScalarMappable to be fed to Colorbar artist below
        smap = ScalarMappable(
            cmap = self.imshow.cmap
        )
        smap.set_array([])
        smap.set_clim(self.imshow.vmin, self.imshow.vmax)

        
        self.artist: Colorbar = fig.colorbar(
            mappable = smap,
            ax = axes,
            **self.styling_dict
        )

    def set_styling_properties(self, **styling):
        raise ValueError('For Colorbars, styling properties must be set via upon instantiation via styling_dict')




        