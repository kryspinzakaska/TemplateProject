"""ArgParser class implementation.

Handles argument parsing for the script.
"""

import argparse
import json
import logging

from template_package.config.basic_args import LogLevel, BasicParam, LogMode
from template_package.config.common_args import CommonIntParam, CommonListParam
from template_package.config.constants import __name__, __version__
from template_package.config.mode import Mode
from template_package.config.mode_a_args import AModeOnlyParam
from template_package.lib.utilities import iterable_to_string


class CommandLineParser:
    """Represents argument parser.
    """

    def __init__(self):
        self.params = None
        self._parser = None
        self._subparsers = None
        self._common_parser = None

    def _prepare_basic_parser(self):
        """Prepares a basic parser.
        """
        self._parser = argparse.ArgumentParser(description=__doc__,
                                               formatter_class=argparse.RawTextHelpFormatter,
                                               fromfile_prefix_chars='@',
                                               epilog='You can store all parameters into configuration file and pass '
                                                      'it via @file_name parameter.\nParameters should be separated '
                                                      'via new line and should be in format --parameter-name=value.',
                                               add_help=False)
        # Creating an argument group is required to correctly classify arguments in the help message.
        argument_group = self._parser.add_argument_group('Basic', 'Script basic parameters.')
        argument_group.add_argument('-h', '--help',
                                    action='help',
                                    help='Show this help message and exit.')
        argument_group.add_argument('-v', '--version',
                                    help='Show program\'s version number and exit.',
                                    action='version',
                                    version='{0} {1}'.format(__name__, __version__))
        LogLevel.add_arg(argument_group)
        LogMode.add_arg(argument_group)
        BasicParam.add_arg(argument_group)

    def _prepare_subparsers(self):
        """Prepares a subparsers allowing to choose a mode of script.
        """
        self._subparsers = Mode.add_subparsers(self._parser)

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
        self._a_mode_parser = Mode.add_mode_a_parsers(self._subparsers, parents=[self._common_parser])
        argument_group = self._a_mode_parser.add_argument_group('Mode A', 'Parameters specific for A-mode.')
        AModeOnlyParam.add_arg(argument_group)

    def _prepare_mode_b_parser(self):
        """Prepares a parser for "b" mode with specific parameters for this mode.
        """
        self._b_mode_parser = Mode.add_mode_b_parsers(self._subparsers, parents=[self._common_parser])

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
