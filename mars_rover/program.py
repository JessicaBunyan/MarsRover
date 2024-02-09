import sys
import re
from mars_rover.robot import Robot
from typing import Iterator, List

grid_regex = "(\d+) (\d+)"
robot_regex = "\((\d+), ?(\d+), ?([NESW])\) ?([FLR]*)"


def run_rovers(lines: Iterator[str]) -> List[str]:

    output = []

    # Grab the grid definition first
    grid_def = next(lines)
    grid_match = re.search(grid_regex, grid_def)
    if not grid_match:
        print("Bad input, exiting")
        exit(1)

    xmax, ymax = grid_match.groups()

    # all remaining lines are robot definitions
    for line in lines:
        robot_match = re.search(robot_regex, line)
        if not robot_match:
            print("Bad input, exiting")
            exit(1)

        x, y, orientation, instructions = robot_match.groups()
        robo = Robot(
            x=int(x), y=int(y), orientation=orientation, xmax=int(xmax), ymax=int(ymax)
        )
        for char in instructions:
            robo.tick(char)
        output.append(robo.output())

    return output
