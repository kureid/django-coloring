from django.urls import path
from . import views

app_name = 'webtop'

urlpatterns = [
    path('', views.index, name='index'),
]
