CREATE USER web_app_user WITH PASSWORD 'mayhew';
CREATE DATABASE web_app_user;
ALTER ROLE web_app_user SET client_encoding TO 'utf8';
ALTER ROLE web_app_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE web_app_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE library_website TO web_app_user;
REVOKE ALL ON DATABASE library_website FROM PUBLIC;
