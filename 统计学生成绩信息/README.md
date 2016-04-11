#以学生为单位统计

  1. statisticByStudent.py
  
     该脚本完成以学生为单个的统计功能。运行脚本时把excel表格所在路径换成实际路径即可。
     
  2. statisticByStudent.json
  
     这是statisticByStudent.py脚本的运行结果。其格式如下：
     
     {"numberOfStudent": 学生个数, "result":[每个学生为一个对象]]}
     
     其中"result"数组中每个对象的格式为：
     
        {"sName":姓名，
          "sNo":学号，
           "info":[{"cNo":课程号，"cName":课程名,"grade":成绩,"credit":学分,"cAttribute":课程属性}……]
         }
     
#以课程为单位统计

   1. statisticByCourse.py
  
     该脚本完成以学生为单个的统计功能。运行脚本时把excel表格所在路径换成实际路径即可。
     
  2. statisticByCourse.json
  
     这是statisticByCourse.py脚本的运行结果。其格式如下：
     
     {"numberOfCourse": 课程个数, "result":[每门课程为一个对象]]}
     
     其中"result"数组中每个对象的格式为：
     每门课程为一个对象
     {"cNo":课程号，"cName":课程名,"credit":学分,"cAttribute":课程属性，
       "info":[{"sName":姓名，"sNo":学号，"grade":成绩}]
     }
