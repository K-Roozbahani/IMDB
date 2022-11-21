from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_join', 'is_active', 'is_staff']
    list_filter = ['is_active', 'is_staff']
