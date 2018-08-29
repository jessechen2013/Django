from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
	response = "Hello, I am your first request!"
	return HttpResponse(response)

def new(request):
	response = "Hello, new"
	return HttpResponse(response)

def create(request):
	response = "Create"
	return HttpResponse(response)

def show(request, number):
	response = number
	return HttpResponse("show: " + response)

def edit(request, number):
	response = "Edit: " + number
	return HttpResponse(response)

def delete(request, number):
	response = "Delete: " + number
	return HttpResponse(response)