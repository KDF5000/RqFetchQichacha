#-*-coding:utf-8 -*-
__author__ = 'Defei'

from redis import Redis
from rq import Queue
from SearchData import fetch_data

#连接redis
redis_conn = Redis(host='192.168.1.108', port=6378)
q = Queue(connection=redis_conn, async=True)  # 设置async为False则入队后会自己执行 不用调用perform

with open("job.txt", 'r') as f:
    for line in f.readlines():
        job = q.enqueue(fetch_data, line.strip())
        print job.id
