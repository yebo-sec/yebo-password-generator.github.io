import random


def generate_password(long=12):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    random.seed()
    password = ''.join(random.choice(characters) for _ in range(long))
    return password


print(generate_password(16))  # Generar una contraseña de 16 caracteres
