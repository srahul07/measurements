from copy import copy
from lengths.utils import sys_version


class LengthBase(object):
    """Base class for length conversions
    
    """
    DEFAULT_UNIT = None
    UNITS = {}
    ALIAS = []

    def __init__(self, **kwargs):
        self.value = self.default_unit_value(kwargs)
    
    def __repr__(self):
        return "{0} {1}".format(self.value, self.DEFAULT_UNIT)
    
    @classmethod
    def get_default_unit(cls):
        return cls.DEFAULT_UNIT
    
    @classmethod
    def get_units(cls):
        return cls.UNITS.copy()

    @classmethod
    def get_aliases(cls):
        return cls.ALIAS.copy() if sys_version == 3 else copy(cls.ALIAS)

    @classmethod
    def has_alias(cls, alias):
        return alias in cls.ALIAS
    
    @classmethod
    def get_default_from_aliases(self, unit):
        return self.DEFAULT_UNIT if self.has_alias(unit) else None
        
    def default_unit_value(self, kwargs):
        """Convert value to unit provided in dictionary. This is the default conversion, hence the name.
        
        :param kwargs: dictionary containing unit and value as key-value pairs
        :type kwargs: dict
        :raises AttributeError: Exception to indicate invalid attribute / unit provided
        :return: converted value
        :rtype: float
        """
        aliases = self.get_aliases()
        val = 0.0
        units = self.get_units()
        for unit, value in kwargs.items():
            unit = unit.lower()
            if unit in units:
                val = self._convert_value_from(units[unit], value)
            elif unit in aliases:
                val = self._convert_value_from(units[self.DEFAULT_UNIT], value)
            else:
                raise AttributeError("Invalid length unit found for {0}".format(unit))
        return val

    
    def _convert_value_from(self, unit, value):
        """Convert value from object length type to unit type
        
        :param unit: unit conversion number / multiplier
        :type unit: float
        :param value: value of this unit type
        :type value: float / int (number)
        :return: unit converted value
        :rtype: float
        """
        if not isinstance(value, float):
            value = float(value)
        
        return unit * value

