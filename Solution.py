import math
from collections import Counter, defaultdict, deque
from functools import cache
from typing import List, Callable
from math import inf, comb
from sortedcontainers import SortedList
from copy import deepcopy
from itertools import pairwise, permutations
from heapq import heappush, heappop

MOD = 10 ** 9 + 7


def get_primes(n: int) -> list:
    """质因数分解"""
    i, ans = 2, []
    while i ** 2 <= n:
        if n % i == 0:
            ans.append([i, 0])
            while n % i == 0:
                n //= i
                ans[-1][1] += 1
        i += 1
    if n > 1:
        ans.append([n, 1]) # 为什么要加这一步，这一步是否正确
    return ans

print(get_primes(396))