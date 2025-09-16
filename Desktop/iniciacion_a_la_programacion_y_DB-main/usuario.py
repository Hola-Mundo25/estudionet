from db import cursor, conn

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def guardar(self):
        raise NotImplementedError("Implementar en subclases.")

class Cliente(Usuario):
    def __init__(self, nombre, email, password):
        super().__init__(nombre, email)
        self.password = password

    def mostrar_info(self):
        print(f"Cliente -> Nombre: {self.nombre}, Email: {self.email}, Contraseña: {self.password}")

    def guardar(self):
        cursor.execute(
            "INSERT INTO clientes (nombre, email, password) VALUES (?, ?, ?)",
            (self.nombre, self.email, self.password)
        )
        conn.commit()

class Administrador(Usuario):
    def __init__(self, nombre, email, password):
        super().__init__(nombre, email)
        self.password = password

    def mostrar_info(self):
        print(f"Administrador -> Nombre: {self.nombre}, Email: {self.email}, Contraseña: {self.password}")

    def guardar(self):
        cursor.execute(
            "INSERT INTO administradores (nombre, email, password) VALUES (?, ?, ?)",
            (self.nombre, self.email, self.password)
        )
        conn.commit()
