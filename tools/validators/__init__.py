class NotValid(Exception):
    pass


class ValidatorError(Exception):
    pass


class Validator(object):
    def __init__(self, value, **kwargs):
        self.value = value

    def validate(self):
        pass
