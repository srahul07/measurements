from lengths.base import LengthBase


__all__ = ['Inch']

"""Inch objects to allow for conversion.

"""
class Inch(LengthBase):
    """Class representing Length in Inch.

    """
    DEFAULT_UNIT = 'in'
    UNITS = {
        'in': 1.0,
        'm': 0.0254,
        'yd': 0.02778
    }
    ALIAS = ['in', 'inch', 'inches']

