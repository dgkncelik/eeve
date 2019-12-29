from model.field import Field, FieldValidationException, FieldException


class FloatField(Field):
    def __init__(self, value=None, required=False, min_value=None, max_value=None, apply_default=True):
        _default = None
        self.min_value = min_value
        self.max_value = max_value
        if apply_default is True:
            _default = 0.0

        if min_value is not None and not isinstance(min_value, float):
            raise FieldException('min_value must be integer')
        if max_value is not None and not isinstance(max_value, float):
            raise FieldException('max_value must be integer')

        super(FloatField, self).__init__(primitive_type=float, value=value, required=required, default=_default)

    def value(self):
        super().validate()

        if self.min_value and self.__value < self.min_value:
            raise FieldValidationException('value is lower then minimum')
        if self.max_value and self.__value > self.max_value:
            raise FieldValidationException('value is bigger then maximum')

        return True
