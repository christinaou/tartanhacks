from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader



def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())
def onboard(request):
    template = loader.get_template("onboard.html")
    return HttpResponse(template.render())
def onboard3(request):
    template = loader.get_template("onboard3.html")
    return HttpResponse(template.render())
