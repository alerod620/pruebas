CREATE DATABASE redes2;
USE redes2;

CREATE TABLE reporte (
id INT PRIMARY KEY auto_increment,
carnet VARCHAR(10) NOT NULL,
nombre VARCHAR(200) NOT NULL,
curso VARCHAR(200) NOT NULL,
mensaje VARCHAR(500) NOT NULL,
servidor VARCHAR(10) NOT NULL
);

CREATE TABLE asistencia (
id INT PRIMARY KEY auto_increment,
carnet VARCHAR(10) NOT NULL,
nombre VARCHAR(200) NOT NULL,
evento VARCHAR(200) NOT NULL,
id_evento INT NOT NULL,
imagen MEDIUMTEXT NOT NULL,
fecha_hora DATE NOT NULL,
servidor VARCHAR(10) NOT NULL
);