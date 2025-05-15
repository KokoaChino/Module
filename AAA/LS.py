# for _ in range(int(input())):
#    n, a = int(input()), map(int, input().split())

import sys
input = lambda: sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 6 + 10)

# from copy import deepcopy
# from functools import lru_cache
# from heapq import heappush, heappop
# from decimal import Decimal, getcontext
# from bisect import bisect_left, bisect_right
# from datetime import datetime, date, timedelta
# from math import inf, gcd, sqrt, ceil, floor, log
# from collections import Counter, defaultdict, deque
# from random import randint, choice, choices, shuffle
# from itertools import count, accumulate, permutations, combinations, combinations_with_replacement
# getcontext().prec = 50


def solve():
    a = list(map(int, input().split('@')))
    print(sum(a))



is_more = 1
for _ in range(int(input()) if is_more else 1):
    solve()