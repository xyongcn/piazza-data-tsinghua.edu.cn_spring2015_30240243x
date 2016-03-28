__author__ = 'zhangyanni'
# -*- coding:utf-8 -*-
import codecs
import json
import os
import os.path
import math

def readFile(file_name):
    fileObj=codecs.open(file_name, encoding='utf-8')
    try:
        data=fileObj.read()
        return data

    except:
        print "cannot read!"
    finally:
        fileObj.close()


def saveFile(file_name,data):
    output = codecs.open(file_name+".json",'w',"utf-8")
    output.write(data)
    output.close()

def get_student_info_lab1():
    student_info_lab1={}
    student_info_lab1["result"]=[]
    answer_list_dir=r"C:\Users\zhangyanni\Desktop\answer-master-004957cb911c1481f53eab3c3a626e5d361b6b5d"

    for parent,dirnames,filenames in os.walk(answer_list_dir):
        for filename in filenames:
            (shortname,extension) = os.path.splitext(filename)
            if shortname.isdigit():
                if(int(shortname)==1489):

                    parentdir=parent.rsplit('\\',1)[0]
                    student_info={}
                    for dir in os.listdir(parentdir):
                        if(int(dir)==1489):

                            fileName= os.path.join(parentdir,r'1489\1489.json')
                            data=readFile(fileName)
                            dataDict=json.loads(data)
                            student_name= dataDict["answer"][0]["answer"]
                            student_info["student_name"]=student_name

                        if(int(dir)==1490):

                            fileName= os.path.join(parentdir,r'1490\1490.json')
                            data=readFile(fileName)
                            dataDict=json.loads(data)
                            student_id_or_email= dataDict["answer"][0]["answer"]
                            student_info["student_id_or_email"]=student_id_or_email

                        if(int(dir)==1491):

                            fileName= os.path.join(parentdir,r'1491\1491.json')
                            data=readFile(fileName)
                            dataDict=json.loads(data)
                            student_ucore_gitlab_url= dataDict["answer"][0]["answer"]

                            student_info["student_ucore_gitlab_url"]=student_ucore_gitlab_url
                    student_info_lab1["result"].append(student_info)


    student_info_lab1["sum"]=len(student_info_lab1["result"])
    student_info_lab1["lab_number"]="lab1"

    data=json.dumps(student_info_lab1)
    saveFile('student_info_lab1',data)

if __name__ == '__main__':

    get_student_info_lab1()











