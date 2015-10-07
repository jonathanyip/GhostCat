from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='Homepage', permanent=True)),
    url(r'^logout/', views.userLogout, name='Logout'),
    url(r'^login/', views.userLogin, name='Login'),
    url(r'^post/', views.userPost, name='Post'),
    url(r'^follow/(?P<userpk>[0-9]+)', views.userFollow, name='Follow'),
    url(r'^unfollow/(?P<userpk>[0-9]+)', views.userUnfollow, name='Unfollow'),
]