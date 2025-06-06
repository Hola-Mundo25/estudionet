from auth import crear_admin, crear_cliente, login_admin, login_cliente


def gestionar_usuario(tipo):
    while True:
        respuesta = input(f"¿Ya tienes usuario {tipo}? (s/n): ").strip().lower()
        if respuesta == "s":
            if tipo == "admin":
                login_admin()
            else:
                login_cliente()
            break
        elif respuesta == "n":
            if tipo == "admin":
                crear_admin()
            else:
                crear_cliente()
            break
        else:
            print("Por favor, responde 's' o 'n'.")