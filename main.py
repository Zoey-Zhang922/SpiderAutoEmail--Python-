# -*- coding: utf-8 -*-

'''
@Time    : 2020/2/6 15:44
@Author  : Zoey Zhang
@FileName: main.py
@Software: PyCharm
 
'''
from apscheduler.schedulers.blocking import BlockingScheduler

import Spider

if __name__ == '__main__':
    """
    定时执行spider以及auto-email
    """
    # 定时执行主任务BlockingScheduler
    scheduler = BlockingScheduler()
    # 定时爬取数据并发送邮件至用户
    scheduler.add_job(func=Spider.spider_tecent_news.send_request, trigger='cron', day_of_week='1-5', hour=20,
                      minute=8)
    scheduler.start()
