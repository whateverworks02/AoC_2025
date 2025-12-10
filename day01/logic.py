from typing import List


def cnt_zero_dials(instructions: List[str], start: int) -> int:
    ans = 0
    cur = start
    for cmd in instructions:
        dir = -1 if cmd[0] == "L" else 1
        num = int(cmd[1:])
        cur += dir * num
        cur %= 100
        if cur == 0:
            ans += 1
    return ans


def cnt_potential_zero_dials(instructions: List[str], start: int) -> int:
    ans = 0
    cur = start
    for cmd in instructions:
        dir = -1 if cmd[0] == "L" else 1
        num = int(cmd[1:])
        prev = cur
        cur += dir * num
        if dir == 1:
            ans += cur // 100
        else:
            if prev != 0:
                if num >= prev:
                    ans += 1 + (num - prev) // 100
            else:
                ans += num // 100
        cur %= 100
    return ans
