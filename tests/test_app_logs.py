# ------------------------------------------------------------------------------
# Copyright (c) 2021, Mike Babst
#
# Distributed under the terms of the MIT License
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

import logging
from pathlib import Path
import os
import pytest

import cryptater.app.logs
from cryptater.app.logs import _console_handler_name, _file_handler_name, _get_root_handler

logger = logging.getLogger(__name__)


def test_configure_console_logger():

    templogfile = Path('./.tmpdir/log.txt').resolve()

    if not templogfile.parent.exists():
        os.makedirs(str(templogfile.parent), exist_ok=True)

    root_logger = cryptater.app.logs.configure_root_logger()
    assert root_logger.level == logging.INFO
    assert isinstance(_get_root_handler(_console_handler_name), logging.Handler)
    assert not (_get_root_handler(_file_handler_name))

    with pytest.raises(NotADirectoryError):
        root_logger = cryptater.app.logs.configure_root_logger(logfile='./doesnotexist/log.txt')

    root_logger = cryptater.app.logs.configure_root_logger(logfile=templogfile)
    assert root_logger.level == logging.INFO
    assert isinstance(_get_root_handler(_console_handler_name), logging.Handler)
    assert isinstance(_get_root_handler(_file_handler_name), logging.Handler)

    # Change logging level
    cryptater.app.logs.set_logging_level(level=logging.DEBUG)
    assert root_logger.level == logging.DEBUG

    # os.remove(str(templogfile))
    # os.rmdir(str(templogfile.parent))
