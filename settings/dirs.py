# *_*coding:utf-8 *_*
'''
Descri：
'''
from os.path import dirname, abspath, join



# 获取项目根目录
ROOT = dirname(dirname(abspath(__file__)))

# 数据文件存放路径
DATASETS_DIR = join(ROOT, "datasets")

# 图片文件路径
IMAGES_DIR = join(DATASETS_DIR, "images")

# 字体文件路径
FONTS_DIR = join(DATASETS_DIR, "fonts")

# 结果文件路径
RESULTS_DIR = join(DATASETS_DIR, "results")

# log文件路径
LOGS_DIR = join(DATASETS_DIR, "logs")
