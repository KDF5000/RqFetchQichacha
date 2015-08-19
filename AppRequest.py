# -*- coding:utf-8 -*-
__author__ = 'Defei'
import urllib2
import json
import hashlib
import time
class AppRequest(object):
    headers = {
       'User-Agent': "android-async-http/1.4.4 (http://loopj.com/android-async-http)"
    }
    cloud_search = "http://app.qichacha.com//enterprises/new/cloudSearch"
    company_detail = "http://app.qichacha.com//enterprises/new/newGetData"

    __code = "f2f4f29192a11c87864adcd918127a7e"

    def __init__(self, company_name, province=''):
        self.__company_name = company_name
        self.__province = province


    def set_company_name(self, company_name):
        self.__company_name = company_name

    def set_province(self, province):
        self.__province = province

    def set_code(self, code):
        self.__code = code

    '''
        获取unique code
    '''
    def get_unique_code(self):
        unique_code = None
        # 请求获取Unique
        md5 = hashlib.md5()
        md5.update(self.__company_name + self.__province + self.__code)
        token = md5.hexdigest()  #获取MD5后的token
        cloud_search = self.cloud_search + "?key=%s&province=%s&token=%s" % \
                                           (self.__company_name, self.__province, token)
        # # The proxy address and port:
        # proxy_info = {'host': '223.19.139.172', 'port': 80}
        #
        # # We create a handler for the proxy
        # proxy_support = urllib2.ProxyHandler({"http": "http://%(host)s:%(port)d" % proxy_info})
        #
        # # We create an opener which uses this handler:
        # opener = urllib2.build_opener(proxy_support)
        #
        # # Then we install this opener as the default opener for urllib2:
        # urllib2.install_opener(opener)

        req = urllib2.Request(cloud_search, headers=self.headers)
        response = urllib2.urlopen(req)
        try:
            res = json.loads(response.read())
            status = res['status']  # 1是成功
            print 'get unique code:', status
            if status != "1":
                return unique_code
            data_list = res['data']  # data list
            if len(data_list) > 0:
                company = data_list[0]  # 取第一个
                unique_code = company['Unique']
        except Exception, e:
            print e.message
        finally:
            return unique_code



    def get_company_info(self):
        unicode_code = self.get_unique_code()

        if unicode_code is None:
            return None

        company_detail_url = self.company_detail+"?province=%s&unique=%s&user=" % (self.__province, unicode_code)

        # # The proxy address and port:
        # proxy_info = {'host': '223.19.139.172', 'port': 80}
        #
        # # We create a handler for the proxy
        # proxy_support = urllib2.ProxyHandler({"http": "http://%(host)s:%(port)d" % proxy_info})
        #
        # # We create an opener which uses this handler:
        # opener = urllib2.build_opener(proxy_support)
        #
        # # Then we install this opener as the default opener for urllib2:
        # urllib2.install_opener(opener)
        # time.sleep(2)  # 延时1s
        req = urllib2.Request(company_detail_url, headers=self.headers)
        response = urllib2.urlopen(req)

        try:
            res_json = json.loads(response.read())
            status = res_json['status']
            print 'get company_info:', status
            # print res_json
            if status != 1:
                return None
            return res_json['data']
        except Exception, e:
            print e.message














