from django.shortcuts import render,get_object_or_404
from forms import ClientForm
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from .models import Client

# Create your views here.


def index(request):
	if request.POST:
		form=ClientForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/')
	else:
		form=ClientForm()
	
	return render(request,'intro/index.html',{'form':form})	

def design01(request):
	return render(request,'intro/sub/design/01.html',{})

def design02(request):
	return render(request,'intro/sub/design/02.html',{})

def design03(request):
	return render(request,'intro/sub/design/03.html',{})

def design04(request):
	return render(request,'intro/sub/design/04.html',{})

def design05(request):
	return render(request,'intro/sub/design/05.html',{})

def design06(request):
	return render(request,'intro/sub/design/06.html',{})

def design07(request):
	return render(request,'intro/sub/design/07.html',{})

def design08(request):
	return render(request,'intro/sub/design/08.html',{})

def design09(request):
	return render(request,'intro/sub/design/09.html',{})

def design10(request):
	return render(request,'intro/sub/design/10.html',{})

def development01(request):
	return render(request,'intro/sub/development/01.html',{})