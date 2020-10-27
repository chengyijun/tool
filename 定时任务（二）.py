# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 定时任务（二）.py
@time: 2020/10/27 13:39
@desc:
"""
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler


# 输出时间
def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def main():
    # BlockingScheduler
    scheduler = BlockingScheduler()
    # scheduler.add_job(job, 'cron', day_of_week='1-5', hour=6, minute=30)
    scheduler.add_job(job, 'interval', seconds=5)
    scheduler.start()


if __name__ == '__main__':
    main()
