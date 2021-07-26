create table if not exists `tushare_stock_basic` (
    `ts_code` varchar(100) DEFAULT NULL COMMENT 'None',
    `symbol` varchar(100) DEFAULT NULL COMMENT 'None',
    `name` varchar(100) DEFAULT NULL COMMENT 'None',
    `area` varchar(100) DEFAULT NULL COMMENT 'None',
    `industry` varchar(100) DEFAULT NULL COMMENT 'None',
    `fullname` varchar(100) DEFAULT NULL COMMENT 'None',
    `enname` varchar(100) DEFAULT NULL COMMENT 'None',
    `market` varchar(100) DEFAULT NULL COMMENT 'None',
    `exchange` varchar(100) DEFAULT NULL COMMENT 'None',
    `list_date` varchar(100) DEFAULT NULL COMMENT 'None',
    `is_hs` varchar(100) DEFAULT NULL COMMENT 'None'
) DEFAULT CHARSET=utf8mb4;

CREATE TABLE if not exists `tushare_stock_basic_info` (
  `ts_code` varchar(100) DEFAULT NULL COMMENT 'None',
  `exchange` varchar(100) DEFAULT NULL COMMENT 'None',
  `chairman` varchar(100) DEFAULT NULL COMMENT 'None',
  `manager` varchar(100) DEFAULT NULL COMMENT 'None',
  `secretary` varchar(100) DEFAULT NULL COMMENT 'None',
  `reg_capital` float DEFAULT NULL COMMENT 'None',
  `setup_date` varchar(100) DEFAULT NULL COMMENT 'None',
  `province` varchar(100) DEFAULT NULL COMMENT 'None',
  `city` varchar(100) DEFAULT NULL COMMENT 'None',
  `introduction` varchar(100) DEFAULT NULL COMMENT 'None',
  `website` varchar(100) DEFAULT NULL COMMENT 'None',
  `email` varchar(100) DEFAULT NULL COMMENT 'None',
  `office` varchar(100) DEFAULT NULL COMMENT 'None',
  `business_scope` varchar(100) DEFAULT NULL COMMENT 'None',
  `employees` float DEFAULT NULL COMMENT 'None',
  `main_business` varchar(100) DEFAULT NULL COMMENT 'None'
) DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tushare_income` (
  `id` varchar(100) NOT NULL COMMENT 'None',
  `ts_code` varchar(100) DEFAULT NULL COMMENT 'None',
  `ann_date` varchar(100) DEFAULT NULL COMMENT 'None',
  `f_ann_date` varchar(100) DEFAULT NULL COMMENT 'None',
  `end_date` varchar(100) DEFAULT NULL COMMENT 'None',
  `report_type` varchar(100) DEFAULT NULL COMMENT 'None',
  `comp_type` varchar(100) DEFAULT NULL COMMENT 'None',
  `basic_eps` float DEFAULT NULL COMMENT 'None',
  `diluted_eps` float DEFAULT NULL COMMENT 'None',
  `total_revenue` float DEFAULT NULL COMMENT 'None',
  `revenue` float DEFAULT NULL COMMENT 'None',
  `int_income` float DEFAULT NULL COMMENT 'None',
  `prem_earned` varchar(100) DEFAULT NULL COMMENT 'None',
  `comm_income` float DEFAULT NULL COMMENT 'None',
  `n_commis_income` float DEFAULT NULL COMMENT 'None',
  `n_oth_income` float DEFAULT NULL COMMENT 'None',
  `n_oth_b_income` float DEFAULT NULL COMMENT 'None',
  `prem_income` varchar(100) DEFAULT NULL COMMENT 'None',
  `out_prem` varchar(100) DEFAULT NULL COMMENT 'None',
  `une_prem_reser` varchar(100) DEFAULT NULL COMMENT 'None',
  `reins_income` varchar(100) DEFAULT NULL COMMENT 'None',
  `n_sec_tb_income` varchar(100) DEFAULT NULL COMMENT 'None',
  `n_sec_uw_income` varchar(100) DEFAULT NULL COMMENT 'None',
  `n_asset_mg_income` varchar(100) DEFAULT NULL COMMENT 'None',
  `oth_b_income` float DEFAULT NULL COMMENT 'None',
  `fv_value_chg_gain` float DEFAULT NULL COMMENT 'None',
  `invest_income` float DEFAULT NULL COMMENT 'None',
  `ass_invest_income` float DEFAULT NULL COMMENT 'None',
  `forex_gain` float DEFAULT NULL COMMENT 'None',
  `total_cogs` float DEFAULT NULL COMMENT 'None',
  `oper_cost` varchar(100) DEFAULT NULL COMMENT 'None',
  `int_exp` float DEFAULT NULL COMMENT 'None',
  `comm_exp` float DEFAULT NULL COMMENT 'None',
  `biz_tax_surchg` float DEFAULT NULL COMMENT 'None',
  `sell_exp` varchar(100) DEFAULT NULL COMMENT 'None',
  `admin_exp` float DEFAULT NULL COMMENT 'None',
  `fin_exp` varchar(100) DEFAULT NULL COMMENT 'None',
  `assets_impair_loss` float DEFAULT NULL COMMENT 'None',
  `prem_refund` varchar(100) DEFAULT NULL COMMENT 'None',
  `compens_payout` varchar(100) DEFAULT NULL COMMENT 'None',
  `reser_insur_liab` varchar(100) DEFAULT NULL COMMENT 'None',
  `div_payt` varchar(100) DEFAULT NULL COMMENT 'None',
  `reins_exp` varchar(100) DEFAULT NULL COMMENT 'None',
  `oper_exp` float DEFAULT NULL COMMENT 'None',
  `compens_payout_refu` varchar(100) DEFAULT NULL COMMENT 'None',
  `insur_reser_refu` varchar(100) DEFAULT NULL COMMENT 'None',
  `reins_cost_refund` varchar(100) DEFAULT NULL COMMENT 'None',
  `other_bus_cost` float DEFAULT NULL COMMENT 'None',
  `operate_profit` float DEFAULT NULL COMMENT 'None',
  `non_oper_income` float DEFAULT NULL COMMENT 'None',
  `non_oper_exp` float DEFAULT NULL COMMENT 'None',
  `nca_disploss` varchar(100) DEFAULT NULL COMMENT 'None',
  `total_profit` float DEFAULT NULL COMMENT 'None',
  `income_tax` float DEFAULT NULL COMMENT 'None',
  `n_income` float DEFAULT NULL COMMENT 'None',
  `n_income_attr_p` float DEFAULT NULL COMMENT 'None',
  `minority_gain` float DEFAULT NULL COMMENT 'None',
  `oth_compr_income` float DEFAULT NULL COMMENT 'None',
  `t_compr_income` float DEFAULT NULL COMMENT 'None',
  `compr_inc_attr_p` float DEFAULT NULL COMMENT 'None',
  `compr_inc_attr_m_s` float DEFAULT NULL COMMENT 'None',
  `ebit` float DEFAULT NULL COMMENT 'None',
  `ebitda` float DEFAULT NULL COMMENT 'None',
  `insurance_exp` varchar(100) DEFAULT NULL COMMENT 'None',
  `undist_profit` varchar(100) DEFAULT NULL COMMENT 'None',
  `distable_profit` varchar(100) DEFAULT NULL COMMENT 'None',
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tushare_cashflow` (
  `id` varchar(100) NOT NULL COMMENT 'None',
  `ts_code` varchar(100) DEFAULT NULL COMMENT 'None',
  `ann_date` varchar(100) DEFAULT NULL COMMENT 'None',
  `f_ann_date` varchar(100) DEFAULT NULL COMMENT 'None',
  `end_date` varchar(100) DEFAULT NULL COMMENT 'None',
  `comp_type` varchar(100) DEFAULT NULL COMMENT 'None',
  `report_type` varchar(100) DEFAULT NULL COMMENT 'None',
  `net_profit` float DEFAULT NULL COMMENT 'None',
  `finan_exp` varchar(100) DEFAULT NULL COMMENT 'None',
  `c_fr_sale_sg` varchar(100) DEFAULT NULL COMMENT 'None',
  `recp_tax_rends` varchar(100) DEFAULT NULL COMMENT 'None',
  `n_depos_incr_fi` float DEFAULT NULL COMMENT 'None',
  `n_incr_loans_cb` float DEFAULT NULL COMMENT 'None',
  `n_inc_borr_oth_fi` float DEFAULT NULL COMMENT 'None',
  `prem_fr_orig_contr` varchar(100) DEFAULT NULL COMMENT 'None',
  `n_incr_insured_dep` varchar(100) DEFAULT NULL COMMENT 'None',
  `n_reinsur_prem` varchar(100) DEFAULT NULL COMMENT 'None',
  `n_incr_disp_tfa` varchar(100) DEFAULT NULL COMMENT 'None',
  `ifc_cash_incr` float DEFAULT NULL COMMENT 'None',
  `n_incr_disp_faas` varchar(100) DEFAULT NULL COMMENT 'None',
  `n_incr_loans_oth_bank` float DEFAULT NULL COMMENT 'None',
  `n_cap_incr_repur` varchar(100) DEFAULT NULL COMMENT 'None',
  `c_fr_oth_operate_a` float DEFAULT NULL COMMENT 'None',
  `c_inf_fr_operate_a` float DEFAULT NULL COMMENT 'None',
  `c_paid_goods_s` varchar(100) DEFAULT NULL COMMENT 'None',
  `c_paid_to_for_empl` float DEFAULT NULL COMMENT 'None',
  `c_paid_for_taxes` float DEFAULT NULL COMMENT 'None',
  `n_incr_clt_loan_adv` float DEFAULT NULL COMMENT 'None',
  `n_incr_dep_cbob` float DEFAULT NULL COMMENT 'None',
  `c_pay_claims_orig_inco` varchar(100) DEFAULT NULL COMMENT 'None',
  `pay_handling_chrg` float DEFAULT NULL COMMENT 'None',
  `pay_comm_insur_plcy` varchar(100) DEFAULT NULL COMMENT 'None',
  `oth_cash_pay_oper_act` float DEFAULT NULL COMMENT 'None',
  `st_cash_out_act` float DEFAULT NULL COMMENT 'None',
  `n_cashflow_act` float DEFAULT NULL COMMENT 'None',
  `oth_recp_ral_inv_act` float DEFAULT NULL COMMENT 'None',
  `c_disp_withdrwl_invest` float DEFAULT NULL COMMENT 'None',
  `c_recp_return_invest` float DEFAULT NULL COMMENT 'None',
  `n_recp_disp_fiolta` float DEFAULT NULL COMMENT 'None',
  `n_recp_disp_sobu` varchar(100) DEFAULT NULL COMMENT 'None',
  `stot_inflows_inv_act` float DEFAULT NULL COMMENT 'None',
  `c_pay_acq_const_fiolta` float DEFAULT NULL COMMENT 'None',
  `c_paid_invest` float DEFAULT NULL COMMENT 'None',
  `n_disp_subs_oth_biz` varchar(100) DEFAULT NULL COMMENT 'None',
  `oth_pay_ral_inv_act` varchar(100) DEFAULT NULL COMMENT 'None',
  `n_incr_pledge_loan` varchar(100) DEFAULT NULL COMMENT 'None',
  `stot_out_inv_act` float DEFAULT NULL COMMENT 'None',
  `n_cashflow_inv_act` float DEFAULT NULL COMMENT 'None',
  `c_recp_borrow` float DEFAULT NULL COMMENT 'None',
  `proc_issue_bonds` float DEFAULT NULL COMMENT 'None',
  `oth_cash_recp_ral_fnc_act` varchar(100) DEFAULT NULL COMMENT 'None',
  `stot_cash_in_fnc_act` float DEFAULT NULL COMMENT 'None',
  `free_cashflow` float DEFAULT NULL COMMENT 'None',
  `c_prepay_amt_borr` float DEFAULT NULL COMMENT 'None',
  `c_pay_dist_dpcp_int_exp` float DEFAULT NULL COMMENT 'None',
  `incl_dvd_profit_paid_sc_ms` varchar(100) DEFAULT NULL COMMENT 'None',
  `oth_cashpay_ral_fnc_act` varchar(100) DEFAULT NULL COMMENT 'None',
  `stot_cashout_fnc_act` float DEFAULT NULL COMMENT 'None',
  `n_cash_flows_fnc_act` float DEFAULT NULL COMMENT 'None',
  `eff_fx_flu_cash` float DEFAULT NULL COMMENT 'None',
  `n_incr_cash_cash_equ` float DEFAULT NULL COMMENT 'None',
  `c_cash_equ_beg_period` float DEFAULT NULL COMMENT 'None',
  `c_cash_equ_end_period` float DEFAULT NULL COMMENT 'None',
  `c_recp_cap_contrib` float DEFAULT NULL COMMENT 'None',
  `incl_cash_rec_saims` float DEFAULT NULL COMMENT 'None',
  `uncon_invest_loss` varchar(100) DEFAULT NULL COMMENT 'None',
  `prov_depr_assets` float DEFAULT NULL COMMENT 'None',
  `depr_fa_coga_dpba` float DEFAULT NULL COMMENT 'None',
  `amort_intang_assets` float DEFAULT NULL COMMENT 'None',
  `lt_amort_deferred_exp` float DEFAULT NULL COMMENT 'None',
  `decr_deferred_exp` varchar(100) DEFAULT NULL COMMENT 'None',
  `incr_acc_exp` varchar(100) DEFAULT NULL COMMENT 'None',
  `loss_disp_fiolta` float DEFAULT NULL COMMENT 'None',
  `loss_scr_fa` varchar(100) DEFAULT NULL COMMENT 'None',
  `loss_fv_chg` float DEFAULT NULL COMMENT 'None',
  `invest_loss` float DEFAULT NULL COMMENT 'None',
  `decr_def_inc_tax_assets` float DEFAULT NULL COMMENT 'None',
  `incr_def_inc_tax_liab` float DEFAULT NULL COMMENT 'None',
  `decr_inventories` varchar(100) DEFAULT NULL COMMENT 'None',
  `decr_oper_payable` float DEFAULT NULL COMMENT 'None',
  `incr_oper_payable` float DEFAULT NULL COMMENT 'None',
  `others` varchar(100) DEFAULT NULL COMMENT 'None',
  `im_net_cashflow_oper_act` float DEFAULT NULL COMMENT 'None',
  `conv_debt_into_cap` varchar(100) DEFAULT NULL COMMENT 'None',
  `conv_copbonds_due_within_1y` varchar(100) DEFAULT NULL COMMENT 'None',
  `fa_fnc_leases` varchar(100) DEFAULT NULL COMMENT 'None',
  `end_bal_cash` float DEFAULT NULL COMMENT 'None',
  `beg_bal_cash` float DEFAULT NULL COMMENT 'None',
  `end_bal_cash_equ` varchar(100) DEFAULT NULL COMMENT 'None',
  `beg_bal_cash_equ` varchar(100) DEFAULT NULL COMMENT 'None',
  `im_n_incr_cash_equ` float DEFAULT NULL COMMENT 'None',
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tushare_fina_indicator` (
  `id` varchar(100) NOT NULL COMMENT 'None',
  `ts_code` varchar(100) DEFAULT NULL COMMENT 'None',
  `ann_date` varchar(100) DEFAULT NULL COMMENT 'None',
  `end_date` varchar(100) DEFAULT NULL COMMENT 'None',
  `eps` float DEFAULT NULL COMMENT 'None',
  `dt_eps` float DEFAULT NULL COMMENT 'None',
  `total_revenue_ps` float DEFAULT NULL COMMENT 'None',
  `revenue_ps` float DEFAULT NULL COMMENT 'None',
  `capital_rese_ps` float DEFAULT NULL COMMENT 'None',
  `surplus_rese_ps` float DEFAULT NULL COMMENT 'None',
  `undist_profit_ps` float DEFAULT NULL COMMENT 'None',
  `extra_item` float DEFAULT NULL COMMENT 'None',
  `profit_dedt` float DEFAULT NULL COMMENT 'None',
  `gross_margin` varchar(100) DEFAULT NULL COMMENT 'None',
  `current_ratio` varchar(100) DEFAULT NULL COMMENT 'None',
  `quick_ratio` varchar(100) DEFAULT NULL COMMENT 'None',
  `cash_ratio` varchar(100) DEFAULT NULL COMMENT 'None',
  `ar_turn` varchar(100) DEFAULT NULL COMMENT 'None',
  `ca_turn` varchar(100) DEFAULT NULL COMMENT 'None',
  `fa_turn` varchar(100) DEFAULT NULL COMMENT 'None',
  `assets_turn` float DEFAULT NULL COMMENT 'None',
  `op_income` float DEFAULT NULL COMMENT 'None',
  `ebit` varchar(100) DEFAULT NULL COMMENT 'None',
  `ebitda` varchar(100) DEFAULT NULL COMMENT 'None',
  `fcff` float DEFAULT NULL COMMENT 'None',
  `fcfe` varchar(100) DEFAULT NULL COMMENT 'None',
  `current_exint` varchar(100) DEFAULT NULL COMMENT 'None',
  `noncurrent_exint` varchar(100) DEFAULT NULL COMMENT 'None',
  `interestdebt` varchar(100) DEFAULT NULL COMMENT 'None',
  `netdebt` varchar(100) DEFAULT NULL COMMENT 'None',
  `tangible_asset` varchar(100) DEFAULT NULL COMMENT 'None',
  `working_capital` varchar(100) DEFAULT NULL COMMENT 'None',
  `networking_capital` varchar(100) DEFAULT NULL COMMENT 'None',
  `invest_capital` varchar(100) DEFAULT NULL COMMENT 'None',
  `retained_earnings` float DEFAULT NULL COMMENT 'None',
  `diluted2_eps` float DEFAULT NULL COMMENT 'None',
  `bps` float DEFAULT NULL COMMENT 'None',
  `ocfps` float DEFAULT NULL COMMENT 'None',
  `retainedps` float DEFAULT NULL COMMENT 'None',
  `cfps` float DEFAULT NULL COMMENT 'None',
  `ebit_ps` varchar(100) DEFAULT NULL COMMENT 'None',
  `fcff_ps` varchar(100) DEFAULT NULL COMMENT 'None',
  `fcfe_ps` varchar(100) DEFAULT NULL COMMENT 'None',
  `netprofit_margin` float DEFAULT NULL COMMENT 'None',
  `grossprofit_margin` varchar(100) DEFAULT NULL COMMENT 'None',
  `cogs_of_sales` varchar(100) DEFAULT NULL COMMENT 'None',
  `expense_of_sales` varchar(100) DEFAULT NULL COMMENT 'None',
  `profit_to_gr` float DEFAULT NULL COMMENT 'None',
  `saleexp_to_gr` varchar(100) DEFAULT NULL COMMENT 'None',
  `adminexp_of_gr` float DEFAULT NULL COMMENT 'None',
  `finaexp_of_gr` varchar(100) DEFAULT NULL COMMENT 'None',
  `impai_ttm` float DEFAULT NULL COMMENT 'None',
  `gc_of_gr` varchar(100) DEFAULT NULL COMMENT 'None',
  `op_of_gr` float DEFAULT NULL COMMENT 'None',
  `ebit_of_gr` varchar(100) DEFAULT NULL COMMENT 'None',
  `roe` float DEFAULT NULL COMMENT 'None',
  `roe_waa` float DEFAULT NULL COMMENT 'None',
  `roe_dt` float DEFAULT NULL COMMENT 'None',
  `roa` varchar(100) DEFAULT NULL COMMENT 'None',
  `npta` float DEFAULT NULL COMMENT 'None',
  `roic` varchar(100) DEFAULT NULL COMMENT 'None',
  `roe_yearly` float DEFAULT NULL COMMENT 'None',
  `roa2_yearly` varchar(100) DEFAULT NULL COMMENT 'None',
  `debt_to_assets` float DEFAULT NULL COMMENT 'None',
  `assets_to_eqt` float DEFAULT NULL COMMENT 'None',
  `dp_assets_to_eqt` float DEFAULT NULL COMMENT 'None',
  `ca_to_assets` varchar(100) DEFAULT NULL COMMENT 'None',
  `nca_to_assets` varchar(100) DEFAULT NULL COMMENT 'None',
  `tbassets_to_totalassets` varchar(100) DEFAULT NULL COMMENT 'None',
  `int_to_talcap` varchar(100) DEFAULT NULL COMMENT 'None',
  `eqt_to_talcapital` varchar(100) DEFAULT NULL COMMENT 'None',
  `currentdebt_to_debt` varchar(100) DEFAULT NULL COMMENT 'None',
  `longdeb_to_debt` varchar(100) DEFAULT NULL COMMENT 'None',
  `ocf_to_shortdebt` varchar(100) DEFAULT NULL COMMENT 'None',
  `debt_to_eqt` float DEFAULT NULL COMMENT 'None',
  `eqt_to_debt` float DEFAULT NULL COMMENT 'None',
  `eqt_to_interestdebt` varchar(100) DEFAULT NULL COMMENT 'None',
  `tangibleasset_to_debt` varchar(100) DEFAULT NULL COMMENT 'None',
  `tangasset_to_intdebt` varchar(100) DEFAULT NULL COMMENT 'None',
  `tangibleasset_to_netdebt` varchar(100) DEFAULT NULL COMMENT 'None',
  `ocf_to_debt` float DEFAULT NULL COMMENT 'None',
  `turn_days` varchar(100) DEFAULT NULL COMMENT 'None',
  `roa_yearly` float DEFAULT NULL COMMENT 'None',
  `roa_dp` float DEFAULT NULL COMMENT 'None',
  `fixed_assets` float DEFAULT NULL COMMENT 'None',
  `profit_to_op` float DEFAULT NULL COMMENT 'None',
  `q_saleexp_to_gr` varchar(100) DEFAULT NULL COMMENT 'None',
  `q_gc_to_gr` varchar(100) DEFAULT NULL COMMENT 'None',
  `q_roe` float DEFAULT NULL COMMENT 'None',
  `q_dt_roe` float DEFAULT NULL COMMENT 'None',
  `q_npta` float DEFAULT NULL COMMENT 'None',
  `q_ocf_to_sales` float DEFAULT NULL COMMENT 'None',
  `basic_eps_yoy` float DEFAULT NULL COMMENT 'None',
  `dt_eps_yoy` float DEFAULT NULL COMMENT 'None',
  `cfps_yoy` float DEFAULT NULL COMMENT 'None',
  `op_yoy` float DEFAULT NULL COMMENT 'None',
  `ebt_yoy` float DEFAULT NULL COMMENT 'None',
  `netprofit_yoy` float DEFAULT NULL COMMENT 'None',
  `dt_netprofit_yoy` float DEFAULT NULL COMMENT 'None',
  `ocf_yoy` float DEFAULT NULL COMMENT 'None',
  `roe_yoy` float DEFAULT NULL COMMENT 'None',
  `bps_yoy` float DEFAULT NULL COMMENT 'None',
  `assets_yoy` float DEFAULT NULL COMMENT 'None',
  `eqt_yoy` float DEFAULT NULL COMMENT 'None',
  `tr_yoy` float DEFAULT NULL COMMENT 'None',
  `or_yoy` float DEFAULT NULL COMMENT 'None',
  `q_sales_yoy` float DEFAULT NULL COMMENT 'None',
  `q_op_qoq` float DEFAULT NULL COMMENT 'None',
  `equity_yoy` float DEFAULT NULL COMMENT 'None',
  `pb` float DEFAULT NULL COMMENT '市净率（总市值/净资产）',
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tushare_balancesheet` (
  `id` varchar(100) NOT NULL COMMENT 'None',
  `ts_code` varchar(100) DEFAULT NULL COMMENT 'None',
  `ann_date` varchar(100) DEFAULT NULL COMMENT 'None',
  `f_ann_date` varchar(100) DEFAULT NULL COMMENT 'None',
  `end_date` varchar(100) DEFAULT NULL COMMENT 'None',
  `report_type` varchar(100) DEFAULT NULL COMMENT 'None',
  `comp_type` varchar(100) DEFAULT NULL COMMENT 'None',
  `total_share` float DEFAULT NULL COMMENT 'None',
  `cap_rese` float DEFAULT NULL COMMENT 'None',
  `undistr_porfit` float DEFAULT NULL COMMENT 'None',
  `surplus_rese` float DEFAULT NULL COMMENT 'None',
  `special_rese` varchar(100) DEFAULT NULL COMMENT 'None',
  `money_cap` varchar(100) DEFAULT NULL COMMENT 'None',
  `trad_asset` float DEFAULT NULL COMMENT 'None',
  `notes_receiv` varchar(100) DEFAULT NULL COMMENT 'None',
  `accounts_receiv` varchar(100) DEFAULT NULL COMMENT 'None',
  `oth_receiv` varchar(100) DEFAULT NULL COMMENT 'None',
  `prepayment` varchar(100) DEFAULT NULL COMMENT 'None',
  `div_receiv` varchar(100) DEFAULT NULL COMMENT 'None',
  `int_receiv` float DEFAULT NULL COMMENT 'None',
  `inventories` varchar(100) DEFAULT NULL COMMENT 'None',
  `amor_exp` varchar(100) DEFAULT NULL COMMENT 'None',
  `nca_within_1y` varchar(100) DEFAULT NULL COMMENT 'None',
  `sett_rsrv` varchar(100) DEFAULT NULL COMMENT 'None',
  `loanto_oth_bank_fi` float DEFAULT NULL COMMENT 'None',
  `premium_receiv` varchar(100) DEFAULT NULL COMMENT 'None',
  `reinsur_receiv` varchar(100) DEFAULT NULL COMMENT 'None',
  `reinsur_res_receiv` varchar(100) DEFAULT NULL COMMENT 'None',
  `pur_resale_fa` float DEFAULT NULL COMMENT 'None',
  `oth_cur_assets` varchar(100) DEFAULT NULL COMMENT 'None',
  `total_cur_assets` varchar(100) DEFAULT NULL COMMENT 'None',
  `fa_avail_for_sale` float DEFAULT NULL COMMENT 'None',
  `htm_invest` float DEFAULT NULL COMMENT 'None',
  `lt_eqt_invest` float DEFAULT NULL COMMENT 'None',
  `invest_real_estate` varchar(100) DEFAULT NULL COMMENT 'None',
  `time_deposits` varchar(100) DEFAULT NULL COMMENT 'None',
  `oth_assets` float DEFAULT NULL COMMENT 'None',
  `lt_rec` varchar(100) DEFAULT NULL COMMENT 'None',
  `fix_assets` float DEFAULT NULL COMMENT 'None',
  `cip` varchar(100) DEFAULT NULL COMMENT 'None',
  `const_materials` varchar(100) DEFAULT NULL COMMENT 'None',
  `fixed_assets_disp` varchar(100) DEFAULT NULL COMMENT 'None',
  `produc_bio_assets` varchar(100) DEFAULT NULL COMMENT 'None',
  `oil_and_gas_assets` varchar(100) DEFAULT NULL COMMENT 'None',
  `intan_assets` float DEFAULT NULL COMMENT 'None',
  `r_and_d` varchar(100) DEFAULT NULL COMMENT 'None',
  `goodwill` float DEFAULT NULL COMMENT 'None',
  `lt_amor_exp` varchar(100) DEFAULT NULL COMMENT 'None',
  `defer_tax_assets` float DEFAULT NULL COMMENT 'None',
  `decr_in_disbur` float DEFAULT NULL COMMENT 'None',
  `oth_nca` varchar(100) DEFAULT NULL COMMENT 'None',
  `total_nca` varchar(100) DEFAULT NULL COMMENT 'None',
  `cash_reser_cb` float DEFAULT NULL COMMENT 'None',
  `depos_in_oth_bfi` float DEFAULT NULL COMMENT 'None',
  `prec_metals` float DEFAULT NULL COMMENT 'None',
  `deriv_assets` float DEFAULT NULL COMMENT 'None',
  `rr_reins_une_prem` varchar(100) DEFAULT NULL COMMENT 'None',
  `rr_reins_outstd_cla` varchar(100) DEFAULT NULL COMMENT 'None',
  `rr_reins_lins_liab` varchar(100) DEFAULT NULL COMMENT 'None',
  `rr_reins_lthins_liab` varchar(100) DEFAULT NULL COMMENT 'None',
  `refund_depos` varchar(100) DEFAULT NULL COMMENT 'None',
  `ph_pledge_loans` varchar(100) DEFAULT NULL COMMENT 'None',
  `refund_cap_depos` varchar(100) DEFAULT NULL COMMENT 'None',
  `indep_acct_assets` varchar(100) DEFAULT NULL COMMENT 'None',
  `client_depos` varchar(100) DEFAULT NULL COMMENT 'None',
  `client_prov` varchar(100) DEFAULT NULL COMMENT 'None',
  `transac_seat_fee` varchar(100) DEFAULT NULL COMMENT 'None',
  `invest_as_receiv` float DEFAULT NULL COMMENT 'None',
  `total_assets` float DEFAULT NULL COMMENT 'None',
  `lt_borr` varchar(100) DEFAULT NULL COMMENT 'None',
  `st_borr` varchar(100) DEFAULT NULL COMMENT 'None',
  `cb_borr` float DEFAULT NULL COMMENT 'None',
  `depos_ib_deposits` varchar(100) DEFAULT NULL COMMENT 'None',
  `loan_oth_bank` float DEFAULT NULL COMMENT 'None',
  `trading_fl` float DEFAULT NULL COMMENT 'None',
  `notes_payable` varchar(100) DEFAULT NULL COMMENT 'None',
  `acct_payable` varchar(100) DEFAULT NULL COMMENT 'None',
  `adv_receipts` varchar(100) DEFAULT NULL COMMENT 'None',
  `sold_for_repur_fa` float DEFAULT NULL COMMENT 'None',
  `comm_payable` varchar(100) DEFAULT NULL COMMENT 'None',
  `payroll_payable` float DEFAULT NULL COMMENT 'None',
  `taxes_payable` float DEFAULT NULL COMMENT 'None',
  `int_payable` float DEFAULT NULL COMMENT 'None',
  `div_payable` varchar(100) DEFAULT NULL COMMENT 'None',
  `oth_payable` varchar(100) DEFAULT NULL COMMENT 'None',
  `acc_exp` varchar(100) DEFAULT NULL COMMENT 'None',
  `deferred_inc` varchar(100) DEFAULT NULL COMMENT 'None',
  `st_bonds_payable` varchar(100) DEFAULT NULL COMMENT 'None',
  `payable_to_reinsurer` varchar(100) DEFAULT NULL COMMENT 'None',
  `rsrv_insur_cont` varchar(100) DEFAULT NULL COMMENT 'None',
  `acting_trading_sec` varchar(100) DEFAULT NULL COMMENT 'None',
  `acting_uw_sec` varchar(100) DEFAULT NULL COMMENT 'None',
  `non_cur_liab_due_1y` varchar(100) DEFAULT NULL COMMENT 'None',
  `oth_cur_liab` varchar(100) DEFAULT NULL COMMENT 'None',
  `total_cur_liab` varchar(100) DEFAULT NULL COMMENT 'None',
  `bond_payable` float DEFAULT NULL COMMENT 'None',
  `lt_payable` varchar(100) DEFAULT NULL COMMENT 'None',
  `specific_payables` varchar(100) DEFAULT NULL COMMENT 'None',
  `estimated_liab` float DEFAULT NULL COMMENT 'None',
  `defer_tax_liab` float DEFAULT NULL COMMENT 'None',
  `defer_inc_non_cur_liab` varchar(100) DEFAULT NULL COMMENT 'None',
  `oth_ncl` varchar(100) DEFAULT NULL COMMENT 'None',
  `total_ncl` varchar(100) DEFAULT NULL COMMENT 'None',
  `depos_oth_bfi` float DEFAULT NULL COMMENT 'None',
  `deriv_liab` float DEFAULT NULL COMMENT 'None',
  `depos` float DEFAULT NULL COMMENT 'None',
  `agency_bus_liab` varchar(100) DEFAULT NULL COMMENT 'None',
  `oth_liab` float DEFAULT NULL COMMENT 'None',
  `prem_receiv_adva` varchar(100) DEFAULT NULL COMMENT 'None',
  `depos_received` varchar(100) DEFAULT NULL COMMENT 'None',
  `ph_invest` varchar(100) DEFAULT NULL COMMENT 'None',
  `reser_une_prem` varchar(100) DEFAULT NULL COMMENT 'None',
  `reser_outstd_claims` varchar(100) DEFAULT NULL COMMENT 'None',
  `reser_lins_liab` varchar(100) DEFAULT NULL COMMENT 'None',
  `reser_lthins_liab` varchar(100) DEFAULT NULL COMMENT 'None',
  `indept_acc_liab` varchar(100) DEFAULT NULL COMMENT 'None',
  `pledge_borr` varchar(100) DEFAULT NULL COMMENT 'None',
  `indem_payable` varchar(100) DEFAULT NULL COMMENT 'None',
  `policy_div_payable` varchar(100) DEFAULT NULL COMMENT 'None',
  `total_liab` float DEFAULT NULL COMMENT 'None',
  `treasury_share` varchar(100) DEFAULT NULL COMMENT 'None',
  `ordin_risk_reser` float DEFAULT NULL COMMENT 'None',
  `forex_differ` varchar(100) DEFAULT NULL COMMENT 'None',
  `invest_loss_unconf` varchar(100) DEFAULT NULL COMMENT 'None',
  `minority_int` float DEFAULT NULL COMMENT 'None',
  `total_hldr_eqy_exc_min_int` float DEFAULT NULL COMMENT 'None',
  `total_hldr_eqy_inc_min_int` float DEFAULT NULL COMMENT 'None',
  `total_liab_hldr_eqy` float DEFAULT NULL COMMENT 'None',
  `lt_payroll_payable` varchar(100) DEFAULT NULL COMMENT 'None',
  `oth_comp_income` float DEFAULT NULL COMMENT 'None',
  `oth_eqt_tools` float DEFAULT NULL COMMENT 'None',
  `oth_eqt_tools_p_shr` float DEFAULT NULL COMMENT 'None',
  `lending_funds` varchar(100) DEFAULT NULL COMMENT 'None',
  `acc_receivable` varchar(100) DEFAULT NULL COMMENT 'None',
  `st_fin_payable` varchar(100) DEFAULT NULL COMMENT 'None',
  `payables` varchar(100) DEFAULT NULL COMMENT 'None',
  `hfs_assets` varchar(100) DEFAULT NULL COMMENT 'None',
  `hfs_sales` varchar(100) DEFAULT NULL COMMENT 'None',
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tushare_daily_basic` (
  `ts_code` varchar(100) DEFAULT NULL COMMENT 'None',
  `trade_date` varchar(100) DEFAULT NULL COMMENT 'None',
  `close` float DEFAULT NULL COMMENT 'None',
  `volume_ratio` float DEFAULT NULL COMMENT 'None',
  `pe` float DEFAULT NULL COMMENT 'None',
  `pe_ttm` float DEFAULT NULL COMMENT 'None',
  `pb` float DEFAULT NULL COMMENT 'None',
  `ps` float DEFAULT NULL COMMENT 'None',
  `ps_ttm` float DEFAULT NULL COMMENT 'None',
  `dv_ratio` float DEFAULT NULL COMMENT 'None',
  `dv_ttm` float DEFAULT NULL COMMENT 'None',
  `total_share` float DEFAULT NULL COMMENT 'None',
  `float_share` float DEFAULT NULL COMMENT 'None',
  `free_share` float DEFAULT NULL COMMENT 'None',
  `total_mv` float DEFAULT NULL COMMENT 'None',
  `circ_mv` float DEFAULT NULL COMMENT 'None'
) DEFAULT CHARSET=utf8mb4;





