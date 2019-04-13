# -*- coding: utf-8 -*-
from tests.test_base import TestBase

from lengths.units.meter import Meter


class TestMeter(TestBase):

    def test_meter_to_yard_conversion_equivalence(self):
        yard = Meter(**{'yd': 2.0})
        assert yard.value != 0.02

    def test_meter_to_inch_conversion_equivalence(self):
        inch = Meter(**{'in': 2.0})
        assert inch.value == 78.74

    def test_get_aliases(self):
        aliases = Meter.get_aliases()
        assert 'metre' in aliases

    def test_default_unit_values(self):
        value = Meter().default_unit_value({'yd': 5.0})
        assert value > 0
