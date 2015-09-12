"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer
from xblock.fragment import Fragment


class PiazzaXBlock(XBlock):
    """
    piazza XBlock to show content according to cid
    """

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the PiazzaXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/piazza.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/piazza.css"))
        frag.add_javascript(self.resource_string("static/js/src/piazza.js"))

        frag.initialize_js('PiazzaXBlock')
        return frag

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("PiazzaXBlock",
             """<vertical_demo>
                <piazza/>
                <piazza/>
                <piazza/>
                </vertical_demo>
             """),
        ]
