from model.field import Field, FieldValidationException, FieldException


class StringField(Field):
    def __init__(self, value=None, required=False, min_length=None, max_length=None, apply_default=True):
        _default = None
        self.min_length = min_length
        self.max_length = max_length
        if apply_default is True:
            _default = ''

        if min_length is not None and not isinstance(min_length, int):
            raise FieldException('min_length must be integer')
        if max_length is not None and not isinstance(max_length, int):
            raise FieldException('max_length must be integer')

        super(StringField, self).__init__(primitive_type=str, value=value, required=required, default=_default)

    def validate(self):
        super().validate()

        if self.min_length != -1 and len(self.value) < self.min_length:
            raise FieldValidationException('value min length is invalid')
        if self.max_length != -1 and len(self.value) > self.max_length:
            raise FieldValidationException('value max length is invalid')

        return True
