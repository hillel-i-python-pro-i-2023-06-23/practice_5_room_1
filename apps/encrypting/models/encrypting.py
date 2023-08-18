from django.db import models


class PrivateKey(models.Model):
    user_id = models.PositiveIntegerField(unique=True)
    private_key = models.BinaryField()

    def __str__(self):
        return f"Private Key for User {self.user_id}"


class EncryptedMessage(models.Model):
    topic = models.CharField(max_length=255)
    encrypted_message = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)
    private_key = models.OneToOneField(PrivateKey, on_delete=models.CASCADE)

    def __str__(self):
        return f"Encrypted Message: {self.topic}"
