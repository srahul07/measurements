# -*- coding: utf-8 -*-
import pytest

from lengths.utils import get_all_lengths, get_unit_class
from lengths.units.inch import Inch
from lengths.units.meter import Meter
from lengths.units.yard import Yard


class TestUtils(object):

    def test_get_all_lengths(self):
        lengths = get_all_lengths()
        with pytest.raises(AssertionError):
            assert Inch not in lengths
    
    def test_get_unit_class_not_inch(self):
        length = get_unit_class('metre')
        assert length is not Inch
    
    def test_get_unit_class_is_meter(self):
        length = get_unit_class('meter')
        assert length is Meter
    
    def test_get_unit_class_not_equal_yard(self):
        length = get_unit_class('m')
        assert length != Yard