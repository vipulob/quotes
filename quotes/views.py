# Created: 05/02/2015   Modified: 05/016/2015

# Author: Vipul Borikar

from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from . import forms
from models import Quote


# First Page
def index(request):

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

    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        print("In POST1")
        return HttpResponseRedirect('/thanks/')

    form = AuthenticationForm()
    return render(request,"quotes/login.html",{'form':form})