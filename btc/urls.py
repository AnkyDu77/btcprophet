from django.urls import path

from . import views

appname = 'btc'
urlpatterns = [
    path('', views.index, name='index'),
]
