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
    app = AppModel('SuperApp')

    # Prevent creating two Applications
    with pytest.raises(RuntimeError):
        app = AppModel('SuperApp')

    # Destroy existing app
    app.destroy()

    # Create a new app using local home folder
    os.mkdir('.tmp')
    app = AppModel('SuperApp', home='.tmp')
    app.destroy()

    # Try to use non-existent directory
    with pytest.raises(NotADirectoryError):
        os.rmdir('.tmp')
        app = AppModel('SuperApp', home='.tmp')

    # Test app getter (create from scratch)
    app.destroy()
    app1 = AppModel('NewApp').get()

    # Re-get existing app object
    app2 = AppModel.get()

    assert app1 is app2

