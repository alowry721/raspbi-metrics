import argparse

from logging_utilities import add_logging_args, add_logging
from storage.metrics_csv import MetricsCsv, add_csv_args
from collect.metrics_collect import MetricsCollector


parser = argparse.ArgumentParser(description="Collect Metrics and store in database")
add_logging_args(parser)
subparsers = parser.add_subparsers()

# db_parser = add_db_args(subparsers)
csv_parser = subparsers.add_parser('csv')
add_csv_args(csv_parser)

def collect_metrics(metrics_collector):
    return {'cpu_tuple': metrics_collector.cpu_percent(),
                   'temp_tuple': metrics_collector.cpu_temp(),
                   'vmem_tuple': metrics_collector.virtual_mem()}

if __name__ == '__main__':
    cli_args = parser.parse_args()
    # add_logging(cli_args)
    metrics_collector = MetricsCollector()
    with MetricsCsv(cli_args) as metrics_database:
        metrics = collect_metrics(metrics_collector)
        metrics_database.add_usage(**metrics)
