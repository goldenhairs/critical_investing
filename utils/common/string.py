# -*- coding: utf-8 -*-
from collections import defaultdict


# author: [bojone](https://github.com/bojone)
# source code link: [bert4keras/snippets.py](https://github.com/bojone/bert4keras/blob/master/bert4keras/snippets.py)
def longest_common_substring(source, target):
    """最长公共子串（source和target的最长公共切片区间）
    返回：子串长度, 所在区间（四元组）
    注意：最长公共子串可能不止一个，所返回的区间只代表其中一个。
    """
    c, l, span = defaultdict(int), 0, (0, 0, 0, 0)
    for i, si in enumerate(source, 1):
        for j, tj in enumerate(target, 1):
            if si == tj:
                c[i, j] = c[i - 1, j - 1] + 1
                if c[i, j] > l:
                    l = c[i, j]
                    span = (i - l, i, j - l, j)
    return l, span


# author: [bojone](https://github.com/bojone)
# source code link: [bert4keras/snippets.py](https://github.com/bojone/bert4keras/blob/master/bert4keras/snippets.py)
def longest_common_subsequence(source, target):
    """最长公共子序列（source和target的最长非连续子序列）
    返回：子序列长度, 映射关系（映射对组成的list）
    注意：最长公共子序列可能不止一个，所返回的映射只代表其中一个。
    """
    c = defaultdict(int)
    for i, si in enumerate(source, 1):
        for j, tj in enumerate(target, 1):
            if si == tj:
                c[i, j] = c[i - 1, j - 1] + 1
            elif c[i, j - 1] > c[i - 1, j]:
                c[i, j] = c[i, j - 1]
            else:
                c[i, j] = c[i - 1, j]
    l, mapping = c[len(source), len(target)], []
    i, j = len(source) - 1, len(target) - 1
    while len(mapping) < l:
        if source[i] == target[j]:
            mapping.append((i, j))
            i, j = i - 1, j - 1
        elif c[i + 1, j] > c[i, j + 1]:
            j = j - 1
        else:
            i = i - 1
    return l, mapping[::-1]
