# -*- coding: utf-8 -*-
from tests.test_base import TestBase

from lengths.units.yard import Yard


class TestYard(TestBase):

    def test_yard_to_inch_conversion_equivalence(self):
        inch = Yard(**{'in': 2.0})
        assert inch.value != 0.02
    
    def test_yard_to_meter_conversion_equivalence(self):
        meter = Yard(**{'m': 2.0})
        assert meter.value == 1.8288
    
    def test_get_aliases(self):
        aliases = Yard.get_aliases()
        assert 'inches' not in aliases
    
    def test_default_unit_values(self):
        value = Yard().default_unit_value({'yd': 5.0})
        assert value > 0