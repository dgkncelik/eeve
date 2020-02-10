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
    def __init__(self, *args, **kwargs):
        self.__storage = kwargs.pop('storage')
        self.__publisher = kwargs.pop('publisher')
        self.__consumer = kwargs.pop('consumer')
        self.__data = kwargs.pop('data')

        if self.__data is not None and not isinstance(self.__data, dict):
            raise ModelException('data must be in dictionary format')
        elif self.__data is None:
            self.__data = {}

        self.__arguments = args
        self.__parameters = kwargs
        self.__fields = None

        for key in self.__data:
            self.__setattr__(key, self.__data[key])

    def __getattribute__(self, item):
        all_attributes = dir(self)
        if item in all_attributes:
            _field = getattr(self, item)
            if isinstance(_field, Field):
                return _field.get()

        return getattr(self, item)

    def __setattr__(self, key, value):
        all_attributes = dir(self)
        if key in all_attributes:
            attr = getattr(self, key)
            if isinstance(attr, Field):
                attr.set(value)
                attr.validate()

            else:
                setattr(self, key, value)
        else:
            _field = Field(None, value)
            # TODO: think! whats gonna happen self.__data when new/old field set?
            setattr(self, key, _field)

    def validate(self):
        pass

    def save(self):
        self.__storage.save(self)

    def update(self):
        self.__storage.save(self)

    def delete(self):
        self.__storage.delete(self)

    def query(self):
        self.__storage.find(self)

    def publish(self):
        self.__publisher.publish(self)

    def consume(self):
        self.__consumer.get(self)

    def data(self):
        return self.__data
