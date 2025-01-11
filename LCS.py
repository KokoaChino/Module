def longestCommonSubsequence(arr1: list, arr2: list) -> int:
    """最长公共子序列"""
    f = [0] * (len(arr2) + 1)
    for x in arr1:
        pre = 0
        for j, y in enumerate(arr2):
            pre, f[j + 1] = f[j + 1], pre + 1 if x == y else max(f[j], f[j + 1])
    return f[-1]