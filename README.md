# 🎓 EstudioNet - Plataforma de Venta de Cursos Online

## 📋 Tabla de Contenidos
- [Descripción](#-descripción)
- [Características](#-características)
- [Tecnologías](#-tecnologías)
- [Arquitectura](#-arquitectura)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Base de Datos](#-base-de-datos)
- [API Endpoints](#-api-endpoints)
- [Pruebas](#-pruebas)
- [Contribución](#-contribución)
- [Equipo](#-equipo)
- [Licencia](#-licencia)

---

## 📖 Descripción
**EstudioNet** es una plataforma educativa que permite a los usuarios explorar, inscribirse y gestionar cursos online.  
El sistema cuenta con un **panel administrativo completo** para la gestión de usuarios, cursos e inscripciones.

---

## ✨ Funcionalidades Principales

### 👨‍🎓 Para Usuarios:
- 🔍 **Explorar** el catálogo completo de cursos disponibles  
- 📝 **Inscribirse** en cursos de interés  
- 📚 **Visualizar** los cursos inscritos junto con el estado de pago  
- 👤 **Gestionar su perfil personal** (editar datos, cambiar contraseña)

### 🧑‍💼 Para Administradores:
- 👥 **Gestión completa de usuarios** (crear, leer, actualizar y eliminar)  
- 📚 **Gestión completa de cursos** (CRUD)  
- 🔄 **Cambio de roles** entre usuarios y administradores  
- 📊 **Visualización de inscripciones** con información detallada

## ✨ Características

- ✅ **Autenticación segura** con contraseñas hasheadas (`bcrypt`)  
- ✅ **Control de acceso basado en roles** (Admin / User)  
- ✅ **Gestión de inscripciones** con estados: *activo*, *completado*, *cancelado*  
- ✅ **Control de pagos** con estados: *pendiente*, *pagado*, *reembolsado*  
- ✅ **Prevención de inscripciones duplicadas**  
- ✅ **Validación de datos** en todos los formularios  
- ✅ **Interfaz CLI intuitiva** con emojis y menús claros  
- ✅ **Base de datos relacional** con integridad referencial  
- ✅ **Arquitectura MVC** escalable y mantenible  

---

## 🛠️ Tecnologías

### 🧩 Backend
- **Python 3.9+** → Lenguaje de programación principal  
- **MySQL 5.7+** → Base de datos relacional  
- **mysql-connector-python** → Driver para conectar Python con MySQL  
- **bcrypt** → Encriptación de contraseñas  

### ⚙️ Herramientas de Desarrollo
- **XAMPP / WAMP** → Servidor local para MySQL  
- **Git** → Control de versiones  
- **Visual Studio Code (VS Code)** → Editor de código  

---

## 🏗️ Arquitectura

El proyecto sigue el patrón **MVC (Model-View-Controller)** con una separación clara de responsabilidades:

estudionet/
│
├── backend/
│ ├── app.py # Vista (CLI Interface)
│ ├── database.py # Capa de acceso a datos
│ │
│ ├── models/ # Modelos de datos
│ │ ├── user.py
│ │ ├── course.py
│ │ └── enrollment.py
│ │
│ ├── controllers/ # Lógica de negocio
│ │ ├── auth_controller.py
│ │ ├── user_controller.py
│ │ ├── course_controller.py
│ │ └── enrollment_controller.py
│ │
│ ├── utils/ # Utilidades
│ │ └── validators.py
│ │
│ └── requirements.txt # Dependencias Python
│
├── database/
│ └── script.sql # Script de creación de BD
│
├── docs/
│ └── IEEE830.md # Especificación de requisitos
│
└── README.md

---

## 🔄 Flujo de Datos

Usuario (CLI)
↓
app.py (Vista)
↓
Controller (Lógica de negocio)
↓
Model (Validaciones)
↓
Database (Acceso a datos)
↓
MySQL (Almacenamiento)

## 📦 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- 🐍 **Python 3.9 o superior** → [Descargar](https://www.python.org/downloads/)  
- 🗄️ **MySQL 5.7 o superior** → [Descargar](https://dev.mysql.com/downloads/)  
- 🧰 **Git** → [Descargar](https://git-scm.com/downloads)  
- ⚙️ **XAMPP (opcional, incluye MySQL)** → [Descargar](https://www.apachefriends.org/es/index.html)  

---

### ✅ Verificar Instalaciones

```bash
# Verificar Python
python --version
# Debe mostrar: Python 3.9.x o superior

# Verificar MySQL
mysql --version
# Debe mostrar: mysql  Ver x.x.x

# Verificar Git
git --version
# Debe mostrar: git version x.x.x
## 🚀 Instalación

### 1️⃣ Clonar el Repositorio

```bash
git clone https://github.com/Hola-Mundo25/estudionet.git
cd estudionet/backend
## 2️⃣ Crear Entorno Virtual (Recomendado)

### 🪟 Windows:
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
### 🐧 Linux / 🍎 Mac:
```bash
python3 -m venv venv
source venv/bin/activate
## 3️⃣ Instalar Dependencias
```bash
pip install -r requirements.txt

**Contenido de requirements.txt:**

mysql-connector-python==9.0.0

bcrypt==4.0.1

python-dotenv==1.0.0

Flask==2.3.3

Flask-CORS==4.0.0

### 4️⃣Configurar Base de Datos**

# Base de datos con XAMPP

Sigue estos pasos para configurar la base de datos usando XAMPP y phpMyAdmin.

### Opción A: Usando XAMPP

1.  Inicia el **Panel de Control de XAMPP** y arranca los módulos de **Apache** y **MySQL**.
2.  Abre **phpMyAdmin** en tu navegador web visitando la siguiente dirección: `http://localhost/phpmyadmin`.
3.  Ve a la pestaña **SQL**.
4.  Copia y pega el contenido del archivo `database/script.sql` en el cuadro de texto.
5.  Haz clic en **Continuar** para ejecutar la consulta.
## Opción B: Usando MySQL CLI

```bash
# Iniciar sesión en MySQL
mysql -u root -p

# Ejecutar el script
source database/script.sql
## 5️⃣ Verificar Instalación

```bash
# Listar bases de datos
mysql -u root -p -e "SHOW DATABASES;"

# Debe aparecer: estudionet_db
## ⚙️ Configuración

### Configurar Conexión a Base de Datos

Edita el archivo `backend/database.py`:

```python
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',      # Cambia si es necesario
    database='estudionet_db',
    user='root',           # Tu usuario MySQL
    password=''            # Tu contraseña MySQL
)
## 🌿 Variables de Entorno (Opcional)

Crea un archivo `.env` en la carpeta `backend/`:

DB_HOST=localhost
DB_DATABASE=estudionet_db
DB_USER=root
DB_PASSWORD=

## 🎮 Uso

### Iniciar la Aplicación
```bash
cd backend
python app.py
## 🔐 Credenciales por Defecto

**Administrador:**
- Usuario: `admin`
- Contraseña: `admin123`
## 👤 Flujo de Usuario Regular

### Registrarse (Opción 1)
- Username: `juan_perez`
- Email: `juan@example.com`
- Password: `mi_password`
- Nombre completo: `Juan Pérez`

1. **Iniciar Sesión (Opción 2)**
   - Username: `juan_perez`
   - Password: `mi_password`
2. **Explorar Cursos (Opción 2 en menú usuario)**
3. **Inscribirse a un Curso (Opción 3)**
4. **Ver Mis Cursos (Opción 1)**

---

## 🛠️ Flujo de Administrador

1. **Iniciar Sesión como admin**
2. **Gestionar Cursos**
   - Opción 4: Listar cursos
   - Opción 5: Agregar curso
   - Opción 6: Modificar curso
   - Opción 7: Eliminar curso
3. **Gestionar Usuarios**
   - Opción 1: Listar usuarios
   - Opción 2: Cambiar rol
   - Opción 3: Eliminar usuario
## 📁 Estructura del Proyecto

estudionet/
│
├── backend/
│ │
│ ├── app.py # Aplicación principal (CLI)
│ ├── database.py # Gestión de conexión a MySQL
│ ├── requirements.txt # Dependencias Python
│ │
│ ├── models/ # Modelos de datos
│ │ ├── user.py # Modelo Usuario
│ │ ├── course.py # Modelo Curso
│ │ └── enrollment.py # Modelo Inscripción
│ │
│ ├── controllers/ # Controladores (lógica de negocio)
│ │ ├── auth_controller.py # Autenticación
│ │ ├── user_controller.py # Gestión de usuarios
│ │ ├── course_controller.py # Gestión de cursos
│ │ └── enrollment_controller.py # Gestión de inscripciones
│ │
│ └── utils/ # Utilidades
│ └── security.py # Validaciones reutilizables
│
├── database/
│ ├── script.sql # Script completo de BD
│ └── DER.png # Diagrama Entidad-Relación
│
├── docs/
│ ├── IEEE830.md # Especificación de requisitos
│ └── SETUP.md # Guía de instalación detallada
│
├── frontend/ # Frontend Web
│ ├── index.html
│ ├── about.html
│ ├── contacto.html
│ ├── cursos.html
│ ├── favicon.ico
│ ├── favicon2.ico
│ ├── login.html
│ ├── register.html
│ ├── styles.css
│ └── validation.js
├── Imagenes/
│ ├── as.jpeg
│ ├── htmlcss.png
│ ├── Imagen1.webp
│ ├── Imagen2.png
│ ├── Imagen3.jpg
│ ├── Imagen4.png
│ ├── js.png
│ ├── node.png
│ ├── python.png
│ └── react.jpg
└── README.md # Este archivo
## 🛠️ Scripts Útiles

```sql
-- Ver todos los usuarios
SELECT * FROM users;

-- Ver todos los cursos
SELECT * FROM courses;

-- Ver inscripciones con nombres de usuarios y cursos
SELECT 
    e.id,
    u.username,
    c.title,
    e.status,
    e.payment_status
FROM enrollments e
JOIN users u ON e.user_id = u.id
JOIN courses c ON e.course_id = c.id;

-- Contar inscripciones por curso
SELECT 
    c.title,
    COUNT(e.id) as total_inscripciones
FROM courses c
LEFT JOIN enrollments e ON c.id = e.course_id
GROUP BY c.id;
## 🧪 Pruebas

### Ejecutar Pruebas Manuales

```bash
# Prueba de registro
python app.py
# Seleccionar opción 1 y completar formulario

# Prueba de inicio de sesión
# Seleccionar opción 2 con credenciales correctas

# Prueba de inscripción
# Login como usuario regular
# Seleccionar opción 3 en menú usuario
## 📋 Casos de Prueba

| ID      | Caso de Prueba                          | Resultado Esperado           |
|---------|----------------------------------------|-----------------------------|
| CP-001  | Registrar usuario con datos válidos     | Usuario creado exitosamente |
| CP-002  | Registrar usuario con username duplicado| Error: Username ya existe   |
| CP-003  | Login con credenciales correctas        | Acceso al sistema           |
| CP-004  | Login con credenciales incorrectas      | Error de autenticación      |
| CP-005  | Crear curso (admin) con datos válidos   | Curso creado                |
| CP-006  | Inscribirse a curso disponible          | Inscripción exitosa         |
| CP-007  | Inscribirse a curso ya inscrito         | Error: Ya inscrito          |

## 👥 Equipo

### Desarrolladores
- **Ivo Konstantinow** - Full Stack Developer - `@konstantinowivo`  
- **Fernando Cazon** - Frontend Developer - `@fercazondev`  
- **Pilar Molina** - Project Manager & QA  `@lindainfinita10` 
- **Lisandro Cisterna** - Backend Developer - `@lichyyyy`
## 🎯 Roles y Responsabilidades

| Integrante   | Rol        | Responsabilidades                        |
|--------------|------------|------------------------------------------|
| Ivo          | Tech Lead  | Arquitectura, Backend, Integración       |
| Lisandro C.  | Frontend   | Interfaz de usuario, UX                   |
| Pilar        | PM/QA      | Scrum Master, Testing, Documentación     |
| Lisandro     | Backend    | API, Base de datos, Lógica de negocio    |
## 📞 Contacto

- **Proyecto:** EstudioNet  
- **Universidad:** Instituto Superior Politécnico de Córdoba  
- **Materias:** Proyecto Integrador I + Desarrollo Web Fullstack  
- **Repositorio:** [https://github.com/Hola-Mundo25/estudionet](https://github.com/Hola-Mundo25/estudionet)  
- **Issues:** [https://github.com/Hola-Mundo25/estudionet/issues](https://github.com/Hola-Mundo25/estudionet/issues)  

---

## 📄 Licencia
MIT License

Copyright (c) 2025 EstudioNet Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
Este proyecto está bajo la **Licencia MIT** - ver el archivo `LICENSE` para más detalles.

---

## 🙏 Agradecimientos

- Profesores de Proyecto Integrador I y Desarrollo Web Fullstack  
- Compañeros por el apoyo y colaboración  
- Comunidad de Python por las excelentes librerías  
- MySQL por el robusto sistema de base de datos  

---

## 📚 Recursos Adicionales

### Documentación
- Especificación IEEE 830  
- Guía de Instalación Detallada  
- Documentación de API  

### Tecnologías Utilizadas
- Python Official Docs  
- Flask Documentation  
- MySQL Reference  
- Bcrypt Guide  

### Tutoriales Relacionados
- MySQL Tutorial  
- Git Tutorial  

---

## 🔮 Roadmap

### Versión 1.0 (Actual)
- [x] Sistema de autenticación  
- [x] Gestión de usuarios (CRUD)  
- [x] Gestión de cursos (CRUD)  
- [x] Sistema de inscripciones  
- [x] Control de estados y pagos  
- [x] Interfaz CLI  

### Versión 2.0 (Próxima)
- [x] API REST completa con Flask  
- [x] Frontend web con HTML/CSS/JS  
- [x] Sistema de pagos integrado  
- [x] Envío de emails de confirmación  
- [x] Certificados de finalización  
- [x] Panel de estadísticas  

### Versión 3.0 (Futuro)
- [ ] Sistema de reviews y calificaciones  
- [ ] Contenido multimedia (videos)  
- [ ] Foro de discusión por curso  
- [ ] Notificaciones push  
- [ ] App móvil (React Native)  
- [ ] Integración con plataformas de pago  

---

## 📊 Estadísticas del Proyecto

- **Líneas de código:** ~2,500  
- **Archivos Python:** 15  
- **Tablas de BD:** 3  
- **Commits:** 50+  
- **Duración desarrollo:** 2 meses  

---

## ⭐ Si te gustó el proyecto, dale una estrella ⭐

Hecho con ❤️ por el equipo EstudioNet

