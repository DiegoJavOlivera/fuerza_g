CREATE DATABASE IF NOT EXISTS flask;
USE flask;

CREATE TABLE IF NOT EXISTS user_lado_oscuro (
    id_user INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(40) NOT NULL,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(20) NOT NULL,
    lastName VARCHAR(20) NOT NULL,
    gender ENUM('Masculino', 'Femenino', 'Otro') NOT NULL,
    payment_service_status TINYINT(1) DEFAULT 0,
    admin TINYINT(1) DEFAULT 0,
    receive_email_notifications TINYINT(1) DEFAULT 0,
    user_active TINYINT(1) DEFAULT 0,
    INDEX(email)
);

CREATE TABLE IF NOT EXISTS lado_oscuro_usuarios_temporales (
    id_user SMALLINT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(60) NOT NULL,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(20) NOT NULL,
    lastName VARCHAR(20) NOT NULL,
    gender ENUM('Masculino', 'Femenino', 'Otro') NOT NULL,
    confirm TINYINT(1) DEFAULT 0,
    receive_email_notifications TINYINT(1) DEFAULT 0,
    INDEX(email)
);

CREATE TABLE IF NOT EXISTS news (
    id_news INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    date DATETIME,
    image VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS subject_utn (
    id_subject INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    imagen_exam VARCHAR(255),
    date DATETIME,
    content TEXT,
    subject ENUM('Matematica_ingreso', 'Base_de_datos', 'Matematica_1', 'Estadistica', 'Ingles_1', 'Programacion_1', 'Programacion_2')
);
