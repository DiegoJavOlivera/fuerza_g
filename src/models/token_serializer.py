
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
from flask import flash

class TokenSerializer:
    def __init__(self, secret_key, salt):
        self.serializer = URLSafeTimedSerializer(secret_key)
        self.salt = salt

    def generate(self, data):
        return self.serializer.dumps(data, salt=self.salt)

    def deserialize(self, token, max_age=3600):
        try:
            return self.serializer.loads(token, max_age=max_age, salt=self.salt)
        except SignatureExpired:
            flash("El enlace ha expirado. Solicite uno nuevo.")
        except BadSignature:
            flash("El enlace es inválido. Verifique la URL.")
        except Exception as e:
            flash(f"Ocurrió un error al validar el enlace: {e}")
        return None
