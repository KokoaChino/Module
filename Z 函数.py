def calc_z(s: str) -> list: # Z 函数
    n = len(s)
    z = [0] * n
    z[0] = n
    box_l = box_r = 0
    for i in range(1, n):
        if i <= box_r:
            z[i] = z[i - box_l] if z[i - box_l] < box_r - i + 1 else box_r - i + 1
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            box_l, box_r = i, i + z[i]
            z[i] += 1
    return z
