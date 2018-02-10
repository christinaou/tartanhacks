from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from django.http import HttpResponse
from . import call
from . import sms
from . import stt
import os
from django.views.decorators.csrf import csrf_exempt
import json



@csrf_exempt
def index(request):
    dirpath = os.path.dirname(os.path.realpath(__file__))
    with open(dirpath + '/../database.json') as src:
        db = json.load(src)
        print(db)

    if request.method=="POST":
        # Delete trigger lol
        if "trigger_id" in request.POST:
            trigger_id = request.POST["trigger_id"]
            trigger_type = request.POST["trigger_type"]
            db['triggers'][trigger_type].pop(int(trigger_id))
            for x in range(int(trigger_id),len(db['triggers'][trigger_type])):
                db['triggers'][trigger_type][x]['id'] = db['triggers'][trigger_type][x]['id'] - 1

        # Add trigger
        else:
            # stt.main("../test/Sample.wav")
            word = request.POST['trigger_word']
            trigger_type = request.POST['trigger_type']
            db['triggers'][trigger_type].append({
                'word': word,
                'id': len(db['triggers'][trigger_type])
            })
            print("Added trigger, so triggers: ",end="")
        with open(dirpath + '/../database.json','w+') as outfile:
            json.dump(db, outfile)

    template = loader.get_template("configurations/index.html")
    print(db['myName'])
    return HttpResponse(template.render({'triggers':db['triggers']}))

def determineTrigger(text):
    for trigger in db['triggers']['emergency']:
        if trigger['word'] in text:
            print('Trigger ' + trigger['word'] + ' calling ' + db['emergencyNumber'])
            # call.main(emergencyNumber)
            for num in friendsNumbers:
                print('texting ' + num)
                sms.main(num, db['myName'])
    for trigger in db['triggers']['social']:
        if trigger['word'] in text:
            print('Trigger ' + trigger['word'] + ' calling ' + db['myNumber'])
            # call.main(myNumber)

@csrf_exempt
def compute(request):
    dirpath = os.path.dirname(os.path.realpath(__file__))
    with open(dirpath + '/../database.json') as src:
        db = json.load(src)
        print(db)
    if request.method == 'POST':
        if len(request.FILES):
            fileObj = request.FILES['filee']
            text = stt.main(fileObj)
            if (text):
                determineTrigger(text)
        else:
            print("no file")
    return HttpResponse("wei")
