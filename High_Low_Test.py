import unittest

import pytest
import high_low
from unittest.mock import Mock
from unittest.mock import patch

HL = high_low.High_Low()
def test_tdd1():
    assert HL.find_high_low([1, 5.3, 3.1, 9, 2])== (9, 1)
def test_tdd2():
    assert HL.find_high_low([5, 5, 5, 5])  ==  (5, 5)
def test_tdd3():
    assert HL.find_high_low([]) == (None,None)

def test_high_low_with_patch():
    with patch.object(high_low.High_Low, 'find_high_low', return_value=(7, 8)):
        assert HL.find_high_low([5,0,6,4])== (7,8)

class TestHighLow(unittest.TestCase):
    def test_high_low_with_Mock_side_effect(self):
        # Create an instance of the High_Low class
        HL = high_low.High_Low()

        # Redefine the find_high_low method using a mock object with a side effect
        HL.find_high_low = Mock(side_effect=[(10, 2), (6, 1), (None, None)])

        # Call the find_high_low method three times with different inputs
        result1 = HL.find_high_low([3, 5, 2, 10, 1])
        result2 = HL.find_high_low([4, 6, 1, 3])
        result3 = HL.find_high_low([])

        # Check that the results are as expected
        self.assertEqual(result1, (10, 2))
        self.assertEqual(result2, (6, 1))
        self.assertEqual(result3, (None, None))

if __name__ == '__main__':
        unittest.main()


def test_high_low_with_Mock():
    HL.find_high_low = Mock(return_value=(0,1))
    assert HL.find_high_low([5,2,10,12]) == (0,1)