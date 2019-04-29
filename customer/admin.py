from django.contrib import admin

# Register your models here.

from .models import LoginModel, TokoModel

admin.site.register(LoginModel)
admin.site.register(TokoModel)
