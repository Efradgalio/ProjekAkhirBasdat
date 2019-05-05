from django.conf.urls import url
from .views import TokoListView, TokoDetailView, TokoCreateView
from . import views

# app_name = 'customer'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/', TokoListView.as_view(), name='list'),
    url(r'^toko/(?P<pk>\d+)$', TokoDetailView.as_view(), name='toko-detail'),
    url(r'^toko/new', TokoCreateView.as_view(), name='toko-create'),

]
