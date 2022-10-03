# pages/views.py
from django.http import HttpResponse
import json
# thsi is the hello world actual viewing file that will be used
def homePageView(request):
    #ghfyjfnl87e87 89er79e8
    data = {
        "Message" : "Hello World!"
    }
    #ghfyjfnl87e87 89er79e8
    #ghfyjfnl87e87 89er79e8
    dump = json.dumps(data)

    #ghfyjfnl87e87 89er79e8
    #ghfyjfnl87e87 89er79e8
    #ghfyjfnl87e87 89er79e8
    #ghfyjfnl87e87 89er79e8
    #ghfyjfnl87e87 89er79e8
    #ghfyjfnl87e87 89er79e8
    #ghfyjfnl87e87 89er79e8
    #ghfyjfnl87e87 89er79e8
    #ghfyjfnl87e87 89er79e8
    #ghfyjfnl87e87 89er79e8
    #ghfyjfnl87e87 89er79e8
    return HttpResponse(dump, content_type='application/json')
'''actul prd ends here'''
