from django.urls import path
from .views import home
from jokes import views

urlpatterns = [
    path('', views.home, name='home'),
]
