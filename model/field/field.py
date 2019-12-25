class Field(object):
    def __init__(self, key, value, primitive_type, required, default=None):
        self.key = key
        self.value = value
        self.default = default
        self.required = required
        self.primitive_type = primitive_type

    def validate(self):
        pass
