from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from django.http import HttpResponse
from . import call
from . import sms
from . import stt
import os
from django.views.decorators.csrf import csrf_exempt

triggers = {
    'emergency':[
        {
            'word': "apple",
            'id':0
        },
        {
            'word': "someone please help me",
            'id':1
        }
    ],
    'social':[
        {
            'word': "i miss my hamster",
            'id':0
        }
    ]
}

myName = "Tina"

myNumber = "19085469708"
emergencyNumber = "19492059539" #would be 911
friendsNumbers = ["15103042628"]

@csrf_exempt
def index(request):
    if request.method=="POST":
        # Delete trigger lol
        if "trigger_id" in request.POST:
            trigger_id = request.POST["trigger_id"]
            trigger_type = request.POST["trigger_type"]
            triggers[trigger_type].pop(int(trigger_id))
            for x in range(int(trigger_id),len(triggers[trigger_type])):
                triggers[trigger_type][x]['id'] = triggers[trigger_type][x]['id'] - 1

        # Add trigger
        else:
            # stt.main("../test/Sample.wav")
            word = request.POST['trigger_word']
            trigger_type = request.POST['trigger_type']
            triggers[trigger_type].append({
                'word': word,
                'id': len(triggers[trigger_type])
            })
            print("Added trigger, so triggers: ",end="")
            print(triggers)
    template = loader.get_template("configurations/index.html")
    return HttpResponse(template.render({'triggers':triggers}))

def determineTrigger(text):
    for trigger in triggers['emergency']:
        if trigger['word'] in text:
            print('Trigger ' + trigger['word'] + ' calling ' + emergencyNumber)
            # call.main(emergencyNumber)
            for num in friendsNumbers:
                print('texting ' + num)
                sms.main(num, myName)
    for trigger in triggers['social']:
        if trigger['word'] in text:
            print('Trigger ' + trigger['word'] + ' calling ' + myNumber)
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
