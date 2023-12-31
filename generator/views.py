from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    #return HttpResponse('Hello!')
    return render(request, 'generator/home.html')


def password(request):

    characters = list('abcdefghijklmnoprstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRST1UVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    lenght = int(request.GET.get('length', 12))

    thepassword = ''

    for x in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

def description(request):
    return render(request, 'generator/description.html')
