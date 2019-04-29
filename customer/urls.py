from django.conf.urls import url
from . import views

# app_name = 'customer'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/', views.create, name='create'),
    url(r'^list/', views.list, name='list'),
    url(r'^login/', views.login, name='login'),
]
