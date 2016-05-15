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

    def __str__(self):
        time_player1 = str(self.created.strftime('%Y-%m-%d %H:%M:%S')) + \
                ' - ' + self.player1.username
        if self.player2:
            return time_player1 + ' vs ' + self.player2.username
        else:
            return time_player1 + ' - waiting for opponent'
