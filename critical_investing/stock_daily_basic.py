# *_*coding:utf-8 *_*
"""
Author：szj
Descri：
"""
import sys, os
from pathlib import Path

ROOT = Path(os.path.abspath(__file__)).parent.parent
sys.path.append(str(ROOT))
import tushare as ts
import datetime
from random import choice
from utils.common import now
from critical_investing import mysql
from tenacity import retry, wait_fixed, wait_random

from settings.sqls import tushare_fina_indicator, tushare_daily_basic

from settings.envs import CONFIG


token_list = CONFIG['tushare_tokens']
token = choice(token_list)  # 随机选择一个token
pro = ts.pro_api(token)

# today = datetime.datetime.now().strftime(
#                 "%Y%m%d")
# yesterday = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime(
#                 "%Y%m%d")

# 更新时间：交易日每日15点～17点之间
if 0 < datetime.datetime.now().hour < 15:
    today = now(num=-1, lever=False)[0:8]  # 20210203
else:
    today = now(lever=False)[0:8]  # 20210203

print("today: ", today)
"""
输出参数

名称	类型	描述
ts_code	str	TS股票代码
trade_date	str	交易日期
close	float	当日收盘价
turnover_rate	float	换手率（%）
turnover_rate_f	float	换手率（自由流通股）
volume_ratio	float	量比
pe	float	市盈率（总市值/净利润， 亏损的PE为空）
pe_ttm	float	市盈率（TTM，亏损的PE为空）
pb	float	市净率（总市值/净资产）
ps	float	市销率
ps_ttm	float	市销率（TTM）
dv_ratio	float	股息率 （%）
dv_ttm	float	股息率（TTM）（%）
total_share	float	总股本 （万股）
float_share	float	流通股本 （万股）
free_share	float	自由流通股本 （万）
total_mv	float	总市值 （万元）
circ_mv	float	流通市值（万元）
"""


# 获取某只股票的行情数据
# df = pro.daily_basic(ts_code='', trade_date='20180726', fields='ts_code,trade_date,turnover_rate,volume_ratio,pe,pb')
# print(df)

# 也可以通过日期取历史某一天的全部历史
# df = pro.query('daily_basic', ts_code='', trade_date=today,fields='ts_code,trade_date,close,pe,pe_ttm,pb,ps,ps_ttm,dv_ratio,dv_ttm,total_share,float_share,free_share,total_mv,circ_mv')
# print(df)
# print(df.columns)


@retry(wait=wait_fixed(3) + wait_random(3, 5))
def get_daily_basic():
    token = choice(token_list)  # 随机选择一个token
    pro = ts.pro_api(token)
    df = pro.query(
        "daily_basic",
        ts_code="",
        trade_date=today,
        fields="ts_code,trade_date,close,volume_ratio,pe,pe_ttm,pb,ps,ps_ttm,dv_ratio,dv_ttm,total_share,float_share,free_share,total_mv,circ_mv",
    )

    # time.sleep(np.random.randint(0, 3))
    return df


if __name__ == "__main__":
    trade_calendar = pro.query("trade_cal", start_date=today, end_date=today)
    # 判断是否是交易日，只有交易日才更新
    if trade_calendar["is_open"].values[0]:
        df = get_daily_basic()
        print(df)
        if not df.empty:
            mysql.truncate_table(tushare_daily_basic.TABLE)
            # mysql.create_table_from_df(table=tushare_daily_basic.TABLE,df=df)
            mysql.insert_df(
                table=tushare_daily_basic.TABLE, df=df, cols=df.columns.tolist()
            )
