"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
import os
import os.path
import json
import time
from xblock.core import XBlock
from xblock.fields import Scope, Integer
from xblock.fragment import Fragment
from lib_log import Log

ISOTIMEFORMAT='%Y-%m-%d %X'
current_time=time.strftime(ISOTIMEFORMAT,time.localtime())  

class GradeXBlock(XBlock):
    """
    GradeXblock achieve QA html page for teacher,to marking students' answer
    """
    logger = Log.logger()
    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")
    
    
    def student_view(self, context=None):
        """
        The primary view of the GradeXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/grade.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/grade.css"))
        frag.add_javascript(self.resource_string("static/js/src/grade.js"))

        frag.initialize_js('GradeXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.

    @XBlock.json_handler
    def generate_list(self, data, suffix=''):
        """
          An generating Question Number List  handler, which generate number list to mark.
        """
        student = self.runtime.get_real_user(self.runtime.anonymous_student_id)
        email = student.email
        username=student.username
        self.logger.info("edx_login_student_email:"+email+",username:"+username)
        # git pull from gitlab
        status=os.system('/var/www/zyni/script/pullFromGitlab.sh')
        self.logger.info("git pull, status="+str(status))
        # generate json file which to be used as data source to generate html page
        status2=os.system('python /var/www/zyni/script/judge_QA_question.py')  
        self.logger.info("invoke judge_QA_question.py,status="+str(status2))   
        # scan "judge_QA_qustion" to get q_number list 
        path="/var/www/zyni/grade_xblock_data/judge_QA_question/"
        QA_list=[]
        for parent,dirnames,filenames in os.walk(path):
            for filename in filenames:
                (shortname,extension)=os.path.splitext(filename)
                QA_list.append(shortname)
                                                       
        return {"option":QA_list}
 
    @XBlock.json_handler
    def select_click(self, data, suffix=''):
        """
        An read json file  handler, which read json file according to selected q_number.
        """
        # read json file
        path="/var/www/zyni/grade_xblock_data/judge_QA_question/"
        fileName=str(data["value"])+".json"
        filePath=os.path.join(path,fileName)                                      
        self.logger.info("invoke select_click,read file:"+filePath)
        fileOut=open(filePath,'r')
        data=fileOut.read()
        fileOut.close() 
        # return file content                                                      
                                                                                                                       
        return {"data":data}
    @XBlock.json_handler
    def save_score(self, data, suffix=''):
        """
        save_score handler,which save score when click save button 
        """
        # save_score according to email
        self.logger.info("invoke save_score,email="+data['email']+",q_number="+str(data['q_number']))
        path="/var/www/zyni/answer/score/"
        email=data['email']
        data['statistic_time']=current_time
        dir_path=os.path.join(path,email)
        if(os.path.exists(dir_path) is not True):
             os.makedirs(dir_path,0777)
        file_name='_'+str(data['q_number'])+'.json'
        file_path=os.path.join(dir_path,file_name)
        fileIn=open(file_path,'w')
        data=json.dumps(data)
        fileIn.write(data)
        fileIn.close()
        # call "pushToGitlab.sh" to push changes to gitlab
        status = os.system("/var/www/zyni/script/pushToGitlab.sh "+email)
        self.logger.info("invoke pushTogitlab.sh,status="+str(status))
        if status == 0:
            message="save suceessfully!"
        else:
            message="save fail!"
        # return message weather push successfully
        return {"score":message}
    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("GradeXBlock",
             """<grade/>
             """),
            ("Multiple GradeXBlock",
             """<vertical_demo>
                <grade/>
                <grade/>
                <grade/>
                </vertical_demo>
             """),
        ]
