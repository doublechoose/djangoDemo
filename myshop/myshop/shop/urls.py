from django.urls import path, re_path

from . import views

# re_path(r'^detail/(?P<id>[-\d]+)/(?P<slug>[-\w]+)/$', views.image_detail,
#             name='image_detail'),
urlpatterns = [
    path('', views.product_list, name='product_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$',
            views.product_list, name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
            views.product_detail, name='product_detail'),

]

app_name = 'shop'
