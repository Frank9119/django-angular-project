from django.contrib import admin
from .models import *



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('primary_key', 'user', 'phone', 'addres', 'created_at', 'is_active')
    search_fields = ('phone', 'addres')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_active')
    search_fields = ('role', 'email')