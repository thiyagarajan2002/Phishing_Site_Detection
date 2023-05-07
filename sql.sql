CREATE DATABASE Phising_site;
USE Phising_site;

CREATE TABLE User_details(User_id INT AUTO_INCREMENT PRIMARY KEY,Name VARCHAR(30),Phone_number VARCHAR(15),Email VARCHAR(40),Password VARCHAR(50));
CREATE TABLE Admin_details(User_id INT AUTO_INCREMENT PRIMARY KEY,Name VARCHAR(30),Phone_number VARCHAR(15),Email VARCHAR(40),Password VARCHAR(50));

CREATE TABLE Phising_result(User_id VARCHAR(5),Url varchar(10000),Result varchar(4));


