"""Generic script exit value class.
"""


class ExitCode:
    """Class handles the exit codes and related messages.

    Keyword arguments
    -----------------
    code: int
        An exit code numeric representation.
    message: str
        A message assigned to given exit code.
    """

    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __repr__(self):
        return f"<code: {self.code}, message: {self.message}>"
