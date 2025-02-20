if not exists create database flask;

CREATE TABLE if not exists user_lado_oscuro (
    id_user INTEGER PRIMARY KEY AUTOINCREMENT,
    email varchar(40) NOT NULL,
    password varchar(255) NOT NULL,
    name varchar(20) NOT NULL,
    lastName varchar(20) NOT NULL,
    gender enum('Masculino', 'Femenino','Otro') NOT NULL,
    payment_service_status tyniint(1) DEFAULT 0,
    admin tyniint(1) DEFAULT 0,
    receive_email_notifications tyniint(1) DEFAULT 0,
    user_active tyniint(1) DEFAULT 0,
    INDEX(email)
);

CREATE table if not exists lado_oscuro_usuarios_temporales(
    id_user smallint PRIMARY KEY AUTOINCREMENT,
    email varchar(60) NOT NULL,
    password varchar(255) NOT NULL,
    name varchar(20) NOT NULL,
    lastName varchar(20) NOT NULL,
    gender enum('Masculino', 'Femenino','Otro') NOT NULL,
    confirm tyniint(1) DEFAULT 0,
    receive_email_notifications tyniint(1) DEFAULT 0,
    INDEX(email)
);

CREATE TABLE if not exists news (
    id_news INTEGER PRIMARY KEY AUTOINCREMENT,
    title varchar(255) NOT NULL,
    content varchar TEXT NOT NULL,
    date datetime ,
    image varchar(255) ,
);

CREATE TABLE if not exists subject_utn(
    id_subject int PRIMARY KEY AUTOINCREMENT,
    title varchar(255) NOT NULL,
    imagen_exam varchar(255),
    date datetime
    content TEXT,
    subject enum('Matematica_ingreso','Base_de_datos', 'Matematica_1', 'Estadistica', 'Ingles_1', ' Programacion_1', ' Programacion_2')
);