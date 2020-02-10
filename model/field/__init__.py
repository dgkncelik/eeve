class FieldValidationException(Exception):
    pass


class FieldException(Exception):
    pass


class Field(object):
    def __init__(self, primitive_type, value=None, required=False, default=None):
        self.value = value
        self.default = default
        self.required = required
        self.primitive_type = primitive_type

        if self.value is None and self.default is not None:
            self.value = self.default

    def set(self, _value):
        if _value is None and self.default is not None:
            self.value = self.default
        else:
            self.value = _value

    def get(self):
        return self.value

    def validate(self):
        if self.primitive_type is None:
            return True

        if self.required is True and self.value is None:
            raise FieldValidationException('value is required for %s field' % self.__class__.__name__)

        if not isinstance(self.value, self.primitive_type):
            raise FieldValidationException('value %s is not instance of %s' % (self.value, self.primitive_type))

        return True
