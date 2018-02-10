from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
import os
import json




@csrf_exempt
def index(request):
    dirpath = os.path.dirname(os.path.realpath(__file__))
    with open(dirpath + '/../database.json') as src:
        db = json.load(src)
    if request.method=="POST":
        if "user_name" in request.POST:
            myName = request.POST['user_name']
            db['myName'] = myName
            with open(dirpath + '/../database.json', 'w+') as outfile:
                json.dump(db, outfile)
            print(myName)
            template = loader.get_template("onboard.html")
        elif "ethnicity" in request.POST:
            ethnicity = request.POST['ethnicity']
            gender = request.POST['gender']
            height_feet = request.POST['height_feet']
            height_inches = request.POST['height_inches']
            hair_color = request.POST['hair_color']

            db['ethnicity'] = ethnicity
            db['gender'] = gender
            db['height_feet'] = height_feet
            db['height_inches'] = height_inches
            db['hair_color'] = hair_color
            template = loader.get_template("onboard2.html")
            return redirect('/configurations')

        with open(dirpath + '/../database.json', 'w+') as outfile:
            json.dump(db, outfile)
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
    dirpath = os.path.dirname(os.path.realpath(__file__))
    with open(dirpath + '/../database.json') as src:
        db = json.load(src)

    template = loader.get_template("onboard3.html")
    return HttpResponse(template.render({'contact': db['friendsNumbers'][0]}))
def landing(request):
    template = loader.get_template("landing.html")
    return HttpResponse(template.render())
def my_info(request):
    template = loader.get_template("my_info.html")
    return HttpResponse(template.render())
def contacts(request):
    dirpath = os.path.dirname(os.path.realpath(__file__))
    with open(dirpath + '/../database.json') as src:
        db = json.load(src)
    template = loader.get_template("contacts.html")
    return HttpResponse(template.render({'contact': db['friendsNumbers'][0]}))
