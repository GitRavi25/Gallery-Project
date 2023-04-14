from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.forms import User
from django import forms

from . models import ImageModel

class RegisterForm(UserCreationForm):

    password1=forms.CharField(label='Enter Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))

    password2=forms.CharField(label='Enter Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))



    class Meta:

        model=User
        fields=['first_name','last_name','username','email']

        labels={
            'first_name':'Enter First Name',
            'last_name':'Enter Last Name',
            'username':'Enter Username',
            'email':'Enter Email'
        }

        widgets={

            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'UserName'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'})

        }


class LoginForm(AuthenticationForm):

    username=forms.CharField(label='Enter UserName',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))

    password=forms.CharField(label='Enter Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))

    class Meta:

        model= User
        fields=['username','password']


class ImageForm(forms.ModelForm):

    class Meta:

        model=ImageModel

        fields=['title','cat','image','desc']


        labels={
            'title':'Enter Image Title',
            'cat':'Enter Image Category',
            'image':'Upload Image',
            'desc':'Enter Image Description'
        }


        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'cat':forms.Select(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'})
        }