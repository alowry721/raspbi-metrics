import logging, psutil
from abc import ABC, abstractmethod
from gpiozero import CPUTemperature
from datetime import datetime

from logging_utilities import get_timestamp


class ACollect(ABC):

    @abstractmethod
    def cpu_percent(self):
        pass

    @abstractmethod
    def virtual_mem(self):
        pass

    @abstractmethod
    def cpu_temp(self):
        pass


class MetricsCollector(ACollect):

    def cpu_percent(self):
        cpu_percentage_tuple = tuple([get_timestamp()] + [str(cpu_p) for cpu_p in psutil.cpu_percent(interval=5, percpu=True)])
        logging.debug(cpu_percentage_tuple)
        return cpu_percentage_tuple

    def virtual_mem(self):
        virtual_mem = psutil.virtual_memory()
        vm_tuple = (get_timestamp(), virtual_mem.used, virtual_mem.free, virtual_mem.percent)
        logging.debug(vm_tuple)
        return vm_tuple

    def cpu_temp(self):
        cpu = CPUTemperature()
        logging.debug(cpu.temperature)
        return (get_timestamp(), cpu.temperature)
