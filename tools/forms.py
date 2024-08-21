from django import forms
    
class Array_limits(forms.Form):
    upper_limit = forms.IntegerField()
    lower_limit = forms.IntegerField(required = False)
    n = forms.IntegerField(required = False)
    
class Fags_search(forms.Form):
    fag = forms.CharField(max_length=20)
    
class Fags_add(forms.Form):
    fag = forms.CharField(max_length=100)
    price = forms.IntegerField()
    switch = forms.BooleanField(required=False)