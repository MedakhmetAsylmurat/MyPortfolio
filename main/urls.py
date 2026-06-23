from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('section/<str:slug>/', views.section, name='section'),
]
