from tools.validators import Validator, NotValid, ValidatorError


class FloatValidator(Validator):
    def __init__(self, value, **kwargs):
        self.value = value

        max = kwargs.get('max', None)
        if max is not None and not isinstance(max, float):
            raise ValidatorError('maximum value must be an float')
        self.max = max

        min = kwargs.get('min', None)
        if min is not None and not isinstance(min, float):
            raise ValidatorError('minimum value must be an float')
        self.min = min

        super(FloatValidator, self).__init__(value, **kwargs)

    def validate(self):
        if not isinstance(self.value, float):
            raise NotValid('value is not instance of float')

        if self.min and self.value < self.min:
            raise NotValid('float lower than minimum')

        if self.max and self.value > self.max:
            raise NotValid('float higher than maximum')

        return True
