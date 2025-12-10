import os
from utils.reader import read_file_as_lines
from .logic import *

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "input.txt")
    grid = read_file_as_lines(file_path)
    passward = cnt_zero_dials(grid, 50)
    secretCode = cnt_potential_zero_dials(grid, 50)
    print(passward)
    print(secretCode)
