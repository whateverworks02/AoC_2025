class UnionFind:
    def __init__(self, n):
        self._fa = list(range(n))
        self._size = [1] * n
        self.cc = n

    def find(self, x) -> int:
        fa = self._fa
        # update the whole trace
        if fa[x] != x:
            fa[x] = self.find(fa[x])
        return fa[x]

    def merge(self, prev, cur) -> bool:
        x, y = self.find(prev), self.find(cur)
        if x == y:
            return False
        self._fa[x] = y
        self._size[y] += self._size[x]
        self._size[x] = 0
        self.cc -= 1
        return True


from typing import List
from heapq import heappop, heapify


def cal_distance(fir: List[int], sec: List[int]) -> int:
    assert len(fir) == len(sec)
    ans = 0

    for x, a in zip(fir, sec):
        ans += (x - a) ** 2

    return ans


def part1(grid: List[List[int]], steps: int) -> int:
    n = len(grid)
    pq = []
    for i in range(n - 1):
        fir = grid[i]
        for j in range(i + 1, n):
            sec = grid[j]
            pq.append((cal_distance(fir, sec), i, j))
    heapify(pq)
    uf = UnionFind(n)
    for _ in range(steps):
        _, prev, cur = heappop(pq)
        uf.merge(prev, cur)
    ans = 1
    for x in sorted(uf._size, reverse=True)[:3]:
        ans *= x
    return ans


def part2(grid: List[List[int]]) -> int:
    n = len(grid)
    pq = []
    for i in range(n - 1):
        fir = grid[i]
        for j in range(i + 1, n):
            sec = grid[j]
            pq.append((cal_distance(fir, sec), i, j))
    heapify(pq)
    uf = UnionFind(n)
    while True:
        _, prev, cur = heappop(pq)
        uf.merge(prev, cur)
        if uf.cc == 1:
            return grid[prev][0] * grid[cur][0]
