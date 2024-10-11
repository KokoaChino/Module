def longestCommonSubsequence(arr1: list, arr2: list) -> int:
    """最长公共子序列"""
    f = [0] * (len(arr2) + 1)
    for x in arr1:
        pre = 0
        for j, y in enumerate(arr2):
            pre, f[j + 1] = f[j + 1], pre + 1 if x == y else max(f[j], f[j + 1])
    return f[-1]

def longestCommonSubsequence(s: str, t: str) -> int:
    """最长公共子序列"""
    f = [0] * (len(t) + 1)
    for x in s:
        pre = 0
        for j, y in enumerate(t):
            pre, f[j + 1] = f[j + 1], pre + 1 if x == y else max(f[j], f[j + 1])
    return f[-1]