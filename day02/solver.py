import os
from utils.reader import read_single_line
from .logic import *

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "input.txt")
    s = read_single_line(file_path)
    ls = s.split(",")
    ori = [tuple(map(int, item.split("-"))) for item in ls]
    print(ori)
    print(gather_invalid_ids(ori, 1))
    print(gather_invalid_ids(ori, 2))
