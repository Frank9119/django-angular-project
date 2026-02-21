from django.contrib import admin
from .models import *



# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('primary_key', 'title', 'description', 'salary', 'created_at', 'is_active')
    search_fields = ('title', 'description')

    

