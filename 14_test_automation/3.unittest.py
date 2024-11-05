import unittest

def is_String(x):
    return isinstance(x, str)

class TestString(unittest.TestCase):
    def test_is_string(self):
        self.assertEqual(is_String("hello"),True)

    def test_is_not_string(self):
        self.assertNotEqual(is_String(3),True)

if __name__ == "__main__":
    unittest.main()