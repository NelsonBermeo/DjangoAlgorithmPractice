from django import forms

class TextboxForm(forms.Form):
    text = forms.CharField(label='Enter Text', max_length=100)