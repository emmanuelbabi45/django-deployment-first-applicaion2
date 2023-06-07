from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Welcome(req):
    ss="hello user welcome to django first project and first app"
    return HttpResponse(ss)