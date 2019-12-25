"""
Use this class to model the data and use common interfaces to storage or messaging
A 'Model' has 'Fields' which are key-value based object attributes
"""
from storage.storage import Storage
from message.publisher import Publisher
from message.consumer import Consumer


class Model(object):
    def __init__(self, storage=Storage(), publisher=Publisher(), consumer=Consumer(), data=None, *args, **kwargs):
        self.__storage = storage
        self.__publisher = publisher
        self.__consumer = consumer

        if data is None:
            self.__data = {}
        else:
            self.__data = data

        self.__arguments = args
        self.__parameters = kwargs
        self.__fields = None

    def validate(self):
        pass

    def save(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def filter(self):
        pass

    def send(self):
        pass

    def receive(self):
        pass

    def data(self):
        pass
