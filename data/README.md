“data”文件夹中存放的是从piazza平台获取的数据。

一、“piazza-data”

      (1)存放的是从piazza平台获取的所有数据，按每一个讨论记录的id排序。
      (2)通过“accessToPiazzaData.py”获得这些数据
      (3)这些数据用于<div id ="page_center" >部分的数据显示。
         其中<div id ="page_center" >位于staticfles文件夹中example-XXX中的example.html中
     
二、“piazza-data-filter”

      (1)存放的是从piazza平台获取的按标签筛选后的返回数据。
      (2)通过“filter_feed.py”获得这些数据
      (3)这些数据用于<div id ="feed" class="page_feed">部分的数据显示。
         其中<div id ="page_center" >位于staticfles文件夹中example-XXX中的example.html中

三、“LoginCheck”

      (1)存放的是用于检测是否登录piazza成功的返回数据。
      (2)如果登录成功则返回的数据与“piazza-login-success.txt”中的内容相似
      (3)如果登录不成功则返回的数据与“piazza-login-fail.txt”中的内容相似      
