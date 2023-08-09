from django.contrib import admin

# Register your models here.
from .models import Drinks, userinfo


admin.site.register(Drinks)
admin.site.register(userinfo)