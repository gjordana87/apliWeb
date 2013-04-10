from django import forms
from django.contrib.auth.models import User


#class ContactForm(forms.Form):
#	Email = forms.EmailField(widget=forms.TextInput())
#	Titulo = forms.CharField(widget=forms.TextInput())
#	Text = forms.CharField(widget=forms.TextInput())

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))