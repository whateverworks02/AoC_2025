from typing import List
from utils.bit import from_bool_list


def act(mask: int, action: List[int]) -> int:
    if not action:
        return mask
    toogle_mask = 0
    for pos in action:
        toogle_mask |= 1 << pos
    return mask ^ toogle_mask


def find_minimal_action_cnt(target: List[bool], actions: List[List[int]]) -> int:
    ans = 0
    tar_mask = from_bool_list(target)
    if tar_mask == 0:
        return 0
    visited = set([0])
    q = [0]
    while q:
        new_q = []
        for cur in q:
            for action in actions:
                nxt = act(cur, action)
                if nxt == tar_mask:
                    return ans + 1
                if nxt not in visited:
                    new_q.append(nxt)
                    visited.add(nxt)
        ans += 1
        q = new_q
    return -1
