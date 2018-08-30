# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return render(request, 'store/index.html')

def process(request):
	request.session['quantity'] = request.POST['quantity']
	request.session['product_id'] = request.POST['product_id']
	return redirect('/result')
# Create your views here.

def result(request):
	context = {
		'quantity' : request.session['quantity'],
		'product_id' : request.session['product_id']
	}
	return render(request, 'store/result.html', context)
