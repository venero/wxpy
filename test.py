# Run with: $ python3 test.py

#coding:utf-8

import itchat
import requests,bs4,urllib,os  
from selenium import webdriver  

resWeather = urllib.request.urlopen('http://www.weather.com.cn/weather/101180101.shtml')  
resWeatherHtml = str(resWeather.read(),'utf-8')
  
bs4Weather = bs4.BeautifulSoup(resWeatherHtml, "html.parser")
city1 = bs4Weather.select('input[id="hidden_title"]')  
  
resWeather = urllib.request.urlopen('http://www.weather.com.cn/weather/401040102.shtml')  
resWeatherHtml = str(resWeather.read(),'utf-8')
  
bs4Weather = bs4.BeautifulSoup(resWeatherHtml, "html.parser")
city2 = bs4Weather.select('input[id="hidden_title"]')  

mail = "今天中国上海的天气是：\n"+city1[0].get('value')+"\n今天美国圣地亚哥的天气是：\n"+city2[0].get('value')+'\n'\
    +"今天有个好心情!\nFrom python script by Shengan"
# print(mail)  

itchat.auto_login(enableCmdQR=True)

friendList = itchat.get_friends(update=True)[1:]

print(friendList)  

# NName is the nickname in Chinese
for friend in friendList:
    if friend['NickName'] == 'NName':
        print(1)
        print(friend['UserName'])
        itchat.send(mail, friend['UserName'])
