from django.urls import path

from . import views

app_name = 'customer'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('list/', views.list, name='list'),
    path('login/', views.login, name='login'),
]
