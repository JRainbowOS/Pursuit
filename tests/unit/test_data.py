import pytest 
from pytest import param

def test_add_correct_data():
    test_variables = 'a, b, expected'
    test_data = [
        param(
            1,
            2,
            3,
            id='easy'
        ),
        param(
            -1,
            -2,
            -3,
            id='negative'
        ),
        param(
            1e10,
            2e10,
            3e10,
            id='large'
        )
    ]
    return test_variables, test_data