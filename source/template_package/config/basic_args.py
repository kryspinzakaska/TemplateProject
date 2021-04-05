"""Basic arguments implementation.
"""

from template_package.config.arg import Arg


class LogLevel(Arg, str):

    _flag = '-l'
    _name = '--log-level'
    dest = 'log_level'
    env_name = 'LOG_LEVEL'

    @staticmethod
    def add_arg(arg_group):
        arg_group.add_argument(LogLevel._flag,
                               LogLevel._name,
                               dest=LogLevel.dest,
                               choices=['NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR'],
                               default='INFO',
                               help='Sets logging severity level.')


# TODO: Assess whether required.
class LogMode(Arg, str):

    _flag = '-m'
    _name = '--log-mode'
    dest = 'log_mode'
    env_name = 'LOG_MODE'

    @staticmethod
    def add_arg(arg_group):
        arg_group.add_argument(LogMode._flag,
                               LogMode._name,
                               dest=LogMode.dest,
                               choices=['w', 'a'],
                               default='w',
                               help='Sets logging mode.It sets weather LOG-file\n'
                                    'should be overwritten (w) or not (a).')


class BasicParam(Arg, str):

    _flag = '-b'
    _name = '--basic-param'
    dest = 'basic_param'
    env_name = 'BASIC_PARAM'

    @staticmethod
    def add_arg(arg_group):
        arg_group.add_argument(BasicParam._flag,
                               BasicParam._name,
                               dest=BasicParam.dest,
                               default='basic_param_default_value',
                               help='Set a basic parameter.')
