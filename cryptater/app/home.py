# ------------------------------------------------------------------------------
# Copyright (c) 2021, Mike Babst
#
# Distributed under the terms of the MIT License
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

from pathlib import Path

class AppHomeDirectory:

    #: Home Path object
    home = property(lambda self: self._home)

    def __init__(self, appname: str, force=''):
        """ Application Home Directory

        Parameters
        ----------
        appname : str
            Application name

        force : str (optional)
            Force set the application home directory

        """

        # Set home directory
        if not force:
            self._home = get_app_home_dir(appname)
        else:
            home_path = Path(force).resolve()
            if home_path.exists() and home_path.is_dir():
                self._home = home_path.absolute()
            else:
                raise NotADirectoryError('Path {} does not exist'.format(home_path))

    def __str__(self):
        return str(self._home)

def get_app_home_dir(appname, foldername=None):
    """ Get Application home directory

    Search for and return application home directory.

    Returns
    -------
    appname : str
        Application name

    """

    if not foldername:
        foldername = '.' + appname

    # Look in current directory and return if found
    chome = Path(foldername).resolve()
    if chome.is_dir():
        return chome.absolute()

    # Search user's home directory
    # Make one if it does not exist
    chome = Path.home() / foldername

    if chome.is_dir():
        return chome.absolute()
    else:
        chome.mkdir()
        return chome.absolute()




