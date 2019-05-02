from django.conf.urls import url
from .views import TokoListView
from . import views

# app_name = 'customer'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/', views.create, name='create'),
    url(r'^list/', TokoListView.as_view(), name='list'),

]
