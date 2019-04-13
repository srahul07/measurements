# -*- coding: utf-8 -*-
from tests.test_base import TestBase

from tests.test_custom_lengths import Foot


class TestFoot(TestBase):

    def test_foot_to_inch_conversion_equivalence(self):
        inch = Foot(**{'in': 2.0})
        assert inch.value == 24.0

    def test_foot_to_meter_conversion_equivalence(self):
        meter = Foot(**{'m': 2.0})
        assert meter.value != 0.6

    def test_get_aliases(self):
        aliases = Foot.get_aliases()
        assert 'inches' not in aliases

    def test_default_unit_values(self):
        value = Foot().default_unit_value({'ft': 5.0})
        assert value > 0
