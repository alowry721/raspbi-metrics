from abc import ABC, abstractmethod


class AMetrics(ABC):
    # def __init__(self, **kwargs):
    #     verbose = kwargs.get('verbose')
    #     add_logging_std(verbose=verbose)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @abstractmethod
    def add_usage(self, metrics):
        pass

    @abstractmethod
    def _add_cpu_usage(self, cpus_tuple):
        if not isinstance(cpus_tuple, tuple):
            raise TypeError("cpu_tuple must be of type 'typle'")
        pass

    @abstractmethod
    def _add_cpu_temp(self, temp_tuple):
        if not isinstance(temp_tuple, tuple):
            raise TypeError("cpu_tuple must be of type 'typle'")
        pass

    @abstractmethod
    def _add_vmem_usage(self, vmem_tuple):
        if not isinstance(vmem_tuple, tuple):
            raise TypeError("cpu_tuple must be of type 'typle'")
        pass

    @abstractmethod
    def display_data(self, table):
        pass

