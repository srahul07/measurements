# -*- coding: utf-8 -*-
import pytest
from lengths.converter import Converter
from lengths.base import LengthBase
from lengths.units.inch import Inch
from lengths.units.meter import Meter
from lengths.units.yard import Yard
from tests.test_custom_lengths import Foot, Kilometer


class TestConverter(object):

    def test_get_length_list(self):
        converter = Converter()
        assert Foot not in converter.get_length_list()

    def test_single_add_length_list(self):
        converter = Converter()
        converter.add_length_list(Foot)
        assert Foot in converter.get_length_list()

    def test_multi_add_length_list(self):
        converter = Converter()
        converter.add_length_list([Foot, Kilometer])
        with pytest.raises(AssertionError):
            assert Kilometer not in converter.get_length_list()

    def test_get_unit_class(self):
        converter = Converter()
        converter.add_length_list(Kilometer)
        assert Kilometer == converter.get_unit_class("km")

    def test_get_unit_class_not_inch(self):
        converter = Converter()
        length = converter.get_unit_class('metre')
        assert length is not Inch

    def test_get_unit_class_is_meter(self):
        converter = Converter()
        length = converter.get_unit_class('meter')
        assert length is Meter

    def test_get_unit_class_not_equal_yard(self):
        converter = Converter()
        length = converter.get_unit_class('m')
        assert length != Yard

    def test_convert_check_return_type(self):
        converter = Converter()
        convert = converter.convert(2, "yd", "inches")
        assert type(convert) == dict

    def test_convert(self):
        converter = Converter()
        convert = converter.convert(3, 'in', 'metres')
        assert convert == {'source_unit': 'in',
                           'source_value': 3,
                           'target_unit': 'metres',
                           'target_value': 0.07619999999999999}

    def test_convert_to_all(self):
        converter = Converter()
        convert = converter.convert_to_all(2, "yards")
        assert "1.8288 meter" in convert

    def test_km_convert_to_all(self):
        converter = Converter()
        converter.add_length_list(Foot)
        convert = converter.convert_to_all(2, "yards")
        assert "0.0018 km" not in convert

    def test_convert_to_length(self):
        converter = Converter()
        convert = converter.convert_to_length(2, "yard", 'in')
        assert convert == "72.0000 in"

    def test_convert_to_length_feet(self):
        converter = Converter()
        converter.add_length_list([Foot, Kilometer])
        convert = converter.convert_to_length(2, "yard", 'feet')
        assert convert == "6.0006 feet"
