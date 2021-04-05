"""Arg class implementation.

It's high level abstract of argument used in the script.
"""
from abc import ABC


class Arg(ABC):

    dest = None
    env_name = None

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    @staticmethod
    def add_arg(arg_group):
        """Adds argument to the <argparse> object created using <add_argument_group> method.
        """
        raise NotImplemented
