from matplotlib import animation
from src.matnimation.canvas.canvas import Canvas

class Animation:
    def __init__(self, canvas: Canvas, interval: int = 30):
        """
        Initialize an Animation object.

        Parameters
        ----------
        canvas : Canvas
            Canvas object representing the animation canvas
        interval : int, optional
            Time interval between frames in milliseconds, by default 30
        """
        self.canvas = canvas
        self.interval = interval

        self.fig = self.canvas.get_figure()

    def animate(self, time_index: int):
        """
        Animate the canvas frame for a specific time index.

        Parameters
        ----------
        time_index : int
            Index representing the time step in the animation animation
        """
        self.canvas.update_frame(time_index)

    def render(self, filename):
        """
        Render and save the animation as a video file.

        Parameters
        ----------
        filename : str
            Name of the file or filepath to save the animation
        """
        anim = animation.FuncAnimation(self.fig, self.animate, frames=len(self.canvas.time_array), interval=self.interval)
        anim.save(filename=filename)