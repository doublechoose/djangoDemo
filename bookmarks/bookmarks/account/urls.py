from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),

]

# app_name = 'login'
