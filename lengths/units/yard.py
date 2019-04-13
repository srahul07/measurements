from lengths.base import LengthBase


__all__ = ['Yard']

"""Yard objects to allow for conversions

"""
class Yard(LengthBase):
    """class representing Length in Yard

    """
    DEFAULT_UNIT = 'yd'
    UNITS = {
        'in': 36,
        'm': 0.9144,
        'yd': 1.0
    }
    ALIAS = ['yd', 'yard', 'yards']
    
