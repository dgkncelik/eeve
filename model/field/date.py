from model.field import Field
import datetime


class DateField(Field):
    def __init__(self, value=None, required=False, apply_default=True):
        _default = None
        if apply_default is True:
            _default = datetime.datetime(1970, 1, 1, 0, 0, 0, 0)

        super(DateField, self).__init__(primitive_type=datetime.datetime, value=value, required=required, default=_default)

    def value(self):
        super().validate()
        return True
