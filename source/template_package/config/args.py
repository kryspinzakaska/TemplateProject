"""Args class implementation.

The class is dict-list object containing all arguments used in the script.
"""

import logging

from template_package.config.basic_args import BasicParam, LogLevel, LogMode
from template_package.config.common_args import CommonIntParam, CommonListParam
from template_package.config.mode import Mode
from template_package.config.mode_a_args import AModeOnlyParam
from template_package.config.notset import NotSetError
from template_package.lib.utilities import gen_exception_handling_log_msg


class Args(dict):
    """A class representing all arguments used in the script.
    """

    _arg_class = [LogLevel,
                  LogMode,
                  BasicParam,
                  Mode,
                  CommonIntParam,
                  CommonListParam,
                  AModeOnlyParam]

    def __repr__(self):
        return 'Args(' + ', '.join([f"{key}={value}" for key, value in self.items()]) + ')'

    def set_args(self, parsed_args):
        for arg in self._arg_class:
            try:
                value = parsed_args[arg.dest]
                logging.debug('Setting up %s=%s.', arg.dest, value)
                self.__setitem__(arg.dest, arg(value))
            except KeyError as exception:
                logging.debug(gen_exception_handling_log_msg(exception))
                logging.debug('Value for "%s" argument wasn\'t provided.', arg.dest)

    # -------------
    # Basic params.
    # -------------

    @property
    def log_level(self):
        try:
            return self.__getitem__(LogLevel.dest)
        except KeyError as exception:
            logging.debug(gen_exception_handling_log_msg(exception))
            raise NotSetError(f"{LogLevel.dest} hasn't been set")

    @property
    def log_mode(self):
        try:
            return self.__getitem__(LogMode.dest)
        except KeyError as exception:
            logging.debug(gen_exception_handling_log_msg(exception))
            raise NotSetError(f"{LogMode.dest} hasn't been set")

    @property
    def basic_param(self):
        try:
            return self.__getitem__(BasicParam.dest)
        except KeyError as exception:
            logging.debug(gen_exception_handling_log_msg(exception))
            raise NotSetError(f"{BasicParam.dest} hasn't been set")

    # --------------
    # Mode params.
    # --------------

    @property
    def mode(self):
        try:
            return self.__getitem__(Mode.dest)
        except KeyError as exception:
            logging.debug(gen_exception_handling_log_msg(exception))
            raise NotSetError(f"{Mode.dest} hasn't been set")

    # --------------
    # Common params.
    # --------------

    @property
    def common_int_param(self):
        try:
            return self.__getitem__(CommonIntParam.dest)
        except KeyError as exception:
            logging.debug(gen_exception_handling_log_msg(exception))
            raise NotSetError(f"{CommonIntParam.dest} hasn't been set")

    @common_int_param.setter
    def common_int_param(self, value):
        if not isinstance(value, int):
            raise AttributeError(f"provided value for {CommonIntParam.dest} argument is {type(value).__name__},"
                                 f" it should be {int.__name__}")
        logging.debug(f"Setting {CommonIntParam.dest}={value}.")
        self.__setitem__(CommonIntParam.dest, value)

    @property
    def common_list_param(self):
        try:
            return self.__getitem__(CommonListParam.dest)
        except KeyError as exception:
            logging.debug(gen_exception_handling_log_msg(exception))
            raise NotSetError(f"{CommonListParam.dest} hasn't been set")

    # --------------
    # A-mode params.
    # --------------

    @property
    def a_mode_param(self):
        try:
            return self.__getitem__(AModeOnlyParam.dest)
        except KeyError as exception:
            logging.debug(gen_exception_handling_log_msg(exception))
            raise NotSetError(f"{AModeOnlyParam.dest} hasn't been set")
