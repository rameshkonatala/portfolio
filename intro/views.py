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