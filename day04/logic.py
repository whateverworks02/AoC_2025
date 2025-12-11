from typing import List
from collections import deque


def cnt_paper_roll(grid: List[List[bool]]) -> int:
    ans = 0
    n, m = len(grid), len(grid[0])

    dirs = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

    for x in range(n):
        for y in range(m):
            if not grid[x][y]:
                continue
            cnt = 0
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny]:
                    cnt += 1
                    if cnt > 3:
                        break
            ans += cnt < 4

    return ans


def lets_remove(grid: List[List[bool]]) -> int:
    n, m = len(grid), len(grid[0])

    dirs = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    pool = dict()
    q = deque()
    for x in range(n):
        for y in range(m):
            if not grid[x][y]:
                continue
            cnt = 0
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny]:
                    cnt += 1
            if cnt < 4:
                q.append((x, y))
            else:
                pool[(x, y)] = cnt
    ans = 0
    while q:
        x, y = q.popleft()
        ans += 1
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) in pool:
                pool[(nx, ny)] -= 1
                if pool[(nx, ny)] < 4:
                    q.append((nx, ny))
                    del pool[(nx, ny)]
    return ans
