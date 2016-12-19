/**
 * User: zhangyanni
 * Date: 15-9-3
 * Time: 下午8:34
 */
$(document).ready(function(){
    var source = $("#page-center-template").html();
    var template = Handlebars.compile(source);
    //注册一个比较大小的Helper,判断v1是否等于于v2
    Handlebars.registerHelper("compare",function(v1,v2,options){
        if(v1==v2){
            //满足添加继续执行
            return options.fn(this);
        }else{
            //不满足条件执行{{else}}部分
            return options.inverse(this);
        }
    });

    $("#btn_read").click(function(){
        var cid = document.getElementById("cid").value;
        url_github="https://raw.githubusercontent.com/xyongcn/piazza-data-tsinghua.edu.cn_spring2015_30240243x/master/data/piazza-data/"+cid+".json";
        $.ajax({
            type : "get",
            cache : false,
            url : url_github , // 请求地址
            success : function(data) { // ajax执行成功后执行的方法
                var data_json = eval("(" + data + ")"); // 把string转化为json
                var html = template(data_json);  // json数据传送给html模板
                $("#page_center").html(html);}
         });
    });
});
