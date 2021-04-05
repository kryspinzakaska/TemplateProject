"""Config class implementation.

It controls script basic configuration.
"""

import json
import logging
import sys
import time

from template_package.config.command_line_parser import CommandLineParser
from template_package.config.args import Args
from template_package.config.constants import LOG_FILE_PATH, DEBUG_LOG_FILE_PATH, __name__, __version__
from template_package.lib.logger import Logger

args = None


class Config:
    """Class handles the script basic configuration.
    """

    def __init__(self):
        self._start_time = time.time()
        self._logger = None
        self._arg_parser = None
        self._init_logger()
        self.args = Args()
        self._init_arg_parser()
        self._config_logger()

    def _init_logger(self):
        """Performs basic logger configuration prior to setting up configuration.
        """
        # TODO: How to configure logging cross-modules?
        self._logger = Logger()
        self._logger.set_level('INFO')
        self._logger.config_stdout_handler()
        self._logger.config_log_file_handler(LOG_FILE_PATH)
        self._logger.config_debug_log_file_handler(DEBUG_LOG_FILE_PATH)
        logging.info('%s (%s) started on %s.',
                     __name__,
                     __version__,
                     time.ctime(self._start_time))
        logging.info('Python version used: %s.%s.%s (%s).',
                     sys.version_info[0],
                     sys.version_info[1],
                     sys.version_info[2],
                     sys.executable)

    def _init_arg_parser(self):
        """Retrieves arguments use in the script.
        """
        self._arg_parser = CommandLineParser()
        self._arg_parser.prepare_parser()
        self._arg_parser.parse()
        self.args.set_args(self._arg_parser.params.__dict__)
        logging.debug('All parsed parameters (input values):\n%s.',
                      json.dumps(self.args, indent=4, separators=(';', ': ')))

    def _config_logger(self):
        """Perform addition logger configuration after retrieving script arguments.
        """
        self._logger.set_level(self.args.log_level)
