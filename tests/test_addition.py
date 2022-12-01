import pytest
from calculator.calculator import Calculator

class TestCalculatorAdditionTests:

    # Test that the add method returns the correct value when passed two or more integers 
    def test_add_method_returns_correct_result(self):
        num_list = [5, 5, 5]
        calc = Calculator()
        result = calc.add_two_or_more(num_list)
        assert result == 15