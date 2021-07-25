# *_*coding:utf-8 *_*
"""
Author：szj
Descri：
"""
import sys, os
from pathlib import Path

ROOT = Path(os.path.abspath(__file__)).parent.parent
sys.path.append(str(ROOT))
import traceback

import click
from critical_investing import mysql
from tenacity import retry, wait_fixed, wait_random

from settings import files
from settings.sqls import tushare_fina_indicator, tushare_income

import tushare as ts
import pandas as pd
import datetime
import random
import datetime
from random import choice
from sqlitedict import SqliteDict
from settings.envs import *
import doger
logger = doger.guru(LOG_LEVEL, __file__)

# token_list = env.get_tushare_token()
token_list = [
    "c473f86ae2f5703f58eecf9864fa9ec91d67edbc01e3294f6a4f9c32",
    "8245313cabb6239a4dce3591e2c64fa199611ee7ade564cf9e437b61",
    "d94b8d1af9f3110dca7acf2e85b4bf10b7d33de74491de8f671c4b8b",
]
token = choice(token_list)  # 随机选择一个token
pro = ts.pro_api(token)

today = datetime.datetime.now().strftime("%Y%m%d")
yesterday = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y%m%d")

"""
输入参数

名称	类型	必选	描述
ts_code	str	Y	股票代码
ann_date	str	N	公告日期
start_date	str	N	公告开始日期
end_date	str	N	公告结束日期
period	str	N	报告期(每个季度最后一天的日期，比如20171231表示年报)
report_type	str	N	报告类型： 参考下表说明
comp_type	str	N	公司类型：1一般工商业 2银行 3保险 4证券
输出参数

名称	类型	默认显示	描述
ts_code	str	Y	TS代码
ann_date	str	Y	公告日期
f_ann_date	str	Y	实际公告日期
end_date	str	Y	报告期
report_type	str	Y	报告类型 1合并报表 2单季合并 3调整单季合并表 4调整合并报表 5调整前合并报表 6母公司报表 7母公司单季表 8 母公司调整单季表 9母公司调整表 10母公司调整前报表 11调整前合并报表 12母公司调整前报表
comp_type	str	Y	公司类型(1一般工商业2银行3保险4证券)
basic_eps	float	Y	基本每股收益
diluted_eps	float	Y	稀释每股收益
total_revenue	float	Y	营业总收入
revenue	float	Y	营业收入
int_income	float	Y	利息收入
prem_earned	float	Y	已赚保费
comm_income	float	Y	手续费及佣金收入
n_commis_income	float	Y	手续费及佣金净收入
n_oth_income	float	Y	其他经营净收益
n_oth_b_income	float	Y	加:其他业务净收益
prem_income	float	Y	保险业务收入
out_prem	float	Y	减:分出保费
une_prem_reser	float	Y	提取未到期责任准备金
reins_income	float	Y	其中:分保费收入
n_sec_tb_income	float	Y	代理买卖证券业务净收入
n_sec_uw_income	float	Y	证券承销业务净收入
n_asset_mg_income	float	Y	受托客户资产管理业务净收入
oth_b_income	float	Y	其他业务收入
fv_value_chg_gain	float	Y	加:公允价值变动净收益
invest_income	float	Y	加:投资净收益
ass_invest_income	float	Y	其中:对联营企业和合营企业的投资收益
forex_gain	float	Y	加:汇兑净收益
total_cogs	float	Y	营业总成本
oper_cost	float	Y	减:营业成本
int_exp	float	Y	减:利息支出
comm_exp	float	Y	减:手续费及佣金支出
biz_tax_surchg	float	Y	减:营业税金及附加
sell_exp	float	Y	减:销售费用
admin_exp	float	Y	减:管理费用
fin_exp	float	Y	减:财务费用
assets_impair_loss	float	Y	减:资产减值损失
prem_refund	float	Y	退保金
compens_payout	float	Y	赔付总支出
reser_insur_liab	float	Y	提取保险责任准备金
div_payt	float	Y	保户红利支出
reins_exp	float	Y	分保费用
oper_exp	float	Y	营业支出
compens_payout_refu	float	Y	减:摊回赔付支出
insur_reser_refu	float	Y	减:摊回保险责任准备金
reins_cost_refund	float	Y	减:摊回分保费用
other_bus_cost	float	Y	其他业务成本
operate_profit	float	Y	营业利润
non_oper_income	float	Y	加:营业外收入
non_oper_exp	float	Y	减:营业外支出
nca_disploss	float	Y	其中:减:非流动资产处置净损失
total_profit	float	Y	利润总额
income_tax	float	Y	所得税费用
n_income	float	Y	净利润(含少数股东损益)
n_income_attr_p	float	Y	净利润(不含少数股东损益)
minority_gain	float	Y	少数股东损益
oth_compr_income	float	Y	其他综合收益
t_compr_income	float	Y	综合收益总额
compr_inc_attr_p	float	Y	归属于母公司(或股东)的综合收益总额
compr_inc_attr_m_s	float	Y	归属于少数股东的综合收益总额
ebit	float	Y	息税前利润
ebitda	float	Y	息税折旧摊销前利润
insurance_exp	float	Y	保险业务支出
undist_profit	float	Y	年初未分配利润
distable_profit	float	Y	可分配利润
update_flag	str	N	更新标识，0未修改1更正过
主要报表类型说明

代码	类型	说明
1	合并报表	上市公司最新报表（默认）
2	单季合并	单一季度的合并报表
3	调整单季合并表	调整后的单季合并报表（如果有）
4	调整合并报表	本年度公布上年同期的财务报表数据，报告期为上年度
5	调整前合并报表	数据发生变更，将原数据进行保留，即调整前的原数据
6	母公司报表	该公司母公司的财务报表数据
7	母公司单季表	母公司的单季度表
8	母公司调整单季表	母公司调整后的单季表
9	母公司调整表	该公司母公司的本年度公布上年同期的财务报表数据
10	母公司调整前报表	母公司调整之前的原始财务报表数据
11	调整前合并报表	调整之前合并报表原数据
12	母公司调整前报表	母公司报表发生变更前保留的原数据
"""


@retry(wait=wait_fixed(3) + wait_random(3, 5))
def get_stock_income(stock):
    token = choice(token_list)  # 随机选择一个token
    pro = ts.pro_api(token)
    # 获取单只股票的利润表数据
    df = pro.income(ts_code=stock, start_date="20130101", end_date=today)
    # time.sleep(np.random.randint(0, 3))
    return df


@click.command()
@click.option(
    "-t",
    "--table",
    default=tushare_income.TABLE,
    show_default=True,
    type=str,
    help="需要插入数据的表名.",
)
@click.option(
    "-s",
    "--start_from_scratch",
    default=False,
    show_default=True,
    type=bool,
    help="Whether or not start from scratch, 1 represent True and 0 is False.",
)
def run(table, start_from_scratch):
    if start_from_scratch:  # bool 是否从头开始爬，False则从上次结束的地方开始
        dictionarydb[SCRAPYED_ITEMS_KEYNAME] = []
    try:
        # 获取A股上市股票列表
        stock_basic = pro.query(
            "stock_basic",
            exchange="",
            list_status="L",
            fields="ts_code,symbol,name,fullname,enname,area,industry,market,exchange,is_hs,list_date",
        )

        scrapyed_items = dictionarydb.get(SCRAPYED_ITEMS_KEYNAME, [])  # 记录处理过的股票数据

        # 遍历股票
        for i, row in stock_basic.iterrows():
            stock = row["ts_code"]
            # 如果股票没有爬取过，则进行处理
            if not stock in scrapyed_items:
                logger.info(f'第{i}只股票：{stock}')
                # 描述：获取上市公司财务指标数据，为避免服务器压力，现阶段每次请求最多返回60条记录，可通过设置日期多次请求获取更多数据。
                df = get_stock_income(stock)  # 获取股票财务指标数据
                if df.empty:  # 如果财务数据为空，则不进行下一步
                    logger.info("该股票没有利润数据：", row)
                else:
                    col_name = df.columns.tolist()
                    col_name.insert(col_name.index("ts_code"), "id")  # 在 ts_code 列前面插入
                    df = df.reindex(columns=col_name)
                    df["id"] = df["ts_code"].map(str) + df["end_date"].map(str)

                    cols = df.columns.tolist()
                    mysql.insert_df(table=table, df=df, cols=cols)

                # 把保存到数据库的股票代码记录一下
                scrapyed_items.append(stock)
                dictionarydb[SCRAPYED_ITEMS_KEYNAME] = scrapyed_items
            else:
                pass  # 如果股票保存过，则跳过
        logger.info("A股所有利润数据爬取完成！")
        dictionarydb[SCRAPYED_ITEMS_KEYNAME] = []  # 把爬取过的股票清空，下次继续从头爬取
    except:
        error = traceback.format_exc()
        sys.stderr.write(error)
        logger.info("Token：", token)


if __name__ == "__main__":
    dictionarydb = SqliteDict(
        files.SQLITE_DICT, tablename="tushare", autocommit=True
    )  # access the db

    TUSHARE_INCOME = tushare_income.TABLE
    SCRAPYED_ITEMS_KEYNAME = TUSHARE_INCOME  # 存放爬取过的股票代码的字典名

    run()


if __name__ == "__main__1":
    df = pro.income(ts_code="600000.SH", start_date="20180101", end_date=today)
    print(df)
    col_name = df.columns.tolist()
    col_name.insert(col_name.index("ts_code"), "id")  # 在 ts_code 列前面插入
    df = df.reindex(columns=col_name)
    df["id"] = df["ts_code"].map(str) + df["end_date"].map(str)

    for i in df.dtypes:
        print(i)

    TABLE = tushare_income.TABLE  # 需更改表名
    mysql.drop_table(table=TABLE)  # 删除表
    mysql.create_table_from_df(table=TABLE, df=df, primary_key="id")  # 创建表

    cols = df.columns.tolist()
    mysql.insert_df(table=TABLE, df=df, cols=cols)  # 插入表
