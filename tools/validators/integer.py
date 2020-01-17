from tools.validators import Validator, NotValid, ValidatorError


class IntegerValidator(Validator):
    def __init__(self, value, **kwargs):
        self.value = value

        max = kwargs.get('max', None)
        if max is not None and not isinstance(max, int):
            raise ValidatorError('maximum value must be an integer')
        self.max = max

        min = kwargs.get('min', None)
        if min is not None and not isinstance(min, int):
            raise ValidatorError('minimum value must be an integer')
        self.min = min

        super(IntegerValidator, self).__init__(value, **kwargs)

    def validate(self):
        if not isinstance(self.value, int):
            raise NotValid('value is not instance of string')

        if self.min and self.value < self.min:
            raise NotValid('integer lower than minimum')

        if self.max and self.value > self.max:
            raise NotValid('integer higher than maximum')

        return True
