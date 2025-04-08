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
        ret = inf
        i += 1; j += 1
        while i <= j:
            if self.a[j] < ret:
                ret = self.a[j]
            j -= 1
            while i <= j - (j & -j):
                if self.d[j] < ret:
                    ret = self.d[j]
                j -= j & -j
        return ret
    
    def update(self, i: int, val: int): # 单点修改
        i += 1
        self.a[i], j = val, i
        while i < self.n:
            if self.a[j] < self.d[i]:
                self.d[i] = self.a[j]
            i += i & -i