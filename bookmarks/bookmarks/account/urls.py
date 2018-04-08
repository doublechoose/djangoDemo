from django.urls import path, re_path
from . import views
from django.contrib.auth.views import login, logout, logout_then_login, \
    password_change, password_change_done, password_reset, password_reset_done, \
    password_reset_confirm, password_reset_complete

urlpatterns = [
    # path('login/', views.user_login, name='login'),

    path('', views.dashboard, name='dashboard'),

    path('register/', views.register, name='register'),

    path('edit/', views.edit, name='edit'),

    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('logout_then_login/', logout_then_login, name='logout_then_login'),
    path('password-change/', password_change, name='password_change'),
    path('password-change/done/', password_change_done, name='password_change_done'),
    path('password-reset', password_reset, name='password_reset'),
    path('password-reset/done/', password_reset_done, name='password_reset_done'),
    re_path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', password_reset_confirm,
            name='password_reset_confirm'),
    path('password-reset/complete/', password_reset_complete, name='password_reset_complete'),

    path('users/follow/', views.user_follow, name='user_follow'),

    path('users/', views.user_list, name='user_list'),
    re_path(r'^users/(?P<username>[-\w]+)/$',
            views.user_detail,
            name='user_detail'),

]

# app_name = 'login'
