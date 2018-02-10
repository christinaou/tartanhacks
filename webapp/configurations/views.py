from django.http import HttpResponse
from . import call
from . import stt
import os

def index(request):
    # number = "15103042628"
    # call.main(number)

    # stt.main("../test/Sample.wav")
    return HttpResponse("Hello, world. You're at the configurations index.")
