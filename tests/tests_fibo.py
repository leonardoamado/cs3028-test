import unittest
import os,sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.fibo import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), 0)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 1)
        self.assertEqual(fibonacci(6), 5)
        self.assertEqual(fibonacci(10), 34)
        
    def test_negative_input(self):
        self.assertEqual(fibonacci(-5), -1)

    def test_zero_input(self):
        self.assertEqual(fibonacci(0), -1)

if __name__ == "__main__":
    unittest.main()