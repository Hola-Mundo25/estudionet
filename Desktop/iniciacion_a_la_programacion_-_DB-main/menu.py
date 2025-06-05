from products import cargar_productos, ver_tabla_productos, modificar_producto, borrar_producto

def menu_admin(admin):
    opciones = {
        "1": admin.mostrar_info,
        "2": cargar_productos,
        "3": ver_tabla_productos,
        "4": modificar_producto,
        "5": borrar_producto
    }

    while True:
        print("\nMenú Administrador:")
        print("1. Ver mis datos")
        print("2. Cargar productos")
        print("3. Ver tabla de productos")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Volver al menú principal")
        opcion = input("Elige una opción: ").strip()

        if opcion == "6":
            print("🔁 Volviendo al menú principal...\n")
            return  # 👈 vuelve al bucle de main()
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("❌ Opción inválida. Intenta de nuevo.\n")

def menu_cliente(cliente):
    opciones = {
        "1": cliente.mostrar_info,
        "2": ver_tabla_productos
    }

    while True:
        print("\nMenú Cliente:")
        print("1. Ver mis datos")
        print("2. Ver tabla de productos")
        print("3. Volver al menú principal")
        opcion = input("Elige una opción: ").strip()

        if opcion == "3":
            print("🔁 Volviendo al menú principal...\n")
            return  # 👈 vuelve al bucle de main()
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("❌ Opción inválida. Intenta de nuevo.\n")
