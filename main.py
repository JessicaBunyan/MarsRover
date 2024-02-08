import fileinput
import sys
import re
from robot import Robot

grid_regex = "(\d+) (\d+)"
robot_regex = "\((\d+), ?(\d+), ?([NESW])\) ?([FLR]*)"

if len(sys.argv) < 2:
    print("Please provide input file e.g python main.py /path/to/input/file")
    exit(2)

# Grab the grid definition first
lines = fileinput.input(sys.argv[1])
grid_def = lines.readline()
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
    robo.output()
