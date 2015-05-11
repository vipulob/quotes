# Created: 05/02/2015   Modified: 05/09/2015

# Author: Vipul Borikar

from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from . import forms
from models import Quote


# First Page
def index(request):

    # Get the quotes from the database
    quote_list = Quote.objects.values_list('quote_text', flat=True)
    form = forms.QuoteForm()
    return render(request,"quotes/index.html",{"form":form,
                                                 "quote_list":quote_list})


# Displays login page
def login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        print("In POST1")
        return HttpResponseRedirect('/thanks/')

    form = AuthenticationForm()
    return render(request,"quotes/login.html",{'form':form})