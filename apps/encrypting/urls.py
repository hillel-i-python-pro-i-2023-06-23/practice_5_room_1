from django.urls import path

from . import views

app_name = "encrypting"

urlpatterns = [
    path('encrypt/', views.encrypt_message, name='encrypt'),
    path('decrypt/', views.decrypt_message, name='decrypt'),
    path('encrypt/encrypted/', views.encrypt_message, name='encrypt'),
    path('decrypt/decrypted/', views.decrypt_message, name='decrypt'),
]
