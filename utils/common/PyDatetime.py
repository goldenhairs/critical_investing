# *_*coding:utf-8 *_*
"""
Author：szj
Descri：
"""
import datetime, time
from functools import wraps

from .time_format import time_convert


# 装饰器函数
def timecount(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration_time = end_time - start_time
        print("函数 %s 执行时间: %s" % (func.__name__, time_convert(duration_time)))
        return result

    return wrapper


def now(num: int = 0, dtype: str = "days", lever=True):
    """

    :param num: 加减的时间数量
    :param dtype: 加减的时间日期类型：weeks, days, hours, minutes
    :param lever: 日期格式是否带杠，默认 2020-11-15 16:36:00 形式
    :return:
    """

    if lever:
        dateformat = "%Y-%m-%d %H:%M:%S"
    else:
        dateformat = "%Y%m%d %H:%M:%S"

    if dtype == "days":
        return (datetime.datetime.now() + datetime.timedelta(days=+num)).strftime(
            dateformat
        )
    elif dtype == "weeks":
        return (datetime.datetime.now() + datetime.timedelta(weeks=+num)).strftime(
            dateformat
        )
    elif dtype == "minutes":
        return (datetime.datetime.now() + datetime.timedelta(minutes=+num)).strftime(
            dateformat
        )
    elif dtype == "hours":
        return (datetime.datetime.now() + datetime.timedelta(hours=+num)).strftime(
            dateformat
        )
