from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='Homepage', permanent=True)),
    url(r'^following/', views.following, name='Following'),
    url(r'^link/(?P<postLinkPk>[0-9]+)', views.postLink, name='PostLink'),
]