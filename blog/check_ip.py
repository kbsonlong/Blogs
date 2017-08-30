# -*- coding: utf-8 -*-
import urllib2
import re

def check_ip(ip):
    try:
        while True:
            ipaddr = ip
            if ipaddr == "" or ipaddr == 'exit':
                break
            else:
                url = "http://www.ip138.com/ips138.asp?ip=%s&action=2" % ipaddr
                u = urllib2.urlopen(url)
                s = u.read()
                # Get IP Address
                ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', s)
                print "\n****** Below Result From IP138 Database *****"
                print "IP Address:", ip[0]
                # Get IP Address Location
                result = re.findall(r'(<li>.*?</li>)', s)
                for i in result:
                    print i[4:-5]
                print "*" * 45
                print "\n"

    except:
        print "Not Data Find"



import requests
def checkip(ip):
    URL = 'http://ip.taobao.com/service/getIpInfo.php'
    try:

        r = requests.get(URL, params={'ip': ip}, timeout=3)
    except requests.RequestException as e:
        print(e)
    else:
        # print r.content
        json_data = r.json()
        print "\n****** Below Result From ip.taobao Database *****"
        if json_data[u'code'] == 0:
            print '所在国家： ' + json_data[u'data'][u'country'].encode('utf-8')
            print '所在地区： ' + json_data[u'data'][u'area'].encode('utf-8')
            print '所在省份： ' + json_data[u'data'][u'region'].encode('utf-8')
            print '所在城市： ' + json_data[u'data'][u'city'].encode('utf-8')
            print '所属运营商：' + json_data[u'data'][u'isp'].encode('utf-8')
        else:
            print '查询失败,请稍后再试！'


def lookup(ip):
    # URL = 'http://freeipapi.17mon.cn/' + ip
    URL = 'http://www.along.party/17monipdb/checkip.php?ip=' + ip
    try:
        r = requests.get(URL, timeout=3)
    except requests.RequestException as e:
        print(e)
    print "\n****** Below Result From 17mon Database *****"
    json_data = r.json()
    print '所在国家：' + json_data[0].encode('utf-8')
    print '所在省份：' + json_data[1].encode('utf-8')
    print '所在城市：' + json_data[2].encode('utf-8')
    return (ip)


ip = '202.102.193.68'
checkip(ip)


check_ip(ip)

lookup(ip)