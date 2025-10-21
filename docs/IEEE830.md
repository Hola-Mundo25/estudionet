# DOCUMENTO DE REQUISITOS DEL SOFTWARE (IEEE 830)

## EstudioNet - Plataforma de Cursos Online

Versión: 2.0  
Fecha: Octubre 2025  
Equipo: Ivo Konstantinow, Lisandro Cisterna, Pilar Molina, Fernando Cazon  
Materias: Proyecto Integrador I + Desarrollo Web Fullstack

----------

## 1. INTRODUCCIÓN

### 1.1 ¿Qué es este documento?

Este documento explica el propósito de este documento es especificar los requisitos funcionales y no funcionales del sistema EstudioNet, detallando las funcionalidades del backend, frontend y base de datos, según el estándar IEEE 830.

### 1.2 ¿Qué hace EstudioNet?

EstudioNet es una página web donde:

-   Las personas pueden ver cursos disponibles    
-   Pueden inscribirse en los cursos que les interesen
-   Los administradores pueden agregar, editar o eliminar cursos
-   Se controla quién está inscrito en qué curso
    
Ejemplo: Es como Udemy o Coursera, pero más simple.

### 1.3 Palabras importantes que vamos a usar

| **Palabra** | **Qué significa** |

| Usuario | Persona que usa la página para ver e inscribirse en cursos |
| Admin | Persona que controla todo (puede agregar cursos, eliminar usuarios, etc.)
| Curso | Una clase que se ofrece en la plataforma (ej: "Python Básico") |
| Inscripción | Cuando un usuario se anota en un curso |
| Base de datos | Donde se guarda toda la información (usuarios, cursos, etc.) |

----------

## 2. DESCRIPCIÓN GENERAL

### 2.1 ¿Cómo se ve el sistema?

┌─────────────────┐

│ Usuario en la │

│ Consola │

└────────┬────────┘

│

▼

┌─────────────────┐

│ Python (app) │ ← El programa que ve el usuario

└────────┬────────┘

│

▼

┌─────────────────┐

│ Controladores │ ← La lógica que procesa todo

└────────┬────────┘

│

▼

┌─────────────────┐

│ Base de Datos │ ← Donde se guarda todo

│ (MySQL) │

└─────────────────┘

  

### 2.2 ¿Qué puede hacer?

**Si eres un usuario normal:**

1.  Registrarte con usuario y contraseña
2.  Iniciar sesión    
3.  Ver todos los cursos disponibles    
4.  Inscribirte en un curso    
5.  Ver en qué cursos estás inscrito    
6.  Cambiar tu información (email, nombre, contraseña)    

**Si eres administrador:**

1.  Todo lo de arriba +    
2.  Crear cursos nuevos    
3.  Editar cursos existentes    
4.  Eliminar cursos    
5.  Ver todos los usuarios    
6.  Cambiar el rol de usuarios (convertir usuario en admin)    
7.  Eliminar usuarios
    

### 2.3 ¿Quién usa el sistema?

**Usuario Regular (Estudiante):**

-   Quiere aprender cosas nuevas    
-   Busca cursos que le interesen    
-   Se inscribe en cursos    
-   No necesita saber mucho de computadoras    

**Administrador:**

-   Controla la plataforma    
-   Agrega los cursos  
-   Gestiona los usuarios 
-   Necesita saber un poco más de computadoras
    

----------

## 3. LO QUE EL SISTEMA TIENE QUE HACER

  

## Requisitos específicos

----------


 ## 3.1 Requisitos Funcionales
-   RF1 : Registro e inicio de sesión   
-   RF2 : Crear, editar y eliminar publicaciones.   
-   RF3 : Comentar publicaciones   
-   RF4 : Crear y administrar grupos de estudio    
-   RF5 : Unirse a grupos    
-   RF6 : Enviar mensajes privados    
-   RF7 : Mostrar perfil con nivel de conocimiento    
-   RF8 : Clasificar publicaciones por categorías    
-   RF9 : Publicar cursos (instructores)   
-   RF10 : Comprar cursos (estudiantes)    
-   RF11 : Gestionar carrito de compras    
-   RF12 : Sistema de reseñas y calificaciones    
-   RF13 : Filtrado de cursos por categoría/nivel    
-   RF14 : Perfiles de instructores verificados




  
 ## 3.1 Requisitos No Funcionales
-   RNF1: Accesible desde navegadores modernos.  
-   RNF2: Almacenamiento seguro de contraseñas (bcrypt).    
-   RNF3: Respuesta del sistema menor a 2 segundos.    
-   RNF4: Interfaz intuitiva y responsive.    
-   RNF5: Disponibilidad 99%.    
-   RNF6: Transacciones seguras (SSL/TLS).    
-   RNF7: Integración con pasarela de pagos.    
-   RNF8: Escalabilidad para contenido multimedia.
    


  ### Sistema de Mensajeria
-   RF15 : Enviar mensajes privados entre usuarios    
-   RF16 : Ver historial de conversaciones    
-   RF17 : Notificaciones de mensajes no leídos    
-   RF18 : Eliminar conversaciones    
-   RF19 : Bloquear usuarios
    

 ## 3.2 Registro de Usuario

**¿Qué hace?**  
Permite que alguien nuevo cree una cuenta.

**¿Qué necesita el usuario ingresar?**

-   Nombre de usuario (ej: "juan123")
-   Email (ej: "juan@gmail.com")    
-   Contraseña (ej: "miPassword123")    
-   Nombre completo (ej: "Juan Pérez")
    

**¿Qué hace el sistema?**

1.  Verifica que el nombre de usuario no exista    
2.  Verifica que el email no esté usado    
3.  Guarda la contraseña de forma segura (la encripta)   
4.  Crea el usuario en la base de datos    
5.  Le dice al usuario "¡Registro exitoso!"
    

**¿Qué puede salir mal?**

-   El nombre de usuario ya existe → Muestra error    
-   El email ya existe → Muestra error    
-   La contraseña es muy corta → Muestra error
    

----------

### 3.3 Iniciar Sesión

**¿Qué hace?**  
Permite que alguien entre al sistema con su cuenta.

**¿Qué necesita el usuario ingresar?**

-   Nombre de usuario    
-   Contraseña
    

**¿Qué hace el sistema?**

1.  Busca si existe ese usuario    
2.  Verifica que la contraseña sea correcta    
3.  Si todo está bien, lo deja entrar    
4.  Lo lleva al menú correcto (admin o usuario)
    

**¿Qué puede salir mal?**

-   Usuario no existe → Muestra error    
-   Contraseña incorrecta → Muestra error
    

----------

### 3.4 Ver Cursos Disponibles

**¿Qué hace?**  
Muestra todos los cursos que existen en la plataforma.

**¿Qué muestra?**

-   Título del curso (ej: "Python para Principiantes")    
-   Descripción (de qué trata el curso)    
-   Precio (ej: $15.000)    
-   Duración (ej: 180 minutos)   
-   Nivel (básico, intermedio o avanzado)    
-   Instructor (quién da el curso)    
-   Categoría (ej: Programación, Diseño, etc.)
    

**Ejemplo de lo que ve el usuario:**

📚 CURSOS DISPONIBLES


🆔 ID: 1
* 📖 Título: Introducción a Python
* 💰 Precio: $15,000.00
* ⏱️ Duración: 180 minutos
* 📊 Nivel: Básico
* 👨‍🏫 Instructor: Juan Pérez
* 🏷️ Categoría: Programación

  

----------

### 3.5 Inscribirse en un Curso

**¿Qué hace?**  
Permite que un usuario se anote en un curso.

**¿Qué necesita?**

-   Usuario debe estar logueado    
-   ID del curso al que se quiere inscribir
    

**¿Qué hace el sistema?**

1.  Verifica que el curso existe    
2.  Verifica que el usuario NO esté ya inscrito    
3.  Crea la inscripción en la base de datos    
4.  Le dice al usuario "¡Inscripción exitosa!"
    

**¿Qué puede salir mal?**

-   El curso no existe → Muestra error    
-   Ya está inscrito en ese curso → Muestra error
    

----------

### 3.6 Ver Mis Cursos

**¿Qué hace?**  
Muestra los cursos en los que el usuario está inscrito.

**¿Qué muestra?**

-   Nombre del curso   
-   Instructor    
-   Precio    
-   Estado de inscripción (activo, completado, cancelado)    
-   Estado de pago (pendiente, pagado, reembolsado)    
-   Fecha en que se inscribió
    

----------

### 3.7 Crear Curso (Solo Admin)

**¿Qué hace?**  
Permite que un admin agregue un curso nuevo.

**¿Qué necesita ingresar?**

-   Título del curso   
-   Descripción 
-   Precio (número mayor a 0)    
-   Duración en minutos (número mayor a 0)    
-   Nivel (básico, intermedio o avanzado)    
-   Instructor    
-   Categoría
    

**¿Qué hace el sistema?**

1.  Valida que todos los datos estén correctos   
2.  Guarda el curso en la base de datos    
3.  Le dice al admin "Curso creado exitosamente"
    

----------

### 3.8 Editar Curso (Solo Admin)

**¿Qué hace?**  
Permite modificar la información de un curso existente.

**Pasos:**

1.  Admin ve la lista de cursos con sus IDs    
2.  Elige qué curso modificar    
3.  El sistema muestra los datos actuales    
4.  Admin ingresa los nuevos datos    
5.  Sistema actualiza el curso
    

----------

### 3.9 Eliminar Curso (Solo Admin)

**¿Qué hace?**  
Borra un curso de la plataforma.

**Importante:**  
Si eliminas un curso, también se eliminan todas las inscripciones a ese curso.

----------

## 4. BASE DE DATOS

### 4.1 ¿Qué tablas tiene?

Nuestra base de datos tiene 3 tablas principales:

**Tabla 1: users (usuarios)**

- id: número único de cada usuario
- username: nombre de usuario
- email: correo electrónico
- password: contraseña (encriptada)
- full_name: nombre completo
- role: si es "admin" o "user"
- created_at: cuándo se registró

  

**Tabla 2: courses (cursos)**

- id: número único de cada curso
- title: título del curso
- description: descripción
- price: precio del curso
- duration: duración en minutos
- level: básico, intermedio o avanzado
- instructor: quién da el curso
- category: categoría
- created_at: cuándo se creó
- updated_at: última vez que se modificó

  

**Tabla 3: enrollments (inscripciones)**

- id: número único de cada inscripción
- user_id: qué usuario se inscribió
- course_id: en qué curso se inscribió
- enrollment_date: cuándo se inscribió
- status: activo, completado o cancelado
- payment_status: pendiente, pagado o reembolsado

  

### 4.2 ¿Cómo se relacionan?

Un USUARIO puede inscribirse en muchos CURSOS
Un CURSO puede tener muchos USUARIOS inscritos

  

Esto se maneja con la tabla ENROLLMENTS (inscripciones)
que conecta usuarios con cursos

### Diagrama Entidad–Relación (DER)
![DER](https://github.com/Hola-Mundo25/estudionet/blob/main/documentos/DER/DER_PRODUCT.png.jpg)



### Diagrama UML de Clases

El diagrama UML de clases muestra la estructura lógica del sistema, sus entidades principales, atributos y relaciones.
Permite visualizar cómo se vinculan las clases y qué dependencias existen entre los objetos.
![Driagrama de Clases](https://github.com/Hola-Mundo25/estudionet/blob/main/documentos/Diagrama%20de%20Clases/umlv3.png.png)





----------

## 5. REQUISITOS TÉCNICOS

### 5.1 ¿Qué necesita estar instalado?

**En la computadora:**

-   Python 3.9 o más nuevo    
-   MySQL (base de datos)    
-   Git (para descargar el proyecto)
    

**Librerías de Python:**

-   mysql-connector-python (para conectarse a la base de datos)    
-   bcrypt (para encriptar contraseñas)
    

### 5.2 Seguridad

**Contraseñas seguras:**

-   Las contraseñas NO se guardan tal cual las escribes   
-   Se encriptan con bcrypt (es como convertirlas en un código secreto)    
-   Nadie puede ver tu contraseña real, ni siquiera los admins
    

**Protección contra ataques:**

-   Validamos todos los datos que ingresan    
-   Usamos "prepared statements" para evitar SQL injection
    

### 5.3 ¿Qué tan rápido debe ser?

-   Iniciar sesión: menos de 1 segundo    
-   Ver lista de cursos: menos de 2 segundos    
-   Inscribirse: menos de 1 segundo
    

----------

## 6. INTERFAZ DE USUARIO

### 6.1 ¿Cómo se ve?

Por ahora es una aplicación de consola (todo en texto).

**Ejemplo de menú:**

🎓 ESTUDIONET - Sistema de Autenticación

 ========================================

📋 MENU PRINCIPAL

1. Registrarse
2. Iniciar sesión
3. Salir

  

Selecciona una opción: _

  

**Si eres usuario:**

👤 PANEL USUARIO - juan_perez

========================================

📚 MIS CURSOS

1. Ver mis cursos inscritos
2. Explorar cursos disponibles
3. Inscribirse a un curso

  

👤 MI CUENTA

4. Ver mis datos
5. Editar mis datos
6. Cerrar sesión

  

Selecciona una opción: _

  

### 6.2 Mensajes que ve el usuario

**Éxito:**

-   ✅ Usuario registrado exitosamente    
-   ✅ ¡Inscripción exitosa!    
-   ✅ Curso creado exitosamente
    

**Errores:**

-   ❌ Usuario ya existe   
-   ❌ Credenciales incorrectas    
-   ❌ Ya estás inscrito en este curso
    

----------

## 7. CASOS DE USO (EJEMPLOS REALES)

### Caso 1: María se registra y se inscribe en un curso

**Paso a paso:**

1.  María abre el programa    
2.  Selecciona "Registrarse" (opción 1)    
3.  Ingresa:
    -   Username: maria_gomez    
    -   Email: maria@gmail.com   
    -   Password: MiPassword123   
    -   Nombre: María Gómez
   
    

5.  Sistema crea su cuenta    
6.  María inicia sesión con sus datos    
7.  Sistema la lleva al menú de usuario    
8.  María selecciona "Explorar cursos disponibles" (opción 2)    
9.  Ve todos los cursos    
10.  Selecciona "Inscribirse a un curso" (opción 3)    
11.  Elige el curso de Python (ID: 1)    
12.  Confirma su inscripción    
13.  Sistema la inscribe y muestra: ✅ ¡Inscripción exitosa!
    

### Caso 2: Admin agrega un curso nuevo

**Paso a paso:**

1.  Admin inicia sesión con usuario "admin"    
2.  Selecciona "Agregar nuevo curso" (opción 5)    
3.  Ingresa:
    -   Título: React Avanzado    
    -   Descripción: Aprende React con hooks    
    -   Precio: 25000    
    -   Duración: 300 minutos    
    -   Nivel: avanzado    
    -   Instructor: Carlos López    
    -   Categoría: Programación
    

5.  Sistema valida los datos    
6.  Sistema crea el curso    
7.  Muestra: ✅ Curso creado exitosamente
    

----------

## 8. LIMITACIONES Y RESTRICCIONES

### 8.1 Lo que NO puede hacer (por ahora)

-   No tiene interfaz web visual (solo consola)    
-   No procesa pagos reales (solo guarda el estado)    
-   No envía emails de confirmación    
-   No tiene videos o contenido multimedia    
-   No puede tener múltiples idiomas
    

### 8.2 Reglas del sistema

**Usuarios:**

-   Username debe ser único (no puede haber dos iguales)    
-   Email debe ser único    
-   Contraseña mínimo 6 caracteres
    

**Cursos:**

-   Precio no puede ser negativo    
-   Duración debe ser mayor a 0    
-   Nivel solo puede ser: básico, intermedio o avanzado
    

**Inscripciones:**

-   Un usuario no puede inscribirse dos veces al mismo curso    
-   Si eliminas un curso, se eliminan sus inscripciones    
-   Si eliminas un usuario, se eliminan sus inscripciones
    

----------

## 9. FUTURAS MEJORAS

### Versión 2.0 (próxima)

-   [ ] Interfaz web con HTML/CSS/JavaScript
    
-   [ ] Sistema de pagos real (MercadoPago, PayPal)
    
-   [ ] Emails automáticos de confirmación
    
-   [ ] Certificados al terminar un curso
    

### Versión 3.0 (más adelante)

-   [ ] Videos de los cursos
    
-   [ ] Calificaciones y comentarios
    
-   [ ] Foro de discusión
    
-   [ ] App para celular
    

----------

## 10. CONCLUSIÓN

Este proyecto es un sistema funcional de gestión de cursos online. Aunque es simple comparado con plataformas grandes como Udemy, tiene todas las funciones básicas necesarias:

✅ Usuarios pueden registrarse e iniciar sesión  
✅ Se pueden inscribir en cursos  
✅ Admins pueden gestionar todo el contenido  
✅ Los datos se guardan de forma segura  
✅ El código está organizado y es fácil de entender

Es un buen proyecto para aprender:

-   Programación en Python    
-   Bases de datos con MySQL    
-   Arquitectura de software (MVC)    
-   Trabajo en equipo    
-   Documentación de proyectos
    

----------

## GLOSARIO TÉCNICO SIMPLE

| Término Técnico | Explicación Simple |
|-----------------|--------------------|
| Backend | La parte del programa que no ves, donde está toda la lógica |
| Frontend | La parte visual que ves en pantalla |
| Base de datos | Como un archivo Excel gigante donde se guarda todo |
| CRUD | Create (Crear), Read (Leer), Update (Actualizar), Delete (Eliminar) | 
| MVC | Forma de organizar el código en 3 partes: Modelo, Vista, Controlador |
| Hash | Convertir texto en código secreto (para contraseñas) |
| SQL | Lenguaje para hablar con la base de datos |
| ID | Número único que identifica cada cosa |
| FK (Foreign Key) | Un número que conecta dos tablas |

----------

**Documento creado por:** Equipo EstudioNet  
**Fecha:** Octubre 2025  
**Para:** Proyecto Integrador I + Desarrollo Web Fullstack
