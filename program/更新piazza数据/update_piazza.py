# -*- coding:utf-8 -*-
# !/usr/bin/python
__author__ = 'zhangyanni'


import urllib2
import cookielib
import urllib
import StringIO
import gzip
import json
import codecs
import socket
import os
import time
#获得今天的时间
cur_time=time.strftime(r"%Y-%m-%d,%H:%M:%S",time.localtime())
#创建日志文件
filewt = open("/mnt/piazza_update/piazza_log.log",'a')
filewt.write("-----------------------a new log-----------------------------\n")
filewt.write(cur_time+"\n")
print(cur_time)
#ungzip解压数据
def ungzip(data):
    try:
        compressedstream = StringIO.StringIO(data)
        gziper = gzip.GzipFile(fileobj=compressedstream)
        data2=gziper.read()
    except:
        filewt.write("未经压缩, 无需解压\n")
    return data2


#getOpener 函数接收一个 head 参数, 这个参数是一个字典. 函数把字典转换成元组集合, 放进 opener.
#自动处理使用 opener 过程中遇到的 Cookies
#自动在发出的 GET 或者 POST 请求中加上自定义的 Header
cookieJar = cookielib.CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
urllib2.install_opener(urlOpener)
def piazza_login():
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection':'keep-alive',
        'Host':'piazza.com',
        'Referer':'https://piazza.com/class/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
        'X-Requested-With':'XMLHttpRequest'
        }
    #postDict是登录时所post的表单
   
    email = "jennyzhang8800@163.com"
   
    password = "jeny20110607"
    filewt.write("登录中...\n")
    postDict = {'from': '/signup','email':email ,'password': password , 'remember': 'on'}
    postData = urllib.urlencode(postDict)   
    url = 'https://piazza.com/class/'   
    loginNum=1
    while 1:
        #生成页面请求的完整数据
        req = urllib2.Request(url,postData,header)
        #利用opener发送页面请求
        response=urlOpener.open(req)
        #获取服务器返回的页面信息
        data=response.read()                       
        data = ungzip(data)
        #登录到piazza，并get登录后的网页保存在piazza_logindata.txt
        data=data.decode(encoding='UTF-8',errors='ignore')
        saveFile("piazza-login-data",data)
        FileSize=os.path.getsize("/mnt/piazza_update/piazza-data-tsinghua.edu.cn_spring2015_30240243x/data/piazza-data/piazza-login-data.json")


        if (FileSize > 150000):
            filewt.write("登录成功！\n")
            break
        else:
            if loginNum==3:
                filewt.write("三次登录失败，请检查用户名，密码是否正确！\n")
                break
            loginNum+=1
            filewt.write("本次登录未成功，正在尝试第"+str(loginNum)+"次登录...\n")
                    
    

#从piazza的api中获得json数据，根据发送的postJson不同获得不同的数据，可获得某一个标签的所有问题，或指是cid的某一个问题    
def piazza_getdata_from_api(postJson):
    header_new={
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/json; charset=utf-8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Host':'piazza.com',
        'Referer':'https://piazza.com/class',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0',
        'X-Requested-With':'XMLHttpRequest'
        }
    #对postJson进行Json格式化编码 
    postData=json.dumps(postJson)    
    url="https://piazza.com/logic/api/"
    tryNum=1
    while 1:
        socket.setdefaulttimeout(20)
        try:
            req = urllib2.Request(url,postData,header_new)
            response=urlOpener.open(req)
            data=response.read()
            data = ungzip(data)
            data=data.decode()
            #处理data的中文
            myjson=json.loads(data)
            newjson=json.dumps(myjson,ensure_ascii=False)
            return newjson
                       
        except:
            if(tryNum==3):
                return '''{"result":"history":{"subject":"","content":"sorry!there is no content"}}'''
            else:
                tryNum+=1
                filewt.write("timeout!"+"try to get:"+str(tryNum)+"again\n")
                           

#保存数据到文件中  
def saveFile(file_name,data):
    output = codecs.open("/mnt/piazza_update/piazza-data-tsinghua.edu.cn_spring2015_30240243x/data/piazza-data/"+file_name+".json",'w',"utf-8")
    output.write(data)
    output.close()   
    filewt.write("already write to "+file_name+".json\n")
#读文件

def saveFilter(file_name,data):
    output = codecs.open("/mnt/piazza_update/piazza-data-tsinghua.edu.cn_spring2015_30240243x/data/piazza-data-filter/"+file_name+".json",'w',"utf-8")
    output.write(data)
    output.close()                                                                                                    
    filewt.write("already write to "+file_name+".json\n")
def readFile(file_name):
    fileIn = codecs.open(file_name,'r',"utf-8")
    data=fileIn.read()
    fileIn.close()
    return data

def push_to_git():
    filewt.write("push to git ...\n")
    status=os.system('/mnt/piazza_update/pushToGithub.sh')
    if status == 0:
        filewt.write("push successfully\n")
    else:
        filewt.write("push failed!\n")




filewt.write("------login piazza----\n")
piazza_login()
filewt.write("------开始更新数据-----\n")
filewt.write("正在获取查询列表，请稍等...\n")
postJson={"method":"network.get_my_feed","params":{"nid":"i5j09fnsl7k5x0","sort":"updated"}}
data=piazza_getdata_from_api(postJson)
saveFile("piazza_my_feed",data)
saveFilter("piazza_my_feed",data)
filewt.write("正在检查更新，请稍等...\n")

data=readFile("/mnt/piazza_update/piazza-data-tsinghua.edu.cn_spring2015_30240243x/data/piazza-data/piazza_my_feed.json")
#把 json字符串转成字典，便于解析数据
data_dict=json.loads(data)
dict = {}
#获得"result"下的"feed"列表
items=data_dict['result']['feed']
#遍历items当遍历到有今天更新的问题时，则加入列表中，获取更新后的信息
for item in items:
    id = item['id']
    nr = item['nr']
    modified=item['modified']
    #今天有更新，则加入请求列表
    if modified[0:10]==cur_time[0:10]:
        dict[nr]=id

#根据nr向api发出POST请求获得有今天更新的问题的json数据
if len(dict.keys())!=0:
    print("these are update list:")
    print(dict.keys())
    filewt.write("检查到:"+str(len(dict.keys()))+"个更新\n")
    for nr in dict.keys():
        filewt.write(str(nr))
        postJson={"method":"content.get","params":{"cid":nr,"nid":"i5j09fnsl7k5x0"}}
        data=piazza_getdata_from_api(postJson)
        file_name=str(nr)
        saveFile(file_name,data)

        
if len(dict.keys())==0:
    print("there is no update")
    filewt.write("today no update!\n")


items=data_dict['result']['tags']['instructor']
print("tags list:")
print items
for filter_folder in items:
    filter_folder=filter_folder.encode("utf8")
    print filter_folder
    postJson={"method":"network.filter_feed","params":{"nid":"i5j09fnsl7k5x0","sort":"updated","filter_folder":filter_folder,"folder":1}}
    data=piazza_getdata_from_api(postJson)                                                                            
    saveFilter("filter_feed_"+filter_folder,data)

push_to_git()
filewt.close()
