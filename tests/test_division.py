import pytest
from calculator.calculator import Calculator

class TestCalculatorDivisionTests:
    
        # Test that the division method returns the correct value when passed argument
        def test_division_method_returns_correct_result(self):
            # Issue https://github.com/Kami-I/Python-Calculator/issues/8
            # Tom and two co-workers share a $15 pizza for lunch and each person wants to pay their share :
            # Equation : $15/3
            # Expected result = $5
                num_of_people = 3
                total = 15
                expected_result = 5
                calc = Calculator()
                result = calc.divide(total, num_of_people)
                assert result == expected_result