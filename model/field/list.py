from model.field import Field, FieldValidationException, FieldException


class ListField(Field):
    def __init__(self, value=None, required=False, min_size=None, max_size=None, apply_default=True):
        _default = None
        self.min_size = min_size
        self.max_size = max_size
        if apply_default is True:
            _default = []

        if min_size is not None and not isinstance(min_size, int):
            raise FieldException('min size must be integer')
        if max_size is not None and not isinstance(max_size, int):
            raise FieldException('max size must be integer')

        super(ListField, self).__init__(primitive_type=list, value=value, required=required, default=_default)

    def validate(self):
        super().validate()

        if self.min_size and len(self.value) < self.min_size:
            raise FieldValidationException('value min size not valid')
        if self.max_size and len(self.value) > self.max_size:
            raise FieldValidationException('value max size not valid')

        return True
