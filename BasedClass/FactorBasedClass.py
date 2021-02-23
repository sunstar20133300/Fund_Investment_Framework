import pandas as pd
import numpy as np

from WindPy import w
import abc


class FactorBaseClass(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def cal_factor(self):
        pass

    @abc.abstractmethod
    def save_factor(self):
        pass

    @abc.abstractmethod
    def get_date_period(self):
        pass

    @abc.abstractmethod
    def get_last_data(self):
        pass

    @abc.abstractmethod
    def get_first_data(self):
        pass

    @abc.abstractmethod
    def restore(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def fill_missing_data(self):
        pass