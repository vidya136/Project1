import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 3 == calculator.subtract(4, 1)


if __name__ == '__main__':
    unittest.main()
