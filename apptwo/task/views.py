from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse("<em>My second project</em>")

def help(request):
	
	date_dict ={'help_insert':"Hello i am from django"}
	return render(request,'apptwo/help.html',context=date_dict)