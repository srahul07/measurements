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
        return cls.ALIAS.copy()

    @classmethod
    def has_alias(cls, alias):
        return alias in cls.ALIAS
    
    @classmethod
    def get_default_from_aliases(self, unit):
        return self.DEFAULT_UNIT if self.has_alias(unit) else None
        
    def default_unit_value(self, kwargs):
        aliases = self.get_aliases()
        units = self.get_units()
        val = 0.0
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
        if not isinstance(value, float):
            value = float(value)
        
        return unit * value

