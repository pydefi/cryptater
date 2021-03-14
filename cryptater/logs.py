# ------------------------------------------------------------------------------
# Copyright (c) 2021, Mike Babst
#
# Distributed under the terms of the MIT License
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

import logging
from pathlib import Path
import datetime

default_log_format = "%(levelname)s:%(name)s: %(message)s"

_console_handler_name = 'app_console_handler'
_file_handler_name = 'app_file_handler'

logger = logging.getLogger(__name__)
rootlogger = logging.getLogger('')


def configure_root_logger(level=logging.INFO, logformat=default_log_format, logfile=None):
    """ Configure root logger

    Enable console logging by adding a StreamHandler to the RootLogger.
    Optionally enable file logging by adding a FileHandler to the RootLogger.

    Parameters
    ----------
    level: int
        Logging Level
    logformat: str
        Logging format string
    logfile: str
        Log file name

    Returns
    -------
    rootlogger: logging.RootLogger

    """

    ch = _get_root_handler(_console_handler_name)

    if not ch:
        ch = logging.StreamHandler()
        ch.name = _console_handler_name
        ch.setLevel(level)
        ch.setFormatter(logging.Formatter(logformat))
        rootlogger.addHandler(ch)
        set_logging_level(level)
        logger.info('New console logging session created %s' % str(datetime.datetime.now()))

    fh = _get_root_handler(_file_handler_name)

    if not fh:
        if logfile:
            logfilepath = Path(logfile).resolve()

            if logfilepath.exists():
                fh = logging.FileHandler(filename=str(logfilepath), mode='a')
            else:
                if not logfilepath.parent.exists():
                    raise NotADirectoryError('Logfile parent directory does not exist %s' % str(logfilepath))
                fh = logging.FileHandler(filename=str(logfilepath), mode='w')

            fh.name = _file_handler_name
            fh.setLevel(level)
            fh.setFormatter(logging.Formatter(logformat))
            rootlogger.addHandler(fh)
            set_logging_level(level)
            logger.info('New file logging session created %s' % str(datetime.datetime.now()))

    return rootlogger


def set_logging_level(level=logging.WARNING):
    """ Set logging level for console and file loggers

    Parameters
    ----------
    level: int
        Logging level

    Returns
    -------
    None
    """
    ch = _get_root_handler(_console_handler_name)
    if ch:
        ch.setLevel(level)

    fh = _get_root_handler(_file_handler_name)
    if fh:
        fh.setLevel(level)

    # Update level in rootlogger
    min_level = logging.CRITICAL
    for handler in rootlogger.handlers:
        if handler.level:
            if handler.level < min_level:
                min_level = handler.level
    rootlogger.setLevel(min_level)


def _get_root_handler(name):
    """ Get root logger Handler by name

    Parameters
    ----------
    name: str
        Handler name

    Returns
    -------
    logging.Handler
    """

    root_logger = logging.getLogger('')

    for handler in root_logger.handlers:
        if handler.name == name:
            return handler

    return None
