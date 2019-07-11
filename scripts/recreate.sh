# psql -d postgres -c "CREATE ROLE jatayu WITH LOGIN SUPERUSER ENCRYPTED PASSWORD 'jatayu';"
psql -d postgres -c "DROP DATABASE IF EXISTS jatayu;"
psql -d postgres -c "CREATE DATABASE jatayu WITH OWNER jatayu;"
