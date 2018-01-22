# -*- coding:utf-8 -*-
#!/usr/bin/env python

import logging
import urllib2
import traceback
import os
import json

headers = {'Content-Type':'application/json;charset=UTF-8'}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# logging.basicConfig(filename='monitor.log' % BASE_DIR,level=logging.DEBUG,format='[%(asctime)s -%(name)s - %(levelname)s] %(message)s')



def get_info(url):
    req = urllib2.Request(url, headers=headers)
    response = None
    try:
        response = urllib2.urlopen(req, timeout=10)
        # print response.getcode()
        # print response.geturl()
        # print response.info()
        result = response.read()
        # logging.info("Success")
        # print result
        return result

    except urllib2.URLError as e:
        # logging.error(e)
        if hasattr(e, 'code'):
            print 'Error code:', e.code
            # print e.read()
            print e.geturl()
            print e.info()
        elif hasattr(e, 'reason'):
            print 'Reason:', e.reason
    except:
        pass
    finally:
        if response:
            response.close()


get_info('https://block.cc/api/v1/coin/list?size=50')