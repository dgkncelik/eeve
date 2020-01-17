class NonValidatedError(Exception):
    pass


class ValidationConfigurationError(Exception):
    pass


class Validator(object):
    def __init__(self, value):
        self.value = value

    def validate(self):
        pass
