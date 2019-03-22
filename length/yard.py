from base import LengthBase


class Yard(LengthBase):
    """class representing Length in Yard

    :param LengthBase: [description]
    :type LengthBase: [type]
    """
    DEFAULT_UNIT = 'yd'
    UNITS = {
        'in': 36,
        'm': 0.9144,
        'yd': 1.0
    }
    ALIAS = ['yd', 'yard', 'yards']
