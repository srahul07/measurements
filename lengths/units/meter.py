from lengths.base import LengthBase


__all__ = ['Meter']

"""Meter objects to allow for conversion.

"""
class Meter(LengthBase):
    """class representing Length in Meter

    """
    DEFAULT_UNIT = 'm'
    UNITS = {
        'in': 39.37,
        'm': 1.0,
        'yd': 1.09361
    }
    ALIAS = ['m', 'metre', 'metres', 'meter', 'meters']

