create database if not exists estudionet_db; 
use estudionet_db;

create table users (
	id int primary key auto_increment,
    username varchar(50) unique not null,
    email varchar(100) unique not null,
    password varchar(255) not null,
    full_name varchar(100),
    role enum('admin','user') default 'user',
    created_at timestamp default 
current_timestamp 
);

-- insertar usuario admin (password: admin123) --
insert into users (username, email, password, full_name, role)
values ('admin', 'admin@estudionet.com', '$2b$12$AJ29A7ZJZm33Th/eFjnvheTAkKGtoDHKkIyIoSKsSfIpjl3ZWzfFe', 'Administrador Principal', 'admin');