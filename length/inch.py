from base import LengthBase


class Inch(LengthBase):
    """Class representing Length in Inch.

    :param LengthBase: [description]
    :type LengthBase: [type]
    """
    DEFAULT_UNIT = 'in'
    UNITS = {
        'in': 1.0,
        'm': 0.0254,
        'yd': 0.02778
    }
    ALIAS = ['in', 'inch', 'inches']
