from db import cursor, conn

def cargar_productos():

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL
        )
    """)
    conn.commit()
    print("✅ Tabla 'productos' creada o ya existía.\n")

    print("📦 Carga de productos")
    
    while True:
        nombre = input("Nombre del producto (o 'fin' para terminar): ").strip()
        if nombre.lower() == "fin":
            break

        try:
            precio = float(input("Precio: $"))
            if precio < 0:
                print("❌ El precio no puede ser negativo.")
                continue
        except ValueError:
            print("❌ Precio inválido. Ingresá un número.")
            continue


        cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", (nombre, precio))
        conn.commit()
        print(f"✅ Producto '{nombre}' cargado.\n")


def ver_tabla_productos():
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    if productos:
        print("\n📋 Lista de productos:")
        for prod in productos:
            print(f"ID: {prod[0]}, Nombre: {prod[1]}, Precio: ${prod[2]:.2f}")
        print("")
        return True
    else:
        print("\n⚠️ No hay productos para mostrar.\n")
        return False  
    

def modificar_producto():
    print("✏️ Modificar Producto")
    
    ver_tabla_productos() 
    
    try:
        id_producto = int(input("Ingrese el ID del producto a modificar: "))
    except ValueError:
        print("❌ ID inválido. Debe ser un número entero.")
        return


    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()
    if not producto:
        print(f"❌ No existe un producto con ID {id_producto}.")
        return

    print(f"Producto seleccionado: ID {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}")

    nuevo_nombre = input("Nuevo nombre (Enter para no cambiar): ").strip()
    if nuevo_nombre == "":
        nuevo_nombre = producto[1] 
    
    try:
        nuevo_precio_input = input("Nuevo precio (Enter para no cambiar): ").strip()
        if nuevo_precio_input == "":
            nuevo_precio = producto[2]  
        else:
            nuevo_precio = float(nuevo_precio_input)
            if nuevo_precio < 0:
                print("❌ El precio no puede ser negativo.")
                return
    except ValueError:
        print("❌ Precio inválido. Debe ser un número.")
        return


    cursor.execute(
        "UPDATE productos SET nombre = ?, precio = ? WHERE id = ?",
        (nuevo_nombre, nuevo_precio, id_producto)
    )
    conn.commit()
    print(f"✅ Producto ID {id_producto} modificado correctamente.")
    


def borrar_producto():
    print("🗑️ Borrar Producto")

    if not ver_tabla_productos():  
        return

    try:
        id_producto = int(input("Ingrese el ID del producto a borrar: "))
    except ValueError:
        print("❌ ID inválido. Debe ser un número entero.")
        return

    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()
    if not producto:
        print(f"❌ No existe un producto con ID {id_producto}.")
        return

    print(f"Producto seleccionado: ID {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}")
    confirmar = input("¿Está seguro que desea borrar este producto? (s/n): ").strip().lower()
    if confirmar == 's':
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conn.commit()
        print(f"✅ Producto ID {id_producto} borrado correctamente.")
    else:
        print("❌ Borrado cancelado.")
