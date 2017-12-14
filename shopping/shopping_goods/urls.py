from django.conf.urls import url
from . import views
from user_cart import views as uviews

urlpatterns=[
    url(r'^$',views.index),
    url(r'^list(\d+)_(\d+)_(\d+)/$',views.list),
    url(r'^(\d+)/$',views.detail),
    url(r'^cart/$', uviews.cart),
]