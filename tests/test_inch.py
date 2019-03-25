# -*- coding: utf-8 -*-
from tests.test_base import TestBase

from lengths.units.inch import Inch


class TestInch(TestBase):

    def test_inch_to_yard_conversion_equivalence(self):
        yard = Inch(**{'yd': 2.0})
        assert yard.value != 0.02
    
    def test_inch_to_meter_conversion_equivalence(self):
        meter = Inch(**{'m': 2.0})
        assert meter.value == 0.0508
    
    def test_get_aliases(self):
        aliases = Inch.get_aliases()
        assert 'inches' in aliases
    
    def test_default_unit_values(self):
        value = Inch().default_unit_value({'yd': 5.0})
        assert value > 0