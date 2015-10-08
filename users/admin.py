from django.contrib import admin
from .models import UserProfile

# Add UserProfile so we can change it in the admin page
admin.site.register(UserProfile)