

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
     url_github="https://raw.githubusercontent.com/xyongcn/piazza-data-tsinghua.edu.cn_spring2015_30240243x/master/data/piazza-data-filter/piazza_my_feed.json";
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


    //页面加载时popular_tags_bar部分显示的是popular tags的内容 ，导航栏显示第一级下拉菜单

    url_github="https://raw.githubusercontent.com/xyongcn/piazza-data-tsinghua.edu.cn_spring2015_30240243x/master/data/piazza-data-filter/piazza_my_feed.json";
    $.ajax({
        type : "get",
        cache : false,
        url : url_github , // 请求地址
        success : function(data) { // ajax执行成功后执行的方法
            var data_json = eval("(" + data + ")"); // 把string转化为json
            var source_popular = $("#popular-tags-bar-template").html();
            var template_popular = Handlebars.compile(source_popular);
            var html_popular = template_popular(data_json);
            $("#popular_tags_bar").html(html_popular);

            var source_select = $("#select-linkage-template").html();
            var template_select = Handlebars.compile(source_select);
            var html_select = template_select(data_json);
            $("#top_bar").html(html_select);

        }
    });





});


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






//一级下拉菜单列出所有标签,选择后显示在feed部分，同时根据第一级所选定的标签生成下一级的标签列表和下一级下拉菜单
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
            $("#feed").html(html_feed);
            //根据第一级所选定的标签生成下一级标签列表
            var next_data=gen_next_list (label ,data_json);

            next_data = eval("(" + next_data + ")"); // 把string转化为json
            //添加一个<select>标签
            addNextSbiling(label,obj.id,label,next_data);
            //由next_data作为数据源，利用js模板生成下拉菜单
            var source_select = $("#select-linkage-template").html();
            var template_select = Handlebars.compile(source_select);
            var html_select = template_select(next_data);
            var ID="#"+label;
            $(ID).html(html_select);
        }
    });



}

/***
 *  函数功能：根据第一级选中的标签生成第二级下拉菜单的json数据。
 *  参数： parent是第一级选中的标签；json_data是第一级筛选的结果，json数据
 *  返回值：返回第二级下拉菜单的json数据，其格式为：next_data={"parent":parent,"children":[{"tag":"lab1","ids":[34,23],{"tag":"lab2","ids":[34,434,34]}……]}。用于生成下一级下拉菜单。
 */
function gen_next_list(parent,json_data){
    var arr1 = [];
    var arr2=[];
    //先把result.feed对象下的第一组tags保存到数组arr1中
    for(j=0;j<json_data.result.feed[0].tags.length ;j++)
    {
        if(json_data.result.feed[0].tags[j]!=parent)
        {
            arr1.push(json_data.result.feed[0].tags[j])
        }
    }
    //遍历feed第一组之后的所有组tags，与前一组tags做并集，最后取得feed中的所有tags.结果保存在arr1中
    for(i=1;i<json_data.result.feed.length;i++)
    {
        for(j=0;j<json_data.result.feed[i].tags.length ;j++)
        {
            if(json_data.result.feed[i].tags[j]!=parent)
            {arr2.push(json_data.result.feed[i].tags[j]);}
        }
        //取arr1和arr2的并集
        mergeArray(arr1,arr2);
    }

    //遍历合并后的数组arr1，遍历json_data。找出每一个二级标签对应的id.
    var next_data='{"parent":"'+parent+'","children":[';

    for(i=0;i<arr1.length;i++)
    {

        var temp='{"tag":"'+arr1[i]+'","ids":[';
        next_data +=temp;
        var num_id=0
        for(j=0;j<json_data.result.feed.length;j++)
        {

            var flag=0;

            for(k=0;k<json_data.result.feed[j].tags.length ;k++)
            {


                if(json_data.result.feed[j].tags[k]==arr1[i])
                {
                    flag+=1;

                }
                else if(json_data.result.feed[j].tags[k]==parent)
                {
                    flag+=1;

                }


            }
            if(flag==2)
            {
                num_id+=1;
            }

            if(flag==2&&num_id>1)
            {
                next_data+=',';
            }
            if(flag==2)
            {

                next_data+=json_data.result.feed[j].nr;

            }


            if(j==json_data.result.feed.length-1)
            {
                next_data+=']}';
            }
        }
        if(i!=arr1.length-1)
        {
            next_data+=',';
        }
        else
        {
            next_data+=']}';
        }

    }

    return next_data;
}


/***
 * 合并数组的函数
 * 数组arr1与arr2合并，结果是把arr2合并到arr1,返回arr1
 ***/
function mergeArray(arr1, arr2) {
    var dup;
    for (var i = 0; i < arr2.length; i++){
        dup = false;
        for ( var j = 0;j < arr1.length; j++){
            if (arr1[j] == arr2[i]){
                dup = true;
                break;
            }
        }
        if (!dup){
            arr1.push(arr2[i]);
        }
    }
    return arr1;
}


/***
 * addNextSbiling（）和clickSelect（）两个函数之间递归调用，实现从第二级下拉菜单开始以后的无限级下拉菜单生成
 *
 */

/***
 * 添加下一个兄弟节点
 *  @param nodeId:第一级下拉菜单中选中的标签，
 * @param nodeId ：当前的节点id
 * @param select_id; 创建的兄弟节点id
 * @param select_id; 上一级生成的json数据
 * 调用该函数后会首先删除当前节点之后的所有兄弟节点，然后以select_id为id创建一个新的兄弟节点。
 */
function addNextSbiling(select_1,nodeId,select_id,next_data) {

    //删除当前节点之后的所有兄弟节点
    $("#"+nodeId).nextAll().remove();
    var currentNode = document.getElementById(nodeId);
    //添加 select节点
    var mySelect = document.createElement("select");
    //设置 div 属性，如 id
    mySelect.setAttribute("id", select_id);
    mySelect.addEventListener('change',function(){
        return clickSelect.apply(this,[select_1,this.value,select_id,next_data]);
    });
    //为当前节点添加一个兄弟节点，以当前节点选中的值为新id
    currentNode.parentNode.appendChild(mySelect);

}

/***
 * 选中第二级（及以后）菜单的某一项
 * @param value：第一级下拉菜单选中的标签值
 * @param value：选中的标签对应的ids
 * @param parent:当前选中的标签做为下一级select的id
 * @param next_data:当前下拉菜单对应的json数据
 */
function clickSelect(select_1,value,parent,next_data)
{
    var obj=this.options[this.selectedIndex];
    upd_feed (value,select_1);
    var IdArray = value.split(",");
    var next_data_new=gen_next_taglist(IdArray,obj.text,next_data);

    addNextSbiling(select_1,this.id,obj.text,next_data_new);
    var source_select = $("#select-linkage-template").html();
    var template_select = Handlebars.compile(source_select);
    var html_select = template_select(next_data_new);
    var ID="#"+obj.text;
    $(ID).html(html_select);

}

/***
 * 生成下一级（第三级及以后）下拉菜单的json数据
 * @param IdArray ：当前级下拉菜单选中项所对应的id列表
 * @param select_text：当前级下拉菜单选中项的值
 * @param next_data：当前级下拉菜单所对应的json数据，用于生成下一级下拉菜单的json数据
 * @returns ：下一级下拉菜单的json数据。其格式为：next_data={"parent"select_text,"children":[{"tag":"lab1","ids":[34,23],{"tag":"lab2","ids":[34,434,34]}……]}
 */
function gen_next_taglist(IdArray,select_text,next_data){
    var arr1 = [];
    var arr2=[];
    //遍历第二级（及以后）下拉菜单选中项标签对应的ids
    var flag=0
    for(k=0;k<IdArray.length;k++){
        arr2=[];
        //遍历next_data的children，找出包含当前id的所有标签。.
        for(i=0;i<next_data.children.length;i++)
        {
            for(j=0;j<next_data.children[i].ids.length;j++){
                if(parseInt(IdArray[k])==next_data.children[i].ids[j] && select_text != next_data.children[i].tag){
                    arr2.push(next_data.children[i].tag);
                    flag+=1;
                    if(flag==1&& select_text != next_data.children[i].tag){
                        arr1.push(next_data.children[i].tag);
                    }
                    break;
                }
            }
        }
        mergeArray (arr1,arr2);
    }

    //next_data_new是生成的下一级下拉菜单的json数据
    var next_data_new={};
    next_data_new["parent"]=select_text;
    next_data_new["children"]=[];

    //遍历arr1
    for (i=0;i<arr1.length;i++){
        next_data_new["children"][i]={};
        next_data_new["children"][i]["tag"]=arr1[i];

        //遍历next_data，得到每一个tag对应的id.
        for(j=0;j<next_data.children.length;j++){
            if(arr1[i]==next_data.children[j].tag){
                next_data_new["children"][i]["ids"]=[];
                num=0;
                for(k=0;k<next_data.children[j].ids.length;k++){
                    for(p=0;p<IdArray.length;p++){
                        if(next_data.children[j].ids[k]==parseInt(IdArray[p]))
                        {



                            next_data_new["children"][i]["ids"][num]=next_data.children[j].ids[k];
                            num+=1;
                            break;
                        }
                    }


                }

            }

        }
    }

    return next_data_new;
}


/***
 * 更新feed部分
 * @param value：当前下拉菜单选中的标签对应的id列表
 * @param parent：当前第一级下拉菜单选中的标签值
 */
function upd_feed(value,parent)
{

    var IdArray = value.split(",");
    url_github="https://raw.githubusercontent.com/xyongcn/piazza-data-tsinghua.edu.cn_spring2015_30240243x/master/data/piazza-data-filter/filter_feed_"+parent+".json";
    $.ajax({
        type : "get",
        cache : false,
        url : url_github , // 请求地址
        success : function(data) { // ajax执行成功后执行的方法
            var data_json=find_feed(data,IdArray,parent);
            var source_feed = $("#feed-template").html();
            var template_feed = Handlebars.compile(source_feed);
            var html_feed = template_feed(data_json);
            $("#feed").html(html_feed);

        }
    })


}


/***
 * 根据下拉菜单的选中项，筛选出对应的id列表
 * @param data：是第一级的标签筛选结果。
 * @param IdArray：是本次（第二级及以后）筛选结果的id列表，以数组方式存放。
 * @param parent：是第一级选中的标签
 * @returns json对象，本次筛选结果的json对象
 */
function find_feed(data,IdArray,parent){
    var data_json = eval("(" + data + ")");//把data转化为json对象
    var data_json_new={}; //创建一个新的json对象"data_json_new"
    data_json_new.result={};//为对象添加属性"result",它的值也是一个对象
    data_json_new.result.feed=[];//添加属性"feed",是一个数组
    //遍历符合条件的所有id.
    for(i=0;i<IdArray.length;i++){
        var nr=parseInt(IdArray[i]);//转化为int型
        for(var j=0;j<data_json.result.feed.length;j++){
            var feed=data_json.result.feed[j];
            if(nr==feed.nr){
                data_json_new.result.feed[i]={};
                //复制data_json.result.feed[j]有对应的属性和值到新的json对象 data_json_new中
                for(var key in feed){
                    if(typeof(feed[key])=="object"){

                        data_json_new.result.feed[i][key]=[];
                        for(var key2 in feed[key]){
                            if(feed[key][key2]!=parent)
                            {

                                data_json_new.result.feed[i][key][key2]=feed[key][key2];

                            }

                        }

                    }
                    else{

                        data_json_new.result.feed[i][key]=feed[key];
                    }


                }

            }

        }
    }

    return data_json_new;


}



