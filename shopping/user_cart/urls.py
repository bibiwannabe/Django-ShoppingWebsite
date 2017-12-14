from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^add(\d+)_(\d+)/$', views.add),
]