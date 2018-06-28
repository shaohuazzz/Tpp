import datetime

class Test:
    def __init__(self):
        self.name = '1',
        self.age = 18,

def to_dict(object):
    obj = {}
    keys = vars(object).keys()