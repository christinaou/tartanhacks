from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from django.http import HttpResponse
from . import call
from . import stt
import os
from django.views.decorators.csrf import csrf_exempt
from dataview import DataView

triggers = [
    {
        'number': 9492059539,
        'word': "apple",
        'type': "call",
        'id':0
    }
]

@csrf_exempt
def index(request):
    if request.method=="POST":
        # Delete trigger lol
        if "trigger_id" in request.POST:
            trigger_id = request.POST["trigger_id"]
            triggers.pop(int(trigger_id))
        # Add trigger
        else:
            # stt.main("../test/Sample.wav")
            number = request.POST["trigger_number"]
            word = request.POST['trigger_word']
            trigger_type = request.POST['trigger_type']
            triggers.append({
                'number':number,
                'word': word,
                'type': trigger_type,
                'id': len(triggers)
            })
            print("Added trigger, so triggers: ",end="")
            print(triggers)
    template = loader.get_template("configurations/index.html")
    return HttpResponse(template.render({'triggers':triggers}))

@csrf_exempt
def compute(request):
    if request.method == 'POST':
        # print(request)
        # print(request.POST)
        # if "filee" in request.POST:
        #     print("found!!!")
        #     print(request.POST["filee"])
        #     print(type(request.POST["filee"]))
        # else:
        #     print("not :(((")
        if len(request.FILES):
            print(request.FILES)
            fileObj = request.FILES['filee']
            print(fileObj)
            print(type(fileObj))
            stt.main(fileObj)
        else:
            print("no file")
    return HttpResponse("wei")





# number = "15103042628"
# call.main(number)
