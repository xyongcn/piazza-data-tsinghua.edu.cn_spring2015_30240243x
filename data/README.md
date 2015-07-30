“data”文件夹中存放的是从piazza平台获取的数据。

一、“piazza-data”

      存放的是从piazza平台获取的所有数据，按每一个讨论记录的id排序。
      通过“accessToPiazzaData.py”获得这些数据
      用于<div id ="page_center" >部分的数据显示。
     
二、“piazza-data-filter”

      存放的是从piazza平台获取的按标签筛选后的返回数据。
      通过“filter_feed.py”获得这些数据
      用于<div id ="feed" class="page_feed">部分的数据显示。

三、“LoginCheck”

      存放的是用于检测是否登录piazza成功的返回数据。
      如果登录成功则返回的数据与“piazza-login-success.txt”中的内容相似
      如果登录不成功则返回的数据与“piazza-login-fail.txt”中的内容相似      