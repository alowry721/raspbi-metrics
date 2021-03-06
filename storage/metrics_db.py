import logging

import mariadb, sys

from .storage import AMetrics

def add_db_args(parser):
    db_parser = parser.add_parser('db', help='store metrics in a mysql database')
    db_parser.add_argument('--user', '-u', help='username of mysql db', default='sa-metrics')
    db_parser.add_argument('--password', '-pwd', help='password of mysql db', default='pass99**')
    db_parser.add_argument('--host', help='host where mysql db resides', default='localhost')
    db_parser.add_argument('--port', '-p', help='host where mysql db resides')
    db_parser.add_argument('--database', '-db', help='mysql database name where metrics get stored')
    db_parser.add_argument('--db_name', help='name of db to ')



class MetricsDbTable(AMetrics):

    def __enter__(self):
        self._conn = mariadb.connect(
            user="sa-metrics",
            password="pass99**",
            host="localhost",
            port=3306,
            database="metrics"
        )
        self._cursor = self._conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.commit()
        self._conn.close()

    def add_usage(self, **metrics):
        self._add_cpu_usage(metrics.get('cpu_tuple'))
        self._add_cpu_temp(metrics.get('temp_tuple'))
        self._add_vmem_usage(metrics.get('vmem_tuple'))

    def _add_cpu_usage(self, cpus_tuple):
        cmd = "INSERT INTO cpu_usage (Timestamp, CPU1, CPU2, CPU3, CPU4) VALUES (?, ?, ?, ?, ?)"
        self._execute_cursor(cmd, cpus_tuple)

    def _add_cpu_temp(self, temp_tuple):
        cmd = "INSERT INTO cpu_temp (Timestamp, Temperature) VALUES (?, ?)"
        self._execute_cursor(cmd, temp_tuple)

    def _add_vmem_usage(self, vmem_tuple):
        cmd = "INSERT INTO mem_usage (Timestamp, Used, Free, Percent) VALUES (?, ?, ?, ?)"
        self._execute_cursor(cmd, vmem_tuple)

    def _execute_cursor(self, cmd, data_tuple):
        logging.debug(cmd)
        self._cursor.execute(cmd, data_tuple)

    def display_data(self, table):
        cmd = "SELECT * FROM ?"
        self._execute_cursor(cmd, (table))
        for items in self._cursor:
            print(items)
