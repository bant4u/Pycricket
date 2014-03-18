from django.db import models


# Create your models here.
class Game(models.Model):
	game_name=models.CharField(max_length=40)
	game_type=models.CharField(max_length=20)
	game_players=models.IntegerField()
	game_start_date=models.DateTimeField()
	game_comment=models.TextField()
	

