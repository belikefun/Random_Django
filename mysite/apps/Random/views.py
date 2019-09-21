from django.shortcuts import render
from django.http import HttpResponse
#from . import randomka
import time
from .models import Random
from django import forms
import random
# Create your views here.
def index (request):
    return render(request,'base.html')

def generate(request):
    start = request.POST['start']
    end = request.POST['end']
    numbers_list = Random.objects.order_by('-id')[:1]
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
    if(ip=="127.0.0.1"):
        return render(request,'Random/generate.html', {'numbers_list': numbers_list})
    else:
        a=list()
        a = random.randrange(int(start),int(end))
        print (a)
        return render(request,'Random/generate.html', {'numbers_list': a})
def main(request,start,end):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
    zapros = randomka.main(1,500,str(ip))
    for a in range(len(zapros)):
        time.sleep(0.005)
        return HttpResponse(zapros[a])
