# *_*coding:utf-8 *_*
"""
Author：szj
输出参数

名称	类型	描述
ts_code	str	TS代码
symbol	str	股票代码
name	str	股票名称
area	str	所在地域
industry	str	所属行业
fullname	str	股票全称
enname	str	英文全称
market	str	市场类型 （主板/中小板/创业板/科创板）
exchange	str	交易所代码
curr_type	str	交易货币
list_status	str	上市状态： L上市 D退市 P暂停上市
list_date	str	上市日期
delist_date	str	退市日期
is_hs	str	是否沪深港通标的，N否 H沪股通 S深股通
"""
import sys, os
from pathlib import Path

ROOT = Path(os.path.abspath(__file__)).parent.parent
sys.path.append(str(ROOT))
import tushare as ts
import datetime
from settings.envs import *
from tenacity import retry, wait_fixed, wait_random
from settings.sqls import tushare_stock_basic
from critical_investing import mysql
from random import choice
from utils.common import now
import doger

logger = doger.guru(LOG_LEVEL, __file__)
token_list = CONFIG["tushare_tokens"]

if 0 < datetime.datetime.now().hour < 15:
    today = now(num=-1, lever=False)[0:8]  # 20210203
else:
    today = now(lever=False)[0:8]  # 20210203


@retry(wait=wait_fixed(3) + wait_random(3, 5))
def get_stock_basic():
    token = choice(token_list)  # 随机选择一个token
    pro = ts.pro_api(token)
    # 查询当前所有正常上市交易的股票列表
    df = pro.query(
        "stock_basic",
        exchange="",
        list_status="L",
        fields="ts_code,symbol,name,fullname,enname,area,industry,market,exchange,is_hs,list_date",
    )
    return df


if __name__ == "__main__":
    token = choice(token_list)  # 随机选择一个token
    pro = ts.pro_api(token)
    trade_calendar = pro.query("trade_cal", start_date=today, end_date=today)
    # 判断是否是交易日，只有交易日才更新
    if trade_calendar["is_open"].values[0] or 1:
        df = get_stock_basic()
        logger.info(df)
        STOCK_BASIC_TABLE = tushare_stock_basic.TABLE

        if not df.empty:
            mysql.truncate_table(table=STOCK_BASIC_TABLE)
            mysql.insert_df(table=STOCK_BASIC_TABLE, df=df, cols=df.columns.tolist())
