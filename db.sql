CREATE DATABASE servicedesk;

USE servicedesk;

CREATE TABLE tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_email VARCHAR(100),
    issue TEXT,
    status VARCHAR(20) DEFAULT 'Open',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
