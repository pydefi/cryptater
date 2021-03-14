# ------------------------------------------------------------------------------
# Copyright (c) 2021, Mike Babst
#
# Distributed under the terms of the MIT License
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------
import logging

from atom.api import Atom, Typed, Str

from cryptater.app.home import AppHomeDirectory

logger = logging.getLogger(__name__)


class AppModel(Atom):
    """ Global Application Model.

    """

    #: Application Name
    name = property(lambda self: self._name)
    _name = Str()


    #: App Home Directory
    home = property(lambda self: self._home)
    _home = Typed(AppHomeDirectory)

    # Private instance storage
    _instance = None

    def __init__(self, name: str, home=None, **kwargs):
        """ Initialize Application Object

        """

        self._name = name

        self._home = AppHomeDirectory('myapp', force=home)

        logger.info('Using Application Home: {}'.format(self._home))

        # Call superclass constructor last
        # This will override defaults with any user provided inputs
        # to constructor
        super(AppModel, self).__init__(**kwargs)

        logger.info('Created new {} application'.format(self.name))

    def __new__(cls, *args, **kwargs):
        """ Create a new App

        """
        if AppModel._instance is not None:
            raise RuntimeError('An application already exists')
        self = super(AppModel, cls).__new__(cls, *args, **kwargs)
        AppModel._instance = self
        return self

    @staticmethod
    def get():
        """ Get the global app instance

        """
        return AppModel._instance

    def destroy(self):
        """ Destroy the instance.

        """
        AppModel._instance = None
