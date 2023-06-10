from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(CartItem)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'phonenumber', 'is_staff', 'is_superuser', 'is_active','is_anonymous')
admin.site.register(User, UsersAdmin)


