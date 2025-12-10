from typing import List


def from_bool_list(arr: List[bool]) -> int:
    mask = 0
    for i, v in enumerate(arr):
        if v:
            mask |= 1 << i
    return mask
