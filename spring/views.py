 
from django.shortcuts import render_to_response
#from django import template



def home(request):
        return render_to_response('home.html', locals())
