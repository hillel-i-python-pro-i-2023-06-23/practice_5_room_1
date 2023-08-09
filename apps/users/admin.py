from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "password", "created_at", "modified_at")
    list_filter = ("created_at", "modified_at")
    search_fields = ("name", "email")
