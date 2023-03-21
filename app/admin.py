from django.contrib import admin

from app.models import Pets, StatusOf, Category, TypeOf, OrderOf, OrderStatus

# Register your models here.

admin.site.register(Pets)
admin.site.register(StatusOf)
admin.site.register(Category)
admin.site.register(TypeOf)
admin.site.register(OrderOf)
admin.site.register(OrderStatus)
