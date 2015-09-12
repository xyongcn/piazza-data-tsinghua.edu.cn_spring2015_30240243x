

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

     //页面加载时feed部分显示的是my_feed的内容 
     url_github="https://raw.githubusercontent.com/xyongcn/piazza-data-tsinghua.edu.cn_spring2015_30240243x/master/data/piazza-data-filter/piazza_my_feed.txt";
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
     
     //页面加载时page_center部分显示的是cid=1的内容 
     var source = $("#page-center-template").html();
     var template = Handlebars.compile(source);
     url_github="https://raw.githubusercontent.com/xyongcn/piazza-data-tsinghua.edu.cn_spring2015_30240243x/master/data/piazza-data/1.json";
     $.ajax({
        type : "get",
        cache : false,
        url : url_github , // 请求地址
        success : function(data) { // ajax执行成功后执行的方法
            var data_json = eval("(" + data + ")"); // 把string转化为json
            var html = template(data_json);  // json数据传送给html模板
            $("#page_center").html(html);}
     });
     
      //页面加载时popular_tags_bar部分显示的是popular tags的内容 
    
      url_github="https://raw.githubusercontent.com/xyongcn/piazza-data-tsinghua.edu.cn_spring2015_30240243x/master/data/piazza-data-filter/piazza_my_feed.txt";
            $.ajax({
                type : "get",
                cache : false,
                url : url_github , // 请求地址
                success : function(data) { // ajax执行成功后执行的方法
                    var data_json = eval("(" + data + ")"); // 把string转化为json
                    var source_feed = $("#popular-tags-bar-template").html();
                    var template_feed = Handlebars.compile(source_feed);
                    var html_feed = template_feed(data_json);
                    $("#popular_tags_bar").html(html_feed);}
            });
     

   

});
//page_center
//点击feed部分特定的项目，在page_center部分显示该cid的详细内容
function clickLi(cid)
{
    var source = $("#page-center-template").html();
    var template = Handlebars.compile(source);
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
}




//点击列出的标签，显示对应的feed部分
   function click_tags(label){
           
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



//下拉菜单列出所有标签,选择后显示在feed部分
function click_select_label(obj){ 
  var opt = obj.options[obj.selectedIndex]

    var label=opt.text;
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


