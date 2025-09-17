from db import insert_user, get_user_by_username, get_all_users
from validators import validate_user

def register_user(username, email, age):
    is_valid, msg = validate_user(username, email, age)
    if not is_valid:
        return False, msg

    existing = get_user_by_username(username)
    if existing:
        return False, "⚠️ El usuario ya existe"

    insert_user(username, email, age)
    return True, "🎉 Usuario registrado con éxito"

def list_users():
    return get_all_users()
