-- Ролі
CREATE ROLE staff NOLOGIN;
CREATE ROLE rental_admin LOGIN PASSWORD 'rental_admin_pass';
CREATE ROLE fleet_sync LOGIN PASSWORD 'fleet_sync_pass';
CREATE ROLE agent_lena LOGIN PASSWORD 'agent_lena_pass' IN ROLE staff;
CREATE ROLE analyst LOGIN PASSWORD 'analyst_pass' IN ROLE staff;

-- Бази даних
CREATE DATABASE rental OWNER rental_admin;
CREATE DATABASE rental_archive OWNER rental_admin;

-- Обмеження підключення на рівні баз
REVOKE CONNECT ON DATABASE rental FROM PUBLIC;
REVOKE CONNECT ON DATABASE rental_archive FROM PUBLIC;

GRANT CONNECT ON DATABASE rental TO staff;
GRANT CONNECT ON DATABASE rental TO fleet_sync;
GRANT CONNECT ON DATABASE rental_archive TO analyst;

-- Налаштування бази rental
\c rental

CREATE TABLE cars (
    id integer,
    plate text
);
ALTER TABLE cars OWNER TO rental_admin;

CREATE TABLE bookings (
    id integer,
    car_id integer,
    customer text
);
ALTER TABLE bookings OWNER TO rental_admin;

GRANT SELECT ON ALL TABLES IN SCHEMA public TO staff;
GRANT INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO agent_lena;
GRANT SELECT, UPDATE ON TABLE cars TO fleet_sync;

-- Налаштування бази rental_archive
\c rental_archive

CREATE TABLE old_bookings (
    id integer,
    car_id integer,
    customer text
);
ALTER TABLE old_bookings OWNER TO rental_admin;

GRANT SELECT ON ALL TABLES IN SCHEMA public TO analyst;