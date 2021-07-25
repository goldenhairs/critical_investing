# -*- coding: utf-8 -*-

# author: [bojone](https://github.com/bojone)
# source code link: [text_compare/compare.py](https://github.com/bojone/text_compare/blob/master/compare.py)
from .string import longest_common_subsequence


def red_color(text):
    return u"\033[1;31m%s\033[0m" % text


def green_color(text):
    return u"\033[32m%s\033[0m" % text


def blue_color(text):
    return u"\033[1;34m%s\033[0m" % text


def string_compare(source, target):
    _, mapping = longest_common_subsequence(source, target)
    source_idxs = set([i for i, j in mapping])
    target_idxs = set([j for i, j in mapping])
    colored_source, colored_target = u"", u""
    for i, j in enumerate(source):
        if i in source_idxs:
            colored_source += green_color(j)
        else:
            colored_source += red_color(j)
    for i, j in enumerate(target):
        if i in target_idxs:
            colored_target += green_color(j)
        else:
            colored_target += blue_color(j)
    print(colored_source)
    print(colored_target)
