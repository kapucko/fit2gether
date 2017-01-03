from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username",
                               max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password",
                               max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username',
                               max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))

    email = forms.EmailField(label='Email',
                             required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email'}))

    password1 = forms.CharField(label="Password",
                              max_length=30,
                              widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                              'name': 'password1'})) #render_value=False
    password2 = forms.CharField(label="Repeat Password",
                              max_length=30,
                              widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                              'name': 'password2'}))

    def clean_username(self): # check if username dos not exist before
        try:
            User.objects.get(username=self.cleaned_data['username']) #get user from user model
        except User.DoesNotExist :
            return self.cleaned_data['username']

        raise forms.ValidationError("this user exist already")


    def clean(self): # check if password 1 and password2 match each other
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:#check if both pass first validation
            if self.cleaned_data['password1'] != self.cleaned_data['password2']: # check if they match each other
                raise forms.ValidationError("passwords dont match each other")

        return self.cleaned_data


    def save(self): # create new user
        new_user=User.objects.create_user(username=self.cleaned_data['username'],
                                          password=self.cleaned_data['password1'],
                                          email=self.cleaned_data['email'])

        return new_user