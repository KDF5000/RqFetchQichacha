#-*-coding:utf-8 -*-
__author__ = 'Defei'

from redis import Redis
from rq import Queue
from SearchData import fetch_data

#连接redis
redis_conn = Redis(host='192.168.0.108', port=6379)
q = Queue(connection=redis_conn, async=True)  # 设置async为False则入队后会自己执行 不用调用perform

i = 0
with open("company_2.txt", 'r') as f:
    for line in f:
        i += 1
        job = q.enqueue(fetch_data, line.strip())
        print i, ": ", job.id
