from typing import Tuple
from typing import Literal

orientation_lookup = {
    "N": 0,
    "E": 90,
    "S": 180,
    "W": 270,
}
reverse_orientation_lookup = {0: "N", 90: "E", 180: "S", 270: "W"}

direction_lookup = {0: [0, 1], 90: [1, 0], 180: [0, -1], 270: [-1, 0]}


class Robot:
    orientation = 0
    x = 0
    y = 0
    xmax = 0
    ymax = 0
    is_lost = False

    def __init__(
        self,
        x: int,
        y: int,
        orientation: Literal["N", "E", "S", "W"],
        xmax: int,
        ymax: int,
    ):
        self.x = x
        self.y = y
        self.orientation = orientation_lookup[orientation]
        self.xmax = xmax
        self.ymax = ymax

    def tick(self, action):
        if self.is_lost:
            return

        if action == "F":
            self._move()
        elif action == "L":
            self._turn(-90)
        elif action == "R":
            self._turn(90)

    def _turn(self, angle):
        self.orientation = (self.orientation + angle) % 360

    def _move(self):
        new_x, new_y = self._get_next_position()

        if new_x > self.xmax or new_y > self.ymax or new_x < 0 or new_y < 0:
            self.is_lost = True
            return

        self.x = new_x
        self.y = new_y

    def _get_next_position(self) -> Tuple[int, int]:

        delta_x, delta_y = direction_lookup[self.orientation % 360]

        return (self.x + delta_x, self.y + delta_y)

    def output(self) -> str:
        lost_str = " LOST" if self.is_lost else ""
        orientation_str = reverse_orientation_lookup.get(
            self.orientation % 360, str(self.orientation) + "°"
        )
        return f"({self.x}, {self.y}, {orientation_str}){lost_str}"
