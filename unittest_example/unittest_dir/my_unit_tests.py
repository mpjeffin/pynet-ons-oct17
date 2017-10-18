import unittest
from my_functions import my_sum, hello_world

class Simplistic(unittest.TestCase):
    def test(self):
        self.assertTrue(True)

    def test_my_sum(self):
        self.assertEqual(12, my_sum(10, 2))
        self.assertEqual(99, my_sum(49, 50))

    def test_hello_world(self):
        self.assertEqual("Hello world", hello_world())

    def whatever(self):
        print("zzz")

if __name__ == '__main__':
    unittest.main()
