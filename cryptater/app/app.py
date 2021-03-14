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
        # # Set home directory
        # if home:
        #     self._home = Path(home).resolve()
        # else:
        #     self._home = get_cryptater_home()

        logger.info('Using Application Home: {}'.format(self._home))

        # Call superclass constructor last
        # This will override defaults with any user provided inputs
        # to constructor
        super(AppModel, self).__init__(**kwargs)

        logger.info('Tater is baked and ready.')

    def __new__(cls, *args, **kwargs):
        """ Create a Tater

        """
        if AppModel._instance is not None:
            raise RuntimeError('A Tater already exists')
        self = super(AppModel, cls).__new__(cls, *args, **kwargs)
        AppModel._instance = self
        return self

    @staticmethod
    def get():
        """ Dig up the global instance

        If none exists, one will be created.
        """
        if not AppModel._instance:
            AppModel()
        return AppModel._instance

    @staticmethod
    def destroy():
        """ Destroy the instance.

        """
        AppModel._instance = None
