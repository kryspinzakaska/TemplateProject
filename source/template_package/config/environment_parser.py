"""ArgParser class implementation.

Handles argument parsing for the script.
"""

import argparse
import json
import logging
import os
import sys

from template_package.config.basic_args import LogLevel, BasicParam, LogMode
from template_package.config.arg import Arg
from template_package.config.common_args import CommonIntParam, CommonListParam
from template_package.config.constants import __name__, __version__
from template_package.config.mode import Mode
from template_package.config.mode_a_args import AModeOnlyParam
from template_package.lib.utilities import iterable_to_string


class EnvironmentParser:
    """Represents environment parser.
    """

    def __init__(self):
        self.params = None
        self._parser = None
        self._subparsers = None
        self._common_parser = None

    def _set_param(self, arg, default=None):
        self.params[arg.dest] = os.environ.get(arg.env_name, default)

    def _prepare_basic_parser(self):
        """Prepares a basic parser.
        """
        for arg in [LogLevel, LogMode, BasicParam]:
            self._set_param(arg)

    def _prepare_subparsers(self):
        """Prepares a subparsers allowing to choose a mode of script.
        """
        self._subparsers = self._parser.add_subparsers(dest='mode',
                                                       title='Mode',
                                                       description='Script execution mode.',
                                                       help='Possible script execution variants.')

    def _prepare_common_parser(self):
        """Prepares parser including common parameters for all of the script's modes.
        """
        self._common_parser = argparse.ArgumentParser(add_help=False)
        argument_group = self._common_parser.add_argument_group('Common', 'Common parameters for all script modes.')
        argument_group.add_argument('-h', '--help',
                                    action='help',
                                    help='Show this help message specific for script mode and exit.')
        CommonIntParam.add_arg(argument_group)
        CommonListParam.add_arg(argument_group)

    def _prepare_mode_a_parser(self):
        """Prepares a parser for "a" mode with specific parameters for this mode.
        """
        self._a_mode_parser = self._subparsers.add_parser(Mode.MODE_A,
                                                          description='Mode A.',
                                                          formatter_class=argparse.RawTextHelpFormatter,
                                                          help='Set a script mode to A-mode.',
                                                          parents=[self._common_parser],
                                                          add_help=False)
        argument_group = self._a_mode_parser.add_argument_group('Mode A', 'Parameters specific for A-mode.')
        AModeOnlyParam.add_arg(argument_group)

    def _prepare_mode_b_parser(self):
        """Prepares a parser for "b" mode with specific parameters for this mode.
        """
        self._b_mode_parser = self._subparsers.add_parser(Mode.MODE_B,
                                                          description='Mode B.',
                                                          formatter_class=argparse.RawTextHelpFormatter,
                                                          help='Set a script mode to B mode.',
                                                          parents=[self._common_parser],
                                                          add_help=False)

    def prepare_parser(self):
        """Prepares commandline parser.
        """
        self._prepare_basic_parser()
        self._prepare_subparsers()
        self._prepare_common_parser()
        self._prepare_mode_a_parser()
        self._prepare_mode_b_parser()

    def parse(self):
        """Parses input parameters.
        """
        self.params, unknown_args = self._parser.parse_known_args()
        logging.debug('Raw parsed arguments:\n%s.', json.dumps(self.params.__dict__, indent=4, separators=(';', ': ')))
        if unknown_args:
            logging.warning('Ignored arguments:\n[%s].', iterable_to_string(con=unknown_args, sep=',\n', wrap="'"))
