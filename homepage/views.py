from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import staticfiles
from homepage import userscript


def index(request):
    context_dict = {'boldmessage': 'Your User Name is Dongzhan XIe'}
    return render(request, 'homepage/index.html', context = context_dict)


def rent(request):
    userscript.add_location(221221)
    return HttpResponse("Let's rent now   <a href='/homepage/'>Index</a>")