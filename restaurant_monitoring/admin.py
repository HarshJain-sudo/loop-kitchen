from django.contrib import admin
from .models import Store, StoreBusinessHour, StoreMenuHour

admin.site.register(Store)
admin.site.register(StoreBusinessHour)
admin.site.register(StoreMenuHour)
