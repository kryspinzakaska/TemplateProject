"""Logger and HiddenPasswordFormatterProxy classes implementation.
"""

import logging
import re
import sys
from logging import Formatter
from pathlib import Path
from typing import Iterable

from template_package.config.constants import DATE_FORMAT, DEBUG_FORMAT, BASIC_FORMAT


class _HiddenSensitiveDataFormatterProxy(Formatter):
    """A handler formatter which hides sensitive data.

    Keyword arguments
    -----------------
    formatter: logging.Formatter
        A formatter used by logger.
    sensitive_patterns: Iterable
        A collection of sensitive phrases. Regex can be used here.
    """

    def __init__(self, formatter: logging.Formatter, sensitive_patterns: Iterable):
        super().__init__()
        self._formatter = formatter
        self.__password_patterns = [re.compile(pattern) for pattern in sensitive_patterns]

    def format(self, record: logging.LogRecord) -> str:
        """Format the specified record as text.
        Method analogous to method of the same name in the Formatter class in logging module.

        Parameters
        ----------
        record: logging.LogRecord
            A LogRecord instance representing an event being logged.

        Returns
        -------
        str
          Formatted record with sensitive data being hidden.
        """
        log_msg = self._formatter.format(record)
        for pattern in self.__password_patterns:
            log_msg = pattern.sub("*" * 5, log_msg)
        return log_msg


class Logger:
    """Class handles logging configuration.
    """

    def __init__(self):
        super().__init__()
        self._log = logging.getLogger()
        self._log.setLevel(logging.NOTSET)
        self._level = logging.NOTSET
        self._stdout_handler = None
        self._file_handler = None
        self._debug_file_handler = None

    def set_level(self, level: str):
        """Sets up logging level

        Parameters
        ----------
        level: str
            A string corresponding to given logging severity:
            CRITICAL, ERROR, WARNING, INFO, DEBUG..
        """
        self._level = logging.getLevelName(level)
        for handler in [h for h in [self._stdout_handler, self._file_handler] if h is not None]:
            handler.setLevel(self._level)
            handler.setFormatter(logging.Formatter(self._logger_format(), DATE_FORMAT))

    def _logger_format(self):
        """Chooses logger format base of logging severity level.

        Returns
        -------
        str
            Logging format string.
        """
        if self._level == logging.DEBUG:
            logger_format = DEBUG_FORMAT
        else:
            logger_format = BASIC_FORMAT
        return logger_format

    def config_stdout_handler(self):
        """Sets up console stream handler.
        """
        if not self._stdout_handler:
            self._stdout_handler = logging.StreamHandler(sys.stdout)
        self._stdout_handler.setFormatter(logging.Formatter(self._logger_format(), DATE_FORMAT))
        self._stdout_handler.setLevel(self._level)
        self._log.addHandler(self._stdout_handler)

    def config_log_file_handler(self, path: Path):
        """Sets up file handler for standard severity.

        Parameters
        ----------
        path: Path
            A path to log-file.
        """
        if not self._file_handler:
            self._file_handler = logging.FileHandler(path, mode='a')
        self._file_handler.setFormatter(logging.Formatter(self._logger_format(), DATE_FORMAT))
        self._file_handler.setLevel(self._level)
        self._log.addHandler(self._file_handler)

    def config_debug_log_file_handler(self, path: Path):
        """Sets up file handler for debug severity.

        Parameters
        ----------
        path: Path
            A path to log-file.
        """
        if not self._debug_file_handler:
            self._debug_file_handler = logging.FileHandler(path, mode='a')
        self._debug_file_handler.setFormatter(logging.Formatter(DEBUG_FORMAT, DATE_FORMAT))
        self._debug_file_handler.setLevel(logging.DEBUG)
        self._log.addHandler(self._debug_file_handler)

    @staticmethod
    def set_hidden_password_formatter(password: str):
        """Sets up formatter for logging handlers to hide password.

        Parameters
        ----------
        password: str
            A password string which have to be hidden in the log.
        """
        for handler in logging.root.handlers:
            handler.setFormatter(_HiddenSensitiveDataFormatterProxy(formatter=handler.formatter,
                                                                    sensitive_patterns=[password]))
