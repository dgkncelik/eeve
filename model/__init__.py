"""
Use this class to model the data and use common interfaces to storage or messaging
A 'Model' has 'Fields' which are key-value based object attributes
"""
from storage import Storage
from message import Publisher
from message import Consumer
from model.field import Field


class ModelException(Exception):
    pass


class Model(object):
    def __init__(self, storage=Storage(), publisher=Publisher(), consumer=Consumer(), data=None, *args, **kwargs):
        self.__storage = storage
        self.__publisher = publisher
        self.__consumer = consumer

        if data is not None and not isinstance(data, dict):
            raise ModelException('data must be dictionary')
        elif data is None:
            self.__data = {}

        self.__arguments = args
        self.__parameters = kwargs
        self.__fields = None

    def __getattribute__(self, item):
        all_attributes = dir(self)
        if item in all_attributes:
            attr = getattr(self, item)
            if isinstance(attr, Field):
                return attr.value
            else:
                return getattr(self, item)
        else:
            getattr(self, item)

    def __setattr__(self, key, value):
        all_attributes = dir(self)
        if key in all_attributes:
            attr = getattr(self, key)
            if isinstance(attr, Field):
                attr.value = value
            else:
                setattr(self, key, value)
        else:
            setattr(self, key, value)

    def validate(self):
        pass

    def save(self):
        self.__storage.save(self)

    def update(self):
        self.__storage.save(self)

    def delete(self):
        self.__storage.delete(self)

    def filter(self):
        self.__storage.find(self)

    def send(self):
        self.__publisher.publish(self)

    def receive(self):
        self.__consumer.get(self)

    def data(self):
        return self.__data
