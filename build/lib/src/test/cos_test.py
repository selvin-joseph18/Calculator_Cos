'''
Python Unit Testing Script
'''
import calculator_cos
import unittest

class Cos_Test(unittest.TestCase):
    def test_positive_angle_values(self):
        self.assertEqual(0.15425144988758405, calculator_cos.calculate_cos(30))

    def test_negative_angle_values(self):
        self.assertEqual(-0.7596879128588213, calculator_cos.calculate_cos(-15))