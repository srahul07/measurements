from lengths.utils import get_all_lengths, get_unit_class

class Converter(object):
    """class to represent converter that will be used to convert units
    
    """
    def __length_converter(self, value, from_unit, to_unit):
        from_length = get_unit_class(from_unit)
        if not from_length:
            raise AttributeError("Invalid {from_unit} is supplied.".format(from_unit=from_unit))
        units = from_length.get_units()
        # Get length type target which to convert
        to_length = get_unit_class(to_unit)
        if not to_length:
            raise AttributeError("Invalid {to_unit} is supplied.".format(to_unit=to_unit))
        default_unit = to_length.get_default_unit()
        return units[default_unit] * value if default_unit in units else 0

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """Method to convert length from one unit to another
        
        :param value: Value to be conveteds
        :type value: float
        :param from_unit: Original unit of the value
        :type from_unit: str
        :param to_unit: Unit into which value needs to be converted
        :type to_unit: str
        :raises AttributeError: Raise Error if invalid units are provided
        :return: key value pairs of value and unit
        :rtype: dict
        """
        result = cls().__length_converter(value, from_unit, to_unit)

        return {
            "source_value": value,
            "source_unit": from_unit,
            "target_value": result,
            "target_unit": to_unit
        }

    @classmethod
    def convert_to_length(cls, value, from_unit, to_unit):
        """Method to convert length from one unit to another
        
        :param value: Value to be conveteds
        :type value: float
        :param from_unit: Original unit of the value
        :type from_unit: str
        :param to_unit: Unit into which value needs to be converted
        :type to_unit: str
        :raises AttributeError: Raise Error if invalid units are provided
        :return: converted length in new unit
        :rtype: str
        """
        result = cls().__length_converter(value, from_unit, to_unit)
        return "{0} {1}".format(result, to_unit)
    
    @classmethod
    def convert_to_all(cls, value, unit, lengths=None):
        """Method to convert length of one type to all the available unit types
        
        :param value: value to be converted
        :type value: float
        :param unit: Original unit
        :type unit: str
        :param lengths: list of units to convet to, defaults to None
        :param lengths: list, optional
        :raises ValueError: Raise Error if invalid units are provided
        :return: converted length in all the possible units
        :rtype: list
        """
        converted_length = []
        if lengths is None:
            lengths = get_all_lengths()
        if lengths:
            aliases = [length.get_default_unit() for length in lengths if length.get_default_from_aliases(unit)]
            if aliases:
                unit = aliases[0]
        for length in lengths:
            unit = unit.lower()
            try:
                converted_length.append(str(length(**{unit: value})))
            except Exception:
                raise AttributeError("Invalid length unit found for {0} {1}; checked {3}".format(value, unit, ', '.join([length.__name__ for length in lengths])))
        return converted_length

