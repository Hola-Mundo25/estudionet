from interfaz import bienvenida
from manage_user import gestionar_usuario
from db import inicializar_db

def main():
    inicializar_db()

    while True:
        opcion = bienvenida()

        if opcion == "1":
            print("\n🔐 Accediste como ADMINISTRADOR\n")
            gestionar_usuario("admin")
        elif opcion == "2":
            print("\n👤 Accediste como CLIENTE\n")
            gestionar_usuario("cliente")
        elif opcion == "3":
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.\n")

if __name__ == "__main__":
    main()