from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return render(request,'survey/index.html')

def process(request):
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']
	return redirect('/result')

def view_result(request):
	context = {
				'name': request.session['name'],
				'location': request.session['location'],
				'language': request.session['language'],
				'comment': request.session['comment'],
    }
	return render(request, 'survey/result.html', context)
