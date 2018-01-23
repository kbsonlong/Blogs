#-*- coding:utf-8 -*-
#!/ust/bin/env python

##用于csdn新版爬取

from bs4 import BeautifulSoup
from wppost import *


headers = {'Content-Type':'application/json;charset=UTF-8'}
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(filename='spider.log',level=logging.DEBUG,format='[%(asctime)s -%(name)s - %(levelname)s] %(message)s')



host='http://blog.csdn.net'

import logging
import urllib2
import traceback
import os
import json

headers = {'Content-Type':'application/json;charset=UTF-8'}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# logging.basicConfig(filename='monitor.log' % BASE_DIR,level=logging.DEBUG,format='[%(asctime)s -%(name)s - %(levelname)s] %(message)s')




def get_links(url):
    soup = BeautifulSoup(get_info(url),'html.parser')
    hrefs =[]
    for h in soup.find('ul',{'class':'blog-units blog-units-box'}).findAll('a'):
        href =host + h.get('href')
        hrefs.append(href)
    return hrefs


def get_context(links,tags='',category=''):

    news = []
    for url in links:
        soup = BeautifulSoup(get_info(url), 'html.parser')
        print
        try:
            title = soup.find('h1',{'class':'csdn_top'}).get_text()
            soup_context = soup.find('div', {
                'class': 'article_content csdn-tracking-statistics tracking-click'})
            ###删除script标签，很多时候爬取内容中带有内嵌的广告script
            # [s.extract() for s in soup_context('script')]
            context = "%s \n 本文转载自 <a href='%s' targe='_blank'> %s</a> " % (str(soup_context), str(url), str(title))
            image_name = ''
            news.append(Contexts(title, tags, category, context, image_name))
        except Exception as e:
            logging.error(traceback.format_exc())
            print traceback.format_exc()

    return news

if __name__ == '__main__':
    url = 'http://blog.csdn.net/huwh_/article/category/6904662'
    # links = get_links(url)
    links=['http://blog.csdn.net/huwh_/article/details/71308171']
    news = get_context(links,category='Docker',tags='Kubernetes')
    try:
        for new in news:
            user = {'website': 'http://www.along.party/xmlrpc.php', 'username': 'xxxx', 'password': 'xxxx'}
            send_news(user,new)
    except Exception as e:
        print traceback.format_exc()

