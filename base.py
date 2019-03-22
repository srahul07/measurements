

class LengthBase(object):
    """Base class for length conversions

    """
    DEFAULT_UNIT = ''
    UNITS = {}
    ALIAS = []

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
