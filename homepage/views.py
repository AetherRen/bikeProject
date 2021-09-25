from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import staticfiles

def index(request):
    context_dict = {'boldmessage': 'Your User Name is Dongzhan XIe'}
    return render(request, 'homepage/index.html', context = context_dict)


def about(request):
    return HttpResponse("Let's go G2!   <a href='/homepage/'>Index</a>")