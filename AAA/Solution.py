import math
from collections import Counter, defaultdict, deque
from functools import cache
from typing import List, Callable
from math import inf, comb
# from sortedcontainers import SortedList
from copy import deepcopy
from itertools import pairwise, permutations, accumulate
from heapq import heappush, heappop

MOD = 10 ** 9 + 7



def DigitalDP(n: int) -> int:
    """数位DP通用模板"""
    s = str(n)

    @cache
    def dfs(i: int, is_limit: bool, is_num: bool, p: int, sx: int) -> int:
        if i == len(s):
            if not is_num:
                return 0
            else:
                return p % sx == 0
        ret = 0 if is_num else dfs(i + 1, False, False, 1, 0)
        up = int(s[i]) if is_limit else 9
        for j in range(1 - int(is_num), up + 1):
            ret += dfs(i + 1, j == up and is_limit, True, p * j, sx + j)
        return ret

    return dfs(0, True, False, 1, 0)


class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        return DigitalDP(r) - DigitalDP(l - 1)