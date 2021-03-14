# ------------------------------------------------------------------------------
# Copyright (c) 2021, Mike Babst
#
# Distributed under the terms of the MIT License
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

import os

import pytest

from cryptater.app.app import AppModel


def test_app_constructor():
    # Create an appliation
    t = AppModel('SuperApp')

    # Prevent creating two Applications
    with pytest.raises(RuntimeError):
        t = AppModel('SuperApp')

    # Destroy existing app
    t = AppModel.destroy()

    # Create a new app using local home folder
    os.mkdir('.tmp')
    t = AppModel('SuperApp', home='.tmp')
    t = AppModel.destroy()

    # Try to use non-existent directory
    with pytest.raises(NotADirectoryError):
        os.rmdir('.tmp')
        t = AppModel('SuperApp', home='.tmp')
