import pytest 

from pursuit import game
from . import test_data as data
# import test_data as data 

@pytest.mark.unit
class TestGame:

    @pytest.mark.parametrize(*data.test_add_correct_data())
    def test_add(self, a, b, expected):
        # Arrange

        # Act
        result = game.add(a, b)

        # Assert
        assert result == expected



