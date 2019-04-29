
from django.contrib import admin
from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^customer/', include('customer.urls', namespace='customer')),
    url(r'^$', views.index, name='index'),
]
