from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from django.http import HttpResponse
<<<<<<< HEAD
from . import call
from . import stt
import os
=======
from django.views.decorators.csrf import csrf_exempt
<<<<<<< HEAD

>>>>>>> 53645ca9a628785fc833130bd8b2a939d4b6bd25
=======
triggers = [
    {
        'number': 9492059539,
        'word': "apple",
        'type': "call",
        'id':0
    }
]
>>>>>>> triggers

@csrf_exempt
def index(request):
<<<<<<< HEAD
    # number = "15103042628"
    # call.main(number)

    # stt.main("../test/Sample.wav")
    return HttpResponse("Hello, world. You're at the configurations index.")
=======
    if request.method=="POST":
        # Delete trigger lol
        if "trigger_id" in request.POST:
            trigger_id = request.POST["trigger_id"]
            triggers.pop(int(trigger_id))
        # Add trigger
        else:
            number = request.POST["trigger_number"]
            word = request.POST['trigger_word']
            trigger_type = request.POST['trigger_type']
            triggers.append({
                'number':number,
                'word': word,
                'type': trigger_type,
                'id': len(triggers)
            })
    template = loader.get_template("configurations/index.html")
<<<<<<< HEAD
    return HttpResponse(template.render())
>>>>>>> 53645ca9a628785fc833130bd8b2a939d4b6bd25
=======
    return HttpResponse(template.render({'triggers':triggers}))
>>>>>>> triggers
