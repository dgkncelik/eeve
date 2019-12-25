class Consumer(object):
    def __init__(self, *args, **kwargs):
        pass

    def configure(self, *args, **kwargs):
        raise NotImplementedError

    def consume(self, *args, **kwargs):
        raise NotImplementedError

    def get(self, *args, **kwargs):
        raise NotImplementedError
