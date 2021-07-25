# *_*coding:utf-8 *_*
'''
Descri：
'''
import datetime
import tushare as ts
from settings.envs import CONFIG

tokens = CONFIG['tushare_tokens']

today = datetime.datetime.now().strftime("%Y%m%d")
# 至少是800积分
pro = ts.pro_api(
    '15cbb84b1fdd9a026aee178b4a1aae1543aaef4b4a08866f4f0c27f1'
)
# ts.set_token(
df = pro.forecast(ann_date='20190131', fields='ts_code,ann_date,end_date,type,p_change_min,p_change_max,net_profit_min')
print(df)