from typing import List


def gen_max_joltage(arr: List[int]) -> int:
    ans = 0
    st = []

    for i, cur in enumerate(arr):
        while st and cur > st[-1]:
            prev = st.pop()
            if i == len(arr) - 1:
                ans = max(ans, prev * 10 + cur)
        if len(st) == 1:
            ans = max(ans, st[-1] * 10 + cur)
        st.append(cur)

    return ans


def gen_with_twelve_constraint(arr: List[int]) -> int:
    BASE = 12
    st = []
    n = len(arr)

    def can_process(idx: int) -> bool:
        already_choosen = len(st)
        lft = BASE - already_choosen
        candidate = n - idx
        return candidate > lft

    for i, cur in enumerate(arr):
        while st and cur > st[-1] and can_process(i):
            st.pop()
        if len(st) < BASE:
            st.append(cur)
    return int("".join(map(str, st)))
