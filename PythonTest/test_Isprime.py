
import unittest
from task2TestPython import *
class TestIsPrime(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(11))
     
    def test_is_not_prime(self):
      
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-1))


if __name__ == '__main__':
    unittest.main()