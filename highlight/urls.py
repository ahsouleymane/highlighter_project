from django.urls import path, include
from highlight import views

urlpatterns = [
    path('', views.acceuil, name='acceuil'),
]