from django.urls import path
from . import views

# url Configuration module
urlpatterns =  [
  path('hello/', views.say_hello)
]