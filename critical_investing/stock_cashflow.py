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

from critical_investing import mysql
from tenacity import retry, wait_fixed, wait_random

from settings.sqls import tushare_cashflow
from settings import files


import tushare as ts
import datetime
from random import choice
from sqlitedict import SqliteDict
from settings.envs import *
import doger
logger = doger.guru(LOG_LEVEL, __file__)
from settings.envs import CONFIG

token_list = CONFIG["tushare_tokens"]
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
report_type	str	N	报告类型：见下方详细说明
comp_type	str	N	公司类型：1一般工商业 2银行 3保险 4证券
输出参数

名称	类型	默认显示	描述
ts_code	str	Y	TS股票代码
ann_date	str	Y	公告日期
f_ann_date	str	Y	实际公告日期
end_date	str	Y	报告期
comp_type	str	Y	公司类型
report_type	str	Y	报表类型
net_profit	float	Y	净利润
finan_exp	float	Y	财务费用
c_fr_sale_sg	float	Y	销售商品、提供劳务收到的现金
recp_tax_rends	float	Y	收到的税费返还
n_depos_incr_fi	float	Y	客户存款和同业存放款项净增加额
n_incr_loans_cb	float	Y	向中央银行借款净增加额
n_inc_borr_oth_fi	float	Y	向其他金融机构拆入资金净增加额
prem_fr_orig_contr	float	Y	收到原保险合同保费取得的现金
n_incr_insured_dep	float	Y	保户储金净增加额
n_reinsur_prem	float	Y	收到再保业务现金净额
n_incr_disp_tfa	float	Y	处置交易性金融资产净增加额
ifc_cash_incr	float	Y	收取利息和手续费净增加额
n_incr_disp_faas	float	Y	处置可供出售金融资产净增加额
n_incr_loans_oth_bank	float	Y	拆入资金净增加额
n_cap_incr_repur	float	Y	回购业务资金净增加额
c_fr_oth_operate_a	float	Y	收到其他与经营活动有关的现金
c_inf_fr_operate_a	float	Y	经营活动现金流入小计
c_paid_goods_s	float	Y	购买商品、接受劳务支付的现金
c_paid_to_for_empl	float	Y	支付给职工以及为职工支付的现金
c_paid_for_taxes	float	Y	支付的各项税费
n_incr_clt_loan_adv	float	Y	客户贷款及垫款净增加额
n_incr_dep_cbob	float	Y	存放央行和同业款项净增加额
c_pay_claims_orig_inco	float	Y	支付原保险合同赔付款项的现金
pay_handling_chrg	float	Y	支付手续费的现金
pay_comm_insur_plcy	float	Y	支付保单红利的现金
oth_cash_pay_oper_act	float	Y	支付其他与经营活动有关的现金
st_cash_out_act	float	Y	经营活动现金流出小计
n_cashflow_act	float	Y	经营活动产生的现金流量净额
oth_recp_ral_inv_act	float	Y	收到其他与投资活动有关的现金
c_disp_withdrwl_invest	float	Y	收回投资收到的现金
c_recp_return_invest	float	Y	取得投资收益收到的现金
n_recp_disp_fiolta	float	Y	处置固定资产、无形资产和其他长期资产收回的现金净额
n_recp_disp_sobu	float	Y	处置子公司及其他营业单位收到的现金净额
stot_inflows_inv_act	float	Y	投资活动现金流入小计
c_pay_acq_const_fiolta	float	Y	购建固定资产、无形资产和其他长期资产支付的现金
c_paid_invest	float	Y	投资支付的现金
n_disp_subs_oth_biz	float	Y	取得子公司及其他营业单位支付的现金净额
oth_pay_ral_inv_act	float	Y	支付其他与投资活动有关的现金
n_incr_pledge_loan	float	Y	质押贷款净增加额
stot_out_inv_act	float	Y	投资活动现金流出小计
n_cashflow_inv_act	float	Y	投资活动产生的现金流量净额
c_recp_borrow	float	Y	取得借款收到的现金
proc_issue_bonds	float	Y	发行债券收到的现金
oth_cash_recp_ral_fnc_act	float	Y	收到其他与筹资活动有关的现金
stot_cash_in_fnc_act	float	Y	筹资活动现金流入小计
free_cashflow	float	Y	企业自由现金流量
c_prepay_amt_borr	float	Y	偿还债务支付的现金
c_pay_dist_dpcp_int_exp	float	Y	分配股利、利润或偿付利息支付的现金
incl_dvd_profit_paid_sc_ms	float	Y	其中:子公司支付给少数股东的股利、利润
oth_cashpay_ral_fnc_act	float	Y	支付其他与筹资活动有关的现金
stot_cashout_fnc_act	float	Y	筹资活动现金流出小计
n_cash_flows_fnc_act	float	Y	筹资活动产生的现金流量净额
eff_fx_flu_cash	float	Y	汇率变动对现金的影响
n_incr_cash_cash_equ	float	Y	现金及现金等价物净增加额
c_cash_equ_beg_period	float	Y	期初现金及现金等价物余额
c_cash_equ_end_period	float	Y	期末现金及现金等价物余额
c_recp_cap_contrib	float	Y	吸收投资收到的现金
incl_cash_rec_saims	float	Y	其中:子公司吸收少数股东投资收到的现金
uncon_invest_loss	float	Y	未确认投资损失
prov_depr_assets	float	Y	加:资产减值准备
depr_fa_coga_dpba	float	Y	固定资产折旧、油气资产折耗、生产性生物资产折旧
amort_intang_assets	float	Y	无形资产摊销
lt_amort_deferred_exp	float	Y	长期待摊费用摊销
decr_deferred_exp	float	Y	待摊费用减少
incr_acc_exp	float	Y	预提费用增加
loss_disp_fiolta	float	Y	处置固定、无形资产和其他长期资产的损失
loss_scr_fa	float	Y	固定资产报废损失
loss_fv_chg	float	Y	公允价值变动损失
invest_loss	float	Y	投资损失
decr_def_inc_tax_assets	float	Y	递延所得税资产减少
incr_def_inc_tax_liab	float	Y	递延所得税负债增加
decr_inventories	float	Y	存货的减少
decr_oper_payable	float	Y	经营性应收项目的减少
incr_oper_payable	float	Y	经营性应付项目的增加
others	float	Y	其他
im_net_cashflow_oper_act	float	Y	经营活动产生的现金流量净额(间接法)
conv_debt_into_cap	float	Y	债务转为资本
conv_copbonds_due_within_1y	float	Y	一年内到期的可转换公司债券
fa_fnc_leases	float	Y	融资租入固定资产
end_bal_cash	float	Y	现金的期末余额
beg_bal_cash	float	Y	减:现金的期初余额
end_bal_cash_equ	float	Y	加:现金等价物的期末余额
beg_bal_cash_equ	float	Y	减:现金等价物的期初余额
im_n_incr_cash_equ	float	Y	现金及现金等价物净增加额(间接法)
update_flag	str	N	更新标识
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
def get_stock_cashflow(stock):
    token = choice(token_list)  # 随机选择一个token
    pro = ts.pro_api(token)
    df = pro.cashflow(ts_code=stock, start_date="20130101", end_date=today)
    # time.sleep(np.random.randint(0, 3))
    return df


if __name__ == "__main__":
    dictionarydb = SqliteDict(
        files.SQLITE_DICT, tablename="tushare", autocommit=True
    )  # access the db

    start_from_scratch = False  # bool 是否从头开始爬，False则从上次结束的地方开始

    TUSHARE_CASHFLOW = tushare_cashflow.TABLE
    SCRAPYED_ITEMS_KEYNAME = TUSHARE_CASHFLOW  # 存放爬取过的股票代码的字典名
    primary_key = "id"  # 主键名

    if start_from_scratch:
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
            stock_code = row["ts_code"]
            # 如果股票没有爬取过，则进行处理
            if not stock_code in scrapyed_items:
                logger.info(f'第{i}只股票：{stock_code}')
                df = get_stock_cashflow(stock_code)  # 获取股票数据
                if df.empty:  # 如果财务数据为空，则不进行下一步
                    logger.info(f"{stock_code}没有数据")
                else:
                    # 新构造一个主键
                    col_name = df.columns.tolist()
                    col_name.insert(
                        col_name.index("ts_code"), primary_key
                    )  # 在 ts_code 列前面插入
                    df = df.reindex(columns=col_name)
                    df[primary_key] = df["ts_code"].map(str) + df["end_date"].map(str)

                    cols = df.columns.tolist()
                    mysql.insert_df(table=TUSHARE_CASHFLOW, df=df, cols=cols)

                # 把保存到数据库的股票代码记录一下
                scrapyed_items.append(stock_code)
                dictionarydb[SCRAPYED_ITEMS_KEYNAME] = scrapyed_items
            else:
                pass
        logger.info("A股所有现金流量数据爬取完成！")
        dictionarydb[SCRAPYED_ITEMS_KEYNAME] = []  # 把爬取过的item清空，下次继续从头爬取
    except:
        error = traceback.format_exc()
        sys.stderr.write(error)
        logger.info("Token：", token)


if __name__ == "__main__1":
    df = pro.cashflow(ts_code="600000.SH", start_date="20180101", end_date=today)
    print(df)
    col_name = df.columns.tolist()
    col_name.insert(col_name.index("ts_code"), "id")  # 在 ts_code 列前面插入
    df = df.reindex(columns=col_name)
    df["id"] = df["ts_code"].map(str) + df["end_date"].map(str)

    for i in df.dtypes:
        print(i)

    TUSHARE_CASHFLOW = tushare_cashflow.TABLE

    # mysql.drop_table(table=TUSHARE_CASHFLOW)
    mysql.create_table_from_df(table=TUSHARE_CASHFLOW, df=df, primary_key="id")

    cols = df.columns.tolist()
    mysql.insert_df(table=TUSHARE_CASHFLOW, df=df, cols=cols)
