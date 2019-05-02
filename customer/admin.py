from django.contrib import admin

# Register your models here.

from .models import TokoModel
from .models import BarangModel
admin.site.register(TokoModel)
admin.site.register(BarangModel)
