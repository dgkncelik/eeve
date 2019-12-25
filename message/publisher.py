class Publisher(object):
    def __init__(self, *args, **kwargs):
        pass

    def configure(self, *args, **kwargs):
        raise NotImplementedError

    def publish(self, *args, **kwargs):
        raise NotImplementedError
