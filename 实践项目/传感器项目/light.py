#_*_ coding:utf-8 _*_
import requests
import re
import math
import time

def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;
second = sleeptime(0,0,0.1);
for i in range(1000):
    time.sleep(second);
    #print(123)
    url = 'http://192.168.0.102:8080/get?illum'
    #模拟浏览器发送http请求
    response = requests.get(url)    #请求打印成一个包
    response.encoding = 'utf-8'
    html = str(response.text)
    #print(html)
    #print(type(html))
    lux = re.findall(r'illum(.*?)}', html,re.S)
    #findall(r'{"buffer":{"illum":{"size":0,"updateMode":"single", "buffer":[(.*?)]}',html)
    lux = str(lux)
    #print(lux)
    #print(type(lux))
    lux1 = re.findall(r'buffer":(.*?)]',lux,re.S)
    lux1 = str(lux1)
    lux1 = lux1.replace('[','')
    lux1 = lux1.replace(']','')
    lux1 = lux1.replace("'","")
    #print(lux1)
    a= '1.23E5'
    #print(a)
    LUX = float(lux1)
    print(LUX)


    data=open("D:\data.txt",'a') 
    print(LUX,file=data)
    data.close()








