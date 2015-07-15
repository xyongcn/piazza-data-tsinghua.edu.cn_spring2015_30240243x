import gzip
import re
import http.cookiejar
import urllib.request
import urllib.parse
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
def getOpener(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

header = {
    
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
     'Accept-Encoding': 'gzip, deflate',
     'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
     'Connection':'keep-alive',
      'Host':'piazza.com',
      'Referer:':'https://piazza.com/',
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
     
   
}
 

#postDict是登录时所post的表单
email = 'jennyzhang8800@163.com'
password = 'jeny20110607'
postDict = {
    'from': '/signup',
    'email':email ,
    'password': password ,
    'remember': 'on'
}
postData = urllib.parse.urlencode(postDict).encode()

url = 'https://www.piazza.com/class'
opener = getOpener(header)
op = opener.open(url, postData)
data = op.read()
data = ungzip(data)

print(data.decode())
