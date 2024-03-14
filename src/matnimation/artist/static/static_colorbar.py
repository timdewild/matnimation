from typing import Union
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.cm import ScalarMappable
from matplotlib.colorbar import Colorbar
from src.matnimation.artist.static.static_artist import StaticArtist
from src.matnimation.artist.static.static_imshow import StaticImshow
from src.matnimation.artist.animated.animated_imshow import AnimatedImshow

class StaticColorBar(StaticArtist):

    def __init__(self, name: str, imshow: Union[StaticImshow, AnimatedImshow], styling_dict: dict = None):
        """
        Initialize a StaticColorBar object.

        Parameters
        ----------
        name : str
            Name of the static color bar
        imshow : StaticImshow | AnimatedImshow
            Artist representing the image (either static or animated) associated with the color bar
        styling_dict : dict, optional
            Styling dictionary, all 'Other Parameters' of matplotlib.figure.Figure.colorbar can be passed here, by default None
        """
        super().__init__(name)
        self.imshow = imshow
        self.imshow_artist = self.imshow.artist
        self.styling_dict = styling_dict

        self.artist = None
        self.legend_handle = None

    def add_to_axes(self, axes: Axes):
        """
        Add the color bar to the specified axes.

        Parameters
        ----------
        axes : Axes
            Axes object to add the color bar to
        """
        # extract figure belonging to axes
        fig: Figure = axes.get_figure()

        # define ScalarMappable to be fed to Colorbar artist below
        smap = ScalarMappable(
            cmap=self.imshow.cmap
        )
        smap.set_array([])
        smap.set_clim(self.imshow.vmin, self.imshow.vmax)

        self.artist: Colorbar = fig.colorbar(
            mappable=smap,
            ax=axes,
            **self.styling_dict
        )

    def set_tick_labels(self, labels: list, orientation: str = 'vertical'):
        """
        Set tick labels for the colorbar. 

        Parameters
        ----------
        labels : list
            List with labels for ticks of colorbar. 
            Should be of same length as list passed to ticks keyword in styling_dict. 
        orientation : str
            Orientation of colorbar, must be either 'vertical' or 'horizontal'.
            Should agree with the value passed to the 'orientation' keyword set in 'styling_dict' upon instantiation.
        
        Raises
        ------
        ValueError
            If keyword is not 'vertical' or 'horizontal'. 
        """
        if orientation == 'vertical':
            self.artist.ax.set_yticklabels(labels)
        if orientation == 'horizontal':
            self.artist.ax.set_xticklabels(labels)
        else:
            raise ValueError("The orientation keyword must be either 'vertical' or 'horizontal' and should agree with the value passed to the 'orientation' keyword set in 'styling_dict' upon instantiation.")

    def set_styling_properties(self, **styling):
        """
        Set styling properties for the color bar.

        Raises
        ------
        ValueError
            For Colorbars, styling properties must be set upon instantiation via styling_dict
        """
        raise ValueError('For Colorbars, styling properties must be set upon instantiation via styling_dict')
