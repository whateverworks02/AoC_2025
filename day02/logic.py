from typing import List, Tuple


def calV1(s: int, e: int) -> int:
    if e < 11:
        return 0
    cnt = 0
    L = 1
    while True:
        base = 10**L + 1
        lower = 10 ** (L - 1)
        higher = 10**L - 1
        mn = lower * base
        if mn > e:
            break

        for x in range(lower, higher + 1):
            n = x * base
            if n > e:
                break
            if n >= s:
                cnt += n
        L += 1
    return cnt


def calV2(s: int, e: int) -> int:
    cnt = 0

    for num in range(s, e + 1):
        ori = str(num)
        dbd = ori * 2
        if dbd.find(ori, 1) != len(ori):
            cnt += num
    return cnt


def gather_invalid_ids(nums: List[Tuple[int]], mode: int) -> int:
    ans = 0
    if mode == 1:
        for s, e in nums:
            ans += calV1(s, e)
    elif mode == 2:
        for s, e in nums:
            ans += calV2(s, e)
    return ans
