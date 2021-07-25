from .json_file import read_json_line, write_json_line, jsonify, content
from .PyHtml import *
from .multi_proc import parallelize

def open_file(file):
    with open(file) as f:
        for row in f.readlines():
            yield row.strip()

__all__ = [
    "read_json_line",
    "write_json_line",
    "table_blue",
    "table_red",
    "table_green",
    "color_table",
    "jsonify",
    "content",
    "parallelize",
]
