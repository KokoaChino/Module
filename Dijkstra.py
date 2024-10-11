import heapq
from math import inf
from collections import deque

def dijkstra(mat: list, a: int) -> list:
    """Dijkstra单源最短路算法"""
    n = len(mat)
    ans = [inf] * n
    ans[a] = 0
    q = deque([a])
    while q:
        x = q.popleft()
        for y, d in enumerate(mat[x]):
            if ans[x] + d < ans[y]:
                ans[y] = ans[x] + d
                q.append(y)
    return ans

def dijkstra(g: list, a: int) -> list:
    n = len(g)
    ans, st, q = [inf] * n, [False] * n, []
    ans[a] = 0
    heapq.heappush(q, (0, a))
    while q:
        dist, x = heapq.heappop(q)
        if st[x]:
            continue
        st[x] = True
        for t in g[x]:
            y, d = t
            if ans[y] > ans[x] + d:
                ans[y] = ans[x] + d
                heapq.heappush(q, (ans[y], y))
    return ans