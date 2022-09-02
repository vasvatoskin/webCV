CREATE DATABASE IF NOT EXISTS cv_db;

USE cv_db;

CREATE TABLE IF NOT EXISTS users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30) NOT NULL,
        date_of_birth DATE,
        gender VARCHAR(20),
        marital_status VARCHAR(20)
    );

CREATE TABLE IF NOT EXISTS contact_types(
        contact_type_id INT AUTO_INCREMENT PRIMARY KEY,
        contact_type VARCHAR(30) NOT NULL
    );

CREATE TABLE IF NOT EXISTS contacts(
        contact_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        contact_type INT NOT NULL,
        value TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE,
        FOREIGN KEY (contact_type) REFERENCES contact_types (contact_type_id) ON DELETE CASCADE
    );

CREATE TABLE IF NOT EXISTS education_types (
    education_type_id INT AUTO_INCREMENT PRIMARY KEY,
    education_type VARCHAR(50) NOT NULL
    );

CREATE TABLE IF NOT EXISTS education (
    education_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    education_type INT NOT NULL,
    start_date DATE,
    end_date DATE,
    description TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE,
    FOREIGN KEY (education_type) REFERENCES education_types (education_type_id) ON DELETE CASCADE
    );

CREATE TABLE IF NOT EXISTS skill_types (
    skill_type_id INT AUTO_INCREMENT PRIMARY KEY,
    skill_type VARCHAR(50) NOT NULL
    );

CREATE TABLE IF NOT EXISTS skills (
    skill_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    skill_type INT NOT NULL,
    start_date DATE,
    end_date DATE,
    description TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE,
    FOREIGN KEY (skill_type) REFERENCES skill_types (skill_type_id) ON DELETE CASCADE
    );

-- One user - one photo! Therefore, it is permissible to store it in the database.
CREATE TABLE IF NOT EXISTS photo (  
    photo_id INT PRIMARY KEY,
    bin_data MEDIUMBLOB NOT NULL,
    mime_type VARCHAR(50) NOT NULL,
    FOREIGN KEY (photo_id) REFERENCES users (user_id) ON DELETE CASCADE
    );