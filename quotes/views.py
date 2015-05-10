# Created: 05/02/2015   Modified: 05/09/2015

# Author: Vipul Borikar

from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from . import forms
from models import Quote


def index(request):

    login
    # Get the quotes from the database
    quote_list = Quote.objects.values_list('quote_text', flat=True)
    form = forms.QuoteForm()
    return render(request,"practice/index.html",{"form":form,
                                                 "quote_list":quote_list})