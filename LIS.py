import bisect

def lengthOfLIS(nums: list) -> int:
    """最长递增子序列"""
    g = []
    for x in nums:
        i = bisect.bisect_left(g, x)
        if i == len(g):
            g.append(x)
        else:
            g[i] = x
    return len(g)