from django.shortcuts import render
from django.views.generic import ListView

from .forms import EncryptForm
from .models import EncryptedMessage
from .services.encrypt_and_decrypt import (
    generate_rsa_pair_key,
    encrypt_with_public_key,
    load_private_key,
    decrypt_with_private_key,
)


def encrypt_message(request):
    if request.method == "POST":
        form = EncryptForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data["topic"]
            message = form.cleaned_data["message"]

            private_key, public_key = generate_rsa_pair_key()
            encrypted_message = encrypt_with_public_key(public_key, message)

            encrypted_message_obj = EncryptedMessage.objects.create(
                topic=topic,
                encrypted_message=encrypted_message,
            )

            encrypted_display_message = str(encrypted_message_obj)
            return render(request, "encrypting/encrypted.html", {"encrypted_message": encrypted_display_message})
    else:
        form = EncryptForm()

    return render(request, "encrypting/encrypt.html", {"form": form})


def decrypt_message(request):
    if request.method == "POST":
        encrypted_message = request.POST["encrypted_message"]
        loaded_private_key = load_private_key("private_key.pem")
        decrypted_message = decrypt_with_private_key(loaded_private_key, encrypted_message)

        return render(request, "encrypting/decrypted.html", {"decrypted_message": decrypted_message})

    return render(request, "encrypting/decrypt.html")


class MessageListView(ListView):
    model = EncryptedMessage
