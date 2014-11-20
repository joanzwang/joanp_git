from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from django.template.loader import get_template
#from django.template import Context

#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')
    
def contact(request):
    return render(request, 'contact.html')
