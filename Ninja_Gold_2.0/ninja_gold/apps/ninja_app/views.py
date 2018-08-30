# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
import random, datetime

def index(request):
	request.session['money'] = 0
	request.session['activity'] = []
	return render(request, 'ninja_app/index.html')

def process(request):
	randNum = 0
	building = ""
	now = datetime.datetime.now().strftime('%H:%M:%S')
	if request.POST['building'] == "farm":
		randNum = random.randrange(10, 21)
		building = "farm"
		request.session['money'] += randNum
	elif request.POST['building'] == "cave":
		building = "cave"
		randNum = random.randrange(5, 11)
		request.session['money'] += randNum
	elif request.POST['building'] == "house":
		building = "house"
		randNum = random.randrange(2, 6)
		request.session['money'] += randNum
	elif request.POST['building'] == "casino":
		building = "casino"
		randNum = random.randrange(-50, 51)
		request.session['money'] += randNum
	if(randNum >= 0):
		request.session['activity'].append(["win", "Earned " + str(randNum) + " gold(s) from "+ building+ "! (" + now + ")" ])
	else:
		request.session['activity'].append(["lost", "Lost " + str(randNum) + " gold(s) from "+ building+ "! (" + now + ")"])
	return redirect('/result')

def result(request):
	context = {
		'gold' : request.session['money'],
		'activities' : request.session['activity'] 
	}
	return render(request, 'ninja_app/index.html', context)

# Create your views here.
