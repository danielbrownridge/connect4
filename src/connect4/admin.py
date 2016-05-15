from django.contrib import admin

from . models import Game

class GameAdmin(admin.ModelAdmin):
    readonly_fields = ['created']

admin.site.register(Game, GameAdmin)
