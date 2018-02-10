from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.template import loader
import os
import json


dirpath = os.path.dirname(os.path.realpath(__file__))
with open(dirpath + '/../database.json') as src:
    db = json.load(src)

@csrf_exempt
def index(request):
    if request.method=="POST":
        myName = request.POST['user_name']
        db['myName'] = myName
        with open(dirpath + '/../database.json', 'w+') as outfile:
            json.dump(db, outfile)
        print(myName)
        template = loader.get_template("onboard.html")
        return HttpResponse(template.render())

    template = loader.get_template("index.html")
    return HttpResponse(template.render())
def onboard(request):
    template = loader.get_template("onboard.html")
    return HttpResponse(template.render())
def onboard2(request):
    template = loader.get_template("onboard2.html")
    return HttpResponse(template.render())
def onboard3(request):
    template = loader.get_template("onboard3.html")
    return HttpResponse(template.render())
def landing(request):
    template = loader.get_template("landing.html")
    return HttpResponse(template.render())
def my_info(request):
    template = loader.get_template("my_info.html")
    return HttpResponse(template.render())
def contacts(request):
    template = loader.get_template("contacts.html")
    return HttpResponse(template.render())
