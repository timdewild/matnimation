from matplotlib.axes import Axes
from matplotlib.text import Text
import numpy as np
from src.matnimation.artist.animated.animated_artist import AnimatedArtist


class AnimatedText(AnimatedArtist):

    def __init__(self, name: str, text_str_data: list[str], text_x_data: np.ndarray, text_y_data: np.ndarray, vis_interval: list[int] = None):
        """
        Initialize an Animated Text.

        Parameters:
        -----------
        name : str
            Name of the animated text.
        text_str_data : list[str]
            List with text strings at all timesteps.
        text_x_data : np.ndarray
            x position of text at all timesteps.
        text_y_data : np.ndarray
            y position of text at all timesteps.
        vis_interval : list[int], optional
            List with time indices at which visibility must be turned ON and OFF, by default None.
        """

        super().__init__(name, vis_interval)
        self.text_str_data = text_str_data

        # check if x and y data types match
        if type(text_x_data) is not type(text_y_data):
            raise ValueError('Types of text_x_data and text_y_data do not match: both should be either float or np.ndarray')

        self.text_x_data = text_x_data
        self.text_y_data = text_y_data

        # define Text artist
        self.artist: Text = Text(
            x = 0,
            y = 0,
            text = '',
        )

        # assume text string and text position are animated by default
        self.text_str_animated = True
        self.text_pos_animated = True

        # check if text string is static
        if isinstance(self.text_str_data, str):
            self.initial_text = self.text_str_data
            self.text_str_max = self.initial_text
            self.text_str_animated = False

        # if text string is anaimated, find maximum length string 
        if isinstance(self.text_str_data, list):
            self.initial_text = self.text_str_data[0]
            self.text_str_max = max(self.text_str_data, key=len)

        self.artist.set_text(self.initial_text)

        # check if text position is static
        if isinstance(self.text_x_data, float):
            self.artist.set_x(self.text_x_data)
            self.artist.set_y(self.text_y_data)
            self.text_pos_animated = False

        # if both text string and position are static, use StaticText instead
        if self.text_str_animated == False and self.text_pos_animated == False:
            print('Both text string and position are static, use StaticText instead.')

        self.legend_handle = None

    def update_timestep(self, time_index):
        """
        Update text and position at specific timestep in animation.

        Parameters:
        -----------
        time_index : int
            Index of the current timestep.
        """
        if self.text_str_animated:
            self.artist.set_text(self.text_str_data[time_index])

        if self.text_pos_animated:
            self.artist.set_x(self.text_x_data[time_index])
            self.artist.set_y(self.text_y_data[time_index])

        self.update_visibility(time_index)

class AnimatedTextBbox(AnimatedArtist):

    def __init__(self, name: str, animated_text: AnimatedText, vis_interval: list[int] = None):
        """
        Initialize an AnimatedTextBbox.

        Parameters:
        -----------
        name : str
            Name of the animated text bounding box.
        animated_text : AnimatedText
            AnimatedText object to create a bounding box around.
        vis_interval : list[int], optional
            List with time indices at which visibility must be turned ON and OFF, by default None.
        """
        super().__init__(name, vis_interval)

        self.bbox_x_data = animated_text.text_x_data
        self.bbox_y_data = animated_text.text_y_data

        self.text_str_max = animated_text.text_str_max

        self.artist: Text = Text()
        self.legend_handle = None

        self.artist.update_from(animated_text.artist)

        # set (transparent) text in bbox to the longest text string of animated_text
        self.artist.set_alpha(0)
        self.artist.set_text(self.text_str_max)

        self.bbox_pos_animated = True
        if isinstance(self.bbox_x_data, float):
            self.artist.set_x(self.bbox_x_data)
            self.artist.set_y(self.bbox_y_data)
            self.bbox_pos_animated = False

    def update_timestep(self, time_index):
        """
        Update bounding box around text at specific timestep in animation.

        Parameters:
        -----------
        time_index : int
            Index of the current timestep.
        """

        if self.bbox_pos_animated:
            self.artist.set_x(self.bbox_x_data[time_index])
            self.artist.set_y(self.bbox_y_data[time_index])

        self.update_visibility(time_index)

        


