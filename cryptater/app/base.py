# ------------------------------------------------------------------------------
# Copyright (c) 2021, Mike Babst
#
# Distributed under the terms of the MIT License
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

import asyncio

from atomdb.base import JSONModel
from atomdb.base import JSONSerializer


class Base(JSONModel):
    """ Base class for application objects

    This class is used as a model class that supports typed attributes,
    and conversion to/from and JSON objects
    """

    pass


def from_json(state, scope=None):
    """ Convert JSON to an Model, dict, or list

    Parameters
    ----------
    state: dict
        Object state in JSON format

    Returns
    -------
    model: Base, dict, or list
        Object converted from JSON
    """

    decoder = JSONSerializer()

    async def decode_state(state, scope):
        obj = await decoder.unflatten(state, scope)
        return obj

    result = asyncio.run(decode_state(state, scope))

    return result


def to_json(model):
    """ Convert an object o JSON

    Parameters
    ----------
    model: Base, dict, or list
        Object to convet to json

    Returns
    -------
    result: dict
        Object state in JSON format
    """
    encoder = JSONSerializer()

    state = encoder.flatten(model)

    return state
