from django.urls import path, re_path
from . import views

urlpatterns = [

    path('create/', views.image_create, name='image_create'),
    path('like/', views.image_like, name='like'),
    re_path(r'^detail/(?P<id>[-\d]+)/(?P<slug>[-\w]+)/$', views.image_detail,
            name='image_detail'),

]

app_name = 'images'
