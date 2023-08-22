from django.shortcuts import render
from django.views.generic import ListView

from .forms import EncryptForm, DecryptForm
from .models import EncryptedMessage, PrivateKey
from .services.encrypt_and_decrypt import (
    encrypt_with_public_key,
)


def encrypt_message(request):
    if request.method == "POST":
        form = EncryptForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data["topic"]
            message = form.cleaned_data["message"]

            private_key_obj = PrivateKey.generate_and_save_private_key()

            public_key = private_key_obj.get_private_key().public_key()
            encrypted_message = encrypt_with_public_key(public_key, message)

            encrypted_message_obj = EncryptedMessage.objects.create(
                topic=topic,
                encrypted_message=encrypted_message,
                private_key=private_key_obj,
            )

            return render(request, "encrypting/encrypted.html", {"encrypted_message": encrypted_message_obj})
    else:
        form = EncryptForm()

    return render(request, "encrypting/encrypt.html", {"form": form})


def decrypt_message(request):
    if request.method == "POST":
        form = DecryptForm(request.POST)
        if form.is_valid():
            encrypted_message_id = request.POST["encrypted_message_id"]
            try:
                encrypted_message_obj = EncryptedMessage.objects.get(id=encrypted_message_id)
                decrypted_message = encrypted_message_obj.decrypt_message()
                return render(request, "encrypting/decrypted.html", {"decrypted_message": decrypted_message})
            except EncryptedMessage.DoesNotExist:
                form.add_error("encrypted_message_id", "Повідомлення з вказаним ідентифікатором не існує")
    else:
        form = DecryptForm()

    encrypted_messages = EncryptedMessage.objects.all()
    return render(request, "encrypting/decrypt.html", {"form": form, "encrypted_messages": encrypted_messages})


class MessageListView(ListView):
    model = EncryptedMessage
