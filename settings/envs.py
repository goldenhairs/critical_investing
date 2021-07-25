from os.path import join, dirname, abspath
from pprint import pprint

from environs import Env
import just
# https://github.com/sloria/environs
env = Env()

# definition of dirs
CURRENT_PATH = abspath(dirname(__file__))
# print(CURRENT_PATH)
CONFIG = just.read(join(CURRENT_PATH, '.config.json'))
LOG_DIR = join(CURRENT_PATH, env.str('LOG_DIR', 'logs'))

# read env config
env.read_env(join(dirname(CURRENT_PATH),'config.cfg'))
MYSQL_ALIAS = env('MYSQL_ALIAS','localhost')
MYSQL_ALIAS_DB = env('MYSQL_ALIAS_DB', 'default')

# definition of environments

########## mysql ##########
with env.prefixed("MYSQL_"):
    MYSQL_CONFIG = env.dict("CONFIG", CONFIG['mysqldbs'].get(MYSQL_ALIAS))
    MYSQL_HOST = env.str("HOST", MYSQL_CONFIG.get('host','localhost'))
    MYSQL_PORT = env.int("PORT", MYSQL_CONFIG.get('port','3306'))
    MYSQL_USER = env.str("USER", MYSQL_CONFIG.get('user','🐳🐳🐳'))
    MYSQL_PASSWD = env.str("PASSWD", MYSQL_CONFIG.get('passwd','The password is None!'))
    MYSQL_DB = env.str("DB", MYSQL_CONFIG.get('db','🐳🐳🐳') if MYSQL_ALIAS_DB == 'default' else MYSQL_ALIAS_DB)
    MYSQL_CHARSET = env.str("CHARSET", MYSQL_CONFIG.get('charset','utf8mb'))

# loger
LOG_LEVEL = env.log_level("LOG_LEVEL", "DEBUG")





