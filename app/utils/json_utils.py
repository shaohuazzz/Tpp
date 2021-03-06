import datetime
from decimal import Decimal


class Test:
    def __init__(self):
        self.name = '1',
        self.age = 18,

def to_dict(object):
    obj = {}
    keys = vars(object).keys()
    for key in keys:
        if not key.startswith("_"):
            if isinstance(getattr(object,key),datetime.datetime):
                obj[key] = getattr(object, key).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(object, key), datetime.date):
                obj[key] = getattr(object, key).strftime('%Y-%m-%d')
            elif isinstance(getattr(object, key), Decimal):
                obj[key] = str(getattr(object, key))
            else:
                obj[key] = getattr(object, key)
    return obj

def to_list(objects):
    if isinstance(objects,list) and objects:
        objs = []
        for obj in objects:
            objs.append(to_dict(obj))
    return objs

if __name__ == '__main__':
    test = Test()
    to_dict(test)
