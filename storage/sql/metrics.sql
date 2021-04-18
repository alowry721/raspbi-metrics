--Create User to interact with metrics database
DROP USER IF EXISTS 'sa-metrics'@'localhost';
CREATE USER 'sa-metrics'@'localhost' IDENTIFIED BY 'pass99**';
--Give privileges to database
GRANT ALL PRIVILEGES ON metrics. * TO 'sa-metrics'@'localhost';

/*Initialize the following tables
  - cpu temperature
  - mem_usage
  - cpu_usage
 */
DROP TABLE IF EXISTS cpu_temp;
CREATE TABLE IF NOT EXISTS cpu_temp (
    Timestamp DATETIME NOT NULL PRIMARY KEY,
    Temperature FLOAT
);

DROP TABLE IF EXISTS mem_usage;
CREATE TABLE IF NOT EXISTS mem_usage (
    Timestamp DATETIME NOT NULL,
    Used LONG,
    Free LONG,
    Percent FLOAT
);

DROP TABLE IF EXISTS cpu_usage;
CREATE TABLE IF NOT EXISTS cpu_usage (
    Timestamp DATETIME NOT NULL,
    CPU1 FLOAT,
    CPU2 FLOAT,
    CPU3 FLOAT,
    CPU4 FLOAT
)