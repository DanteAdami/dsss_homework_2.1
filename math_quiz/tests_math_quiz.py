import unittest
from math_quiz import function_random_integer, function_random_sign, function_operation


class TestMathGame(unittest.TestCase):

    def test_function_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_random_sign(self):
        # Test to check if the operator generated is within the options
        sign_plus = 0
        for _ in range(1000): # Test a large number of random inputs
            sign = function_random_sign()
            self.assertTrue(sign == '+' or sign == '-' or sign == '*')


    def test_function_operation(self):
            # Test the function operation. We first create some sample operations
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (8, 3, '-', '8 - 3', 5),
                (4, 6, '*', '4 * 6', 24),
                (9, 9, '-', '9 - 9', 0),
                (5, 0, '*', '5 * 0', 0),
                (1, 5, '+', '1 + 5', 6)
            ]
            # now for each operation, we make sure that the output of the function is the expected one
            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                expression, result = function_operation(num1, num2, operator)
                self.assertTrue(expression == expected_problem and result == expected_answer)

if __name__ == "__main__":
    unittest.main()


    