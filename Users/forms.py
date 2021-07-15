from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.forms import Form
from .models import UserSymptomFormModel
from Users import models


class UserSignUpForm(UserCreationForm):


    username = forms.CharField(
                    max_length=30,
                    label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Name',
                                                  'id': 'input-text'})
                )

    password1 = forms.CharField(
                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                  'id': 'input-text'}),
                label=''
            )
    password2 = forms.CharField(

            widget=forms.PasswordInput(attrs={'placeholder': 'ConfirmPassword',
                                              'id': 'input-text'}),
            label=''
            )

    class Meta:
        model = User
        fields = ['username', 'password1']

class UserLogInForm(forms.Form):
    username = forms.CharField(
                    max_length=30,
                    label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Name',
                                                  'id': 'input-text'})
                )
    password = forms.CharField(
                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                  'id': 'input-text'}),
                label=''
            )

class UserSymptomForm(forms.ModelForm):

    username = forms.CharField(
                    max_length=30,
                    label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Name',
                                                  'id': 'input-text'})
        )
    email = forms.EmailField(
                    max_length=30,
                    label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                  'id': 'input-text'})

        )
    phone_no = forms.IntegerField(
                                label='',
                                 widget=forms.TextInput(attrs={'placeholder': 'Phone',
                                                               'id': 'input-text'})
    )
    address = forms.CharField(
                               max_length=200,
                               label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Address',
                                                             'id': 'input-text'})
    )


    class Meta:
        model = UserSymptomFormModel
        fields = '__all__'
