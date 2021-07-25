# *_*coding:utf-8 *_*
"""
Descri：
"""


class evernews:
    TABLE = "evernews"

    GET_LAST_NEWSID = """
SELECT news_id 
FROM evernews
WHERE DATE(pub_date) >= DATE("{}")
        """

    DESC_GMT_CREATE = """
SELECT gmt_create
FROM {}
ORDER BY gmt_create DESC
        """.format(
        TABLE
    )
    DDL = """
CREATE TABLE `{}` (
  `id` varchar(20) NOT NULL COMMENT '文章ID（article_code）',
  `publ_date` datetime DEFAULT NULL COMMENT 'datetime',
  `publ_time` datetime DEFAULT NULL COMMENT 'datetime',
  `title` varchar(500) NOT NULL COMMENT '标题',
  `content` longtext COMMENT '内容',
  `author` varchar(50) DEFAULT NULL COMMENT '作者',
  `media_name` varchar(50) DEFAULT NULL COMMENT '媒体源',
  `gmt_create` datetime DEFAULT NULL COMMENT '创建时间',
  `language_code` int DEFAULT NULL COMMENT '语言（1：中文，2：繁体，3：英文）',
  PRIMARY KEY (`title`)
)
    """.format(
        TABLE
    )


class tushare_daily_basic:
    # 每日指标.py
    TABLE = "tushare_daily_basic"
    SELECT_ALL = """
SELECT * FROM tushare_daily_basic
    """


class tushare_stock_basic:
    TABLE = "tushare_stock_basic"


class tushare_stock_basic_info:
    TABLE = "tushare_stock_basic_info"


class tushare_income:
    """利润表"""

    TABLE = "tushare_income"

    BASIC_INFO_FILTER = """
SELECT 
	ts_code AS 股票代码
	,end_date	AS 报告期
	,revenue	AS 营业收入  -- 营业收入=主营业务收入+其他业务收入
	-- 营业总成本=营业成本+营业税金及附加+销售费用+管理费用+财务费用+资产减值损失
	,total_cogs	AS 营业总成本
	-- 营业成本=主营业务成本+其他业务成本。一般由直接材料，直接人工，制造费用等科目组成
	,oper_cost  AS 营业成本
	,oper_cost/total_cogs * 100 AS 营业成本占营业总成本比重
	,total_cogs/revenue * 100 AS 营业总成本占营业收入比重
	
	,sell_exp/(sell_exp + admin_exp + fin_exp + assets_impair_loss) * 100	AS 销售费用占比
	,admin_exp/(sell_exp + admin_exp + fin_exp + assets_impair_loss) * 100	AS 管理费用占比
	-- ,xxx AS 研发费用
	,fin_exp/(sell_exp + admin_exp + fin_exp + assets_impair_loss) * 100	AS 财务费用占比
	,assets_impair_loss/(sell_exp + admin_exp + fin_exp + assets_impair_loss) * 100	AS 资产减值损失占比
	
	
	-- 营业利润=营业收入－营业成本－税金及附加－销售费用－管理费用－财务费用－资产减值损失－信用减值损失+公允价值变动收益（－公允价值变动损失）+投资收益（－投资损失）+资产处置收益（-资产处置损失）+其他收益
	,operate_profit	AS 营业利润   
	-- ,non_oper_income	AS 营业外收入
	-- ,non_oper_exp	AS 营业外支出
	,total_profit	AS 利润总额   -- 利润总额 = 营业利润 + 营业外收入 - 营业外支出
	,income_tax	AS 所得税费用
	,n_income	AS '净利润(含少数股东损益)'  -- 一般看这个指标  净利润 = 利润总额 - 所得税费用
	,n_income/revenue * 100 AS 净利润占营业收入比重
	-- ,n_income_attr_p	AS '净利润(不含少数股东损益)'	
	,ebit	AS 息税前利润
	,ebitda	AS 息税折旧摊销前利润
	,undist_profit	AS 年初未分配利润
	,distable_profit	AS 可分配利润
	,oth_compr_income	AS 其他综合收益
	,t_compr_income	AS 综合收益总额
	,compr_inc_attr_p	AS '归属于母公司(或股东)的综合收益总额'

FROM tushare_income   -- 利润表
WHERE ts_code in ('002157.SZ')
ORDER BY end_date DESC 
    """


class tushare_balancesheet:
    TABLE = "tushare_balancesheet"


class tushare_constitution_of_core_businesses:
    TABLE = "tushare_constitution_of_core_businesses"


class tushare_cashflow:
    TABLE = "tushare_cashflow"

class tushare_long_news:
    TABLE = "tushare_long_news"


class tushare_short_news:
    TABLE = "tushare_short_news"


class tushare_concept_detail:
    TABLE = "tushare_concept_detail"


class tushare_fina_indicator:
    # 财务指标数据.py
    TABLE = "tushare_fina_indicator"

    # 查找股票的指标信息
    SEARCH_STOCKS_INFO = """
SELECT  
    ts_code AS '股票代码',
    end_date	AS	'报告期',
    undist_profit_ps AS '每股未分配利润',
    ebit_ps AS '每股息税前利润',
    bps AS '每股净资产',
    ocfps AS '每股经营活动产生的现金流量净额',
    cfps AS '每股现金流量净额',
    fcff_ps	AS	'每股企业自由现金流量',
    fcfe_ps	AS	'每股股东自由现金流量',
    netprofit_margin	AS	销售净利率,
    grossprofit_margin	AS	销售毛利率,
    cogs_of_sales	AS	销售成本率,
    expense_of_sales	AS	销售期间费用率,
    profit_to_gr	AS	'净利润/营业总收入',
    saleexp_to_gr	AS	'销售费用/营业总收入',
    adminexp_of_gr	AS	'管理费用/营业总收入',
    finaexp_of_gr	AS	'财务费用/营业总收入',
    impai_ttm	AS	'资产减值损失/营业总收入',
    gc_of_gr	AS	'营业总成本/营业总收入',
    op_of_gr	AS	'营业利润/营业总收入',
    ebit_of_gr	AS	'息税前利润/营业总收入',
    roe	AS	净资产收益率,
    roe_yearly	AS	年化净资产收益率,
    roe_waa	AS	加权平均净资产收益率,
    roe_dt	AS	'净资产收益率(扣除非经常损益)',
    roa	AS	总资产报酬率,
    roa2_yearly	AS	年化总资产报酬率,
    roic	AS	投入资本回报率,
    debt_to_assets	AS	'资产负债率',
    ca_to_assets	AS	'流动资产/总资产',
    tbassets_to_totalassets	AS	'有形资产/总资产',
    int_to_talcap	AS	'带息债务/全部投入资本',
    dt_eps_yoy	AS	'稀释每股收益同比增长率(%)',
    cfps_yoy	AS	'每股经营活动产生的现金流量净额同比增长率(%)',
    op_yoy	AS	'营业利润同比增长率(%)',
    ebt_yoy	AS	'利润总额同比增长率(%)',
    netprofit_yoy	AS	'归属母公司股东的净利润同比增长率(%)',
    dt_netprofit_yoy	AS	'归属母公司股东的净利润-扣除非经常损益同比增长率(%)',
    ocf_yoy	AS	'经营活动产生的现金流量净额同比增长率(%)',
    or_yoy	AS	'营业收入同比增长率(%)'

    -- *
FROM tushare_fina_indicator
WHERE 1=1
    AND ts_code REGEXP '002768'   -- 按股票代码

ORDER BY end_date DESC
        """


class tushare_forecast:
    TABLE = "tushare_forecast"

    # 根据业绩预告筛选股票
    FILTER_BY_FORECAST = '''
-- 根据业绩预告筛选出的股票池
SELECT 
	n.name AS 股票名称
-- 	,m.ts_code	AS 股票代码
	,n.industry  AS 行业
	,m.ann_date AS 公告日期
-- 	,n.pe_ttm AS 市盈率
	,m.change_reason	AS	业绩变动原因
	,m.p_change_min	AS 	预告净利润变动幅度下限
	,m.p_change_max	AS	预告净利润变动幅度上限
    ,x.netprofit_margin AS 销售净利率
    ,x.grossprofit_margin AS 销售毛利率
	,m.last_parent_net	AS	上年同期归属母公司净利润
-- 	,m.summary	AS	业绩预告摘要
	,m.end_date	AS	报告期


FROM (
	SELECT * FROM tushare_forecast  -- 业绩预告表
		) m

LEFT JOIN (
	SELECT * FROM tushare_fina_indicator  -- 财务指标表
	WHERE  end_date REGEXP '202009'
-- 		AND dt_netprofit_yoy > 0  -- 上一报告期的扣非净利润增长率大于0
) x
ON m.ts_code=x.ts_code

LEFT JOIN (
	SELECT nm.ts_code
		,nm.pb  -- 市净率（总市值/净资产）
		,nm.pe  -- 市盈率（总市值/净利润， 亏损的PE为空）
		,nm.pe_ttm	-- 市盈率（TTM，亏损的PE为空）
		,nm.ps	 	-- 市销率
		,nm.ps_ttm	-- 市销率（TTM）
		,nm.dv_ratio	-- 股息率 （%）
		,nm.dv_ttm	-- 股息率（TTM）（%）
		,nm.total_mv	-- 总市值 （万元）
		,nm.circ_mv	-- 流通市值（万元）
		,nn.province  -- 所在省份
		,nn.city  -- 所在城市
		,nn.introduction  -- 公司介绍
		,nn.website  -- 公司主页
		,nn.employees  -- 员工人数
		,nn.main_business  -- 主要业务及产品
		,nn.business_scope  -- 经营范围
		,nc.name  -- 股票名称
		,nc.industry  -- 所属行业
		,nc.list_date -- 上市日期
		,nc.is_hs  -- 是否沪深港通标的，N否 H沪股通 S深股通


	FROM ( 
			SELECT * FROM tushare_daily_basic  -- 每日指标
			) nm
		LEFT JOIN ( 
			SELECT * FROM tushare_stock_basic_info  -- 上市股票信息表
			) nn
	        ON nm.ts_code=nn.ts_code
        LEFT JOIN ( 
			SELECT * FROM tushare_stock_basic  -- 上市股票表
			) nc
	        ON nm.ts_code=nc.ts_code
		) n

	ON m.ts_code=n.ts_code


WHERE 1 = 1
	AND m.last_parent_net > 0	-- 上年同期归属母公司净利润
	AND n.pe_ttm > 0 
	AND n.name NOT REGEXP 'ST'
	AND DATE_FORMAT(m.end_date,'%Y-%m-%d') >= DATE_FORMAT(DATE_SUB(now(), INTERVAL 100 DAY),'%Y-%m-%d')   -- 报告期

	AND m.p_change_min > 20 	-- 预告净利润变动幅度下限

-- 	AND (x.netprofit_margin > 4	-- 销售净利率
-- 			OR x.netprofit_margin = 'None'
-- 			)
-- 
-- 	AND (x.grossprofit_margin > 20     -- 销售毛利率，毛利率太低说明没有竞争力，但也不是越高越好
-- 			OR x.grossprofit_margin = 'None'  -- 银行、证券等重要行业不公布毛利率
-- 			)
-- 	AND m.ts_code REGEXP '002475'   -- 按股票代码

ORDER BY m.ann_date DESC  -- 按公告日期排序
-- ORDER BY n.industry DESC  -- 按行业排序
    '''

class good_stocks_pool:
    TABLE = "good_stocks_pool"

    # 通过指标筛选股票，建立一个好股票的股票池
    GOOD_STOCKS_POOL = """
SELECT 
	m.ts_code AS '股票代码'
	,n.name AS 股票名称
	,n.industry AS 行业
	,m.ann_date AS 公告日期
	,m.end_date	AS	报告期
	,m.undist_profit_ps AS '每股未分配利润'
	,m.ebit_ps AS '每股息税前利润'
	,m.bps AS '每股净资产'
	,m.ocfps AS '每股经营活动产生的现金流量净额'
	,m.cfps AS '每股现金流量净额'
	,m.fcff_ps	AS	'每股企业自由现金流量'
	,m.fcfe_ps	AS	'每股股东自由现金流量'
	,m.netprofit_margin	AS	销售净利率  -- 净利润/营业总收入
	,m.grossprofit_margin	AS	销售毛利率
	,m.cogs_of_sales	AS	销售成本率
	,m.expense_of_sales	AS	销售期间费用率

	,m.gc_of_gr	AS	'营业总成本占营业总收入比重'
	,m.op_of_gr	AS	'营业利润占营业总收入比重'
	,m.ebit_of_gr	AS	'息税前利润占营业总收入比重'
	,m.roe	AS	净资产收益率
	,m.roe_yearly	AS	年化净资产收益率
	,m.roe_waa	AS	加权平均净资产收益率
	,m.roe_dt	AS	'扣非净资产收益率' -- 净资产收益率(扣除非经常损益)
	,m.roa	AS	总资产报酬率
	,m.roa2_yearly	AS	年化总资产报酬率
	,m.roic	AS	投入资本回报率
	,m.debt_to_assets	AS	'资产负债率'
	,m.ca_to_assets	AS	'流动资产占总资产比重'
	,m.tbassets_to_totalassets	AS	'有形资产占总资产比重'
	,m.int_to_talcap	AS	'带息债务占全部投入资本比重'
	,m.dt_eps_yoy	AS	'稀释每股收益同比增长率'
	,m.cfps_yoy	AS	'每股经营活动产生的现金流量净额同比增长率'
	,m.op_yoy	AS	'营业利润同比增长率'
	,m.ebt_yoy	AS	'利润总额同比增长率'
	,m.netprofit_yoy	AS	'归属母公司股东的净利润同比增长率'
	,m.dt_netprofit_yoy	AS	'扣非归属母公司股东的净利润同比增长率'
	,m.ocf_yoy	AS	'经营活动产生的现金流量净额同比增长率'
	,m.or_yoy	AS	'营业收入同比增长率'
	,n.pb AS '市净率'
	,n.pe_ttm AS 市盈率  -- TTM
	,n.ps_ttm AS 市销率  -- TTM
	,n.dv_ttm AS 股息率  -- TTM
	,n.province AS 所在省份
	,n.city AS 所在城市
	,n.introduction AS 公司介绍
	,n.website AS 公司主页
	,n.employees AS 员工人数
	,n.main_business AS 主要业务及产品
	,n.business_scope AS 经营范围
	,n.list_date AS 上市日期
	,n.is_hs AS 是否沪深港通标的 -- 是否沪深港通标的，N否 H沪股通 S深股通

	,d.revenue	AS 营业收入  -- 营业收入=主营业务收入+其他业务收入
	-- 营业总成本=营业成本+营业税金及附加+销售费用+管理费用+财务费用+资产减值损失
	,d.total_cogs	AS 营业总成本
	-- 营业成本=主营业务成本+其他业务成本。一般由直接材料，直接人工，制造费用等科目组成
	,d.oper_cost  AS 营业成本
	,d.oper_cost/d.total_cogs * 100 AS 营业成本占营业总成本比重
	,d.total_cogs/d.revenue * 100 AS 营业总成本占营业收入比重
	
	,d.sell_exp/(d.sell_exp + d.admin_exp + d.fin_exp + d.assets_impair_loss) * 100	AS 销售费用占比
	,d.admin_exp/(d.sell_exp + d.admin_exp + d.fin_exp + d.assets_impair_loss) * 100	AS 管理费用占比
	-- ,xxx AS 研发费用
	,d.fin_exp/(d.sell_exp + d.admin_exp + d.fin_exp + d.assets_impair_loss) * 100	AS 财务费用占比
	,d.assets_impair_loss/(d.sell_exp + d.admin_exp + d.fin_exp + d.assets_impair_loss) * 100	AS 资产减值损失占比
	
	
	-- 营业利润=营业收入－营业成本－税金及附加－销售费用－管理费用－财务费用－资产减值损失－信用减值损失+公允价值变动收益（－公允价值变动损失）+投资收益（－投资损失）+资产处置收益（-资产处置损失）+其他收益
	,d.operate_profit	AS 营业利润   
	-- ,d.non_oper_income	AS 营业外收入
	-- ,d.non_oper_exp	AS 营业外支出
	,d.total_profit	AS 利润总额   -- 利润总额 = 营业利润 + 营业外收入 - 营业外支出
	,d.income_tax	AS 所得税费用
	,d.n_income	AS '净利润'  -- 净利润(含少数股东损益) 一般看这个指标  净利润 = 利润总额 - 所得税费用
	,d.n_income/revenue * 100 AS 净利润占营业收入比重
	-- ,d.n_income_attr_p	AS '净利润(不含少数股东损益)'	
	,d.ebit	AS 息税前利润
	,d.ebitda	AS 息税折旧摊销前利润

--  资本支出=净经营长期资产增加+折旧与摊销
	,e.c_pay_acq_const_fiolta AS 资本支出 -- 资本支出 = 购建固定资产、无形资产和其他长期资产所支付的现金
--  自由现金流=净利润+折旧+摊销-资本支出-资本运营增加	
	,e.free_cashflow AS	企业自由现金流量
	
	,b.money_cap/b.total_cur_assets * 100	AS	货币资金占流动资产比
	,b.trad_asset/b.total_cur_assets * 100	AS	交易性金融资产占流动资产比
	,b.notes_receiv/b.total_cur_assets * 100	AS	应收票据占流动资产比
	,b.accounts_receiv/b.total_cur_assets * 100	AS	应收账款占流动资产比
	,b.oth_receiv/b.total_cur_assets * 100	AS	其他应收款占流动资产比
	,b.prepayment/b.total_cur_assets * 100	AS	预付款项占流动资产比
	,b.inventories/b.total_cur_assets * 100	AS	存货占流动资产比

-- 	流动资产合计：货币资金（=现金+银行存款+其他货币资金）+交易性金融资产（即短期投资） +应收票据（=应收票据-已贴现的）+应收账款[=（应收账款+预收账款）借方合计—坏账准备中应收账款的部分）] +预付款项[=（应付账款+预付账款）借方合计 ] +应收利息 +应收股利 +其他应收款(=其他应收款-坏账准备中其他应收款的部分） +存货[=库存商品+原材料+在途物资+生产成本-存货跌价准备+/-材料成本差异] +一年内到期的非流动资产 +其他流动资产
	,b.total_cur_assets	AS	流动资产合计
-- 	非流动资产=（固定资产－累计回折旧）＋答（无形资产－累计摊销）＋（在建工程－固定资产清理）＋在建工程＋工程物资＋长期股权投资
	,b.total_nca AS 非流动资产合计
-- 	资产总额=流动资产+长期投资+固定资产+无形资产及递延资产+其他资产
	,b.total_assets AS 资产总计
-- 	流动负债合计=短期借款+应付票据+应付账款+预收账款+应付工资+应付福利费+应付股利+应交税金+其它暂收应付款项+预提费用+一年内到期的长期借款
	,b.total_cur_liab AS 流动负债合计
	,b.total_cur_assets-b.total_cur_liab AS 营运资金 -- 营运资金=( 流动资产-流动负债)
	,b.total_cur_assets/b.total_cur_liab * 100 AS 流动比率
	,b.total_ncl AS 非流动负债合计
	,b.total_liab AS 负债合计
-- 	,b.total_liab_hldr_eqy AS 负债及股东权益总计
	,b.total_cur_liab/b.total_liab_hldr_eqy * 100 流动负债占总资产的比重
	,d.oper_cost/d.revenue * 100 AS 营业成本占营业收入比重
	

FROM (
	SELECT * FROM tushare_fina_indicator  -- 财务指标表
		) m

LEFT JOIN (
	SELECT nm.ts_code
		,nm.pb  -- 市净率（总市值/净资产）
		,nm.pe  -- 市盈率（总市值/净利润， 亏损的PE为空）
		,nm.pe_ttm	-- 市盈率（TTM，亏损的PE为空）
		,nm.ps	 	-- 市销率
		,nm.ps_ttm	-- 市销率（TTM）
		,nm.dv_ratio	-- 股息率 （%）
		,nm.dv_ttm	-- 股息率（TTM）（%）
		,nm.total_mv	-- 总市值 （万元）
		,nm.circ_mv	-- 流通市值（万元）
		,nn.province  -- 所在省份
		,nn.city  -- 所在城市
		,nn.introduction  -- 公司介绍
		,nn.website  -- 公司主页
		,nn.employees  -- 员工人数
		,nn.main_business  -- 主要业务及产品
		,nn.business_scope  -- 经营范围
		,nc.name  -- 股票名称
		,nc.industry  -- 所属行业
		,nc.list_date -- 上市日期
		,nc.is_hs  -- 是否沪深港通标的，N否 H沪股通 S深股通
		
		
	FROM ( 
			SELECT * FROM tushare_daily_basic  -- 每日指标
			) nm
		LEFT JOIN ( 
			SELECT * FROM tushare_stock_basic_info  -- 上市股票信息表
			) nn
	        ON nm.ts_code=nn.ts_code
        LEFT JOIN ( 
			SELECT * FROM tushare_stock_basic  -- 上市股票表
			) nc
	        ON nm.ts_code=nc.ts_code
		) n
		
	ON m.ts_code=n.ts_code

LEFT JOIN ( 
	SELECT * FROM tushare_balancesheet  -- 资产负债表
		) b
	ON m.ts_code=b.ts_code
	AND m.end_date=b.end_date

LEFT JOIN ( 
	SELECT * FROM tushare_income   -- 利润表
		) d
	ON m.ts_code=d.ts_code
	AND m.end_date=d.end_date

LEFT JOIN ( 
	SELECT * FROM tushare_cashflow   -- 现金流量表
		) e
	ON m.ts_code=e.ts_code
	AND m.end_date=e.end_date

WHERE 1=1
--     AND m.ts_code REGEXP '002415'   -- 按股票代码
    
-- 	AND m.end_date REGEXP '202009'   -- 按报告期
	
	AND NOT n.name REGEXP 'ST'	-- ST股票
-- 	AND NOT n.name REGEXP 'N'	-- 新股
	AND m.netprofit_yoy	> 20	--  归属母公司股东的净利润同比增长率(%)
	AND m.dt_netprofit_yoy > 20    -- 归属母公司股东的净利润-扣除非经常损益同比增长率(%)
	AND m.or_yoy > 20    -- 营业收入同比增长率(%)

-- ORDER BY m.dt_netprofit_yoy DESC  -- 按归属母公司股东的净利润-扣除非经常损益同比增长率(%)排序
ORDER BY m.end_date DESC  -- 按报告期排序
        """

    # 进一步提取优质股票
    UPGRADE_STOCKS = '''
-- 根据财务指标筛选出的股票池
SELECT 
	gsp.股票代码
	,gsp.股票名称
	,gsp.行业
	,gsp.公告日期
	,gsp.报告期	
	,gsp.每股未分配利润
	,gsp.每股息税前利润
	,gsp.每股净资产
	,gsp.每股经营活动产生的现金流量净额
	,gsp.每股现金流量净额
	,gsp.每股企业自由现金流量
	,gsp.每股股东自由现金流量
	,gsp.销售净利率  -- 净利润/营业总收入
	,gsp.销售毛利率
	,gsp.销售成本率
	,gsp.销售期间费用率

	,gsp.营业总成本占营业总收入比重
	,gsp.营业利润占营业总收入比重
	,gsp.息税前利润占营业总收入比重
	,gsp.净资产收益率
	,gsp.年化净资产收益率
	,gsp.加权平均净资产收益率
	,gsp.扣非净资产收益率
	,gsp.总资产报酬率
	,gsp.年化总资产报酬率
	,gsp.投入资本回报率
	,gsp.资产负债率
	,gsp.流动资产占总资产比重
	,gsp.有形资产占总资产比重
	,gsp.带息债务占全部投入资本比重
	,gsp.稀释每股收益同比增长率
	,gsp.每股经营活动产生的现金流量净额同比增长率
	,gsp.营业利润同比增长率
	,gsp.利润总额同比增长率
	,gsp.归属母公司股东的净利润同比增长率
	,gsp.扣非归属母公司股东的净利润同比增长率
	,gsp.经营活动产生的现金流量净额同比增长率
	,gsp.营业收入同比增长率
	,gsp.市净率
	,gsp.市盈率  -- TTM
	,gsp.市销率  -- TTM
	,gsp.股息率  -- TTM
	,gsp.所在省份
	,gsp.所在城市
	,gsp.公司介绍
	,gsp.公司主页
	,gsp.员工人数
	,gsp.主要业务及产品
	,gsp.经营范围
	,gsp.上市日期

	,gsp.营业收入  -- 营业收入=主营业务收入+其他业务收入
	-- 营业总成本=营业成本+营业税金及附加+销售费用+管理费用+财务费用+资产减值损失
	,gsp.营业总成本
	-- 营业成本=主营业务成本+其他业务成本。一般由直接材料，直接人工，制造费用等科目组成
	,gsp.营业成本
	,gsp.营业成本占营业总成本比重
	,gsp.营业总成本占营业收入比重
	
	,gsp.销售费用占比
	,gsp.管理费用占比
	-- ,xxx AS 研发费用
	,gsp.财务费用占比
	,gsp.资产减值损失占比
	
	
	-- 营业利润=营业收入－营业成本－税金及附加－销售费用－管理费用－财务费用－资产减值损失－信用减值损失+公允价值变动收益（－公允价值变动损失）+投资收益（－投资损失）+资产处置收益（-资产处置损失）+其他收益
	,gsp.营业利润   

	,gsp.利润总额   -- 利润总额 = 营业利润 + 营业外收入 - 营业外支出
	,gsp.所得税费用
	,gsp.净利润  -- 一般看这个指标  净利润 = 利润总额 - 所得税费用
	,gsp.净利润占营业收入比重

	,gsp.息税前利润
	,gsp.息税折旧摊销前利润

--  资本支出=净经营长期资产增加+折旧与摊销
	,gsp.资本支出  -- 资本支出 = 购建固定资产、无形资产和其他长期资产所支付的现金
--  自由现金流=净利润+折旧+摊销-资本支出-资本运营增加	
	,gsp.企业自由现金流量
	
	,gsp.货币资金占流动资产比
	,gsp.交易性金融资产占流动资产比
	,gsp.应收票据占流动资产比
	,gsp.应收账款占流动资产比
	,gsp.其他应收款占流动资产比
	,gsp.预付款项占流动资产比
	,gsp.存货占流动资产比

-- 	流动资产合计：货币资金（=现金+银行存款+其他货币资金）+交易性金融资产（即短期投资） +应收票据（=应收票据-已贴现的）+应收账款[=（应收账款+预收账款）借方合计—坏账准备中应收账款的部分）] +预付款项[=（应付账款+预付账款）借方合计 ] +应收利息 +应收股利 +其他应收款(=其他应收款-坏账准备中其他应收款的部分） +存货[=库存商品+原材料+在途物资+生产成本-存货跌价准备+/-材料成本差异] +一年内到期的非流动资产 +其他流动资产
	,gsp.流动资产合计
-- 	非流动资产=（固定资产－累计回折旧）＋答（无形资产－累计摊销）＋（在建工程－固定资产清理）＋在建工程＋工程物资＋长期股权投资
	,gsp.非流动资产合计
-- 	资产总额=流动资产+长期投资+固定资产+无形资产及递延资产+其他资产
	,gsp.资产总计
-- 	流动负债合计=短期借款+应付票据+应付账款+预收账款+应付工资+应付福利费+应付股利+应交税金+其它暂收应付款项+预提费用+一年内到期的长期借款
	,gsp.流动负债合计
	,gsp.营运资金 -- 营运资金=( 流动资产-流动负债)
	,gsp.流动比率
	,gsp.非流动负债合计
	,gsp.负债合计
-- 	,gsp.负债及股东权益总计
	,gsp.流动负债占总资产的比重
	,gsp.营业成本占营业收入比重
	

FROM good_stocks_pool gsp -- 股票池


WHERE 1=1
	AND gsp.每股未分配利润 >= 0
 	AND gsp.市盈率 > 0  -- 市盈率（TTM）
--     AND gsp.上市日期 < '20201001'
	AND gsp.报告期 REGEXP '2021'
	
--     AND gsp.股票代码 REGEXP '300464' -- 值得买没有找出来
    
    AND gsp.行业 IN ('互联网','医疗保健')
    AND gsp.行业 NOT IN ('铝')
-- ('生物制药','塑料','通信设备','软件服务','证券','IT设备','生物制药','玻璃','互联网','医疗保健')

			

-- ORDER BY gsp.扣非归属母公司股东的净利润同比增长率 DESC  -- 按归属母公司股东的净利润-扣除非经常损益同比增长率(%)排序
ORDER BY gsp.公告日期 DESC  -- 按公告日期排序
-- ORDER BY gsp.行业 DESC  -- 按行业排序
    '''


if __name__ == "__main__":

    print(evernews.DDL)
