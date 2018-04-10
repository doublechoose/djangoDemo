from django.urls import path, re_path

from . import views

urlpatterns = [
    path('mine/', views.ManageCourseListView.as_view(),
         name='manage_course_list'),
    path('create/', views.CourseCreateView.as_view(),
         name='course_create'),
    re_path(r'^(?P<pk>\d+)/edit/$', views.CourseUpdateView.as_view(),
            name='course_edit'),

    re_path(r'^(?P<pk>\d+)/delete/$', views.CourseDeleteView.as_view(),
            name='course_delete'),

]
