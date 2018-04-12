from django.urls import path, re_path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('courses',views.CourseViewSet)

urlpatterns = [
    path('subjects/',
         views.SubjectListView.as_view(),
         name='subject_list'),

    re_path(r'^subjects/(?P<pk>\d+)/$',
            views.SubjectDetailView.as_view(),
            name='subject_detail'),

    # re_path(r'^courses/(?P<pk>\d+)/enroll/$',
    #         views.CourseEnrollView.as_view(),
    #         name='course_enroll'),

    path('', include(router.urls)),


]

app_name = 'api'
