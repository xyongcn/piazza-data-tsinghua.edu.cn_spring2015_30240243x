
$(document).ready(function(){

    //注册一个比较大小的Helper,判断v1是否等于于v2
    Handlebars.registerHelper("compare",function(v1,v2,options){
    if(v1==v2){
    //满足添加继续执行
    return options.fn(this);
    }
    else{
    //不满足条件执行{{else}}部分
         return options.inverse(this);
     }
    });
   //feed


    $("ul li a").bind("click",function()
        {
            var label=$(this).html();
            url_github="https://raw.githubusercontent.com/xyongcn/piazza-data-tsinghua.edu.cn_spring2015_30240243x/master/data/piazza-data-filter/filter_feed_"+label +".json";
            $.ajax({
                type : "get",
                cache : false,
                url : url_github , // 请求地址
                success : function(data) { // ajax执行成功后执行的方法
                    var data_json = eval("(" + data + ")"); // 把string转化为json
                    var source_feed = $("#feed-template").html();
                    var template_feed = Handlebars.compile(source_feed);
                    var html_feed = template_feed(data_json);
                    $("#feed").html(html_feed);}
            });
        }
    );

    $("#btn_read").click(function(){
        var label = document.getElementById("label").value;
        url_github="https://raw.githubusercontent.com/xyongcn/piazza-data-tsinghua.edu.cn_spring2015_30240243x/master/data/piazza-data-filter/filter_feed_"+label +".json";
        $.ajax({
            type : "get",
            cache : false,
            url : url_github , // 请求地址
            success : function(data) { // ajax执行成功后执行的方法
                var data_json = eval("(" + data + ")"); // 把string转化为json
                var source_feed = $("#feed-template").html();
                var template_feed = Handlebars.compile(source_feed);
                var html_feed = template_feed(data_json);
                $("#feed").html(html_feed);}
        });
    });


});

