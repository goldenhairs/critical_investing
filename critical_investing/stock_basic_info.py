# *_*coding:utf-8 *_*
"""
Author：szj
输出参数

名称	类型	默认显示	描述
ts_code	str	Y	股票代码
exchange	str	Y	交易所代码 ，SSE上交所 SZSE深交所
chairman	str	Y	法人代表
manager	str	Y	总经理
secretary	str	Y	董秘
reg_capital	float	Y	注册资本
setup_date	str	Y	注册日期
province	str	Y	所在省份
city	str	Y	所在城市
introduction	str	N	公司介绍
website	str	Y	公司主页
email	str	Y	电子邮件
office	str	N	办公室
employees	int	Y	员工人数
main_business	str	N	主要业务及产品
business_scope	str	N	经营范围
"""
import sys, os
from pathlib import Path

ROOT = Path(os.path.abspath(__file__)).parent.parent
sys.path.append(str(ROOT))
import tushare as ts
import datetime
from critical_investing import mysql

from settings.sqls import tushare_stock_basic_info
from random import choice
from utils.common import now
from settings.envs import *
import doger

logger = doger.guru(LOG_LEVEL, __file__)

token_list = CONFIG['tushare_tokens']
token = choice(token_list)  # 随机选择一个token
ts.set_token(token)
pro = ts.pro_api()

if 0 < datetime.datetime.now().hour < 15:
    today = now(num=-1, lever=False)[0:8]  # 20210203
else:
    today = now(lever=False)[0:8]  # 20210203

logger.info("today: ", today)


if __name__ == "__main__":
    trade_calendar = pro.query("trade_cal", start_date=today, end_date=today)
    # 判断是否是交易日，只有交易日才更新
    if trade_calendar["is_open"].values[0]:
        # 查询当前所有正常上市交易的股票列表=
        data = pro.stock_company(
            exchange="SZSE",
            fields="ts_code,exchange,chairman,manager,secretary,reg_capital,setup_date,province,city,introduction,website,email,office,employees,main_business,business_scope",
        )
        data2 = pro.stock_company(
            exchange="SSE",
            fields="ts_code,exchange,chairman,manager,secretary,reg_capital,setup_date,province,city,introduction,website,email,office,employees,main_business,business_scope",
        )
        # exchange交易所代码 ，SSE上交所 SZSE深交所
        df = data.append(data2)
        logger.info(df)

        STOCK_BASIC_INFO_TABLE = tushare_stock_basic_info.TABLE
        # mysql.drop_table(table=STOCK_BASIC_INFO_TABLE)
        # mysql.create_table_from_df(table=STOCK_BASIC_INFO_TABLE, df=df)

        if not df.empty:
            mysql.truncate_table(table=STOCK_BASIC_INFO_TABLE)
            cols = df.columns.tolist()
            mysql.insert_df(table=STOCK_BASIC_INFO_TABLE, df=df, cols=cols)
