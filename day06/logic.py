from typing import List


def operate(nums: List[int], op: str) -> int:
    if op == "+":
        return sum(nums)
    ans = 1
    for num in nums:
        ans *= num
    return ans


def simulation_cal(grid: List[List[int]], ops: List[str]) -> int:
    ans = 0
    for line, op in zip(grid, ops):
        ans += operate(line, op)
    return ans
