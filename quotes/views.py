# Created: 05/02/2015   Modified: 05/016/2015

# Author: Vipul Borikar

from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from . import forms
from models import Quote
from django.http import HttpResponse


# First Page
def index(request):
    '''
    Processes first page
    '''

    # If user has submitted the quote
    if request.method == "POST":
        form = forms.QuoteForm(request.POST)
        if form.is_valid():
            # Save the quote into the database
            quote = form.cleaned_data['quote']
            quote_db = Quote(quote_text=quote)
            quote_db.save()

    # Get the quotes from the database
    quote_list = Quote.objects.values_list('quote_text', flat=True)[::-1]
    form = forms.QuoteForm()
    return render(request,"quotes/index.html",{"form":form,
                                                 "quote_list":quote_list})


# Displays login page
def login(request):
    '''
    Handles authentication of existing user
    '''
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user == None:
            return HttpResponse('Your username does not exist')

        return HttpResponseRedirect('/quotes/')

    form = AuthenticationForm()
    return render(request,"quotes/login.html",{'form':form})


def user_creation(request):
    '''
    Displays User Creation form and prosses it if submitted
    '''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form.save()

    form = UserCreationForm()

    return render(request,"quotes/signup.html",{'form':form})