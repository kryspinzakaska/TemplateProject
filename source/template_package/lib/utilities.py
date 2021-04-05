"""Utilities functions used in the script.
"""

from collections.abc import Iterable


def iterable_to_string(con: Iterable, sep: str = ",", wrap: str = None):
    """Transforms a list into a string.

    Parameters
    ----------
    con: Iterable
        An Iterable intended to be transformed.
    sep: str
        A sign to separate list elements in the string.
    wrap: str
        A string which will be used as a wrapper for each element.

    Returns
    ----------
    str
        An Iterable converted into a string.
    """
    if not isinstance(con, Iterable):
        raise TypeError("'{0}' object is not Iterable".format(type(con).__name__))
    con_list = list(con)
    if wrap:
        con_list = [wrap + str(el) + wrap for el in con_list]
    if len(con_list) > 1:
        r_string = sep.join(con_list)
    elif len(con_list) == 1:
        r_string = con_list[0]
    else:
        r_string = ""
    return r_string


def gen_exception_handling_log_msg(exception: Exception) -> str:
    """Generates a log message regarding exception handling in the script.

    Returns
    -------
    str
        A message to be used in the log.
    """
    if str(exception)[-1] != '.':
        log_msg = f"{type(exception).__name__} exception handling: {exception}."
    else:
        log_msg = f"{type(exception).__name__} exception handling: {exception}"
    return log_msg
