from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import MessageForm, Subscription

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    

    class Meta:
        model = User
        fields = ( "username","password1", "email", "password2", )


class Message(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = MessageForm
        fields = ('first_name', 'email', 'message')


class SubsForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Subscription
        fields = (
            'email',
        )
