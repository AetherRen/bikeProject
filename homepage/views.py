from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import staticfiles


def index(request):
    context_dict = {'boldmessage': 'Your User Name is Dongzhan XIe'}
    return render(request, 'homepage/index.html', context = context_dict)


def rent(request):
    return HttpResponse("Let's rent now   <a href='/homepage/'>Index</a>")