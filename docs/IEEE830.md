# Especificación de Requerimientos de Software (IEEE 830)

## Proyecto: EstudioNet

## 1. Introducción

### 1.1 Propósito
El propósito de este documento es describir los requerimientos funcionales y no funcionales del sistema EstudioNet, una red social de tipo foro enfocada en la comunidad de estudiantes de programación de todos los niveles.

### 1.2 Alcance
EstudioNet permitirá a los usuarios: crear perfiles, publicar posts, comentar, unirse a grupos de estudio y comunicarse mediante mensajes privados.

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

### 2.3 Características de los usuarios
- Principiantes
- Intermedios
- Avanzados

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

### 3.2 No funcionales
- **RNF1**: Accesible desde navegadores modernos
- **RNF2**: Almacenamiento seguro de contraseñas
- **RNF3**: Respuesta < 2 segundos
- **RNF4**: Interfaz intuitiva
- **RNF5**: Disponibilidad 99%

## 4. Modelos del sistema

### 4.1 Diagrama de clases (conceptual)
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

### 4.2 Modelo Entidad-Relación (MER)

**Entidades y atributos:**
- **Usuario** (`idUsuario` PK, nombre, email, contraseña, nivelConocimiento)
- **Post** (`idPost` PK, titulo, contenido, fechaCreacion, `idUsuario` FK)
- **Comentario** (`idComentario` PK, contenido, fecha, `idUsuario` FK, `idPost` FK)
- **GrupoEstudio** (`idGrupo` PK, nombre, descripcion)
- **Usuario_GrupoEstudio** (`idUsuario` FK, `idGrupo` FK) - PK compuesta

## 5. Requerimientos de interfaz

- Interfaz web amigable
- Formularios de registro/login
- Perfiles editables

## 6. Otras consideraciones

- Posibilidad de implementar gamificación
- Futuras integraciones con APIs externas (ej: GitHub)