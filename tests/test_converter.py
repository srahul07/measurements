# -*- coding: utf-8 -*-
from lengths.converter import Converter

class TestConveter(object):

    def test_convert_check_return_type(self):
        convert = Converter.convert(2, "yd", "inches")
        assert type(convert) == dict
    
    def test_convert(self):
        convert = Converter.convert(3, 'in', 'metres')
        assert convert == {'source_unit': 'in', 
                           'source_value': 3, 
                           'target_unit': 'metres', 
                           'target_value': 0.07619999999999999}

    def test_convert_to_all(self):
        convert = Converter.convert_to_all(2, "yards")
        assert "1.8288 m" in convert
    
    def test_convert_to_length(self):
        convert = Converter.convert_to_length(2, "yard", 'in')
        assert convert == "72 in"