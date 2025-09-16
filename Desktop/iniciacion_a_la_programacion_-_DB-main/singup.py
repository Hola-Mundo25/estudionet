from usuario import Administrador, Cliente
from auth import login_admin, login_cliente
from utils import email_existente

def crear_admin():
    print("🔐 Creando Administrador...")
    nombre = input("Nombre: ")
    email = input("Email: ")

    if email_existente(email, "administradores"):
        print(f"❌ Ya existe un administrador con el email '{email}'")
        return

    password = input("Contraseña: ")
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

    password = input("Contraseña: ")
    cliente = Cliente(nombre, email, password)
    cliente.guardar()
    print("✅ Cliente guardado.\n")
    cliente.mostrar_info()
    login_cliente()