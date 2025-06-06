from db import cursor

def email_existente(email: str, tabla: str) -> bool:
    cursor.execute(f"SELECT 1 FROM {tabla} WHERE email = ?", (email,))
    return cursor.fetchone() is not None