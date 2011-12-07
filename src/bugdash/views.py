from django.template.response import TemplateResponse

from .agents import DashboardAgent
from .bugs import Dashboard



def home(request):
    agent = DashboardAgent("cjm46543@yahoo.com", "testpw") # @@@
    bugs = agent.get_bugs(creator="carl@oddbird.net") # @@@
    intervals = Dashboard(bugs, 7)
    return TemplateResponse(request, "home.html", {"intervals": intervals})
