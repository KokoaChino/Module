def one_prefix_sum(nums: list) -> list: # 一维前缀和
    ans = [0] * (len(nums) + 1)
    for i, v in enumerate(nums):
        ans[i + 1] += ans[i] + v
    return ans

def get_sum(P: list, i: int, j: int) -> int: # 区间求和
    return P[j + 1] - P[i]

def two_prefix_sum(mat: list) -> list: # 二维前缀和
    m, n = len(mat), len(mat[0])
    ans = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            ans[i + 1][j + 1] = ans[i][j + 1] + ans[i + 1][j] - ans[i][j] + mat[i][j]
    return ans

def get_sum(P: list, x1: int, y1: int, x2: int, y2: int) -> int: # 区域求和
    return P[x2 + 1][y2 + 1] - P[x1][y2 + 1] - P[x2 + 1][y1] + P[x1][y1]