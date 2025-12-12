from typing import List, Tuple


def cnt_split_times(grid: List[List[bool]], start: int) -> int:
    ans = 0
    syc = set([start])
    for row in grid:
        for i, v in enumerate(row):
            if v and i in syc:
                syc.remove(i)
                ans += 1
                if i + 1 < len(grid[0]):
                    syc.add(i + 1)
                if i - 1 >= 0:
                    syc.add(i - 1)
    return ans


def cnt_multi_universe(grid: List[List[bool]], start: int) -> int:
    m, n = len(grid), len(grid[0])
    f = [[0] * n for _ in range(m)]
    f[0][start] = 1

    for i in range(1, m):
        for j in range(n):
            if j - 1 >= 0 and grid[i - 1][j - 1]:
                f[i][j] += f[i - 1][j - 1]
            if j + 1 < n and grid[i - 1][j + 1]:
                f[i][j] += f[i - 1][j + 1]
            if not grid[i - 1][j]:
                f[i][j] += f[i - 1][j]

    return sum(f[-1])
