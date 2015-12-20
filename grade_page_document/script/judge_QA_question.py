__author__ = 'zhangyanni'

# -*- coding:utf-8 -*-
import codecs
import json
import os
import time


ISOTIMEFORMAT='%Y-%m-%d %X'


def get_q_list():
    q_list=[]
    doneList=[]
    answer_list_dir=r"/var/www/zyni/answer"

    for parent,dirnames,filenames in os.walk(answer_list_dir):
        for filename in filenames:
            (shortname,extension) = os.path.splitext(filename)
            if shortname.isdigit():
                if int(shortname) not in q_list:
                   q_list.append(int(shortname))
            if(shortname[0]=='_'):
                 (pdir,email)=os.path.split(parent)                                                                              
                 tmp=os.path.join(email,shortname[1:])
                 if(tmp not in doneList):
                     doneList.append(tmp) 
    return (q_list,doneList)

def judge_QA_question(q_list,doneList):
   

    for q_number in q_list:

        all_items=readFile(r"/var/www/zyni/grade_xblock_data/all_items.json")
        all_items_dict=eval(all_items)

        if all_items_dict[str(q_number )][0]==4:
            result={}

            right_answer=all_items_dict[str(q_number )][1]

            file_dir=os.path.join(r"/var/www/zyni/grade_xblock_data/md2json",str(q_number/100 + 1))
            file_path=os.path.join(file_dir,str(q_number)+".json")
            q_file=readFile(file_path)
            q_file_dict=eval(q_file)

            question=q_file_dict["question"]
            result["q_number"]=q_number
            result["question"]=question
            result["right_answer"]=right_answer

            statistic_time=time.strftime(ISOTIMEFORMAT,time.localtime())
            result ["statistic_time"]=statistic_time

            result["answer_list"]=[]

            answer_list_dir="/var/www/zyni/answer"
            for parent,dirnames,filenames in os.walk(answer_list_dir):
                for filename in filenames:

                    (shortname,extension)=os.path.splitext(filename)
                     
                    if (shortname==str(q_number)):

                        jsonUnicode=readFile(os.path.join(parent,filename))

                        list=jsonUnicode.split('\n')
                        jsonUnicode=list[-1]
                        data_file_dict=eval(jsonUnicode)
                        jsonStr=json.dumps(data_file_dict)
                        jsonStr=json.loads(jsonStr)
                        jsonStr=json.dumps(jsonStr,ensure_ascii=False)
                        data_file_dict=eval(jsonStr)
                        moveIt=0
                        for checkDone in doneList:
                            (email,Number)=os.path.split(checkDone)
                            if (email==data_file_dict["email"] and Number==str(q_number)):
                                moveIt=1
                                break
                        if(moveIt==0):
                            temp={}
                            temp["answer"]=data_file_dict["answer"]
                            temp["user_name"]=data_file_dict["username"]
                            temp["email"]=data_file_dict ["email"]
                            temp["summit_time"]=data_file_dict ["time"]
                            result["answer_list"].append(temp)
            if result["answer_list"]:           
                result_jsonObj=json.dumps(result)
                data=json.loads(result_jsonObj)
                json_data=json.dumps(data,ensure_ascii=False)
                saveFile(r"/var/www/zyni/grade_xblock_data/judge_QA_question/",str(q_number),json_data)
            else:
                fileRM='/var/www/zyni/grade_xblock_data/judge_QA_question/'+str(q_number)+'.json'
                os.system('rm '+fileRM)

def readFile(file_path):
    fileObj=codecs.open(file_path, encoding='utf-8')
    data=fileObj.read()
    return data

def saveFile(file_path,file_name,data):
    output = codecs.open(file_path+file_name+".json",'w',"utf-8")
    output.write(data)
    output.close()

if __name__ == '__main__':
    (q_list,doneList)=get_q_list()
    judge_QA_question(q_list,doneList)


