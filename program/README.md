#从piazza获取数据的程序

一、登录piazza

    "LoginPiazza.py"是登录到piazza的脚本。
     运行该脚本
     按提示输入您在Piazza注册的用户名及密码
     如果登录成功，会得到与piazza-login-data.txt相似的返回数据。
     如果登录不成功，会得到与piazza-login-fail.txt相同的返回数据。

     注意：此脚本是获取piazza数据的基础，如果登录不成功，请重试几次，或者改变header后重试。

二、从piazza获取数据
 
    "accessToPiazza.py"是从piazza平台获取数据的脚本。
     运行该脚本
     （1）按提示输入您在Piazza注册的用户名及密码登录到piazza
      (2) 按提示输入nid 即课程id。cid可以通过浏览器登录piazza时的url地址栏看到。由于一个用户在piazza平台上可能加入了多个课程，因此这里需要指定要获取数据的课程id.
      (3) 按提示选择要获取指定id的讨论记录（输入2）还是所有的讨论记录数据（输入1）。
          如果获取指定id的讨论记录，可能重复多次获取，输入exit停止。

      运行结果：获得所有讨论记录数据如data/piazza-data所示

三、按标签筛选数据

    "filter-feed.py"是从piazza平台获取按标签筛选后的返回数据的脚本。

     运行该脚本
     （1）按提示输入您在Piazza注册的用户名及密码登录到piazza
      (2) 按提示输入nid 即课程id。cid可以通过浏览器登录piazza时的url地址栏看到。由于一个用户在piazza平台上可能加入了多个课程，因此这里需要指定要获取数据的课程id.
      (3) 按提示指定筛选条件，即输入标签名。

      运行的结果如data/piazza-data-filter所示
      
#对数据进行解析的程序
  
  “对数据解析／static”中包含的是一个简单的解析版本，完善后的版本位于“staticfiles”文件夹中。
  
  https://github.com/xyongcn/piazza-data-tsinghua.edu.cn_spring2015_30240243x/tree/master/staticfiles
  
#自动从piazza获取有更新的数据，并同步到github仓库。

1. update_piazza.py  实现以下三方面功能：

         （1）.登录piazza平台
         （2）.从piazza获取返回数据（对数据解析可获得所有记录的更新时间），
         （3）.检测这一天内是否有更新，并获取更新
         （4）.更新后的数据同步到github仓库,
         （5）.同时生成日志piazza_log.log
    

     update_piazza.py该文件用于IBM的EDX机器上。路径为为：/mnt/piazza_update/update_piazza.py
     
     生成的日志位于：/mnt/piazza_update/piazza_log.log


2. 定时执行脚本（update_piazza.py）的实现：
    
    具体的方法为：
    
    （1）利用crontab创建定时任务：
    
         crontab -e
    
    （2）输入下面的命令：
    
         30 23 * * * /usr/bin/python /mnt/piazza_update/update_piazza.py >/mnt/piazza_update/piazza_log_today.log 2>&1
     
    每天的23:30，执行脚本 update_piazza.py。把本次执行该脚本输出的结果记录在piazza_log_today.log
    所有的日志记录在piazza_log.log。
     
    注意：

         piazza_log_today.log：只是本次的日志，仅记录更新时间，以及有无实际更新

         piazza_log.log：记录了所有的日志详细信息。

附：以下两个脚本是为手动更新时使用而准备。平时用不到。
    运行脚本前请先修改存放文件的路径。
     
    upd-data-during-time.py
    如果只想手动更新一个时间段内的piazza数据，则可以运行此脚本。如：更新2015年11月5日至2015年12月8日期间的所有更新，则运行upd-data-during-time.py 根据提示输入：2015-11-05  2015-12-08 即可。注：运行前请根据你的数据存放位置更改脚本中相应的路径。
    upd-filter.py
    只更新标签
    
    
