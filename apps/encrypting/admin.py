from django.contrib import admin

from .models import EncryptedMessage


@admin.register(EncryptedMessage)
class EncryptedMessageAdmin(admin.ModelAdmin):
    list_display = ("topic", "encrypted_message", "created_at")
    list_filter = ("topic", "created_at")

