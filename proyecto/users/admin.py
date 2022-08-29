from django.contrib import admin
from .models import User_profile



@admin.register(User_profile)
class User_profileAdmin(admin.ModelAdmin):
    list_display = ['name','last_name', 'email', 'description', 'image', 'website']