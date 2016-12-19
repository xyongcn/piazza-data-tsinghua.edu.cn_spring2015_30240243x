/* Javascript for GradeXBlock. */
function GradeXBlock(runtime, element) {

    
    function saveCallBack(result) {
        alert(result.score);
    }


     function generateOption(result){   
        var div_question=document.getElementById("QAList");
        $('#generateList').nextAll().remove();    
        var div_gradeBlock = document.getElementById("gradePage");
        div_gradeBlock.innerHTML=""; 
        var select_element= document.createElement("select");

        select_element.setAttribute("id", "Select");
        select_element.setAttribute("style","height:30px;width:120px");
        var opt= new Option("please select","please select");
             select_element.options.add(opt); 
                                                                                      
        for (var i in result.option){
            var opt= new Option(result.option[i],result.option[i]);
             select_element.options.add(opt);
          }
        select_element.addEventListener("change",function(){return clickSelect.apply(this,[this.value]); });
        div_question.appendChild(select_element);
      
      }
       
       function clickSelect(value){

          $.ajax({
            type: "POST",
            url: handlerUrlSelect,                                                                                           
            data: JSON.stringify({"value": value}),
            success: selectCallBack                                                                                       
        });
       } 

                                                                                                                     
    function selectCallBack(result){
        data=eval("("+result.data+")");
        var div_gradeBlock = document.getElementById("gradePage");
        div_gradeBlock.innerHTML=""; 
        var div_start_title=document.createElement("div");
        div_start_title.setAttribute("class","start_title");
        div_start_title.innerHTML ="批改页面";
        div_gradeBlock.appendChild (div_start_title );
        var br_element=document.createElement("br");
       var hr_element=document.createElement('div');
       hr_element.setAttribute('style','height:2px;width:100%;border-bottom:2px solid  white;');   
        div_gradeBlock.appendChild(hr_element);

        var div_page_main=document.createElement("div");
        div_page_main.setAttribute("id","page_main");
        div_gradeBlock.appendChild (div_page_main);

        var div_view=document.createElement("div");
        div_view.setAttribute("id","view");
        div_gradeBlock.appendChild (div_view);

        var div_question=document.createElement("div");
        div_question.setAttribute("id","question");
        div_question.setAttribute("class","region_box");
        div_view.appendChild(div_question);


        var div_post_title=document.createElement("div");
        div_post_title.setAttribute("class","post_title");
        div_post_title.innerHTML="题目";
        div_question.appendChild(div_post_title);
         var br_1=document.createElement('br');
        div_question.appendChild(br_1);
        var hr_1=document.createElement('hr');
        hr_1.setAttribute('style','width:100%;');
        div_question.appendChild(hr_1);

        var div_QuestionInfo = document.createElement("div");
        div_QuestionInfo.setAttribute("id","QuestionInfo");
        div_QuestionInfo.setAttribute("class","post_content");
        div_question.appendChild(div_QuestionInfo);

        var div_q_content=document.createElement("div");
        div_q_content.id="q_content";
        div_q_content.setAttribute("class","post_content");
        div_q_content.innerHTML=data.question;
        div_QuestionInfo.appendChild(div_q_content);

        var div_RightAnswer=document.createElement("div");
        div_RightAnswer.setAttribute("id","RightAnswer");
        div_RightAnswer.setAttribute("class","region_box");
        div_view.appendChild(div_RightAnswer);

        var div_post_title_1=document.createElement("div");
        div_post_title_1.setAttribute("class","post_title");
        div_post_title_1.innerHTML="参考答案";
        div_RightAnswer.appendChild(div_post_title_1);
        var br_2=document.createElement('br');
        div_RightAnswer.appendChild(br_2);                                              
        var hr_2=document.createElement('hr');
        hr_2.setAttribute('style','width:100%;');
        div_RightAnswer.appendChild(hr_2)
        var div_RightAnswerInfo=document.createElement("div");
        div_RightAnswerInfo.setAttribute("id","RightAnswerInfo");
        div_RightAnswer.appendChild (div_RightAnswerInfo);

        var div_right_answer = document.createElement("div");
        div_right_answer.id = "right_answer";
        div_right_answer.setAttribute("class","post_content");
        div_right_answer.innerHTML = data.right_answer;
        div_RightAnswerInfo.appendChild(div_right_answer);

        var div_AnswerList=document.createElement("div");
        div_AnswerList.setAttribute("id","AnswerList");
        div_AnswerList.setAttribute("class","region_box");
        div_view.appendChild (div_AnswerList);

        var div_post_title_2=document.createElement("div");
        div_post_title_2.setAttribute("class","post_title");
        div_post_title_2.innerHTML="待批改列表";
        div_AnswerList.appendChild(div_post_title_2);
        var br_3=document.createElement('br');
        div_AnswerList.appendChild(br_3);
        var hr_3=document.createElement('hr');
        hr_3.setAttribute('style','width:100%;');
        div_AnswerList.appendChild(hr_3);
        var div_AnswerListInfo=document.createElement("div");
        div_AnswerListInfo.setAttribute("id","AnswerListInfo");
        div_AnswerList.appendChild (div_AnswerListInfo);


        for(i=0;i<data.answer_list.length;i++)
        {
           var div=document.createElement("div");
           div.setAttribute("class","region_box_inner");
           div_AnswerListInfo.appendChild(div);

           var div_answer=document.createElement("div");
           div_answer.setAttribute("class","post_content");
           div_answer.innerHTML=data.answer_list[i].answer;
           div.appendChild(div_answer);

           var p = document.createElement("p");
           p.innerHTML="请给分: "
           var input_element = document.createElement("input");
           input_element.setAttribute("type","text");
           input_element.setAttribute("name","grade");
           input_element.setAttribute("id",data.answer_list[i].email);
           input_element.setAttribute("style","background:white;width:100px;height:30px;");
           p.appendChild(input_element);

           var btn_element=document.createElement("input");
           btn_element.setAttribute("type","button");
           btn_element.setAttribute("value","save");
           btn_element.setAttribute("style","vertical-align:middle;height:30px;");
           btn_element.setAttribute("id",data.answer_list[i].user_name+","+data.answer_list[i].email);
          
            btn_element.onclick=function(){click_btn(element,this,data.q_number);}
            p.appendChild(btn_element);
            div.appendChild(p);
       }
        var br_5=document.createElement('br');
        div_AnswerListInfo.appendChild(br_5);
        var br_7=document.createElement('br');
        div_view.appendChild(br_7);



   
    }                       
    var handlerUrl = runtime.handlerUrl(element, 'increment_count');
    var handlerUrlSave = runtime.handlerUrl(element, 'save_score');
    var handlerUrlGen = runtime.handlerUrl(element, 'generate_list');
    var handlerUrlSelect = runtime.handlerUrl(element, 'select_click');
    $('#generateList', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrlGen,                                                                                        

            data: JSON.stringify({"hello": "world"}),
            success: generateOption                                                                                    

        });
    });
    
    function click_btn(element,btn,q_number){
                                                                                                                       
        arr = new Array;
        arr = btn.id.split(",");
        var user_name = arr[0];
        var email = arr[1];
        var score = document.getElementById(email).value;
        var score_json={"user_name":user_name ,"email":email,"q_number":q_number,"score":score}
        var score_str = JSON.stringify(score_json)
        $.ajax({
            type: "POST",
            url: handlerUrlSave,                                                                                          
            data: JSON.stringify(score_json),
            success: saveCallBack                                                                                       
        });
   
                                                                                                                       
                                                                                                                       
    }

    $('p', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"hello": "world"}),
            success: updateCount
        });
    });
   
    $('.fullscreen',element).click(function(eventObject){
       var screen=document.getElementById("grade_block");
       if(screen.requestFullscreen){
          screen.requestFullscreen();}
       else if (screen.mozRequestFullScreen){
         screen.mozRequestFullScreen();
         }
      else if (screen.webkitRequestFullscreen){
           screen.webkitRequestFullscreen();
       }
      });
    $(function ($) {
        /* Here's where you'd do things on page load. */
        
I       
    });
}

