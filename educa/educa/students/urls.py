from django.urls import path, re_path
from . import views

urlpatterns = [
    path('register',views.StudentRegistrationView.as_view(),
         name='student_registration'),
    path('enroll-course',views.StudentEnrollCourseView.as_view(),
         name='student_enroll_course'),
    path('courses',views.StudentCourseListView.as_view(),
         name='student_course_list'),
    re_path(r'^course/(?P<pk>\d+)/$',
            views.StudentCourseDetailView.as_view(),
            name='student_course_detail'),
    re_path(r'^course/(?P<pk>\d+)/(?P<module_id>\d+)$',
            views.StudentCourseDetailView.as_view(),
            name='student_course_detail_module'),


]

