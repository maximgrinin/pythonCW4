from typing import Union
import base64
import hashlib
import hmac
from flask import current_app


def __generate_password_digest(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def generate_password_hash(password: str) -> str:
    return base64.b64encode(__generate_password_digest(password)).decode('utf-8')


def compose_passwords(password_hash: Union[str, bytes], password: str) -> bool:
    password_hash_decode = base64.b64decode(password_hash)
    password_digest = __generate_password_digest(password)
    return hmac.compare_digest(password_hash_decode, password_digest)
