# -*- coding: utf-8 -*-
'''
版权所有（C） 2017 <SetnameWang>
这一程序是自由软件，你可以遵照自由软件基金会出版的GNU通用公共许可证条款来修改和重新发布这一程序。或者用许可证的第二版，或者（根据你的选择）用任何更新的版本。
发布这一程序的目的是希望它有用，但没有任何担保。甚至没有适合特定目的的隐含的担保。更详细的情况请参阅GNU通用公共许可证。
你应该已经和程序一起收到一份GNU通用公共许可证的副本。如果还没有，
写信给：
The Free Software Foundation, Inc., 675 Mass Ave, Cambridge,
MA02139, USA
还应加上如何和你保持联系的信息。
如果程序以交互方式进行工作，当它开始进入交互方式工作时，使它输出类似下面的简短声明：
Gnomovision 第69版， 版权所有（C） 19XX， 作者姓名，
Gnomovision绝对没有担保。 要知道详细情况，请输入‘show w’。
这是自由软件，欢迎你遵守一定的条件重新发布它，要知道详细情况，
请输入‘show c’。
假设的命令‘show w’和‘show c’应显示通用公共许可证的相应条款。当然，你使用的命令名称可以不同于‘show w’和‘show c’。根据你的程序的具体情况，也可以用菜单或鼠标选项来显示这些条款。
如果需要，你应该取得你的上司（如果你是程序员）或你的学校签署放弃程序版权的声明。下面只是一个例子，你应该改变相应的名称：
Yoyodyne公司以此方式放弃James Harker
所写的 Gnomovision程序的全部版权利益。
，1989.4.1
Ty coon副总裁
这一许可证不允许你将程序并入专用程序。如果你的程序是一个子程序库。
你可能会认为用库的方式和专用应用程序连接更有用。如果这是你想做的事，使用GNU库通用公共许可证代替本许可证。
'''
import dateutil.parser
#import pytz

from datetime import datetime
from urllib import request
import json
from threading import Timer
import time
import os
from cqhttp import CQHttp, Error
from gevent import monkey
from gevent.pywsgi import WSGIServer
import ssl
from sqlitedata import initdb,deledb
import logging
import socket

socket.setdefaulttimeout(20)
LOG_FILENAME = 'C:/Users/Administrator/Downloads/warframe-qqbot/eventTracker/tmp/logging_example.out'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,)
 
logging.debug('This message should go to the log file')

ssl._create_default_https_context = ssl._create_unverified_context
monkey.patch_all()

bot = CQHttp(api_root='http://127.0.0.1:5700/',
             access_token='123',
             secret='abc')



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
def choujiang(common):
    print(common)
    empty = True
    try: 
        name = memberDict[0][str(common)]
        empty = False
    except:
        pass
    if empty == True:
        #载入词库
        path = os.path.dirname(os.path.realpath(__file__))
        file = open(path + "\choujiangdict.txt", "a+",encoding="utf-8")
        #写入词库
        file.write('\n' + str(common))
        #加入字典文件
        memberDict[0][str(common)] = str(common)
        return '参加成功(*/ω＼*)'
    else:
        return '你已经参加过了呢(。﹏。*)'

def translate(common):
    print(common)
    info = common
    global itemDirectionary
    numTry = 0
    empty = True
    while numTry < 2:
        try: 
            name = worldDict[numTry][info[0]]
            empty = False
            numTry = numTry +1
        except:
            numTry = numTry+1
    print(info)
    if empty == True:
        #载入词库
        path = os.path.dirname(os.path.realpath(__file__))
        file = open(path + "\worldDATA.txt", "a+",encoding="utf-8")
        #写入词库
        file.write('\n' + info[0] + '=' + info[1])
        #加入字典文件
        worldDict[0][info[0]] = info[1]
        worldDict[1][info[1]] = info[0]
        return '翻译成功(*/ω＼*)智子更聪明啦'
    else:
        return '写入字典失败(。﹏。*)\n哪里出了问题呢......'

def clock():
    gl = bot.get_group_list()
    if gl is not None:
        for group in gl:
            bot.send_group_msg(group_id=int(group['group_id']), message='护肝小天使智子提醒您，现在已经'+str(int(time.localtime(time.time()).tm_hour))+'点了\n注意身体请及时睡觉喔')
def translateitems(common):
    print(common)
    info = common
    global itemDirectionary
    numTry = 0
    empty = True
    while numTry < 2:
        try: 
            name = itemDirectionary[numTry][info[0]]
            empty = False
            numTry = numTry +1
        except:
            numTry = numTry+1
    print(info)
    if empty == True:
        #载入词库
        path = os.path.dirname(os.path.realpath(__file__))
        file = open(path + "\data.txt", "a+",encoding="utf-8")
        #写入词库
        file.write('\n' + info[0] + '=' + info[1])
        #加入字典文件
        itemDirectionary[0][info[0]] = info[1]
        itemDirectionary[1][info[1]] = info[0]
        return '翻译成功(*/ω＼*)智子更聪明啦'
    else:
        return '写入字典失败(。﹏。*)\n哪里出了问题呢......'




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

#循环
def timerLoop(inc, updateJson):
    t = Timer(inc, updateJson)
    t.start()

def study(data):
    initdb(data)
    return '学习成功(*/ω＼*)智子更聪明啦'
    
def delestudy(data):
    deledb(data)

def loadDataDict():
    #载入词库
    path = os.path.dirname(os.path.realpath(__file__))
    file = open(path + "\data.txt", "r", encoding='UTF-8')
    itemDirc = [{},{}]
    for lines in file.readlines():
        lines = lines.rstrip("\n")
        linebar = lines.split('=')
        itemDirc[0][linebar[0]] = linebar[1]
        itemDirc[1][linebar[1]] = linebar[0]
    file.close()
    return itemDirc
def loadDict():
    #载入词库
    path = os.path.dirname(os.path.realpath(__file__))
    file = open(path + "\worldDATA.txt", "r", encoding='UTF-8')
    itemDirc = [{},{}]
    for lines in file.readlines():
        lines = lines.rstrip("\n")
        linebar = lines.split('=')
        itemDirc[0][linebar[0]] = linebar[1]
        itemDirc[1][linebar[1]] = linebar[0]
    file.close()
    return itemDirc

def loadmemberDict():
    #载入词库
    path = os.path.dirname(os.path.realpath(__file__))
    file = open(path + "\choujiangdict.txt", "r", encoding='UTF-8')
    itemDirc = [{},{}]
    for lines in file.readlines():
        lines = lines.rstrip("\n")
        itemDirc[0][lines] = lines
    file.close()
    return itemDirc

def searchPrice(name):
    try: 
        name = itemDirectionary[0][name]
    except:
        empty = True
    name=name.replace(" ","_")
    print(name+'asdasdasd')
    print('searching item price...')
    url = 'https://api.warframe.market/v1/items/'+name+'/orders?'
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
        
    data['payload']['orders'].sort(key=lambda k: (k.get('platinum', 0)))
    #存储worldstate数据
    PriceData = data['payload']['orders']
    print('update complate...')
    Output='智子为您查询到以下信息(。・∀・)ノ\n名称: ' + name+'\n名字  价格  状态'

    for i in PriceData:
        if i['order_type']=='sell' and i['user']['status']!='offline':
            Output=Output+'\n'+i['user']['ingame_name']+'  '+str(i['platinum'])+'  '+i['user']['status']
    return Output
#获取JSON文件
def updateJson():
    if int(time.localtime(time.time()).tm_hour)==23 and int(time.localtime(time.time()).tm_min)==0:
        print('sending world tip...')
        clock()
    print('updating world data...')
    url = 'http://content.warframe.com/dynamic/worldState.php'
    url1 = 'https://api.warframestat.us/pc/cetusCycle'
    url2 = 'https://api.warframestat.us/pc/vallisCycle'
    url3 = 'https://api.warframestat.us/pc/nightwave'
    try:
        header={'user-agent':'chrome/10'}
        req = request.Request(url)
        response = request.urlopen(req)
        data = response.read()
        data = json.loads(data)
        req1 = request.Request(url1,headers=header)
        response1 = request.urlopen(req1)
        data1 = response1.read()
        data1 = json.loads(data1)
        req2 = request.Request(url2,headers=header)
        response2 = request.urlopen(req2)
        data2 = response2.read()
        data2 = json.loads(data2)
        req3 = request.Request(url3,headers=header)
        response3 = request.urlopen(req3)
        data3 = response3.read()
        data3 = json.loads(data3)
#    json_string=json.dumps(info['body'])
    
        del(data['Date'])
        del(data['WorldSeed'])
        del(data['Version'])
        del(data['MobileVersion'])
        del(data['BuildLabel'])
        del(data['Events'])
        del(data['Goals'])
        del(data['GlobalUpgrades'])
        del(data['FlashSales'])
        del(data['HubEvents'])
        del(data['NodeOverrides'])
        del(data['BadlandNodes'])
        del(data['PrimeAccessAvailability'])
        del(data['PrimeVaultAvailabilities'])
        del(data['LibraryInfo'])
        del(data['PVPChallengeInstances'])
        del(data['PersistentEnemies'])
        del(data['PVPAlternativeModes'])
        del(data['PVPActiveTournaments'])
        del(data['ProjectPct'])
        del(data['ConstructionProjects'])
        del(data['TwitchPromos'])
    
        global worldData
        global timeNow,vallistimeNow,Nightwavestate
        global warList
        global lastAlerts
        global thisAlerts
    #存储上一次警报
        try:
            Nightwavestate=data3
      #  print(data3)
            timeNow = data1
      #  print(data1)
            vallistimeNow = data2
            print(data2)
            worldData = data
            print('update complate...')
    #存储本次警报
            thisAlerts = data['Alerts']
            lastAlerts = worldData['Alerts']
        except:
            lastAlerts = []
    #存储worldstate数据
     
        response.close()
    except:
        logging.exception(time.localtime(time.time()))
    '''
    剩余八个参数：
    Time              > 时间
    Alerts            > 警报
    Sorties           > 突击
    SyndicateMissions > 集团任务
    ActiveMissions    > 裂隙
    Invasions         > 入侵
    VoidTraders       > 虚空商人
    DailyDeals        > 每日折扣
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
    '''

    timerLoop(60, updateJson)

#突击函数
def Nightwave():
    output =  '午夜电波更新时间还剩\n智子发现现在有午夜电波任务[' + str(len(Nightwavestate['activeChallenges'])) + ']个：'
    for i in Nightwavestate['activeChallenges']:
        output = output + '\n\任务: ' + i['title']
        output = output + '\n\n内容: ' + i['desc']
        output = output + '\n获得声望: ' + i['reputation']
        if i['active']==true:
            output = output + '\n状态: 正在进行'
        else:
            output = output + '\n状态: 未进行'
        if i['isDaily']==true:
            output = output + '\n任务类型: 日常'
        else:
            output = output + '\n任务类型: 周常'
        if i['isElite']==true:
            output = output + '精英任务'
        else:
            output = output + '任务'
        local_time = dateutil.parser.parse(i['expiry']).astimezone(pytz.timezone('Asia/Shanghai'))-datetime.now()  
    return output

#突击函数
def Sorties():
    output = str(worldDict[0][worldData['Sorties'][0]['Boss']]) + ''
    for i in worldData['Sorties'][0]['Variants']:
        try:
            output = output + '\n\n地点: ' + worldDict[0][i['node']]
        except:
            output = output + '\n\n地点: ' + i['node']
        output = output + '\n任务: ' + worldDict[0][i['missionType']]
        output = output + '\n状态: ' + worldDict[0][i['modifierType']]
    return output
#突击函数
def Active():
    output = '智子发现现在有裂缝[' + str(len(worldData['ActiveMissions'])) + ']个：'
    for i in worldData['ActiveMissions']:
        if i['Modifier']=='VoidT1':
            try:
                output = output + '\n\n地点: ' + worldDict[0][i['Node']]
            except:
                output = output + '\n\n地点: ' + i['Node']
            output = output + '\n任务: ' + worldDict[0][i['MissionType']]
            output = output + '\n状态: ' + worldDict[0][i['Modifier']]
            timeLeft = int(int(i['Expiry']['$date']['$numberLong'])/1000) - time.time()
            minitue = int(timeLeft/60)
            sec = int(timeLeft - minitue*60)
            output = output + '\n剩余时间: ' + str(minitue) + ' 分钟 ' + str(sec) + ' 秒 '
    for i in worldData['ActiveMissions']:
        if i['Modifier']=='VoidT2':
            try:
                output = output + '\n\n地点: ' + worldDict[0][i['Node']]
            except:
                output = output + '\n\n地点: ' + i['Node']
            output = output + '\n任务: ' + worldDict[0][i['MissionType']]
            output = output + '\n状态: ' + worldDict[0][i['Modifier']]
            timeLeft = int(int(i['Expiry']['$date']['$numberLong'])/1000) - time.time()
            minitue = int(timeLeft/60)
            sec = int(timeLeft - minitue*60)
            output = output + '\n剩余时间: ' + str(minitue) + ' 分钟 ' + str(sec) + ' 秒 '  
    for i in worldData['ActiveMissions']:
        if i['Modifier']=='VoidT3':
            try:
                output = output + '\n\n地点: ' + worldDict[0][i['Node']]
            except:
                output = output + '\n\n地点: ' + i['Node']
            output = output + '\n任务: ' + worldDict[0][i['MissionType']]
            output = output + '\n状态: ' + worldDict[0][i['Modifier']]
            timeLeft = int(int(i['Expiry']['$date']['$numberLong'])/1000) - time.time()
            minitue = int(timeLeft/60)
            sec = int(timeLeft - minitue*60)
            output = output + '\n剩余时间: ' + str(minitue) + ' 分钟 ' + str(sec) + ' 秒 ' 
    for i in worldData['ActiveMissions']:
        if i['Modifier']=='VoidT4':
            try:
                output = output + '\n\n地点: ' + worldDict[0][i['Node']]
            except:
                output = output + '\n\n地点: ' + i['Node']
            output = output + '\n任务: ' + worldDict[0][i['MissionType']]
            output = output + '\n状态: ' + worldDict[0][i['Modifier']]
            timeLeft = int(int(i['Expiry']['$date']['$numberLong'])/1000) - time.time()
            minitue = int(timeLeft/60)
            sec = int(timeLeft - minitue*60)
            output = output + '\n剩余时间: ' + str(minitue) + ' 分钟 ' + str(sec) + ' 秒 '   
    return output

#警报
def Alerts():
    output = '智子发现现在有警报[' + str(len(worldData['Alerts'])) + ']个：'
    for i in worldData['Alerts']:
        try: 
            output = output + '\n\n' + worldDict[0][i['MissionInfo']['location']] + ' 等级 ' + str(i['MissionInfo']['minEnemyLevel']) + '-' + str(i['MissionInfo']['maxEnemyLevel'])
        except:
            output = output + '\n\n' + i['MissionInfo']['location'] + ' 等级 ' + str(i['MissionInfo']['minEnemyLevel']) + '-' + str(i['MissionInfo']['maxEnemyLevel'])
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
    return output

def Bangi():
    url='https://bangumi.bilibili.com/web_api/timeline_global'  
    req = request.Request(url)
    data = request.urlopen(req).read()
    data =json.loads(data)  
    anime =data['result'] 
 
    tplt ="{:20}\n{:4}\t{:6}{:8}"  
    output=tplt.format("番名","日期","时间","集数")
    tplt ="{:20}\n{:4}\t{:6}\t{:8}" 
    for i in anime:
        date =i.get('date')
        seasons =i['seasons']
        for n in seasons:
            index =n.get('pub_index')
            time =n.get('pub_time')
            title =n.get('title')
            output=output+'\n'+tplt.format(title,time,str(index),date)
    return output

def LBangi():
    url='https://idanmu.at/category/v09/v10/feed/'  
    req = request.Request(url)
    data = request.urlopen(req).read()
    data =json.loads(data)  
    anime =data['result'] 
 
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

@bot.on_request('group', 'friend')
def handle_request(context):
   return {'approve': True}  # 同意所有加群、加好友请求

@bot.on_message()
def handle_msg(context):
    contexts=context['message'].split()
    # 下面这句等价于 bot.send_private_msg(user_id=context['user_id'], message='你好呀，下面一条是你刚刚发的：')
    #if context['user_id']== 525040433 and context['message_type']== 'private':
       # bot.send(context,'[CQ:share,url=baidu.com,image=https://pub-static.haozhaopian.net/static/web/site/features/cn/crop/images/crop_20a7dc7fbd29d679b456fa0f77bd9525d.jpg] ')
    #    bot.send_private_msg(user_id=context['user_id'], message='护肝小天使智子提醒您，现在已经' + str(int(time.localtime(time.time()).tm_hour)) + '点了\n注意身体请及时睡觉喔')
    if context['message'] in ('js','奸商','虚空商人') and context['message'] != '':
        timeLeft = int(worldData['VoidTraders'][0]['Activation']['$date']['$numberLong'])/1000 - int(worldData['Time'])
        if timeLeft > 0:
            day = int(timeLeft/86400)
            hour = int(timeLeft/3600 - day*24)
            minitue = int(timeLeft/60 - hour*60 - day*1440)
            bot.send(context, '智子翻了翻日历ʅ（´◔౪◔）ʃ\n奸商还剩：\n' + str(day) + ' 天 ' + str(hour) + ' 小时 ' + str(minitue) + ' 分钟 就来坑你钱啦！')
        else:
            timeLeft = int(worldData['VoidTraders'][0]['Expiry']['$date']['$numberLong'])/1000 - int(worldData['Time'])
            day = int(timeLeft/86400)
            hour = int(timeLeft/3600 - day*24)
            minitue = int(timeLeft/60 - hour*60 - day*1440)
            bot.send(context, '奸商还剩：\n' + str(day) + ' 天 ' + str(hour) + ' 小时 ' + str(minitue) + ' 分钟 就要跑啦！\n刺杀奸商 = 3')
    if context['message'] in ('平原','希图斯','稀图斯','平原时间') and context['message'] != '':
        timeL=timeNow['timeLeft']
        if timeNow['isDay'] ==True: 
            output = '智子偷偷告诉你，白天的平原风景正好，赶紧去捕鱼吧~\n\n还剩 ' + timeL + ' Boss就要来吓人了喔'    
            bot.send(context,output)
        elif timeNow['isDay']==False: 
            output = '晚上啦，平原闹鬼啦\n\n还剩 ' + timeL + ' Boss就要休息不吓人了哟。'
            bot.send(context,output)
    if context['message'] in ('金星平原','金星','金星时间') and context['message'] != '':
        timeL=vallistimeNow['timeLeft']
        if vallistimeNow['isWarm'] ==True: 
            output = '智子偷偷告诉你，白天的金星平原温度正好，赶紧去捕鱼吧~\n\n还剩 ' + timeL + ' 就要变冷了喔'    
            bot.send(context,output)
        elif vallistimeNow['isWarm']==False: 
            output = '晚上啦，金星平原变得更加寒冷啦\n\n还剩 ' + timeL + ' 就要暖和起来了哟。'
            bot.send(context,output)
   # if context['message'] in ('午夜电波'，'电波','土狼') and context['message'] != '':
   #     try:
   #         bot.send(context, Nightwave())
   #     except Error:
    #        pass
    if context['message']=='突击':
        try:
            bot.send(context, Sorties())
        except Error:
            pass
  
    if context['message']=='裂缝':
        try:
            bot.send(context, Active())
        except Error:
            pass
    if context['message']=='新番':
        try:
            bot.send(context, Bangi())
        except Error:
            pass
    print(len(contexts))
    if len(contexts)==3:
        if contexts[0] == '翻译' and contexts[1] != '':
            common=[contexts[1],contexts[2]]
            bot.send(context, translate(common))
        if contexts[0] == '物品' and contexts[1] != '':
            common=[contexts[1],contexts[2]]
            bot.send(context, translateitems(common))
        if contexts[0] == '学习' and contexts[1] != '':
            common=[(100,1,0,contexts[1],contexts[2])]
            bot.send(context, study(common))
    if len(contexts)==2:   
        if contexts[0] == 'cd' and contexts[1] != '':
            bot.send(context, searchPrice(contexts[1]))


'''
def onQQMessage(bot, contact, member, content):
    if contact.qq in blackList:
        print('拦截黑名单')
        return False
    if content in ('js','奸商','虚空商人') and content != '':
        timeLeft = int(worldData['VoidTraders'][0]['Activation']['$date']['$numberLong'])/1000 - int(worldData['Time'])
        if timeLeft > 0:
            day = int(timeLeft/86400)
            hour = int(timeLeft/3600 - day*24)
            minitue = int(timeLeft/60 - hour*60 - day*1440)
            bot.send(contact, '智子翻了翻日历ʅ（´◔౪◔）ʃ\n奸商还剩：\n' + str(day) + ' 天 ' + str(hour) + ' 小时 ' + str(minitue) + ' 分钟 就来坑你钱啦！')
        else:
            timeLeft = int(worldData['VoidTraders'][0]['Expiry']['$date']['$numberLong'])/1000 - int(worldData['Time'])
            day = int(timeLeft/86400)
            hour = int(timeLeft/3600 - day*24)
            minitue = int(timeLeft/60 - hour*60 - day*1440)
            bot.send(contact, '奸商还剩：\n' + str(day) + ' 天 ' + str(hour) + ' 小时 ' + str(minitue) + ' 分钟 就要跑啦！\n刺杀奸商 = 3')
    if content in ('平原','希图斯','稀图斯','平原时间') and content != '':
        timeNow = int(time.time() - 1513450500)
        timeNow = timeNow - int(timeNow/9000)*9000
        if timeNow - 6000 < 0 : 
            timeLeft = int(6000 - timeNow)
            hour = int(timeLeft/3600)
            minitue = int(timeLeft/60 - hour * 60)
            sec = int(timeLeft - minitue*60 - hour * 3600)
            output = '小取名偷偷告诉你，白天的平原风景正好，赶紧去捕鱼吧~\n\n还剩 ' + str(hour) + ' 小时 ' + str(minitue) + ' 分钟 ' + str(sec) + ' 秒 Boss就要来吓人了喔'
            bot.send(contact,output)
        elif timeNow - 3000 >= 0 : 
            timeLeft = int(9000 - timeNow)
            hour = int(timeLeft/3600)
            minitue = int(timeLeft/60 - hour*60)
            sec = int(timeLeft - minitue*60 - hour * 3600)
            output = '晚上啦，平原闹鬼啦\n\n还剩 ' + str(hour) + ' 小时 ' + str(minitue) + ' 分钟 ' + str(sec) + ' 秒 Boss就要休息不吓人了哟。'
            bot.send(contact,output)
    if content in ('突击','每日') and content != '':
        bot.send(contact,Sorties())
    if content in ('警报') and content != '':
        bot.send(contact, Alerts())
    if content in ('集团任务') and content != '':
        bot.send(contact, '功能未上线！')
    if content in ('裂隙') and content != '':
        bot.send(contact, '功能未上线！')
    if content in ('入侵') and content != '':
        bot.send(contact, '功能未上线！')
    if content in ('每日折扣','折扣') and content != '':
        bot.send(contact, '功能未上线！')
'''
#开始循环
print('loading directionary...')
#wroldData[0]是中>英
#wroldData[1]是英>中
memberDict = loadmemberDict()
worldDict = loadDict()
worldData = {}
itemDirectionary = loadDataDict()
PriceData = {}
warList = []
lastAlerts = []
thisAlerts = []
timeNow = []
updateJson()



http_server = WSGIServer(('127.0.0.1', 8080),bot.wsgi)
http_server.serve_forever()

#黑名单
blackList = ['643489949']