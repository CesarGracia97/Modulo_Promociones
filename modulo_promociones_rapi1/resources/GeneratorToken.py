import random
import string


class GeneratorToken:
    @staticmethod
    def generate_token(length=95):
        characters = string.ascii_letters + string.digits  # Mayúsculas, minúsculas y números
        token = ''.join(random.choice(characters) for _ in range(length))
        return token

