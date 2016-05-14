from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.Form):
    username = forms.CharField(label='Choose a username', max_length=30)
    password = forms.CharField(label='Choose a password', widget=forms.PasswordInput())
    password_confirmation = forms.CharField(label='Confirm the password',
            widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("That username is already taken. Try another.")
        return username

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')
        if password and password_confirmation:
            if password != password_confirmation:
                raise forms.ValidationError("Your passwords do not match")
