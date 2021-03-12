

def remove_dict_keys(obj, remove_keys=[], empty_keys=False, recursive=False):
    """ Modify a dictionary by removing items with matching and/or empty keys

    Parameters
    ----------
    obj: dict
        Dictionary to modify by removing keys

    remove_keys: list of str
        Keys to remove

    empty_keys: bool
        If true, keys will be removed if bool(obj[key]) is false

    recursive: bool
        If true, will search dict recursively

    Returns
    -------
        None

    """

    if isinstance(obj, dict):
        for key in list(obj.keys()):
            if key in list(remove_keys):
                del obj[key]
            elif empty_keys and not obj[key]:
                del obj[key]
            else:
                if recursive:
                    remove_dict_keys(obj[key], remove_keys, empty_keys)

