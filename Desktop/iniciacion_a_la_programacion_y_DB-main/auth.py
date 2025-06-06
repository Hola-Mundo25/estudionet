from db import cursor
from usuario import Cliente, Administrador
from menu import menu_cliente, menu_admin
from utils import email_existente

def login_cliente():
    intentos = 0

    while True:
        print("🔓 Login Cliente")
        email = input("Email: ").strip()
        password = input("Contraseña: ").strip()

        cursor.execute("SELECT nombre, email, password FROM clientes WHERE email = ? AND password = ?", (email, password))
        resultado = cursor.fetchone()

        if resultado:
            nombre, email, _ = resultado
            cliente = Cliente(nombre, email, password)
            print(f"\n✅ Bienvenido, {cliente.nombre} (Cliente)\n")
            menu_cliente(cliente)
            break  # salir del bucle después de login exitoso
        else:
            intentos += 1
            print("❌ Email o contraseña incorrectos.\n")

            if intentos >= 2:
                crear = input("¿Desea crear una cuenta? (s/n): ").strip().lower()
                if crear == 's':
                    crear_cliente()
                    break
                elif crear == 'n':
                    print("🔁 Volviendo al menú principal...\n")
                    break

                
def login_admin():
    intentos = 0

    while True:
        print("🔓 Login Administrador")
        email = input("Email: ").strip()
        password = input("Contraseña: ").strip()

        cursor.execute("SELECT nombre, email, password FROM administradores WHERE email = ? AND password = ?", (email, password))
        resultado = cursor.fetchone()

        if resultado:
            nombre, email, _ = resultado
            admin = Administrador(nombre, email, password)
            print(f"\n✅ Bienvenido, {admin.nombre} (Administrador)\n")
            menu_admin(admin)
            break
        else:
            intentos += 1
            print("❌ Email o contraseña incorrectos.\n")

            if intentos >= 2:
                crear = input("¿Desea crear una cuenta de administrador? (s/n): ").strip().lower()
                if crear == 's':
                    crear_admin()
                    break
                elif crear == 'n':
                    print("🔁 Volviendo al menú principal...\n")
                    break


def validar_contraseña(password):
    if len(password) < 6:
        print("❌ La contraseña debe tener al menos 6 caracteres.")
        return False
    if not any(c.isalpha() for c in password) or not any(c.isdigit() for c in password):
        print("❌ La contraseña debe contener letras y números.")
        return False
    return True


def crear_admin():
    print("🔐 Creando Administrador...")
    nombre = input("Nombre: ")
    email = input("Email: ")

    if email_existente(email, "administradores"):
        print(f"❌ Ya existe un administrador con el email '{email}'")
        return

    while True:
        password = input("Contraseña (mínimo 6 caracteres, letras y números): ")
        if validar_contraseña(password):
            break

    admin = Administrador(nombre, email, password)
    admin.guardar()
    print("✅ Administrador guardado.\n")
    admin.mostrar_info()
    login_admin()


def crear_cliente():
    print("👤 Creando Cliente...")
    nombre = input("Nombre: ")
    email = input("Email: ")

    if email_existente(email, "clientes"):
        print(f"❌ Ya existe un cliente con el email '{email}'")
        return

    while True:
        password = input("Contraseña (mínimo 6 caracteres, letras y números): ")
        if validar_contraseña(password):
            break

    cliente = Cliente(nombre, email, password)
    cliente.guardar()
    print("✅ Cliente guardado.\n")
    cliente.mostrar_info()
    login_cliente()