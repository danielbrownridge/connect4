from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SignupForm

class IndexView(View):
    template = 'connect4/index.html'
    context = {
        'appname': 'Connect4',
        'signup_text': 'Sign-up for an account',
        'games_text': 'Play!',
    }
    def get(self, request):
        return render(request, self.template, self.context)

class SignupView(View):
    template = 'connect4/signup.html'
    context = {
        'signup_heading_text': 'Sign-up to play Connect4',
        'input_label_submit': 'Sign up',
        'cancel_text': 'cancel',
    }
    def get(self, request):
        self.context['signup_form'] = SignupForm()
        return render(request, self.template, self.context)
    def post(self, request):
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            username = signup_form.cleaned_data['username']
            password = signup_form.cleaned_data['password']
            user = User.objects.create_user(username, password=password)
            return HttpResponseRedirect(reverse('connect4:login'))
        self.context['signup_form'] = signup_form
        return render(request, self.template, self.context)

class GamesView(LoginRequiredMixin, View):
    login_url = 'connect4:login'
    template = 'connect4/games.html'
    context = {
        'games_heading_text': 'Play Connect 4',
    }
    def get(self, request):
        return render(request, self.template, self.context)
