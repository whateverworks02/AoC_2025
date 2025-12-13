import os
from utils.reader import read_file_as_lines
from .logic import *

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "input.txt")
    grid = read_file_as_lines(file_path)
    for i, line in enumerate(grid):
        grid[i] = list(map(int, line.split(",")))
    print(part1(grid, 1000))
    print(part2(grid))
