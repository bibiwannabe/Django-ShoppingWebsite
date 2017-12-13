from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^detail/$', views.cart_order),
]