class UnionFindSet: # 并查集

    __slots__ = ("n", "fa", "rank", "num")

    def __init__(self, n: int):
        self.n = n
        self.fa = list(range(n))
        self.rank = [1] * n
        self.num = [1] * n

    def find(self, x: int) -> int: # 查找元素 x 所在集合的代表元素
        rt, fa = x, self.fa
        while fa[rt] != rt:
            rt = fa[rt]
        while fa[x] != rt:
            fa[x], x = rt, fa[x]
        return rt

    def union(self, i: int, j: int): # 合并元素 i 和 j 所在的集合
        fa, rank, num = self.fa, self.rank, self.num
        x, y = self.find(i), self.find(j)
        if rank[x] <= rank[y]:
            fa[x] = y
        else:
            fa[y] = x
        if rank[x] == rank[y] and x != y:
            rank[y] += 1
        if x != y:
            num[x] = num[y] = num[x] + num[y]

    def check(self, i: int, j: int) -> bool: # 判断元素 i 和 j 是否属于同一集合
        return self.find(i) == self.find(j)

    def number(self, x: int) -> int: # 查询元素 x 所在集合的元素个数
        return self.num[self.find(x)]

    def total(self) -> int: # 查询不同集合的总数
        for i in range(self.n):
            self.fa[i] = self.find(i)
        return len(set(self.fa))