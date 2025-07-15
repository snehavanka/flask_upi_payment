CREATE DATABASE IF NOT EXISTS payment_db;

USE payment_db;
SHOW tables;

CREATE TABLE IF NOT EXISTS payments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    upi_id VARCHAR(100),
    payment_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE payments ADD COLUMN receiver_upi_id VARCHAR(100);
DESC payments;
delete from payments where name='sneha';
SELECT*from payments;