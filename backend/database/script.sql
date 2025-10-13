CREATE DATABASE IF NOT EXISTS estudionet_db; 
USE estudionet_db;

-- TABLA DE USUARIOS --
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    full_name VARCHAR(100),
    role ENUM('admin','user') DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

-- TABLA DE CURSOS --
CREATE TABLE IF NOT EXISTS courses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    price DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    duration INT NOT NULL COMMENT 'Duración en minutos',
    level ENUM('basico', 'intermedio', 'avanzado') NOT NULL,
    instructor VARCHAR(100) NOT NULL,
    category VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Insertar usuario admin (password: admin123) --
INSERT INTO users (username, email, password, full_name, role)
VALUES ('admin', 'admin@estudionet.com', '$2b$12$AJ29A7ZJZm33Th/eFjnvheTAkKGtoDHKkIyIoSKsSfIpjl3ZWzfFe', 'Administrador Principal', 'admin');

-- Insertar cursos de ejemplo --
INSERT INTO courses (title, description, price, duration, level, instructor, category) VALUES
('Introducción a Python', 'Aprende los fundamentos de Python desde cero. Incluye variables, estructuras de control, funciones y más.', 15000.00, 180, 'basico', 'Juan Pérez', 'Programación'),
('JavaScript Avanzado', 'Domina conceptos avanzados de JavaScript: closures, promesas, async/await y patrones de diseño.', 20000.00, 240, 'avanzado', 'María González', 'Programación'),
('Diseño Web con HTML y CSS', 'Crea sitios web responsivos y atractivos usando HTML5 y CSS3 moderno.', 12000.00, 150, 'basico', 'Carlos Rodríguez', 'Diseño Web'),
('React para Principiantes', 'Construye aplicaciones web modernas con React. Aprende componentes, hooks y estado.', 18000.00, 200, 'intermedio', 'Ana Martínez', 'Programación'),
('Marketing Digital', 'Estrategias de marketing digital, SEO, SEM y redes sociales para hacer crecer tu negocio.', 16000.00, 160, 'intermedio', 'Luis Fernández', 'Marketing'),
('Base de Datos con MySQL', 'Aprende a diseñar, crear y gestionar bases de datos relacionales con MySQL.', 14000.00, 170, 'intermedio', 'Laura Sánchez', 'Bases de Datos');