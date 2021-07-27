# *_*coding:utf-8 *_*
import sys, os
from pathlib import Path

ROOT = Path(os.path.abspath(__file__)).parent.parent
sys.path.append(str(ROOT))
import traceback

from critical_investing import mysql
from tenacity import retry, wait_fixed, wait_random

from settings.sqls import tushare_balancesheet
from settings import files
import doger
logger = doger.guru('INFO', __name__)

import tushare as ts
import datetime
from random import choice
from sqlitedict import SqliteDict
from settings.envs import CONFIG

token_list = CONFIG["tushare_tokens"]
token = choice(token_list)
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
report_type	str	Y	报表类型
comp_type	str	Y	公司类型
total_share	float	Y	期末总股本
cap_rese	float	Y	资本公积金
undistr_porfit	float	Y	未分配利润
surplus_rese	float	Y	盈余公积金
special_rese	float	Y	专项储备
money_cap	float	Y	货币资金
trad_asset	float	Y	交易性金融资产
notes_receiv	float	Y	应收票据
accounts_receiv	float	Y	应收账款
oth_receiv	float	Y	其他应收款
prepayment	float	Y	预付款项
div_receiv	float	Y	应收股利
int_receiv	float	Y	应收利息
inventories	float	Y	存货
amor_exp	float	Y	待摊费用
nca_within_1y	float	Y	一年内到期的非流动资产
sett_rsrv	float	Y	结算备付金
loanto_oth_bank_fi	float	Y	拆出资金
premium_receiv	float	Y	应收保费
reinsur_receiv	float	Y	应收分保账款
reinsur_res_receiv	float	Y	应收分保合同准备金
pur_resale_fa	float	Y	买入返售金融资产
oth_cur_assets	float	Y	其他流动资产
total_cur_assets	float	Y	流动资产合计
fa_avail_for_sale	float	Y	可供出售金融资产
htm_invest	float	Y	持有至到期投资
lt_eqt_invest	float	Y	长期股权投资
invest_real_estate	float	Y	投资性房地产
time_deposits	float	Y	定期存款
oth_assets	float	Y	其他资产
lt_rec	float	Y	长期应收款
fix_assets	float	Y	固定资产
cip	float	Y	在建工程
const_materials	float	Y	工程物资
fixed_assets_disp	float	Y	固定资产清理
produc_bio_assets	float	Y	生产性生物资产
oil_and_gas_assets	float	Y	油气资产
intan_assets	float	Y	无形资产
r_and_d	float	Y	研发支出
goodwill	float	Y	商誉
lt_amor_exp	float	Y	长期待摊费用
defer_tax_assets	float	Y	递延所得税资产
decr_in_disbur	float	Y	发放贷款及垫款
oth_nca	float	Y	其他非流动资产
total_nca	float	Y	非流动资产合计
cash_reser_cb	float	Y	现金及存放中央银行款项
depos_in_oth_bfi	float	Y	存放同业和其它金融机构款项
prec_metals	float	Y	贵金属
deriv_assets	float	Y	衍生金融资产
rr_reins_une_prem	float	Y	应收分保未到期责任准备金
rr_reins_outstd_cla	float	Y	应收分保未决赔款准备金
rr_reins_lins_liab	float	Y	应收分保寿险责任准备金
rr_reins_lthins_liab	float	Y	应收分保长期健康险责任准备金
refund_depos	float	Y	存出保证金
ph_pledge_loans	float	Y	保户质押贷款
refund_cap_depos	float	Y	存出资本保证金
indep_acct_assets	float	Y	独立账户资产
client_depos	float	Y	其中：客户资金存款
client_prov	float	Y	其中：客户备付金
transac_seat_fee	float	Y	其中:交易席位费
invest_as_receiv	float	Y	应收款项类投资
total_assets	float	Y	资产总计
lt_borr	float	Y	长期借款
st_borr	float	Y	短期借款
cb_borr	float	Y	向中央银行借款
depos_ib_deposits	float	Y	吸收存款及同业存放
loan_oth_bank	float	Y	拆入资金
trading_fl	float	Y	交易性金融负债
notes_payable	float	Y	应付票据
acct_payable	float	Y	应付账款
adv_receipts	float	Y	预收款项
sold_for_repur_fa	float	Y	卖出回购金融资产款
comm_payable	float	Y	应付手续费及佣金
payroll_payable	float	Y	应付职工薪酬
taxes_payable	float	Y	应交税费
int_payable	float	Y	应付利息
div_payable	float	Y	应付股利
oth_payable	float	Y	其他应付款
acc_exp	float	Y	预提费用
deferred_inc	float	Y	递延收益
st_bonds_payable	float	Y	应付短期债券
payable_to_reinsurer	float	Y	应付分保账款
rsrv_insur_cont	float	Y	保险合同准备金
acting_trading_sec	float	Y	代理买卖证券款
acting_uw_sec	float	Y	代理承销证券款
non_cur_liab_due_1y	float	Y	一年内到期的非流动负债
oth_cur_liab	float	Y	其他流动负债
total_cur_liab	float	Y	流动负债合计
bond_payable	float	Y	应付债券
lt_payable	float	Y	长期应付款
specific_payables	float	Y	专项应付款
estimated_liab	float	Y	预计负债
defer_tax_liab	float	Y	递延所得税负债
defer_inc_non_cur_liab	float	Y	递延收益-非流动负债
oth_ncl	float	Y	其他非流动负债
total_ncl	float	Y	非流动负债合计
depos_oth_bfi	float	Y	同业和其它金融机构存放款项
deriv_liab	float	Y	衍生金融负债
depos	float	Y	吸收存款
agency_bus_liab	float	Y	代理业务负债
oth_liab	float	Y	其他负债
prem_receiv_adva	float	Y	预收保费
depos_received	float	Y	存入保证金
ph_invest	float	Y	保户储金及投资款
reser_une_prem	float	Y	未到期责任准备金
reser_outstd_claims	float	Y	未决赔款准备金
reser_lins_liab	float	Y	寿险责任准备金
reser_lthins_liab	float	Y	长期健康险责任准备金
indept_acc_liab	float	Y	独立账户负债
pledge_borr	float	Y	其中:质押借款
indem_payable	float	Y	应付赔付款
policy_div_payable	float	Y	应付保单红利
total_liab	float	Y	负债合计
treasury_share	float	Y	减:库存股
ordin_risk_reser	float	Y	一般风险准备
forex_differ	float	Y	外币报表折算差额
invest_loss_unconf	float	Y	未确认的投资损失
minority_int	float	Y	少数股东权益
total_hldr_eqy_exc_min_int	float	Y	股东权益合计(不含少数股东权益)
total_hldr_eqy_inc_min_int	float	Y	股东权益合计(含少数股东权益)
total_liab_hldr_eqy	float	Y	负债及股东权益总计
lt_payroll_payable	float	Y	长期应付职工薪酬
oth_comp_income	float	Y	其他综合收益
oth_eqt_tools	float	Y	其他权益工具
oth_eqt_tools_p_shr	float	Y	其他权益工具(优先股)
lending_funds	float	Y	融出资金
acc_receivable	float	Y	应收款项
st_fin_payable	float	Y	应付短期融资款
payables	float	Y	应付款项
hfs_assets	float	Y	持有待售的资产
hfs_sales	float	Y	持有待售的负债
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
def get_stock_balancesheet(stock):
    token = choice(token_list)  # 随机选择一个token
    pro = ts.pro_api(token)
    df = pro.balancesheet(
        ts_code=stock,
        start_date="20130101",
        end_date=today,
        # fields="ts_code,ann_date,f_ann_date,end_date,report_type,comp_type,cap_rese",
    )
    # time.sleep(np.random.randint(0, 3))
    return df


if __name__ == "__main__":
    dictionarydb = SqliteDict(
        files.SQLITE_DICT, tablename="tushare", autocommit=True
    )  # access the db

    start_from_scratch = False  # bool 是否从头开始爬，False则从上次结束的地方开始

    TUSHARE_BALANCESHEET = tushare_balancesheet.TABLE
    SCRAPYED_ITEMS_KEYNAME = TUSHARE_BALANCESHEET  # 存放爬取过的股票代码的字典名
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
                df = get_stock_balancesheet(stock_code)  # 获取股票数据
                if df.empty:  # 如果数据为空，则不进行下一步
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
                    mysql.insert_df(table=TUSHARE_BALANCESHEET, df=df, cols=cols)

                # 把保存到数据库的股票代码记录一下
                scrapyed_items.append(stock_code)
                dictionarydb[SCRAPYED_ITEMS_KEYNAME] = scrapyed_items
            else:
                pass
        logger.info("A股所有资产负债数据爬取完成！")
        dictionarydb[SCRAPYED_ITEMS_KEYNAME] = []  # 把爬取过的item清空，下次继续从头爬取
    except:
        error = traceback.format_exc()
        sys.stderr.write(error)
        logger.info("Token：", token)

