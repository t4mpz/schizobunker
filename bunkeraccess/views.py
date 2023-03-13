from django.shortcuts import render
from django.http      import HttpResponse
from django.template  import loader

# Create your views here

def index(request):
	"""
	Simple index view just for the login etc
	"""
	return render(request, 'index.html')
