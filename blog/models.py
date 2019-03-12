from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length = 100) #a character field of our post table 
	content = models.TextField()
	date_posted = models.DateTimeField(default =timezone.now)
	author = models.ForeignKey(User, on_delete = models.CASCADE) #if a user is deleted, delete his posts 

	def __str__(self):
		return self.title
