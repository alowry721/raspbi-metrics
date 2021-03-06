import logging
import os

from metrics.storage.storage import AMetrics

def add_logging(file_name):
    file_dir = os.path.abspath(os.path.dirname(__file__))
    logging.basicConfig(filename=os.path.join(file_dir, file_name), filemode='a',
                        format='%(asctime)s, %(message)s', level=logging.INFO)

class MetricsCsv(AMetrics):

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @abstractmethod
    def add_cpu_usage(self, cpus_tuple):
        if not isinstance(cpus_tuple, tuple)
            raise TypeError("cpu_tuple must be of type 'typle'")
        pass

    @abstractmethod
    def add_cpu_temp(self, temp_tuple):

    @abstractmethod
    def add_vmem_usage(self, vmem_tuple):
        logging.info(str(vmem_tuple))

    @abstractmethod
    def display_data(self, table):
        pass


