def validate_user(username, email, age):
    """
    Valida un usuario con varias condiciones.
    Aquí hay if/else anidados → alta complejidad ciclomatica.
    """
    if not username:
        return False, "❌ El nombre de usuario es obligatorio"
    else:
        if len(username) < 3:
            return False, "⚠️ El nombre de usuario debe tener al menos 3 caracteres"
        elif len(username) > 20:
            return False, "⚠️ El nombre de usuario no puede tener más de 20 caracteres"
        else:
            if " " in username:
                return False, "🚫 El nombre de usuario no puede contener espacios"
            elif not username.isalnum():
                return False, "🚫 El nombre de usuario debe ser alfanumérico"

    if not email:
        return False, "❌ El email es obligatorio"
    else:
        if "@" not in email or "." not in email:
            return False, "⚠️ El email no es válido"

    if age is None:
        return False, "❌ La edad es obligatoria"
    else:
        if age < 0:
            return False, "🚫 La edad no puede ser negativa"
        elif age < 18:
            return False, "🔞 Debes ser mayor de edad para registrarte"
        elif age > 120:
            return False, "👴 La edad no puede ser mayor a 120"

    return True, "✅ Usuario válido"
