import json
import os


def read_json_line(filename: str, error_file: str = None):
    """
    从文件中逐行获取json对象
    :param filename: json文件名
    :param error_file: 保存错误信息的文件路径，若不指定则系统默认当前执行路径下`error.log`文件
    :return: json object 迭代器
    """
    if not error_file:
        error_file = os.path.abspath(".") + os.sep + "error.log"
    with open(filename, encoding="utf-8") as f:
        line_count = 0
        for line in f:
            line_count += 1
            try:
                json_line = json.loads(line.strip())
                yield json_line
            except Exception as e:
                with open(error_file, "a+", encoding="utf-8") as err_f:
                    err_f.write("line{}: {}".format(line_count, line))
                    continue


def write_json_line(file_obj, json_obj):
    """
    将数据对象以json格式写入到文件中
    :param file_obj: 文件对象
    :param json_obj: 可以被序列化为json字符串的数据对象
    :return:
    """
    file_obj.write(json.dumps(json_obj, ensure_ascii=False))
    file_obj.write("\n")


def jsonify(data: dict):
    """
    format the dict data
    :param data:
    :return:
    """
    return json.dumps(data, indent=2, ensure_ascii=False, default=str)


def content(file_path, encoding="utf-8"):
    """
    get content of html file
    :param encoding: file encoding
    :param file_path:
    :return:
    """
    with open(file_path, encoding=encoding) as f:
        return f.read()


if __name__ == "__main__":
    data = {"d": 2, "c": 4}
    jf = jsonify(data=data)
    print(jf)
