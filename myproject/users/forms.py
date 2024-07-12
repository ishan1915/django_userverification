# users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add this line

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
