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

#以课程为单位统计

def statisticByCourse():
    #打开excel
    data=open_excel("F:\\test.xlsx")
    #表单"grade"
    table = data.sheet_by_name(u'grade')
    #获得表单行数
    nrows = table.nrows
    #定义json对象存放统计结果
    result={}
    
#"result"字面量是对象数组，数组的每一个元素是一个课程的信息（包括该课程所有学生的成绩信息）
    result["result"]=[]
    #遍历该表单所有行，进行统计，从第二行开始
    for rownum in range(table.nrows):
        if rownum>0:
            stuObj=table.row_values(rownum)
            
#课程号
            cNo=stuObj[2]
            #课程名
            cName=stuObj[3]
            #课程属性
            cAttribute=stuObj[7]
            #学分
            credit=int(stuObj[6])
            #学生信息
            stuInfo={}
            #学号
            stuInfo["sNo"]=stuObj[0]
            #课程名
            stuInfo["sName"]=stuObj[1]
            #成绩
            stuInfo["grade"]=stuObj[4]
            #第一个学生，直接写入
            if rownum==1:
                cNew={}
                cNew["cNo"]=cNo
                cNew["cName"]=cName
                cNew["credit"]=credit
                cNew["cAttribute"]=cAttribute
                cNew["info"]=[]
                cNew["info"].append(stuInfo)
                result["result"].append(cNew)
            else:
                flag=0
                #如果该课程己经有统计过的记录，则将学生信息直接加入已有课程中
                for item in result["result"]:
                    if cNo==item["cNo"]:
                        flag=0
                        item["info"].append(stuInfo)
                        break
                    else:
                        flag=1
                #flag=1该课程没有统计过，新建一个对象
                if flag==1:
                    cNew={}
                    cNew["cNo"]=cNo
                    cNew["cName"]=cName
                    cNew["credit"]=credit
                    cNew["cAttribute"]=cAttribute
                    cNew["info"]=[]
                    cNew["info"].append(stuInfo)
                    result["result"].append(cNew)
    #课程总数
    result["numberOfCourse"]=len(result["result"])
    

    
#dict 转为 str
    result_json=json.dumps(result)
    
#处理中文
    jsonStr=json.loads(result_json)
    jsonStr=json.dumps(jsonStr,ensure_ascii=False)
    #保存结果，写入文件
    saveFile("statisticByCourse",jsonStr)
    
if __name__=="__main__":
    
    statisticByCourse()
