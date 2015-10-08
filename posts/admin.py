from django.contrib import admin
from .models import Post

# Add Post so we can edit it in the admin page
admin.site.register(Post)