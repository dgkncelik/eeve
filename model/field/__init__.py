class FieldValidationException(Exception):
    pass


class FieldException(Exception):
    pass


class Field(object):
    def __init__(self, primitive_type, value=None, required=False, default=None):
        self.default = default
        self.required = required
        self.primitive_type = primitive_type

        self.value = value
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        self.__value = v
        self.validate()

    def validate(self):
        if self.required is True and self.__value is None:
            raise FieldValidationException('value is required for %s field' % self.__class__.__name__)

        if self.__value is None and self.default is not None:
            self.__value = self.default

        if not isinstance(self.__value, self.primitive_type):
            raise FieldValidationException('value %s is not instance of %s' % (self.__value, self.primitive_type))

        return True
