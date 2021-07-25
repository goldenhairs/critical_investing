# *_*coding:utf-8 *_*
from settings.envs import *
import mysqling

mysql = mysqling.register(
    host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=MYSQL_DB
)