import abc
from abc import ABCMeta


class Calculator:
    """Base class for all loan calculators"""
    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def monthly_repayment(self):
        """
        This is an abstract method for the calculation of monthly repayment of a loan.
        Different calculators can be configured that give slightly different results.
        """

