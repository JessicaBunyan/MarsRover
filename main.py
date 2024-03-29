import fileinput
import sys
from mars_rover.program import run_program

if len(sys.argv) < 2:
    print("Please provide input file e.g python main.py /path/to/input/file")
    exit(2)

input_file = fileinput.input(sys.argv[1])
output = run_program(input_file)

for line in output:
    print(line)
