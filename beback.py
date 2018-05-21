# Usage: $ python3 test.py
# To end BeBack: Modify `stat.txt` to `end`

#coding:utf-8

import itchat
import requests,bs4,urllib,os  
from selenium import webdriver  
import time   
import datetime

# Input the nickname of your main account
my_name = 'Place_Holder'

# Input the nickname of target account
target_name = 'Place_Holder'

itchat.auto_login(enableCmdQR=True)
# itchat.auto_login()

friendList = itchat.get_friends(update=True)[1:]

# print(friendList)  
msg = "BeBack starts"

for friend in friendList:
    if friend['NickName'] == my_name:
        itchat.send(msg, friend['UserName'])

time.sleep(20)

while 1:
    # print(time.strftime('%H',time.localtime(time.time())))
    # print(time.strftime('%M',time.localtime(time.time())))
    # if (time.strftime('%H',time.localtime(time.time())) == '22' and time.strftime('%M',time.localtime(time.time())) == '00'):

    stat = open('stat.txt')
    line = stat.readline()
    if (line == 'end'):
        break
    stat.close()

    dater = open('dater.txt','w') 
    dater.write(time.strftime('%H:%M',time.localtime(time.time())))
    dater.close()

    if (time.strftime('%M',time.localtime(time.time())) == '00'):

        d1 = datetime.datetime.now()
        d2 = datetime.datetime(2018, 9, 10)
        # print(d1)
        # print(d2)
        d3 = (d2-d1).days

        resWeather = urllib.request.urlopen('http://www.weather.com.cn/weather/101180101.shtml')  
        resWeatherHtml = str(resWeather.read(),'utf-8')
        
        bs4Weather = bs4.BeautifulSoup(resWeatherHtml, "html.parser")
        city1 = bs4Weather.select('input[id="hidden_title"]')  
        
        resWeather = urllib.request.urlopen('http://www.weather.com.cn/weather/401040102.shtml')  
        resWeatherHtml = str(resWeather.read(),'utf-8')
        
        bs4Weather = bs4.BeautifulSoup(resWeatherHtml, "html.parser")
        city2 = bs4Weather.select('input[id="hidden_title"]')  

        mail = "早上好~\n距离回国还有" + str(d3) + "天。\n\n"+\
            "今天中国上海的天气：\n"+city1[0].get('value')+"\n今天美国圣地亚哥的天气：\n"+city2[0].get('value')+'\n'\
            +"每天都要有好心情~\n\nFrom python script by Shengan"

        # NName is the nickname in Chinese
        for friend in friendList:
            if (time.strftime('%H',time.localtime(time.time())) == '6'):
                if friend['NickName'] == my_name:
                    # print(friend['UserName'])
                    itchat.send(mail, friend['UserName'])
            if (time.strftime('%H',time.localtime(time.time())) == '15'):
                if friend['NickName'] == target_name:
                    itchat.send(mail, friend['UserName'])
    time.sleep(60)

msg = "BeBack ends"

for friend in friendList:
    if friend['NickName'] == my_name:
        itchat.send(msg, friend['UserName'])