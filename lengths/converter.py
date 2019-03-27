from lengths import units
from lengths.base import LengthBase
from lengths.utils import get_child_members_list

class Converter(object):
    """class to represent converter that will be used to convert units
    
    """
    def __init__(self):
        self.length_list = get_child_members_list(units, LengthBase)
    
    def add_length_list(self, lengths):
        if isinstance(lengths, list):
            self.length_list.extend(lengths)
        else:
            self.length_list.append(lengths)
    
    def get_length_list(self):
        return self.length_list
    
    def get_unit_class(self, unit):
        unit_class = None
        for length in self.length_list:
            if not length.has_alias(unit):
                continue
            unit_class = length
        if not unit_class:
            raise AttributeError("Invalid length unit {unit} is supplied.".format(unit=unit))
        return unit_class

    def _length_converter(self, value, source_unit, target_unit):
        # Get length type source details
        source_length = self.get_unit_class(source_unit)
        if not source_length:
            raise AttributeError("Invalid length unit {from_unit} is supplied.".format(from_unit=source_unit))
        source_units = source_length.get_units()
        source_default_unit = source_length.get_default_unit()

        # Get length type target details
        target_length = self.get_unit_class(target_unit)
        if not target_length:
            raise AttributeError("Invalid length unit {to_unit} is supplied.".format(to_unit=target_unit))
        target_default_unit = target_length.get_default_unit()

        if target_default_unit not in source_units:
            # If target converter is not present in source units, 
            # Check if the source default unit is present in target units
            if source_default_unit not in target_length.get_units().keys():
                raise AttributeError("Length unit converter for {from_unit} to {unit} does not exists.".format(unit=target_unit, from_unit=source_unit))

            source_units[target_default_unit] = 1/target_length.get_units()[source_default_unit]
        return source_units[target_default_unit] * value

    def convert(self, value, from_unit, to_unit):
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
        result = self._length_converter(value, from_unit, to_unit)

        return {
            "source_value": value,
            "source_unit": from_unit,
            "target_value": result,
            "target_unit": to_unit
        }

    def convert_to_length(self, value, from_unit, to_unit):
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
        result = self._length_converter(value, from_unit, to_unit)
        return "{0:.4f} {1}".format(result, to_unit)
    
    def convert_to_all(self, value, unit, lengths=None):
        """Method to convert length of one type to all the available unit types
        
        :param value: value to be converted
        :type value: float
        :param unit: Original unit
        :type unit: str
        :param lengths: list of units to convert to, defaults to None
        :param lengths: list, optional
        :raises ValueError: Raise Error if invalid units are provided
        :return: converted length in all the possible units
        :rtype: list
        """
        converted_length = []
        unit = unit.lower()
        if not lengths:
            lengths = self.get_length_list()
        elif isinstance(lengths, str):
            # It's an alias name of the length, get unit class from it and convert it to list
            lengths = [self.get_unit_class(lengths)]
        for length in lengths:
            converted_length.append(self.convert_to_length(value, unit, length.__name__.lower()))
        return converted_length

