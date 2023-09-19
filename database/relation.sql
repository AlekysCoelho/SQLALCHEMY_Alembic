CREATE DATABASE IF NOT EXISTS enterprise;

USE enterprise;

CREATE TABLE IF NOT EXISTS teachers (
	id_teacher INTEGER NOT NULL AUTO_INCREMENT, 
	name VARCHAR(50) NOT NULL, 
	fullname VARCHAR, 
	cpf VARCHAR(11) NOT NULL, 
	PRIMARY KEY (id_teacher)
);

CREATE TABLE courses (
	id_course INTEGER NOT NULL AUTO_INCREMENT, 
	name VARCHAR(50) NOT NULL, 
	codigo VARCHAR(3) NOT NULL, 
	id_teacher INTEGER NOT NULL, 
	PRIMARY KEY (id_course), 
	FOREIGN KEY(id_teacher) REFERENCES teachers (id_teacher)
);

CREATE TABLE students (
	id_student INTEGER NOT NULL AUTO_INCREMENT, 
	name VARCHAR(50) NOT NULL, 
	fullname VARCHAR, 
	cpf VARCHAR(11) NOT NULL, 
	PRIMARY KEY (id_student)
);

CREATE TABLE registrations (
	id_student INTEGER NOT NULL, 
	id_course INTEGER NOT NULL, 
	PRIMARY KEY (id_student, id_course), 
	FOREIGN KEY(id_course) REFERENCES courses (id_course), 
	FOREIGN KEY(id_student) REFERENCES students (id_student)
);
