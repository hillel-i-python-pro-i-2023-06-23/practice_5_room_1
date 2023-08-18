# Generated by Django 4.2.4 on 2023-08-18 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PrivateKey",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("user_id", models.PositiveIntegerField(unique=True)),
                ("private_key", models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name="EncryptedMessage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("topic", models.CharField(max_length=255)),
                ("encrypted_message", models.BinaryField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "private_key",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="encrypting.privatekey"),
                ),
            ],
        ),
    ]