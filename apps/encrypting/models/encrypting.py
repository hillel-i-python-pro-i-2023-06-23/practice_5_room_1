from cryptography.hazmat.primitives import serialization
from django.db import models

from apps.encrypting.services.encrypt_and_decrypt import (
    generate_rsa_pair_key,
    load_private_key,
    decrypt_with_private_key,
)


class PrivateKey(models.Model):
    private_key = models.BinaryField()

    def get_private_key(self):
        return load_private_key(self.private_key)

    @classmethod
    def generate_and_save_private_key(cls):
        private_key, _ = generate_rsa_pair_key()
        private_key_bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
        return cls.objects.create(private_key=private_key_bytes)


class EncryptedMessage(models.Model):
    topic = models.CharField(max_length=255)
    encrypted_message = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)
    private_key = models.OneToOneField(
        PrivateKey, on_delete=models.CASCADE, related_name="encrypted_message", null=True
    )

    def decrypt_message(self):
        private_key = self.private_key.get_private_key()
        decrypted_message = decrypt_with_private_key(private_key, self.encrypted_message)
        return decrypted_message

    def __str__(self) -> str:
        return f"Повідомлення по темі {self.topic} зашифровано"

    __repr__ = __str__
