#一、简要说明

   三个文件夹内的文件结构相同，分别实现不同的功能，都是对从piazza平台获得的json数据进行解析。解析时用到的是js模板引擎handlebars
   
#二、详细说明（以example_together为例）

   1.example.html
      
      主要定义了三个js模板。
      
      (1) popular_tags_list部分的js模板 ，动态显示标签
      
       	 <script id="popular-tags-bar-template" type="text/x-handlebars-template">……</script>
      
      (2) page_center部分的js模板，显示某一个id对应的讨论记录
      
       	 <script id="page-center-template" type="text/x-handlebars-template">……</script>
       	
      (3)feed部分的js模板, 显示某一个讨论记录的索引列表
      
         <script id="feed-template" type="text/x-handlebars-template">……</script>
         
   2.dashboard_all.css
    
       是css文件，对piazza的dashboard_1116.css文件作了一些修改。
      
   3.piazza_together.js
    
      注册Helper以及以json数据传送给在example.html中定义的模板。定义了一些函数。
      具体的函数以及功能见程序中的注释
      
   4.handlebars_v3.0.3.js以及jquery_1.11.3.min.js是handlebars模板引擎所需的脚本。
    
#三、相关链接
  
  有关handlebars的使用
     
       官网： http://handlebarsjs.com/
       
       有用的博客：http://www.cnblogs.com/iyangyuan/archive/2013/12/12/3471227.html
                   http://blog.csdn.net/jyy_12/article/details/7937712
                   http://www.thinksaas.cn/group/topic/345756/
                   https://software.intel.com/zh-cn/articles/HTML5Handlebars
