import os
from utils.reader import read_several_parts
from .logic import *

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "input.txt")
    ranges, nums = read_several_parts(file_path)
    ranges = [(int(pr[: pr.find("-")]), int(pr[pr.find("-") + 1 :])) for pr in ranges]
    nums = list(map(int, nums))
    print(cnt_fresh_num(ranges, nums))
    print(cnt_all_freshes(ranges))
