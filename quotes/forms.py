# Created: 05/02/2015   Modified: 05/02/2015

# Author: Vipul Borikar

from django import forms

class QuoteForm(forms.Form):
    quote = forms.CharField(label="Enter Your Quote",widget=forms.Textarea)

