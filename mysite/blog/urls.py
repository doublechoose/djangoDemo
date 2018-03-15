from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<str:post>', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/',views.post_share,app_name='post_share')

]

app_name = 'blog'
