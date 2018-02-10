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
        'number': "9492059539",
        'word': "apple",
        'type': "call",
        'id':0
    },
    {
        'number': "9492059539",
        'word': "i have a boyfriend",
        'type': "call",
        'id':0
    },
    {
        'number': None,
        'word': "blackberry",
        'type': "receive",
        'id':1
    }
]

myNumber = "9085469708"

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

def determineTrigger(text):
    for trigger in triggers:
        if trigger['word'] in text:
            if trigger['type'] == 'call':
                print('Trigger ' + trigger['word'] + ' calling ' + trigger['number'])
                # call.main(trigger['number'])
            elif trigger['type'] == 'receive':
                print('Trigger ' + trigger['word'] + ' receiving to ' + myNumber)
                # call.main(myNumber)

@csrf_exempt
def compute(request):
    if request.method == 'POST':
        if len(request.FILES):
            fileObj = request.FILES['filee']
            text = stt.main(fileObj)
            if (text):
                determineTrigger(text)
        else:
            print("no file")
    return HttpResponse("wei")





# number = "15103042628"
# call.main(number)
