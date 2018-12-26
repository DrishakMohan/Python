"""
    Name:Drishak Mohan
	Date: December 1th, 2018
	Description: Introduction to unit tes using example from Intro_Doc_Test.py .
"""



import unittest

# Globally Defined Output Message
msg = 'abs({}): expected {}, received {}'

# Function (from previous) Absolute Value
def abs(x):
    if x < 0:
        return -x
    return x

# Class in which I'm creating my Unit Tests
class TestNumbers(unittest.TestCase):
    def test_positive(self):
        input = 8
        expected = 8
        result = abs(input)
        self.assertEqual(expected, result, msg.format(input, expected, result))

    def test_negative(self):
        input = -2
        expected = 2
        result = abs(input)
        self.assertEqual(expected, result, msg.format(input, expected, result))

    def test_zero(self):
        input = 0
        expected = 0
        result = abs(input)
        self.assertEqual(expected, result, msg.format(input, expected, result))


if __name__ == '__main__':
    unittest.main()