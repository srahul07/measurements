# -*- coding: utf-8 -*-
import pytest

from lengths.utils import get_child_members_list
from lengths.base import LengthBase
from lengths import units
from lengths.units.inch import Inch


class TestUtils(object):

    def test_get_child_members_list(self):
        lengths = get_child_members_list(units, LengthBase)
        with pytest.raises(AssertionError):
            assert Inch not in lengths
