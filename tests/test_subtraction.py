import pytest
from calculator.calculator import Calculator

class TestCalculatorSubtractionTests:
    
        # Test that the subtract method returns the correct value when passed two integers
        def test_subtract_method_returns_correct_result(self):
            # Issue https://github.com/Kami-I/Python-Calculator/issues/9
            # Tom and two co-workers share a $15 pizza.
            # Tom and one coworker pay and want to determine how much the third coworker owes:
            # Equation = $15 - $5 + $5 = $15
            # Expected result = $15
                
                # BODMAS says we should do the addition first before substracting
                paid = 5 + 5
                total = 15


                expected_result = 5
                calc = Calculator()
                result = calc.subtract(paid, total)
                assert result == expected_result