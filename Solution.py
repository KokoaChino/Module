from collections import Counter
from typing import List, Callable
from math import inf
from BeatCode import BeatCode
from random import randint


def ac_fun(a: int, b: int) -> int:  # 正确代码
    return a + b


def my_fun(a: int, b: int) -> int:  # 测试代码
    return abs(a + b)


def get_params() -> list:  # 测试样例
    res = []
    for _ in range(500):
        res.append([randint(-10000, 10 ** 5), randint(-10000, 10 ** 5)])
    return res


BeatCode.run(ac_fun, my_fun, get_params())  # 开始对拍
