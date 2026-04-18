import unittest
from age import categorize_by_age

class TestSubtestAge(unittest.TestCase):
    
    def test_is_child(self):
        """Tests all valid ages in the Child range (0-9)"""
        
        for age in range(0, 10):
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Child")

    def test_is_adult(self):
        """Tests all valid ages in the Adult range (19-65)"""
        
        for age in range(19, 66):
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Adult")

    def test_is_golden(self):
        """Tests all valid ages in the Golden age range (66-150)"""
        for age in range(66, 151):
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Golden age")

if __name__ == "__main__":
    unittest.main(verbosity=2)