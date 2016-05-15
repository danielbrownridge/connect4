from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player_1')
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player_2',
            blank=True, null=True)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='winner',
            blank=True, null=True)
    finished = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
