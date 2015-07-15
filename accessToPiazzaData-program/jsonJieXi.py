__author__ = 'zhangyanni'
#! /usr/bin/env python3
#coding=utf-8
#从文件中读数据
import json
import codecs
def readFile(file_name):
    fileIn = codecs.open(file_name,'r',"utf-8")
    data=fileIn.read()
    fileIn.close()
    return data

def saveFile(file_name,data):
    output = codecs.open(file_name+".html",'w',"utf-8")
    output.write(data)
    output.close()   
    print("already write to "+file_name+".html")
    
#获得tags
def getTags():
    tags=data_dict['result']['tags']
    html='''<div class="tags">tags:'''
    for list in tags:
        html+=list        
        html+=","
    html+="</div>"+"</br>"
    return html

#把"result"下，键值为"history"的数据有用的内容解析为html,放在类名为history的div中<div class="history">
def getHistory():
    history=data_dict['result']['history'][0]
    html='''<div class="history">'''
    subject=history['subject']
    content=history['content']
    created=history['created']
    html+="<div>"+"<h2>"+subject+"</h2>"+created+"</div>"+"<div>"+content+"</div>"
    html+="</div>"
    return html

#处理children,有用的内容解析为html,放在类名为history的div中<div class="children">
def getChildren():
    children=data_dict['result']['children']
    html='''<div class="children">'''
  
    for d in children:
        if d['type']=='i_answer':
            subject=d['history'][0]['subject']
            content=d['history'][0]['content']
            created=d['history'][0]['created']
            html+="<div>"+"----instructors' answers:------"+"</br>"+created+"</br>"+subject+"</div>"+"<div>"+content+"</div>"
        elif d['type']=='s_answer':
            subject=d['history'][0]['subject']
            content=d['history'][0]['content']
            created=d['history'][0]['created']
            html+="<div>"+"------students' answers:-----"+"</br>"+created+"</br>"+createdsubject+"</div>"+"<div>"+content+"</div>"
        elif d['type']=='followup':
            subject=d['subject']
            created=d['created']
            html+="<div>"+"------followup:------"+"</br>"+created+"</br>"+subject
            if d['children'] is not None:
                for feedback in d['children']:
                    subject=feedback['subject']
                    created=feedback['created']
                    html+="<div>"+"------feedback:------"+"</br>"+created+"</br>"+subject+"</div>"
            html+="</div>"
    html+="</div>"
    return html 

data=readFile("piazza_331.txt")
#把 json字符串转成字典，便于解析数据
data_dict=json.loads(data)

#获得"result"下的"tags","id","nr","type"添加到<div class="result">的属性中
cid_post=data_dict['result']['id']
cid_url=str(data_dict['result']['nr'])
Type=data_dict['result']['type']
html='''<div class="result"'''+" cid_post="+cid_post+" cid_url="+cid_url+" Type="+Type+">"          
html+=getTags()
html+=getHistory()
html+=getChildren()
html+="</div>"
saveFile("piazza_331_jiexi",html)


