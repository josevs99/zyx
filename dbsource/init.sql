-- init.sql
CREATE DATABASE IF NOT EXISTS my_database;
USE my_database;
-- CREATE SCHEMA my_schema AUTHORIZATION root;

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name STRING,
    email STRING UNIQUE
);

INSERT INTO users (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com');

CREATE TABLE operations(
   id UUID PRIMARY KEY,
   operation STRING,
   status INT,
   details JSONB 
);

CREATE TABLE services(
   id UUID PRIMARY KEY,
   service_name STRING,
   status STRING,
   details JSONB,
   started_at TIMESTAMP, 
   ended_at TIMESTAMP
);
