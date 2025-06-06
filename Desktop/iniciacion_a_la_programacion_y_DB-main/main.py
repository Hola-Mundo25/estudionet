from manage_user import gestionar_usuario

def main():

    while True:
        print("\n📋 Menú Principal")
        print("────────────────────────────")
        print("1️⃣  Ingresar como Cliente")
        print("2️⃣  Ingresar como Administrador")
        print("3️⃣  Salir del sistema")
        print("────────────────────────────")

        opcion = input("👉 Seleccione una opción (1-3): ").strip()

        if opcion == "1":
            print("\n🧑‍💼 Accediendo como Cliente...\n")
            gestionar_usuario("cliente")
        elif opcion == "2":
            print("\n🛠️  Accediendo como Administrador...\n")
            gestionar_usuario("admin")
        elif opcion == "3":
            print("\n👋 ¡Hasta pronto! Gracias por usar el sistema.\n")
            break
        else:
            print("\n⚠️  Opción no válida. Por favor, intente nuevamente.\n")

if __name__ == "__main__":
    main()
