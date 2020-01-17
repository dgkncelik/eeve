from tools.validators import Validator, NotValid, ValidatorError


class StringValidator(Validator):
    def __init__(self, value, **kwargs):
        self.value = value

        min_len = kwargs.get('min_len', None)
        if min_len is not None and not isinstance(min_len, int):
            raise ValidatorError('minimum length must be an integer')
        self.min_len = min_len

        max_len = kwargs.get('max_len', None)
        if max_len is not None and not isinstance(max_len, int):
            raise ValidatorError('maximum length must be an integer')
        self.max_len = max_len

        self.regex = kwargs.get('regex', None)
        self.allow_empty = kwargs.get('allow_empty', True)
        super(StringValidator, self).__init__(value, **kwargs)

    def validate(self):
        if not isinstance(self.value, str):
            raise NotValid('value is not instance of string')

        if self.allow_empty is False and self.value.strip() == '':
            raise NotValid('empty string is not allowed')

        if self.min_len and len(self.value) < self.min_len:
            raise NotValid('string length lower than allowed len=%s' % len(self.value))

        if self.max_len and len(self.value) > self.max_len:
            raise NotValid('string length higher than allowed len=%s' % len(self.value))

        if self.regex:
            import re
            if re.match(self.regex, self.value) is None:
                raise NotValid('regex not matched for value')

        return True
