"""Implementation of arguments common for all script modes.
"""

from template_package.config.arg import Arg


class CommonIntParam(Arg, int):

    _flag = '-ci'
    _name = '--common-int-param'
    dest = 'common_int_param'

    @staticmethod
    def add_arg(arg_group):
        arg_group.add_argument(CommonIntParam._flag,
                               CommonIntParam._name,
                               dest=CommonIntParam.dest,
                               type=int,
                               help='Set a common int parameter.')


class CommonListParam(Arg, list):

    _flag = '-cl'
    _name = '--common-list-param'
    dest = 'common_list_param'

    def __init__(self, value):
        Arg.__init__(self, value)
        list.__init__(self, value)

    @staticmethod
    def add_arg(arg_group):
        arg_group.add_argument(CommonListParam._flag,
                               CommonListParam._name,
                               dest=CommonListParam.dest,
                               nargs='+',
                               help='Set a common list parameter.')
