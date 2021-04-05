"""Script exit code implementation.
"""

from template_package import __name__, __author__
from template_package.lib.exit_code import ExitCode


class ScriptExitCode:
    """Script exit codes.
    """

    OK = ExitCode(0, 'The script execution was successful.')
    INTERNAL_ERROR = ExitCode(1, f"Some internal {__name__} problem. Please contact with {__author__}.")
    SOME_OTHER_ERROR = ExitCode(2, 'Some other script specific error.')