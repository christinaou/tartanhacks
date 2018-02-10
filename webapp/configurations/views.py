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

>>>>>>> 53645ca9a628785fc833130bd8b2a939d4b6bd25

@csrf_exempt
def index(request):
<<<<<<< HEAD
    # number = "15103042628"
    # call.main(number)

    # stt.main("../test/Sample.wav")
    return HttpResponse("Hello, world. You're at the configurations index.")
=======
    if request.method=="POST":
        data = request.POST["name_field"]
        print(data)
    template = loader.get_template("configurations/index.html")
    return HttpResponse(template.render())
>>>>>>> 53645ca9a628785fc833130bd8b2a939d4b6bd25
