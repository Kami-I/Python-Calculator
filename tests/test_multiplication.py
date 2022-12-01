import pytest
from calculator.calculator import Calculator

class TestCalculatorMultiplicationTests:
    
        # Test that the multiplication method returns the correct value when passed two integers
        def test_multiplication_method_returns_correct_result(self):
            # Issue https://github.com/Kami-I/Python-Calculator/issues/10
            # Tom and two co-workers have $5 to spend each for a pizza and want to know what price pizza they can afford:
            # Equation : $5 x 3 
            # Expected result = $15
                
                num_to_multiply = 5
                num_of_times = 3


                expected_result = 15
                calc = Calculator()
                result = calc.multiply(num_to_multiply, num_of_times)
                assert result == expected_result