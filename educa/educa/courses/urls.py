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

    re_path(r'^subject/(?P<subject>[\w-]+)/$', views.CourseListView.as_view(),
            name='course_list_subject'),

    re_path(r'^(?P<slug>[\w-]+)/$', views.CourseDetailView.as_view(),
            name='course_detail'),

    re_path(r'^(?P<pk>\d+)/module/$', views.CourseModuleUpdateView.as_view(),
            name='course_module_update'),

    re_path(r'^module/(?P<module_id>\d+)/content/(?P<model_name>\w+)/create/$', views.ContentCreateUpdateView.as_view(),
            name='module_content_create'),

    re_path(r'^module/(?P<module_id>\d+)/content/(?P<model_name>\w+)/(?P<id>\d+)/$',
            views.ContentCreateUpdateView.as_view(),
            name='module_content_update'),

    re_path(r'^content/(?P<id>\d+)/delete/$',
            views.ContentDeleteView.as_view(),
            name='module_content_delete'),
    re_path(r'^module/(?P<module_id>\d+)/$',
            views.ModuleContentListView.as_view(),
            name='module_content_list'),


]
