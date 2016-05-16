# piazza-data-tsinghua.edu.cn_spring2015_30240243x
Piazza discussion data for https://piazza.com/tsinghua.edu.cn/spring2015/30240243x/home

   一、data中包含的是piazza获得的数据。
   
:sparkles: 详细说明见：
 https://github.com/xyongcn/piazza-data-tsinghua.edu.cn_spring2015_30240243x/blob/master/data/
 
   二、piazzaXBlock是用于集成到Open edX平台的XBlock.包括三个xblock.
   
:sparkles:  详细说明见：
https://github.com/xyongcn/piazza-data-tsinghua.edu.cn_spring2015_30240243x/tree/master/piazzaXBlock

   三、program中包含从piazza获取数据的程序，以及对得到的json数据进行解析的程序
   
:sparkles: 详细说明见：
https://github.com/xyongcn/piazza-data-tsinghua.edu.cn_spring2015_30240243x/tree/master/program

 四、staticfiles包括的是数据解析的具体代码，安装xblock时也会用到。
 
:sparkles: 详细说明见：
 https://github.com/xyongcn/piazza-data-tsinghua.edu.cn_spring2015_30240243x/tree/master/staticfiles


#结果展示

*piazza讨论信息的筛选可以在页面的下拉菜单中选择，也可以直接在url中加入参数直接进行快速筛选*
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－

**1. 利用多级标签进行讨论信息的筛选（url中不指定参数）**

     依次选择标签："lecture9","课堂问答","instructor-note"
   
      每一次选择后列表中包含的记录会相应的减少。
     
   
   + 如：当选择“lecture9”,"课堂问答"时结果中有6条符合条件的记录；
   
   + 当再加入"instructor-note"选择时结果中只有1条符合条件的记录。
   
**2. 利用多级标签进行讨论信息的筛选（url中指定参数）**

     参数的指定格式为：?tags=参数1,参数2,参数3
   
   + 例如指定参数为按"lecture9","课堂问答"进行筛选，则url为：
   
   [http://crl.ptopenlab.com:8811/courses/Tsinghua/CS101/2015_T1/courseware/65a2e6de0e7f4ec8a261df82683a2fc3/896b56b6156047869eecd8b519852558/?tags=lecture9,课堂问答](http://crl.ptopenlab.com:8811/courses/Tsinghua/CS101/2015_T1/courseware/65a2e6de0e7f4ec8a261df82683a2fc3/896b56b6156047869eecd8b519852558/?tags=lecture9,%E8%AF%BE%E5%A0%82%E9%97%AE%E7%AD%94)
   
   结果下：
   
   + 例如指定参数为按"lecture9","课堂问答"，"instructor-note"进行筛选，则url为：

   [http://crl.ptopenlab.com:8811/courses/Tsinghua/CS101/2015_T1/courseware/65a2e6de0e7f4ec8a261df82683a2fc3/896b56b6156047869eecd8b519852558/?tags=lecture9,课堂问答,instructor-note](http://crl.ptopenlab.com:8811/courses/Tsinghua/CS101/2015_T1/courseware/65a2e6de0e7f4ec8a261df82683a2fc3/896b56b6156047869eecd8b519852558/?tags=lecture9,%E8%AF%BE%E5%A0%82%E9%97%AE%E7%AD%94,instructor-note)

   结果如下：
