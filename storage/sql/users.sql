--Create User to interact with metrics database
DROP USER IF EXISTS '&1'@'&2';
CREATE USER '&1'@'&2' IDENTIFIED BY '&3';
--Give privileges to database
GRANT ALL PRIVILEGES ON '&4'. * TO '&1'@'&2';
