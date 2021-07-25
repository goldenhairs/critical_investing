# -*- coding: utf-8 -*-


def batch(iterable, n=10):
    """
    将迭代器转换为返回批量数据的形式
    :param iterable: 待转换迭代器
    :param n: 每批数据容量
    :return: 批量数据迭代器
    """
    iterable = iter(iterable)
    while True:
        chunk = []
        for i in range(n):
            try:
                chunk.append(next(iterable))
            except StopIteration:
                if chunk:
                    yield chunk
                return
        yield chunk


def cutoff_iter(iterable, n=10):
    """
    将迭代器截断只返回前面一部分，类似linux中的head命令
    :param iterable:
    :param n:
    :return:
    """
    iterable = iter(iterable)
    try:
        for i in range(n):
            yield next(iterable)
    except StopIteration:
        return
