from typing import List, Tuple


def cnt_fresh_num(ranges: List[Tuple[int]], nums: List[int]) -> int:
    ans = 0
    ranges.sort()
    cur = list(ranges[0])
    limits = []
    for s, e in ranges:
        if s > cur[1] or e < cur[0]:
            limits.append(cur)
            cur = [s, e]
            continue
        cur[0] = min(cur[0], s)
        cur[1] = max(cur[1], e)
    limits.append(cur)

    for num in nums:
        for s, e in limits:
            if s <= num <= e:
                ans += 1
                break

    return ans


def cnt_all_freshes(ranges: List[Tuple[int]]) -> int:
    ans = 0
    ranges.sort()
    cur = list(ranges[0])
    for s, e in ranges:
        if s > cur[1] or e < cur[0]:
            ans += cur[1] - cur[0] + 1
            cur = [s, e]
            continue
        cur[0] = min(cur[0], s)
        cur[1] = max(cur[1], e)
    return ans + cur[1] - cur[0] + 1
