import logging
import csv

import os

from .storage import AMetrics


def add_csv_args(parser):
    parser.add_argument('--cpu_temp_file', default='cpu_temp.csv')
    parser.add_argument('--cpu_usage_file', default='cpu_usage.csv')
    parser.add_argument('--ps_file', default='ps.csv')


class MetricCsv(object):
    def __init__(self, filepath, *fields):
        csv_file = open(filepath, 'a')
        self.csv_writer = csv.writer(csv_file, delimiter=',')
        if os.stat(filepath).st_size == 0:
            self.csv_writer.writerow(fields)

    def add_usage(self, tuple):
        self.csv_writer.writerow(tuple)


class MetricsCsv(AMetrics):

    def __init__(self, args):
        self.cpu_usage = MetricCsv(args.cpu_usage_file, *['time', 'CPU1', 'CPU2', 'CPU3', 'CPU4'])
        self.cpu_temp = MetricCsv(args.cpu_temp_file, *['time', 'temperature'])
        self.ps = MetricCsv(args.ps_file, *['time', 'used', 'free', 'percent'])

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def _add_cpu_usage(self, cpus_tuple):
        if not isinstance(cpus_tuple, tuple):
            raise TypeError("cpu_tuple must be of type 'tuple'")
        logging.info(str(cpus_tuple))

    def _add_cpu_temp(self, temp_tuple):
        logging.info(str(temp_tuple))

    def _add_vmem_usage(self, vmem_tuple):
        logging.info(str(vmem_tuple))

    def display_data(self, table):
        pass

    def add_usage(self, **metrics):
        self.cpu_usage.add_usage(metrics.get('cpu_tuple'))
        self.cpu_temp.add_usage(metrics.get('temp_tuple'))
        self.ps.add_usage(metrics.get('vmem_tuple'))
