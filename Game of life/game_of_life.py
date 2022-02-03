# See: https://conwaylife.com
from logging import exception
from click import pass_context
import matplotlib.pyplot as plt
import numpy as np
import abc
import unittest
from matplotlib import colors


class Matrix:
    def __init__(self, size: int) -> None:
        self.matrix = np.zeros((size, size))
        self.size = size
        self.number_of_cells = size * size

    def set(self, index: int, value: int):
        x, y = self.to_coor(index)
        self.matrix[x][y] = value

    def to_coor(self, index) -> tuple[int, int]:
        num_line = index // self.size
        num_col = index - num_line * self.size
        return num_line, num_col

    def get_size(self) -> int:
        return self.size

    def to_index(self, x: int, y: int) -> int:
        return x * self.size + y

    def get_cell(self, index: int) -> int:
        num_line, num_col = self.to_coor(index)

        return self.matrix[num_line][num_col]

    def set_cell(self, index: int, value: int) -> None:
        num_line, num_col = self.to_coor(index)
        self.matrix[num_line][num_col] = value

    def get_number_of_cells(self) -> int:
        return self.number_of_cells

    def get_matrix(self) -> np.ndarray:
        return self.matrix

    def get_moore(self, index: int) -> np.ndarray:
        ret = np.ndarray(0, dtype=int)
        x, y = self.to_coor(index)

        if x > 0 and y < self.size - 1:
            ret = np.append(ret, index - self.size + 1)
        if x > 0 and y > 0:
            ret = np.append(ret, index - self.size - 1)
        if x < self.size - 1 and y > 0:
            ret = np.append(ret, index + self.size - 1)
        if x < self.size - 1 and y < self.size - 1:
            ret = np.append(ret, index + self.size + 1)

        return np.append(ret, self.get_von_neumann(index))

    def get_von_neumann(self, index: int) -> np.ndarray:
        ret = np.ndarray(0, dtype=int)
        x, y = self.to_coor(index)

        if y < self.size - 1:
            ret = np.append(ret, index + 1)
        if y > 0:
            ret = np.append(ret, index - 1)
        if x < self.size - 1:
            ret = np.append(ret, index + self.size)
        if x > 0:
            ret = np.append(ret, index - self.size)

        return ret


class TestMatrix(unittest.TestCase):
    def test_get_number_of_cells(self):
        self.matrix = Matrix(50)
        self.assertEqual(self.matrix.get_number_of_cells(), 50 * 50)

    def test_to_coor(self):
        self.matrix = Matrix(50)
        self.assertEqual(self.matrix.to_coor(0), (0, 0))
        self.assertEqual(self.matrix.to_coor(49), (0, 49))
        self.assertEqual(self.matrix.to_coor(49 * 50), (49, 0))
        self.assertEqual(self.matrix.to_coor(50 * 50 - 1), (49, 49))

    def test_get_moore(self):
        self.matrix = Matrix(50)

        corner1 = self.matrix.get_moore(80)
        self.assertEqual(len(corner1), 8)

        corner1 = self.matrix.get_moore(0)
        self.assertEqual(len(corner1), 3)

        corner2 = self.matrix.get_moore(49)
        self.assertEqual(len(corner2), 3)

        corner3 = self.matrix.get_moore(49 * 50)
        self.assertEqual(len(corner3), 3)

        corner4 = self.matrix.get_moore(50 * 50 - 1)
        self.assertEqual(len(corner4), 3)


class Cellular_automaton(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def compute(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass

    def __init__(self, size: int) -> None:
        self.matrix = Matrix(size)
        self.cells_new_state: dict[int, int] = {}
        self.state: dict[str, int] = {}


class Game_of_life(Cellular_automaton):
    def __init__(self, size: int) -> None:
        super().__init__(size)
        self.state["DED"] = 0
        self.state["ALIVE"] = 1
        for cell in range(self.matrix.get_number_of_cells()):
            if np.random.rand() < 0.5:
                self.matrix.set_cell(cell, self.state["ALIVE"])
            else:
                self.matrix.set_cell(cell, self.state["DED"])

    def load_pattern_RLE(self, rle: str):
        for cell in range(self.matrix.get_number_of_cells()):
            self.matrix.set_cell(cell, self.state["DED"])

        x_shift = 3
        y_shift = 5
        x = 0
        y = 0
        num = ""
        for c in rle:
            if c == "$":
                x = 0
                y += 1
            elif (
                c == "0"
                or c == "1"
                or c == "2"
                or c == "3"
                or c == "4"
                or c == "5"
                or c == "6"
                or c == "7"
                or c == "8"
                or c == "9"
            ):
                num += c
            elif c == "b":
                if num == "":
                    x += 1
                else:
                    cpt = int(num)
                    for _ in range(cpt):
                        x += 1
                    num = ""
            elif c == "o":
                if num == "":
                    self.matrix.set_cell(
                        self.matrix.to_index(y_shift + y, x_shift + x),
                        self.state["ALIVE"],
                    )
                    x += 1
                else:
                    cpt = int(num)
                    for _ in range(cpt):
                        self.matrix.set_cell(
                            self.matrix.to_index(y_shift + y, x_shift + x),
                            self.state["ALIVE"],
                        )
                        x += 1
                    num = ""
            elif c == "!":
                pass
            else:
                raise Exception("[-] Pattern is malformed")

    # rule = B3/S23
    def compute(self):
        for cell in range(self.matrix.get_number_of_cells()):
            neighbors = self.matrix.get_moore(cell)
            count_alife = 0

            for neighbor in neighbors:
                if self.matrix.get_cell(neighbor) == self.state["ALIVE"]:
                    count_alife += 1
            if self.matrix.get_cell(cell) == self.state["DED"] and count_alife == 3:
                self.cells_new_state[cell] = self.state["ALIVE"]
            elif self.matrix.get_cell(cell) == self.state["ALIVE"] and (
                count_alife == 2 or count_alife == 3
            ):
                continue
            elif self.matrix.get_cell(cell) == self.state["ALIVE"]:
                self.cells_new_state[cell] = self.state["DED"]

    def update(self):
        for cell in self.cells_new_state.keys():
            self.matrix.set_cell(cell, self.cells_new_state[cell])
        self.cells_new_state.clear()


def animation(cellular_automaton: Cellular_automaton, savefigs=""):
    fig, ax = plt.subplots(figsize=(6, 6))
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)

    plt.xticks(np.arange(0, cellular_automaton.matrix.get_size(), 1.0))
    plt.yticks(np.arange(0, cellular_automaton.matrix.get_size(), 1.0))
    iteration = 0
    plt.pcolormesh(
        cellular_automaton.matrix.get_matrix(),
        cmap=colors.ListedColormap(["black", "red"]),
    )
    plt.grid(which="both", color="w", linestyle="-", linewidth=0.1)
    plt.savefig(savefigs + "-" + str(iteration).zfill(4) + ".png")
    while iteration < 15:
        iteration += 1
        ax.cla()
        plt.xticks(np.arange(0, cellular_automaton.matrix.get_size(), 1.0))
        plt.yticks(np.arange(0, cellular_automaton.matrix.get_size(), 1.0))

        cellular_automaton.compute()
        cellular_automaton.update()

        plt.pcolormesh(
            cellular_automaton.matrix.get_matrix(),
            cmap=colors.ListedColormap(["black", "red"]),
        )
        # ax.set_axis_off()
        # ax.set_title("frame {}".format(iteration))
        plt.grid(which="both", color="w", linestyle="-", linewidth=0.1)
        if savefigs == "":
            plt.pause(0.1)
        else:
            plt.savefig(savefigs + "-" + str(iteration).zfill(4) + ".png")


if __name__ == "__main__":
    # unittest.main()
    game_of_life = Game_of_life(size=13)
    game_of_life.load_pattern_RLE("3ob3o$o5bo$2bobo$b2ob2o$o5bo!")
    print(game_of_life.matrix.matrix)
    animation(game_of_life, "test/xp14_j9d0d9j")
