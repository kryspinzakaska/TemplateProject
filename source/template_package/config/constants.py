"""Constants container.
"""

import os
from pathlib import Path

# ------
# Basic.
# ------

__name__ = 'Python Template Package'
__version__ = '0.1.0'
__author__ = 'kryspinzakaska'
SCRIPT_NAME_FORMATTED = __name__.lower().replace(" ", "_")
FILE_NAME = "_".join(__name__.lower().split())

# -----------------
# Logging specific.
# -----------------

LOG_FILE_PATH = Path(os.getcwd(), f"{SCRIPT_NAME_FORMATTED}.log")
DEBUG_LOG_FILE_PATH = Path(os.getcwd(), f"{SCRIPT_NAME_FORMATTED}_debug.log")
BASIC_FORMAT = "%(asctime)s %(levelname)-8s %(message)s"
DEBUG_FORMAT = "%(asctime)s %(levelname)-8s [%(module)s | %(funcName)s | %(lineno)d]  %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
