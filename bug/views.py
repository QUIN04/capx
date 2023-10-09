from django.shortcuts import render
from django.template import loader
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse


# from django.http import Http404
# from django.http import HttpResponse
# from .models import Bug

# Bug = get_bug_model()

#creating views 
def index(request):
	return render(request, 'bug/index.html')

def loginform(request):
	return render(request, 'bug/index.html')

def detail(request):
	return render(request, 'bug/detail.html')

def list(request):
	return render(request, 'bug/list.html')