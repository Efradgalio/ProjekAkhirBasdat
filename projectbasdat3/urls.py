
from django.contrib import admin
from django.conf.urls import url, include
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^customer/', include('customer.urls', namespace='customer')),
    url(r'^$', views.index, name='index'),
    url(r'^register/', user_views.register, name='register'),
    url(r'^profile/', user_views.profile, name='profile'),
    url(r'^login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
