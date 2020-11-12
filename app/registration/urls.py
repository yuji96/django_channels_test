from django.urls import path
from django.contrib.auth import views

from .views import home

app_name = 'registration'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('home/', home, name='home'),
]
