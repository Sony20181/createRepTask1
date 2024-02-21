import unittest

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True

class TestIsPrime(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-1))

if __name__ == '__main__':
    unittest.main()