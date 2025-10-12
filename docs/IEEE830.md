# Especificación de Requerimientos de Software (IEEE 830)

## Proyecto: EstudioNet

## 1. Introducción

### 1.1 Propósito
El propósito de este documento es describir los requerimientos funcionales y no funcionales del sistema EstudioNet, una red social de tipo foro enfocada en la comunidad de estudiantes de programación de todos los niveles.

### 1.2 Alcance
EstudioNet permitirá a los usuarios: crear perfiles, publicar posts, comentar, unirse a grupos de estudio y comunicarse mediante mensajes privados, publicar cursos, comprar cursos y gestionar un carrito de compras.

### 1.3 Definiciones
- **SRS**: Software Requirements Specification
- **UML**: Unified Modeling Language
- **MER**: Modelo Entidad-Relación

## 2. Descripción general

### 2.1 Perspectiva
Sistema web cliente-servidor con base de datos centralizada.

### 2.2 Funciones
- Gestión de usuarios
- Gestión de posts
- Gestión de comentarios
- Gestión de grupos de estudio
- Mensajería
- Gestión de cursos (crear, editar, eliminar)
- Carrito de compras
- Sistemas de pagos integrados
- Reseñas y valoraciones

### 2.3 Características de los usuarios
- Estudiantes (principiantes, intermedios, avanzados)
- instructores

### 2.4 Restricciones
- Uso de tecnologías web
- Seguridad de datos

### 2.5 Suposiciones
- Acceso a internet
- Uso de BD relacional

## 3. Requerimientos específicos

### 3.1 Funcionales
- **RF1**: Registro e inicio de sesión
- **RF2**: Crear, editar y eliminar posts
- **RF3**: Comentar publicaciones
- **RF4**: Crear y administrar grupos de estudio
- **RF5**: Unirse a grupos
- **RF6**: Enviar mensajes privados
- **RF7**: Mostrar perfil con nivel de conocimiento
- **RF8**: Clasificar publicaciones por categorías
- **RF9**: Publicar cursos (instructores)
- **RF10**: Comprar cursos (estudiantes)
- **RF11**: Gestionar carrito de compras
- **RF12**: Sistema de reseñas y calificaciones 
- **RF13**: Filtrado de cursos por categoría/nivel
- **RF14**: Perfiles de instructores verificados

### 3.1 No funcionales
- **RNF1**: Accesible desde navegadores modernos
- **RNF2**: Almacenamiento seguro de contraseñas
- **RNF3**: Respuesta < 2 segundos
- **RNF4**: Interfaz intuitiva
- **RNF5**: Disponibilidad 99%
- **RNF6**: Transacciones seguras (SSL/TLS)
- **RNF7**: Integración con pasarela de pagos
- **RNF8**: Escalabilidad para contenido multimedia

### 3.2 Sistema de Mensajería
- **RF15**: Enviar mensajes privados entre usuarios
- **RF16**: Ver historial de conversaciones
- **RF17**: Notificaciones de mensajes no leídos
- **RF18**: Eliminar conversaciones
- **RF19**: Bloquear usuarios



## 4. Modelos del sistema

### 4.1 Diagrama de clases (v1)

**Clases principales:**
- Usuario
- Post
- Comentario
- GrupoEstudio

**Relaciones:**
- Usuario 1..* → Post
- Usuario 1..* → Comentario
- Post 1..* → Comentario
- Usuario *..* ↔ GrupoEstudio

**Diagrama de clases (v2):**
**Clases principales:**
- Curso
- Instructor (hereda de Usuario)
- Carrito
- Compra
- Reseña

**Nueva clase:**
- Mensaje (idMensaje, contenido, fechaEnvio, leido)

**Nuevas relaciones:**
- Usuario 1..* → Mensaje (como remitente)
- Usuario 1..* → Mensaje (como destinatario)

**Relaciones:**
- Instructor 1..* → Curso
- Usuario 1 → 1 Carrito
- Usuario 1..* → Compra
- Curso 1..* → Reseña
- Usuario 1..* → Reseña


### 4.2 Modelo Entidad-Relación (MER)

**Entidades y atributos:**
- **Usuario** (`idUsuario` PK, nombre, email, contraseña, nivelConocimiento)
- **Post** (`idPost` PK, titulo, contenido, fechaCreacion, `idUsuario` FK)
- **Comentario** (`idComentario` PK, contenido, fecha, `idUsuario` FK, `idPost` FK)
- **GrupoEstudio** (`idGrupo` PK, nombre, descripcion)
- **Usuario_GrupoEstudio** (`idUsuario` FK, `idGrupo` FK) - PK compuesta
- **Curso** (`idCurso` PK, titulo, descripcion, precio, duracion, nivel, `idInstructor` FK)
- **Carrito** (`idCarrito` PK, `idUsuario` FK)
- **Carrito_Curso** (`idCarrito` FK, `idCurso` FK, cantidad)
- **Compra** (`idCompra` PK, fecha, total, `idUsuario` FK)
- **Compra_Curso** (`idCompra` FK, `idCurso` FK, precio)
- **Reseña** (`idReseña` PK, calificacion, comentario, `idUsuario` FK, `idCurso` FK)

## 5. Requerimientos de interfaz

- Interfaz web amigable
- Formularios de registro/login
- Perfiles editables
- Catálogo de cursos con filtros
- Carrito de compras visible
## 6. Otras consideraciones

- Posibilidad de implementar gamificación
- Futuras integraciones con APIs externas (ej: GitHub)
- Sistema de notificaciones por email
