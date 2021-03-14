
from atom.api import Int, Str
from cryptater.app.base import Base, to_json, from_json

class BaseSubclass(Base):
    name = Str()
    amount = Int()

def test_class_state():

    obj = BaseSubclass(amount=5)
    state = obj.__getstate__()



def test_encode_model():
    """ Test encoding a model to JSON

    """

    obj = BaseSubclass(amount=5, name='Aloysius')
    state = to_json(obj)
    assert state['__model__'] == 'tests.test_app_base.BaseSubclass'
    assert state['name'] == 'Aloysius'

def test_from_json():
    """ Test restoring model and other objects from JSON state

    """

    state = {'__model__': 'tests.test_app_base.BaseSubclass', '__ref__': '9230a086921eae1f94b6fcdb1940cc', '_id': '', 'name': 'frank', 'amount': 5}
    obj = from_json(state)

    state = {'__model__': 'tests.test_app_base.BaseSubclass', 'name': 'Bartholemew', 'amount': 5}
    obj = from_json(state)
    assert isinstance(obj, BaseSubclass)
    assert obj.amount == 5
    assert obj.name == 'Bartholemew'

    state = {'name': 'Aloysius', 'amount': 5}
    obj = from_json(state)
    assert isinstance(obj, dict)
    assert obj['amount'] == 5
    assert obj['name'] == 'Aloysius'


