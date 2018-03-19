# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
# Create your views here.

def index(request):
    
    return render(request, 'survey_app/index.html')

def create(request):
    if request.session['counter'] < 1:
        request.session['counter'] = 0
    if request.method == 'POST':
        request.session['counter'] += 1
        request.session['name'] = request.POST['name']
        request.session['dojolocation'] = request.POST['dojolocation']
        request.session['favoritelanguage'] = request.POST['favoritelanguage']
        request.session['comment'] = request.POST['comment']
        return redirect('/survey_app/result')
def result(request):
    request.session['counter']
    request.session['name']
    request.session['dojolocation']
    request.session['favoritelanguage']    
    return render(request, "survey_app/result.html")
    
def gohome(request):
    # if request.method == 'POST':
    return redirect("/")
