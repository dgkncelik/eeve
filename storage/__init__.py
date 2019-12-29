class Storage(object):
    def __init__(self, *args, **kwargs):
        pass

    def configure(self, *args, **kwargs):
        raise NotImplementedError

    def find(self, *args, **kwargs):
        raise NotImplementedError

    def save(self, *args, **kwargs):
        raise NotImplementedError

    def update(self, *args, **kwargs):
        raise NotImplementedError

    def delete(self, *args, **kwargs):
        raise NotImplementedError
