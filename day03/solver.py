import os
from utils.reader import read_file_as_lines
from .logic import *

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "input.txt")
    grid = read_file_as_lines(file_path)
    ansV1 = ansV2 = 0
    for line in grid:
        arr = list(map(int, line))
        ansV1 += gen_max_joltage(arr)
        ansV2 += gen_with_twelve_constraint(arr)
    print(ansV1)
    print(ansV2)
