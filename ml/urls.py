from django.urls import path
from . import views

urlpatterns = [
    path('', views.listt, name='listt'),
    path('find', views.find, name='find'),
]
