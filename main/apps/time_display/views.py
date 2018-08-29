from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime
def index(request):
	context = {
	"time": strftime("%Y-%m-%d %H:%M %p", localtime())
	}
	return render(request,'time_display/index.html', context)
