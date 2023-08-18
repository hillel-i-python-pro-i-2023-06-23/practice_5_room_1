from cryptography.hazmat.primitives import serialization
from django.db import models

from apps.encrypting.services.encrypt_and_decrypt import (
    generate_rsa_pair_key,
    encrypt_with_public_key,
    #    decrypt_with_private_key,
)


class PrivateKey(models.Model):
    private_key = models.BinaryField()


@staticmethod
def generate_and_save_private_key():
    private_key, _ = generate_rsa_pair_key()
    return PrivateKey.objects.create(
        private_key=private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )


class EncryptedMessage(models.Model):
    topic = models.CharField(max_length=255)
    encrypted_message = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)
    private_key = models.OneToOneField(
        PrivateKey, on_delete=models.CASCADE, related_name="encrypted_message", null=True
    )

    def __str__(self) -> str:
        return f"Зашифроване повідомлення {self.topic} створене {self.created_at}"

    __repr__ = __str__


def create_encrypted_message(topic, message):
    private_key_obj = PrivateKey.generate_and_save_private_key()
    encrypted_message = encrypt_with_public_key(private_key_obj.private_key, message)

    return EncryptedMessage.objects.create(
        topic=topic, encrypted_message=encrypted_message, private_key=private_key_obj
    )


#    def decrypt(self):
#        private_key = serialization.load_pem_private_key(self.private_key.private_key, password=None)

# decrypted_message = decrypt_with_private_key(private_key, self.encrypted_message)
