import os
from utils.reader import read_file_as_lines, read_original_file_as_lines
from .logic import *


def parse_vertical_numbers(grid):
    if not grid:
        return []

    max_len = max(len(row) for row in grid)
    cur = []
    ans = []

    for col in range(max_len):
        vertical_num = []
        for row in grid:
            if col < len(row) and row[col] != " ":
                vertical_num.append(row[col])

        if vertical_num:
            cur.append(int("".join(vertical_num)))
        else:
            ans.append(cur)
            cur = []
    if cur:
        ans.append(cur)
    return ans


def part1(file_path: str) -> None:
    grid = read_file_as_lines(file_path)
    ori, ops = grid[:-1], grid[-1]
    ori = [list(map(int, row.split())) for row in ori]
    trans = list(map(list, zip(*ori)))
    ops = ops.split()
    print(simulation_cal(trans, ops))


def part2(file_path: str) -> None:
    grid = read_original_file_as_lines(file_path)
    ori, ops = grid[:-1], grid[-1]
    ori = parse_vertical_numbers(ori)
    ops = ops.strip().split()
    print(simulation_cal(ori, ops))


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "input.txt")
    part1(file_path)
    part2(file_path)
