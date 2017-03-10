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
  
     

      
         


    