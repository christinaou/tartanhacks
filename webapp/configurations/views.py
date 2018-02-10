from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method=="POST":
        data = request.POST["name_field"]
        print(data)
    template = loader.get_template("configurations/index.html")
    return HttpResponse(template.render())
