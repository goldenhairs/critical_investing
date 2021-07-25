# *_*coding:utf-8 *_*
# TODO：加商誉，质押率，负债率，存货，营收账款，净利润
import datetime
import tushare as ts
from settings.envs import CONFIG

tokens = CONFIG['tushare_tokens']

today = datetime.datetime.now().strftime("%Y%m%d")
for token in tokens:
    # 至少是800积分
    pro = ts.pro_api(token)
    df = pro.forecast(ann_date='20190131',
                      fields='ts_code,ann_date,end_date,type,p_change_min,p_change_max,net_profit_min')
    print(df)

