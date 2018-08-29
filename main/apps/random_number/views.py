from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime
from django.utils.crypto import get_random_string

def index(request):
	return render(request,'random_number/index.html')

def generate(request):
	request.session['unique_id'] = get_random_string(length=14)
	return render(request, 'random_number/index.html')
