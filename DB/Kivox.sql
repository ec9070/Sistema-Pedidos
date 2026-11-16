CREATE DATABASE IF NOT EXISTS kivox;

USE kivox;

CREATE TABLE kivox.Usuarios(
ID_Usuario int not null auto_increment,
Correo varchar(256) not null,
Contraseña varchar(256) not null,
Nombre varchar(100) not null,
Telefono varchar(20),
Foto longblob,
Rol enum('Administrador','Vendedor','Bodega','Taller','Asistente'),
primary key(ID_Usuario));

-- create user 'usuario'@'%' identified by 'contra';
-- grant all privileges on kivox.* to 'usuario';
-- flush privileges;