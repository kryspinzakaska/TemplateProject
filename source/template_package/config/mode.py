"""Mode class implementation.

Represents possible script modes.
"""
import argparse

from template_package.config.arg import Arg


class Mode(Arg, str):
    """The possible mode of the script.
    """
    MODE_A = 'mode-a'
    MODE_B = 'mode-b'
    dest = 'mode'

    @staticmethod
    def add_subparsers(parser):
        return parser.add_subparsers(dest=Mode.dest,
                                     title='Mode',
                                     description='Script execution mode.',
                                     help='Possible script execution variants.')

    @staticmethod
    def add_mode_a_parsers(parser, parents: list = None):
        return parser.add_parser(Mode.MODE_A,
                                 description='Mode A.',
                                 formatter_class=argparse.RawTextHelpFormatter,
                                 help='Set a script mode to A-mode.',
                                 parents=parents,
                                 add_help=False)

    @staticmethod
    def add_mode_b_parsers(parser, parents: list = None):
        return parser.add_parser(Mode.MODE_B,
                                 description='Mode B.',
                                 formatter_class=argparse.RawTextHelpFormatter,
                                 help='Set a script mode to B mode.',
                                 parents=parents,
                                 add_help=False)
