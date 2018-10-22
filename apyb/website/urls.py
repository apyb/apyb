from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('sobre', views.Markdown.as_view(), {'slug': 'sobre'}), 
]
