#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import sys, os
from pathlib import Path
import time
ROOT = Path(os.path.abspath(__file__)).parent
sys.path.append(str(ROOT))
from deco import *


PROJECT_DIR = ROOT
print("PROJECT_DIR：", PROJECT_DIR)


def execute_tushare_finances(job):
    os.system(f"bash {PROJECT_DIR}/scripts/run.sh critical_investing/{job}")



@concurrent
def tushare_finances():
    """   """
    try:
        TushareFinances_Jobs = [
            "stock_final_indicator.py",
            "stock_cashflow.py",
            "stock_income.py",
            "stock_balancesheet.py",
        ]
        for job in TushareFinances_Jobs:
            execute_tushare_finances(job)

    except:
        pass


@concurrent
def tushare_basices():
    """   """
    try:
        basic_jobs = [
            "stock_basic.py",  # 股票信息数据
            "stock_basic_info.py",  # 股票信息明细数据
        ]
        for job in basic_jobs:
            execute_tushare_finances(job)

    except:
        pass

@concurrent
def tushare_final_indicator():
    """   """
    try:
        TushareFinances_Jobs = [
            "stock_final_indicator.py",
        ]
        for job in TushareFinances_Jobs:
            execute_tushare_finances(job)

    except:
        pass


@concurrent
def tushare_cashflow():
    """   """
    try:
        TushareFinances_Jobs = [
            "stock_cashflow.py",
        ]
        for job in TushareFinances_Jobs:
            execute_tushare_finances(job)

    except:
        pass


@concurrent
def tushare_income():
    """   """
    try:
        TushareFinances_Jobs = [
            "stock_income.py",
        ]
        for job in TushareFinances_Jobs:
            execute_tushare_finances(job)

    except:
        pass


@concurrent
def tushare_balancesheet():
    """   """
    try:
        TushareFinances_Jobs = [
            "stock_balancesheet.py",
        ]
        for job in TushareFinances_Jobs:
            execute_tushare_finances(job)

    except:
        pass

@concurrent
def good_stocks_pool():
    """   """
    try:
        os.system(
            f"bash {PROJECT_DIR}/artch/stocks_pool/execute.sh good_stocks_pool.py"
        )
    except:
        pass

@synchronized
def run():
    tushare_basices()
    tushare_balancesheet()
    tushare_final_indicator()
    tushare_income()
    tushare_cashflow()


if __name__ == "__main__":
    try:
        run()
        # good_stocks_pool()
        time.sleep(10)  # 睡10秒，等待任务执行完成
    finally:
        Jobs = ['critical_investing']
        for job in Jobs:
            os.system(
                "ps -ef | grep '%(job)s' | grep -v grep | awk '{print$2}' | xargs kill -9" % {"job": job}
            )
