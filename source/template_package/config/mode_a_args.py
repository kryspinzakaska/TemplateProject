"""Implementation of arguments specific to mode-a.
"""

from template_package.config.arg import Arg


class AModeOnlyParam(Arg, str):

    _flag = '-a'
    _name = '--a-mode-only-param'
    dest = 'a_mode_only_param'

    @staticmethod
    def add_arg(arg_group):
        arg_group.add_argument(AModeOnlyParam._flag,
                               AModeOnlyParam._name,
                               dest=AModeOnlyParam.dest,
                               help='Set a parameter specific for A-mode.')
