from math import inf

class BinaryIndexedTreesMin: # 树状数组 Min

    __slots__ = ("n", "a", "d")

    def __init__(self, nums: list):
        self.n = len(nums) + 1
        self.a = [inf] * self.n
        self.d = [inf] * self.n
        for i, v in enumerate(nums):
            self.update(i, v)

    def query(self, i: int, j: int) -> int: # 区间查询
        ans = inf
        i += 1; j += 1
        while i <= j:
            if ans > self.a[j]:
                ans = self.a[j]
            j -= 1
            while i <= j - (j & -j):
                if ans > self.d[j]:
                    ans = self.d[j]
                j -= j & -j
        return ans
    
    def update(self, i: int, val: int): # 单点修改
        i += 1
        self.a[i] = val
        while i < self.n:
            if self.d[i] > val:
                self.d[i] = val
            i += i & -i