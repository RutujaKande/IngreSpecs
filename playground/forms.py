from django import forms

class MyForm(forms.Form):
     field1 = forms.CharField(max_length=100)
     field2 = forms.EmailField()
     message = forms.CharField(widget=forms.Textarea)