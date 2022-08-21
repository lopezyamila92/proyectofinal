from django.contrib import admin
from .models import User_profile

# Register your models here.

@admin.register(User_profile)
class User_profileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'description', 'image', 'website']
