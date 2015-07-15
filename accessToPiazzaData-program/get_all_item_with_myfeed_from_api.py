__author__ = 'zhangyanni'

#coding=utf-8
import gzip
import http.cookiejar
import urllib.request
import urllib.parse
import json
import codecs



#ungzip解压数据
def ungzip(data):
    try:        # 尝试解压
        print('正在解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data


#getOpener 函数接收一个 head 参数, 这个参数是一个字典. 函数把字典转换成元组集合, 放进 opener.
#自动处理使用 opener 过程中遇到的 Cookies
#自动在发出的 GET 或者 POST 请求中加上自定义的 Header
cj = http.cookiejar.CookieJar()
pro = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(pro)
urllib .request .install_opener(opener)

def piazza_login():
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection':'keep-alive',
        'Host':'piazza.com',
        'Referer:':'https://piazza.com/class/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0',
        'X-Requested-With':'XMLHttpRequest'
        }
    #postDict是登录时所post的表单
    email = 'jennyzhang8800@163.com'
    password = 'jeny20110607'
    postDict = {'from': '/signup','email':email ,'password': password , 'remember': 'on'}
    postData = urllib.parse.urlencode(postDict).encode()


    #登录到piazza，并get登录后的网页保存在piazza_data.txt
    url = 'https://piazza.com/class/'

    req = urllib.request.Request (url,postData,header)
    response=urllib .request .urlopen(req)
    data=response.read()
    data = ungzip(data)
    output = open('piazza_login-6-5.txt','w')
    output.write(data.decode())
    output.close()
    print("login suceesful!")
    print('''already write to "piazza_login.txt".''')

#从piazza的api中获得json数据，根据发送的postJson不同获得不同的数据，可获得某一个标签的所有问题，或指是cid的某一个问题    
def piazza_getdata_from_api(postJson):
    
    header_new={
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/json; charset=utf-8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Host':'piazza.com',
        'Referer:':'https://piazza.com/class',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0',
        'X-Requested-With':'XMLHttpRequest'
        }
    
    postData=json.dumps(postJson).encode()
    url="https://piazza.com/logic/api/"
    req = urllib.request.Request(url,postData,header_new)
    response=urllib .request .urlopen(req)
    data=response.read()
    data = ungzip(data)
    data=data.decode() 
    #处理data的中文
    myjson=json.loads(data)
    newjson=json.dumps(myjson,ensure_ascii=False)
    return newjson

#保存数据到文件中  
def saveFile(file_name,data):
    output = codecs.open("result/"+file_name+".json",'w',"utf-8")
    output.write(data)
    output.close()   
    print("already write to "+file_name+".json")
#读文件
def readFile(file_name):
    fileIn = codecs.open(file_name,'r',"utf-8")
    data=fileIn.read()
    fileIn.close()
    return data

#调用函数登录到piazza
piazza_login()
#获得所有问题列表,get_my_feed_form_api
postJson={"method":"network.get_my_feed","params":{"nid":"i5j09fnsl7k5x0","offest":170,"sort":"updated"}}
data=piazza_getdata_from_api(postJson)
saveFile("piazza_my_feed",data)

data=readFile("piazza_my_feed.txt")
#把 json字符串转成字典，便于解析数据
data_dict=json.loads(data)

dict = {}
#获得"result"下的"feed"列表
items=data_dict['result']['feed']
#遍历items获得所有问题的id和nr
for item in items:
    id = item['id']
    nr = item['nr']
    dict[nr]=id
#根据nr向api发出POST请求获得所有问题的json数据
for nr in dict.keys():
    postJson={"method":"content.get","params":{"cid":nr,"nid":"i5j09fnsl7k5x0"}}
    data=piazza_getdata_from_api(postJson)
    file_name=str(nr)
    saveFile(file_name,data)



