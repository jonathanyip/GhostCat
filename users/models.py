from django.db import models
from django.contrib.auth.models import User

# UserProfile model - Adds attributes to a User
# In this case, it is the followers.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	following = models.ManyToManyField(User, related_name='following')
	
	def __str__(self):
		return self.user.__str__()