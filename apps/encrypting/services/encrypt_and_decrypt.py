from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding


def generate_rsa_pair_key():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key


def load_private_key(key_bytes):
    return serialization.load_pem_private_key(
        key_bytes,
        password=None,
    )


def save_public_key(public_key, filename):
    with open(filename, "wb") as keyfile:
        keyfile.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )


def load_public_key(filename):
    with open(filename, "rb") as keyfile:
        return serialization.load_pem_public_key(keyfile.read())


def encrypt_with_public_key(public_key, message):
    encrypted_message = public_key.encrypt(
        message.encode(),
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None),
    )
    return encrypted_message


def decrypt_with_private_key(private_key, encrypted_message):
    decrypted_message = private_key.decrypt(
        encrypted_message,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None),
    )
    return decrypted_message.decode()
