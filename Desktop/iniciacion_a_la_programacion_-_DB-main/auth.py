from db import cursor
from usuario import Cliente, Administrador
from menu import menu_cliente, menu_admin
from interfaz import bienvenida

def login_cliente():
    print("🔓 Login Cliente")
    email = input("Email: ").strip()
    password = input("Contraseña: ").strip()

    cursor.execute("SELECT nombre, email, password FROM clientes WHERE email = ? AND password = ?", (email, password))
    resultado = cursor.fetchone()

    if resultado:
        nombre, email, _ = resultado
        cliente = Cliente(nombre, email, password)
        print(f"\n✅ Bienvenido, {cliente.nombre} (Cliente)\n")
        menu_cliente(cliente)  # <--- LLAMADA AL MENÚ
    else:
        print("❌ Email o contraseña incorrectos.\n")
        bienvenida()


def login_admin():
    print("🔓 Login Administrador")
    email = input("Email: ").strip()
    password = input("Contraseña: ").strip()

    cursor.execute("SELECT nombre, email, password FROM administradores WHERE email = ? AND password = ?", (email, password))
    resultado = cursor.fetchone()

    if resultado:
        nombre, email, _ = resultado
        admin = Administrador(nombre, email, password)
        print(f"\n✅ Bienvenido, {admin.nombre} (Administrador)\n")
        menu_admin(admin)  # <--- LLAMADA AL MENÚ
    else:
        print("❌ Email o contraseña incorrectos.\n")
        bienvenida()