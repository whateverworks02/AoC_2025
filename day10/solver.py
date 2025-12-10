import os
import re
from utils.reader import read_file_as_lines
from .logic import find_minimal_action_cnt


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "input.txt")
    grid = read_file_as_lines(file_path)
    cnt = 0
    for line in grid:
        lights_match = re.search(r"\[([#.]+)\]", line)
        lights = [c == "#" for c in lights_match.group(1)] if lights_match else []
        buttons = []
        for match in re.finditer(r"\(([\d,]*)\)", line):
            nums = match.group(1)
            buttons.append([int(x) for x in nums.split(",")] if nums else [])
        cnt += find_minimal_action_cnt(lights, buttons)
    print(cnt)
