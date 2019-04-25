# -*- coding: utf-8 -*-
from urllib import request
import json
from threading import Timer
import time
import os
from cqhttp import CQHttp, Error
from gevent import monkey
from gevent.pywsgi import WSGIServer
import brotli
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


'''

                             _ooOoo_
                            o8888888o
                            88" . "88
                            (| -_- |)
                            O\  =  /O
                         ____/`---'\____
                       .'  \\|     |//  `.
                      /  \\|||  :  |||//  \
                     /  _||||| -:- |||||-  \
                     |   | \\\  -  /// |   |
                     | \_|  ''\---/''  |   |
                     \  .-\__  `-`  ___/-. /
                   ___`. .'  /--.--\  `. . __
                ."" '<  `.___\_<|>_/___.'  >'"".
               | | :  `- \`.;`\ _ /`;.`/ - ` : | |
               \  \ `-.   \_ __\ /__ _/   .-` /  /
          ======`-.____`-.___\_____/___.-`____.-'======
                             `=---='
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                     佛祖保佑        永无BUG
'''



'''
#定时发送高价警报消息
@qqbotsched(second='0')
def warning(bot):
    try:
        for i in warList:
            try: 
                output = '取...取名发现了高价值警报(ฅ´ω`ฅ)\n\n' + worldDict[0][i['MissionInfo']['location']] + ' 等级 ' + str(i['MissionInfo']['minEnemyLevel']) + '-' + str(i['MissionInfo']['maxEnemyLevel'])
            except:
                output = '取...取名发现了高价值警报(ฅ´ω`ฅ)\n\n' + i['MissionInfo']['location'] + ' 等级 ' + str(i['MissionInfo']['minEnemyLevel']) + '-' + str(i['MissionInfo']['maxEnemyLevel'])
            output = output + '\n任务: ' + worldDict[0][i['MissionInfo']['missionType']] + ' - ' + worldDict[0][i['MissionInfo']['faction']]
            if 'countedItems' in i['MissionInfo']['missionReward']:
                item = i['MissionInfo']['missionReward']['countedItems'][0]['ItemType'].split('/')
                try: 
                    item = worldDict[0][item[len(item)-1]]
                except:
                    item = item[len(item)-1]
                item = item + str(i['MissionInfo']['missionReward']['countedItems'][0]['ItemCount']) + ' + 现金 ' + str(i['MissionInfo']['missionReward']['credits'])
            elif 'items' in i['MissionInfo']['missionReward']:
                item = i['MissionInfo']['missionReward']['items'][0].split('/')
                try: 
                    item = worldDict[0][item[len(item)-1]]
                except:
                    item = item[len(item)-1]
                item = item + ' + 现金 ' + str(i['MissionInfo']['missionReward']['credits'])
            else:
                item = '现金 ' + str(i['MissionInfo']['missionReward']['credits'])
            output = output + '\n奖励: ' + item
            timeLeft = int(int(i['Expiry']['$date']['$numberLong'])/1000) - time.time()
            minitue = int(timeLeft/60)
            sec = int(timeLeft - minitue*60)
            output = output + '\n剩余时间: ' + str(minitue) + ' 分钟 ' + str(sec) + ' 秒 '
            gl = bot.List('group', '643489949')
            if gl is not None:
                for group in gl: bot.send(group, output)
            warList.remove(i)
    except:
        pass

'''
'''
@qqbotsched(hour='11,17', minute='55')
def mytask(bot):
    gl = bot.List('group', '456班')
    if gl is not None:
        for group in gl:
            bot.send(group, '同志们：开饭啦啦啦啦啦啦！！！')

'''

'''
    try:
        for i in lastAlerts:
            thisAlerts.remove(i)
    except:
        pass
    try:
        for i in thisAlerts:
            if 'countedItems' in i['MissionInfo']['missionReward']:
                item = i['MissionInfo']['missionReward']['countedItems'][0]['ItemType'].split('/')
                try: 
                    item = worldDict[0][item[len(item)-1]]
                except:
                    item = item[len(item)-1]
            elif 'items' in i['MissionInfo']['missionReward']:
                item = i['MissionInfo']['missionReward']['items'][0].split('/')
                try: 
                    item = worldDict[0][item[len(item)-1]]
                except:
                    item = item[len(item)-1]
            for element in ('泥炭萃取物','蓝图','狗蛋','库娃遗传密码','枪托','枪机','破坏者','亡魂','希芙','光环','反应堆','催化剂','裂罅') :
                if (element in item): warList.append(i)
    except:
        pass
    
    timerLoop(30, updateJson)
'''

def Bangi():
    url='https://api.warframe.market/v1/items/nova_prime_set/orders?'  
    req = request.Request(url)
    data = request.urlopen(req).read()
#    json_string=json.dumps(info['body'])
    

    data = json.loads(data)
    for i in data['payload']['orders']:
        del(i['creation_date'])
        del(i['last_update'])
        del(i['platform'])
        del(i['visible'])
        del(i['id'])
        del(i['quantity'])
        del(i['region'])
        if i['order_type']=='sell':
            del(i['user'])
            del(i['order_type'])
            del(i['platinum'])
        elif i['user']['status']=='offline':
            del(i['user']) 
            del(i['order_type'])
            del(i['platinum'])     
    data['payload']['orders'].sort(key=lambda k: (k.get('platinum', 0)))     
    print(data['payload']['orders'])
'''    anime =data['result'] 
 
    tplt ="{:4}\t{:6}{:8}\n{:20}"  
    output=tplt.format("日期","时间","集数","番名")
    tplt ="{:4}\t{:6}\t{:8}\n{:20}" 
    for i in anime:
        date =i.get('date')
        seasons =i['seasons']
        for n in seasons:
            index =n.get('pub_index')
            time =n.get('pub_time')
            title =n.get('title')
            output=output+'\n'+tplt.format(date,time,str(index),title)
    return output
'''
Bangi()