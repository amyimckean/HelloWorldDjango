from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, "home.html", {
        'HelloWorldText': "Hello World!",
    })


def GetJSON(request):
    return JsonResponse({'Message': 'Hello World!'})
