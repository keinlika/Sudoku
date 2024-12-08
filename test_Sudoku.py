'''This is a driver'''
from Lab06 import parse_pos
import pytest

# parse_pos returns (row, col), where row is the number and col is the letter.

def test_parse_pos_boundaries():
    '''Test the boundaries for the parameters passed into parse_pos'''

    # Test the first column and first row.
    assert parse_pos("A1") == (0, 0)

    # Test the first column and a middle row.
    assert parse_pos("A5") == (4, 0)

    # Test the first column and the last row.
    assert parse_pos("A9") == (8, 0)

    # Test a middle column and the first row.
    assert parse_pos("D1") == (0, 3)

    # Test a middle column and a middle row.
    assert parse_pos("D5") == (4, 3)

    # Test a middle column and the last row.
    assert parse_pos("D9") == (8, 3)

    # Test the last column and first row.
    assert parse_pos("I1") == (0, 8)

    # Test the last column and a middle row.
    assert parse_pos("I6") == (5, 8)

    # Test the last column and last row.
    assert parse_pos("I9") == (8, 8)


def test_parse_pos_requirements():
    '''Test typical valid entries for the parameters passed into parse_pos'''

    # Test casing.
    assert parse_pos("B1") == (0, 1)
    assert parse_pos("b1") == (0, 1)

    # Test order.
    assert parse_pos("C7") == (6, 2)
    assert parse_pos("7C") == (6, 2)

def test_parse_pos_errors():
    '''Test invalid entries for the parameters passed into parse_pos'''

    # Test incorrect parameter type; not a string.
    assert parse_pos(21) == (-1, -1)

    # Test too long; many numbers.
    assert parse_pos("A4512") == (-1, -1)

    # Test too long; many letters.
    assert parse_pos("Adfjkdlhfjc2")

    # Test too long; many letters and many numbers.
    assert parse_pos("fjkENKLD438230") == (-1, -1)

    # Test too short: one character.
    assert parse_pos("a") == (-1, -1)

    # Test too short: empty string.
    assert parse_pos("") == (-1, -1)

    # Test characters; one incorrect character.
    assert parse_pos("%A") == (-1, -1)

    # Test characters; two incorrect characters.
    assert parse_pos("%$") == (-1, -1)

# Call the main function in pytest so that the test functions in this file will
# execute.
pytest.main(["-v", "--tb=line", "-rN", __file__])
