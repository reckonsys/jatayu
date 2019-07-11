# psql -d postgres -c "CREATE ROLE cerberus WITH LOGIN SUPERUSER ENCRYPTED PASSWORD 'cerberus';"
psql -d postgres -c "DROP DATABASE IF EXISTS cerberus;"
psql -d postgres -c "CREATE DATABASE cerberus WITH OWNER cerberus;"
