# -*- coding: utf-8 -*-
import os
from typing import Union, List


class NotSpecifiedFileException(Exception):
    def __init__(self, info: Union[str, List[str]]):
        if isinstance(info, str):
            self._info = info
        else:
            self._info = "/".join(info)

    def __str__(self):
        return "并非指定的文件错误，应该是形如：xx.{}".format(self._info)


def check_file(file_path: str, ext: Union[str, List[str]] = None):
    if not os.path.exists(file_path):
        raise FileNotFoundError
    if ext:
        if isinstance(ext, str) and not file_path.endswith(ext):
            raise NotSpecifiedFileException(ext)
        if isinstance(ext, list):
            file_ext = os.path.splitext(file_path)[-1]
            if file_ext:
                file_ext = file_ext[1:]
            if file_ext not in ext:
                raise NotSpecifiedFileException(ext)


def get_pure_filename(file_path: str):
    """获取文件名，例如：

    :param file_path: fuck/fuck/fuck.txt -> fuck
    :return: 文件名，不含拓展名
    """
    _, name = os.path.split(file_path)
    file_name, _ = os.path.splitext(name)
    return file_name


if __name__ == "__main__":
    # check_file('fuck.txt', 'txt')
    # check_file('__init__.py', 'txt')
    check_file("__init__.py", "py")
    check_file("__init__.py", ["py", "pyw"])
    print(get_pure_filename("hello_world.py"))
