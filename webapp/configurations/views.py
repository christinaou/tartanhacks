from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
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
    return HttpResponse(template.render({'triggers':triggers}))
