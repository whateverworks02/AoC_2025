import os
from utils.reader import read_file_as_lines
from .logic import *

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "input.txt")
    grid = read_file_as_lines(file_path)
    st = grid[0].find("S")
    grid = grid[1:]
    for i, row in enumerate(grid):
        grid[i] = [c == "^" for c in row]
    print(cnt_split_times(grid, st))
    print(cnt_multi_universe(grid, st))
