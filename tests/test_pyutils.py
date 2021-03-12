from cryptater.utils.pyutils import remove_dict_keys


def test_remove_dict_keys():

    d = {'a': 1, 'b': 2, 'c': 3, 4: {'d': 6, 'e': 7}}
    remove_dict_keys(d, remove_keys='a')
    assert 'a' not in d

    d = {'a': 1, 'b': 2, 'c': 3, 4: {'d': 6, 'e': 7}}
    remove_dict_keys(d, remove_keys=['a'])
    assert 'a' not in d

    d = {'a': 1, 'b': 2, 'c': 3, 4: {'d': 6, 'e': 7}}
    remove_dict_keys(d, remove_keys=['d'])
    print(d)
    assert 'd' in d[4]
    remove_dict_keys(d, remove_keys=['d'], recursive=True)
    assert 'd' not in d[4]

    lst = ['a', 'b', 'c']

    remove_dict_keys(lst, remove_keys=['b'])

    print(lst)
