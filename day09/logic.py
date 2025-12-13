from typing import List


def cal_area(fir, sec) -> int:
    assert len(fir) == len(sec)
    ans = 1
    for x, a in zip(fir, sec):
        ans *= abs(x - a) + 1
    return ans


def gen_max_area(vertex: List[List[int]]) -> int:
    ans = 0
    n = len(vertex)
    for i in range(n - 1):
        for j in range(i + 1, n):
            ans = max(ans, cal_area(vertex[i], vertex[j]))
    return ans
