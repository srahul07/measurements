from base import LengthBase


class Meter(LengthBase):
    """class representing Length in Meter

    :param LengthBase: [description]
    :type LengthBase: [type]
    """
    DEFAULT_UNIT = 'm'
    UNITS = {
        'in': 39.37,
        'm': 1.0,
        'yd': 0.9144
    }
    ALIAS = ['m', 'metre', 'metres', 'meter', 'meters']
