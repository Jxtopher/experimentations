# see: https://en.wikipedia.org/wiki/Random_walk
# mp4 to gif : ffmpeg -i output.avi -pix_fmt rgb24  out.gif

from typing import List, Optional, Callable, Tuple
from math import cos, sin, pi
from random import randint

# import matplotlib
# matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation

Coordinates = List


class Turtle:
    def __init__(self, coordinates: Coordinates):
        self.position: Coordinates = coordinates

    def move(self, distance: float, angle_degree: float):
        angle_radian = angle_degree * (pi / 180)
        new_position = [distance * cos(angle_radian), distance * sin(angle_radian)]
        new_position[0] += self.position[0]
        new_position[1] += self.position[1]
        self.position = new_position

    def get_position(self) -> Coordinates:
        return self.position

    def set_xy(self, x: float, y: float):
        self.position = [x, y]


class Turtles(List[Turtle]):
    def __init__(self, number_of_turtles):
        for _ in range(0, number_of_turtles):
            self.append(Turtle([0, 0]))

    def get_number_of_turtles(self):
        return len(self)

    def set_one_xy(self, id: int, x: float, y: float):
        assert id < len(self)
        self[id].set_xy(x, y)

    def move_all(self, forward: float = 1, angle_degree: Optional[float] = None):
        for i in range(0, len(self)):
            if angle_degree is None:
                self[i].move(forward, randint(0, 360))
            else:
                self[i].move(forward, angle_degree)

    def get_data(self) -> Tuple[List, List]:
        x = [self[i].get_position()[0] for i in range(0, len(self))]
        y = [self[i].get_position()[1] for i in range(0, len(self))]
        return x, y


class Scene(animation.TimedAnimation):
    def __init__(
        self,
        transition_function: Callable[[], Tuple[List, List]],
        max_iterations,
        xmin: float,
        xmax: float,
        ymin: float,
        ymax: float,
    ):
        self.transition_function = transition_function
        self.fig, ax = plt.subplots(figsize=(5, 5))
        ax.margins(0.05)
        (self.scene,) = plt.plot([], [], "o", markersize=1, color="xkcd:blue")
        self.iteration = 0
        self.ticks = plt.text(
            0,
            ymax + 5,
            self.iteration,
            fontsize=12,
            horizontalalignment="center",
            verticalalignment="center",
        )
        self.max_iterations = max_iterations

        plt.axis([xmin, xmax, ymin, ymax])

        animation.TimedAnimation.__init__(self, self.fig, interval=50, blit=True)

    def __del__(self):
        plt.close()

    def show(self):
        plt.show()

    def _draw_frame(self, framedata):
        x, y = self.transition_function()
        self.ticks.set_text(self.iteration)
        self.scene.set_xdata(x)
        self.scene.set_ydata(y)

        self.iteration += 1

        plt.pause(0.01)

    def new_frame_seq(self):
        return iter(range(self.max_iterations))

    def _init_draw(self):
        self.iteration = 0


if __name__ == "__main__":
    turtles = Turtles(500)
    for turtle in turtles:
        turtle.set_xy(0,randint(-200,200))

    def transition() -> Tuple[List, List]:
        turtles.move_all()
        turtles.get_data()
        return turtles.get_data()

    scene = Scene(transition, 20000, -200, 200, -200, 200)
    scene.show()
    # scene.save("test_sub.mp4", dpi = 800)
