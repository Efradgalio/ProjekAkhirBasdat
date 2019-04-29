
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', include('customer.urls', namespace='customer')),
    path('', views.index, name='index'),
]
