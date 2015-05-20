# Created: 05/02/2015   Modified: 05/20/2015

# Author: Vipul Borikar

from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from . import forms
from models import Quote
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone


# First Page
def index(request):
    '''
    Processes first page
    '''

    # Check whether the user is having session or not
    username = request.user

    # If its anonymous user.
    if str(username) == "AnonymousUser":
        username = None

    # If user has submitted the quote
    if request.method == "POST":
        # Only authenticated user can post quote. Alert if not logged in
        if username == None:
            messages.error(request, 'You should login to post the Quote')

        else:
            form = forms.QuoteForm(request.POST)
            if form.is_valid():
                # Save the quote into the database
                quote = form.cleaned_data['quote']
                author = form.cleaned_data['quote_author']
                quote_db = Quote(quote_text=quote,
                                 user_who_uploaded=str(username),
                                 submission_date=timezone.now(),
                                 quote_author=author
                                 )
                quote_db.save()

    # Get the quotes from the database
    quote_list = Quote.objects.all()[::-1]
    form = forms.QuoteForm()
    return render(request,"quotes/index.html",
                  {"form":form,"quote_list":quote_list,'username':username,
                   })


# Displays login page
def login_view(request):
    '''
    Handles authentication of existing user
    '''

    user = None
    flag = True

    if request.method == 'POST':
        form = AuthenticationForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            # login maintaines the session till user doesn't logout
            login(request, user)
            return HttpResponseRedirect("/quotes/")

        else:
            flag = False
            return render(request,"quotes/login.html",
                          {'form':form,'flag':flag})


    form = AuthenticationForm()
    return render(request,"quotes/login.html",
                  {'form':form,'flag':flag})


def logout_view(request):
    '''
    Logout any existing user has session
    '''

    logout(request)
    return HttpResponseRedirect("/quotes/")

def user_creation(request):
    '''
    Displays User Creation form and prosses it if submitted
    '''

    # If user has submitted the data
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form.save()

    form = UserCreationForm()
    return render(request,"quotes/signup.html",{'form':form})