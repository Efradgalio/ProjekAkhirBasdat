from django.contrib import admin

# Register your models here.

from .models import TokoModel
from .models import BarangModel
from .models import OrderModel
admin.site.register(OrderModel)
admin.site.register(TokoModel)
admin.site.register(BarangModel)
