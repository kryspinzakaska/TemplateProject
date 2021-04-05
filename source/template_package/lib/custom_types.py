"""Custom types used for configuration of arguments parsing.
"""

from argparse import ArgumentTypeError
from typing import Iterable


class TupleType:
    """Factory for creating tuple type.

    Instance of the class are typically passed as type argument to the ArgumentParser add_argument() method,
    e.g. "(...).add_argument((...), type=TupleType(), (...))".

    Keyword arguments
    -----------------
    sep: str
        Signs used to separate a string into tuple's elements.
        First sign of the sep sequence found in given string is used as separator.
        If nested parameter is enable all sings in sequence are used.
    min_size: int
        Indicates a minimum amount of values which should be given.
        Applies only to highest level of the generated tuple.
    max_size: int
        Indicates a maximum amount of values which should be given.
        Applies only to highest level of the generated tuple.
    valid_values: Iterable
        A iterable object containing all valid input values.
    nested: bool
        True if splitting throw a sting should be nested, false otherwise.
        Separation signs are used in the order of sequence given with sep parameter.
    """

    def __init__(self,
                 sep: str = ';, ',
                 min_size: int = None,
                 max_size: int = None,
                 valid_values: Iterable = None,
                 nested: bool = False):
        self._sep = list(sep)
        self._min_size = min_size
        self._max_size = max_size
        self._valid_values = valid_values
        self._nested = nested

    def __call__(self, string):
        if string == '':
            raise ArgumentTypeError(f'can not be an empty sting')
        if self._nested:
            if len(self._sep) == 1:
                raise ArgumentTypeError('it is required more than one separation sign input with sep parameter')
            list_v = self._nested_split(string, self._sep)
        else:
            for sep in self._sep:
                if sep in string:
                    list_v = string.split(sep)
                    break
            else:
                list_v = [string]
        tuple_v = tuple(list_v)
        tuple_l = len(tuple_v)
        if self._min_size:
            if tuple_l < self._min_size:
                raise ArgumentTypeError(f'parameter takes at lease {self._min_size} values but {tuple_l} were given')
        if self._max_size:
            if tuple_l > self._max_size:
                raise ArgumentTypeError(f'parameter takes {self._max_size} values at most but {tuple_l} were given')
        if self._valid_values:
            for val in tuple_v:
                if val not in self._valid_values:
                    raise ArgumentTypeError(f'"{val}" not found in the set of possible values: {self._valid_values}')
        return tuple_v

    def __repr__(self):
        kwargs = [('sep', self._sep),
                  ('min_size', self._min_size),
                  ('max_size', self._max_size),
                  ('valid_values', self._valid_values)]
        args_list = []
        for keyword, arg in kwargs:
            if isinstance(arg, str):
                arg = f"'{arg}'"
            args_list.append(f'{keyword}={arg}')
        args_str = ', '.join(args_list)
        return f'{type(self).__name__}({args_str})'

    def _nested_split(self, string: str, sep: list):
        """Generates a nested list based on given separation signs.

        Parameters
        ----------
        string: str
            A string to be split.
        sep: list
            A list of separation signs.

        Returns
        -------
        list
            Nested list.
        """
        temp_list = []
        if sep:
            for element in string.split(sep[0]):
                temp_list.append(self._nested_split(element, sep[1:]))
        else:
            return string
        return temp_list


class NonemptyStrType:
    """Factory for creating not empty string type.

    Instance of the class are typically passed as type argument
    to the ArgumentParser add_argument() method.
    """

    def __call__(self, string):
        if string == "":
            raise ArgumentTypeError('can not be an empty string')
        return string

    def __repr__(self):
        return f'{type(self).__name__}()'
