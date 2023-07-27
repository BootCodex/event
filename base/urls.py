from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('event/<str:pk>/', views.event_page, name="event"),
    path('reg_confirmation/<str:pk>/', views.reg_confirmation, name="confirm"),
    
]
