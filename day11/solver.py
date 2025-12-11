import os
from utils.reader import read_file_as_lines
from .logic import cnt_diff_paths_v1, cnt_diff_paths_v2

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "input.txt")
    grid = read_file_as_lines(file_path)
    print(cnt_diff_paths_v1(grid))
    print(cnt_diff_paths_v2(grid))
