from . import views
from django.urls import path
from .feeds import LatestPostsFeed

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tag/<str:tag_slug>/', views.post_list, name='post_list_by_tag'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<str:post>', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'),

]

app_name = 'blog'
