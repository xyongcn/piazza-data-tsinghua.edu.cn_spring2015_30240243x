# -*- coding: utf-8 -*- 
import xlrd
import json
import codecs
#读excel
def open_excel(fname):
    try:
        data = xlrd.open_workbook(fname)
        return data
    except Exception,e:
        print str(e)
        
#保存数据到文件中  
def saveFile(file_name,data):
    output = codecs.open(file_name+".json",'w',"utf-8")
    output.write(data)
    output.close()   
    print("already write to "+file_name+".json")
#以学生为单位统计
def statisticByStudent():
    #打开excel
    data=open_excel("F:\\test.xlsx")
    #表单"grade"
    table = data.sheet_by_name(u'grade')
    #获得表单行数
    nrows = table.nrows
    #定义json对象存放统计结果
    result={}
    #"result"字面量是对象数组，数组的每一个元素是一个学生的信息（包括该学生所有课程的成绩信息）
    result["result"]=[]
    #遍历该表单所有行，进行统计，从第二行开始
    for rownum in range(table.nrows):
        if rownum>0:
            stuObj=table.row_values(rownum)
            #学号
            sNo=int(stuObj[0])
            #姓名
            sName=stuObj[1]
            #学生信息
            stuInfo={}
            #课程号
            stuInfo["cNo"]=stuObj[2]
            #课程名
            stuInfo["cName"]=stuObj[3]
            #成绩
            stuInfo["grade"]=stuObj[4]
            #学分
            stuInfo["credit"]=int(stuObj[6])
            #课程属性
            stuInfo["cAttribute"]=stuObj[7]
            #第一个学生，直接写入
            if rownum==1:
                sNew={}
                sNew["sNo"]=sNo
                sNew["sName"]=sName
                sNew["info"]=[]
                sNew["info"].append(stuInfo)
                result["result"].append(sNew)
            else:
                flag=0
                #如果该学生己经有统计过的记录，则直接加入新的课程信息
                for item in result["result"]:
                    if sNo==item["sNo"]:
                        item["info"].append(stuInfo)
                        break
                    else:
                        flag=1
                #flag=1该学生没有统计过，新建一个对象
                if flag==1:
                    sNew={}
                    sNew["sNo"]=sNo
                    sNew["sName"]=sName
                    sNew["info"]=[]
                    sNew["info"].append(stuInfo)
                    result["result"].append(sNew)
    #学生总人数
    result["numberOfStudent"]=len(result["result"])
    #dict 转为 str
    result_json=json.dumps(result)
    #处理中文
    jsonStr=json.loads(result_json)
    jsonStr=json.dumps(jsonStr,ensure_ascii=False)
    #保存结果，写入文件
    saveFile("statisticByStudent",jsonStr)
          
if __name__=="__main__":
    statisticByStudent()
