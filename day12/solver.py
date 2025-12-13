import os
from utils.reader import read_file_as_lines
from .logic import *

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "input.txt")
    grid = read_file_as_lines(file_path)
    samples = []
    questions = []
    ans = 0
    for i in range(len(grid)):
        line = grid[i]
        pos = line.find(":")
        if pos == 1:
            cnt = 0
            for j in range(1, 4):
                nxt = grid[i + j]
                for c in nxt:
                    if c == "#":
                        cnt += 1
            samples.append(cnt)
        elif pos != -1:
            pivot = line.find("x")
            x = int(line[:pivot])
            y = int(line[pivot + 1 : pos])
            acts = line[pos + 1 :].strip().split()
            acts = list(map(int, acts))
            cnt = 0
            for i, v in enumerate(acts):
                cnt += v * samples[i]
            if cnt < x * y:
                ans += 1
    print(ans)
