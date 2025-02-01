# write a function to generate sum of two numbbers
def add(a, b):
    return a + b

# Unit tests for the add function
import unittest

class TestAddFunction(unittest.TestCase):
    
    def test_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)
        
    def test_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)
        
    def test_mixed_numbers(self):
        self.assertEqual(add(-1, 2), 1)
        
    def test_zero(self):
        self.assertEqual(add(0, 0), 0)
        
if __name__ == '__main__':
    unittest.main()
