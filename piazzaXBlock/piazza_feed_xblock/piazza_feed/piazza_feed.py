"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer
from xblock.fragment import Fragment


class PiazzaFeedXBlock(XBlock):
    """
    XBlock for piazza-feed.according to label to show content
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.


    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the PiazzaFeedXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/piazza_feed.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/piazza_feed.css"))
        frag.add_javascript(self.resource_string("static/js/src/piazza_feed.js"))
        frag.initialize_js('PiazzaFeedXBlock')
        return frag

  
    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("PiazzaFeedXBlock",
             """<vertical_demo>
                <piazza_feed/>
                <piazza_feed/>
                <piazza_feed/>
                </vertical_demo>
             """),
        ]
