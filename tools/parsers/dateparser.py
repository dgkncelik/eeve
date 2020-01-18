DATE_STRING_FORMATS = ['%Y-%m-%dT%H:%M:%S%z',
                       '%Y-%m-%dT%H:%M:%S',
                       '%Y-%m-%d',
                       '%Y-%m-%dT%H:%M:%S.%fZ',
                       '%d.%m.%Y %H:%M']


class DateParser(object):
    def __init__(self):
        pass

    @staticmethod
    def now():
        pass

    @staticmethod
    def now_timestamp():
        pass

    @staticmethod
    def str2date(date_string, date_format=None):
        pass

    @staticmethod
    def date2str(date, output_format=None):
        pass

    @staticmethod
    def date2unix(date):
        pass

    @staticmethod
    def unix2date(unix_timestamp):
        pass

    @staticmethod
    def string2unix(date_string, date_format=None):
        pass
