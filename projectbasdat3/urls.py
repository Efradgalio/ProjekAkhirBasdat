
from django.contrib import admin
from django.conf.urls import url, include
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import BarangListView, BarangDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^customer/', include('customer.urls', namespace='customer')),
    url(r'^$', BarangListView.as_view(), name='index'),
    url(r'^register/', user_views.register, name='register'),
    url(r'^profile/', user_views.profile, name='profile'),
    url(r'^login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url(r'^barang/(?P<pk>\d+)$', BarangDetailView.as_view(), name='barang-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
