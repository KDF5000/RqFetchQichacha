# -*- coding=utf-8 -*-
__author__ = 'Defei'
from AppRequest import AppRequest
import json
import time
import sys
reload(sys)

sys.setdefaultencoding('UTF-8')

if __name__ == '__main__':
    appRequest = AppRequest('东莞辣妈萌宝')

    su_num = 0
    err_num = 0

    txt = 'sort.txt'
    fw = open('res.txt', 'w')
    fe = open('error.txt', 'w')
    with open(txt, 'r') as f:
        for line in f.readlines():
            print line.strip().encode('gbk')
            # time.sleep(2)  # 延时2s
            appRequest.set_company_name(line.strip())
            res = appRequest.get_company_info()
            if res is None:
                err_num += 1
                print line.strip().encode('gbk'), 'failed'
                fe.write(line.strip()+'\n')
            else:
                su_num += 1
                fw.write(json.dumps(res)+'\n')
            print 'su:', su_num, 'err_num:', err_num
    fw.close()
    fe.close()






