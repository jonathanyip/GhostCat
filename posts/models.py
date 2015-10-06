from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
	post_text = models.CharField(max_length=140)
	post_date = models.DateTimeField(default=timezone.now())
	post_author = models.ForeignKey(User)
	
	def __str__(self):
		return self.post_text