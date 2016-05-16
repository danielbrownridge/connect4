from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .forms import SignupForm
from .models import Game

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
        active_list = Game.objects.filter(Q(player1=request.user) | Q(player2=request.user)
                ).exclude(player2=None).exclude(finished=True)
        waiting_list = Game.objects.filter(player1=request.user).filter(player2=None)
        available_list = Game.objects.exclude(player1=request.user).filter(player2=None)
        completed_list = Game.objects.filter(player1=request.user).filter(finished=True)

        self.context['active_list'] = active_list
        self.context['waiting_list'] = waiting_list
        self.context['available_list'] = available_list
        self.context['completed_list'] = completed_list
        return render(request, self.template, self.context)

class GameDataView(LoginRequiredMixin, View):
    def get(self, request, game_id):
        try:
            game = Game.objects.get(id=game_id)
            if request.user == game.player1:
                player = 0
            else:
                player = 1
            json = {
                'moves': game.moves,
                'player': player,
            }
        except Game.DoesNotExist:
            json = {}
        return JsonResponse( json )
    def post(self, request, game_id):
        try: 
            game = Game.objects.get(id=game_id)
            moves = request.POST.getlist('moves[]')
            game.moves = moves
            game.save()
            return JsonResponse( {"result":"success"} )
        except Game.DoesNotExist:
            return JsonResponse( {"result":"failure"} )


class PlayView(LoginRequiredMixin, View):
    login_url = 'connect4:login'
    template = 'connect4/play.html'
    context = {}
    def get(self, request, game_id):
        self.context['game_id'] = game_id
        return render(request, self.template, self.context)
