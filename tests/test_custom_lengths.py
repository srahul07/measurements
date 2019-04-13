from lengths.base import LengthBase


class Foot(LengthBase):
    DEFAULT_UNIT = 'ft'
    UNITS = {
        'in': 12.0,
        'm': 0.3048,
        'yd': 0.3333,
        'ft': 1.0
    }
    ALIAS = ['ft', 'foot', 'feet']


class Kilometer(LengthBase):
    DEFAULT_UNIT = 'km'
    UNITS = {
        'in': 39370.1,
        'm': 1000,
        'yd': 1093.61,
        'ft': 3280.84,
        'km': 1.0,
    }
    ALIAS = ['km', 'kilometer', 'kilometers', 'kilometre', 'kilometres']
