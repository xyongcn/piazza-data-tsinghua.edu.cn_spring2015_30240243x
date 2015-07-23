__author__ = 'zhangyanni'

#coding='utf-8'
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
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
        'X-Requested-With':'XMLHttpRequest'
        }
    #postDict是登录时所post的表单
   
    email = input('请输入piazza用户名：')
   
    password = input('请输入密码：')
    print('登录中...')
    postDict = {'from': '/signup','email':email ,'password': password , 'remember': 'on'}
    postData = urllib.parse.urlencode(postDict).encode()


   
    url = 'https://piazza.com/class/'

    req = urllib.request.Request (url,postData,header)
    response=urllib .request .urlopen(req)
    data=response.read()
    data = ungzip(data)
    #登录到piazza，并get登录后的网页保存在piazza_logindata.txt
    data=data.decode(encoding='UTF-8',errors='ignore')
    saveFile("piazza-login-data",data)
    print("登录成功！")
    



#保存数据到文件中  
def saveFile(file_name,data):
    output = codecs.open(file_name+".txt",'w',"utf-8")
    output.write(data)
    output.close()   
    print("already write to "+file_name+".txt")


#调用函数登录到piazza
piazza_login()
    



