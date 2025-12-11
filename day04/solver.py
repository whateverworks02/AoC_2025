import os
from utils.reader import read_file_as_lines
from .logic import *

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "input.txt")
    grid = read_file_as_lines(file_path)
    ori = []
    for line in grid:
        row = list(line)
        row = [c == "@" for c in row]
        ori.append(row)
    print(cnt_paper_roll(ori))
    print(lets_remove(ori))
