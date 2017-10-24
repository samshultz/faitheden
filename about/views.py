from django.shortcuts import render

def About(request):
	context={}
	return render(request, 'about/about.html', context)