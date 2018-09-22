from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
def index(request):
	return render(request, 'theApp/index.html')

def create(request):
	valid, response = User.objects.validate_and_create_user(request.POST)
	if valid:
		request.session['user_id'] = response.id
	else:
		for error in response:
			messages.error(request, error)
	return redirect('/theApp/new')

def new(request):
	return render(request, 'theApp/index.html')

def logIn(req):
  if req.method != 'POST':
    return redirect('/theApp/new')
  valid, response = User.objects.validate_and_login(req.POST)
  if valid == False:
    for error in response:
      messages.error(req, error)
    return redirect('/theApp/new')
  else:
    req.session['user_id'] = response.id
    print "ID = " +  str(response.id)
    return redirect('/theApp/success')

def success(request):
	user = User.objects.get(id=request.session['user_id'])
	print "name : " + user.firstname 
	context = {
		'firstname' : user.firstname
	}
	return render(request, 'theApp/success.html', context)