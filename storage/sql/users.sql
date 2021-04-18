--Create User to interact with metrics database
DROP USER IF EXISTS '&1'@'&2';
CREATE USER '&1'@'&2' IDENTIFIED BY '&3';
--Give privileges to database
GRANT ALL PRIVILEGES ON '&4'. * TO '&1'@'&2';

GRANT ALL PRIVILEGES ON *.* TO 'sa-metrics'@'192.168.1.%'
  IDENTIFIED BY 'pass99**' WITH GRANT OPTION;
