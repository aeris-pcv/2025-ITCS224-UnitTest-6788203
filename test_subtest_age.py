import unittest
from age import categorize_age

class TestCategorizeByAge(unittest.TestCase):

    def test_child(self):
        for age in [0, 5, 12]:
            with self.subTest(age=age):
                self.assertEqual(categorize_age(age), "Child")

    def test_adult(self):
        for age in [18, 30, 59]:
            with self.subTest(age=age):
                self.assertEqual(categorize_age(age), "Adult")

    def test_golden_age(self):
        for age in [60, 70, 80]:
            with self.subTest(age=age):
                self.assertEqual(categorize_age(age), "Golden Age")

if __name__ == "__main__":
    unittest.main(verbosity=2)