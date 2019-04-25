__author__ = 'JianqingJiang'
# -*- coding: utf-8 -*-
import urllib.request
from lxml import etree
import os
pre_url ='https://cn.torrentkitty.org/search/tokyohot/'
os.chdir('C:\\Users\\Administrator\\Downloads\\新建文件夹\\pyhttp\\eventTracker\\')

def steve(page_num,file_name):
    url = pre_url + str(page_num)
    print(url) 
    hv = urllib.request.Request(url)
    ht=urllib.request.urlopen(hv).read()
    content = etree.HTML(ht.lower().decode('utf-8'))
    mags = content.xpath("//a[@rel='magnet']")
    with open(file_name,'a') as p: # '''Note'''：Ａppend mode, run only once!
        for mag in mags:
            p.write("%s \n \n"%(mag.attrib['href'])+"\n") ##!!encode here to utf-8 to avoid encoding
            print("%s \n \n"%(mag.attrib['href']))

for page_num in range(0,10):
    print (page_num)
    steve(page_num, 'steve.txt')
