from typing import List


def build_pool(grid: List[str]) -> dict:
    pool = dict()
    for line in grid:
        cur, cons = line.split(":")
        pool[cur] = cons.split(" ")
    return pool


def cnt_diff_paths_v1(grid: List[str]) -> int:
    source = "you"
    tar = "out"
    pool = build_pool(grid)
    counter = dict()

    def dfs(cur: str) -> int:
        if cur == tar:
            return 1
        if cur in counter:
            return counter[cur]
        if cur not in pool:
            return 0
        cnt = 0
        for nxt in pool[cur]:
            cnt += dfs(nxt)
        counter[cur] = cnt
        return cnt

    return dfs(source)


def cnt_diff_paths_v2(grid: List[str]) -> int:
    source = "svr"
    tar = "out"
    pool = build_pool(grid)
    counter = dict()
    blockers = set(["fft", "dac"])

    def gen_status_code(blockers: set) -> int:
        if not blockers:
            return 0
        if len(blockers) == 2:
            return 1
        return 2 if "fft" in blockers else 3

    def dfs(cur: str) -> int:
        if cur == tar:
            return 0 if blockers else 1
        code = (cur, gen_status_code(blockers))
        if code in counter:
            return counter[code]
        if cur not in pool:
            return 0
        cnt = 0
        for nxt in pool[cur]:
            should_recover = False
            if nxt in blockers:
                blockers.remove(nxt)
                should_recover = True
            cnt += dfs(nxt)
            if should_recover:
                blockers.add(nxt)
        counter[code] = cnt
        return cnt

    return dfs(source)
