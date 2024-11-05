import unittest

def este_bisect(an):
    return an % 400 == 0 or (an % 4 == 0  and an % 100 != 0) 

class TestBisect(unittest.TestCase):
    
    def test_divizibil_cu_4(self):
        self.assertTrue(este_bisect(2024))

    def test_nu_este_divizibil_cu_4(self):
        self.assertFalse(este_bisect(2023))
    
    def test_este_divizibil_cu400(self):
        self.assertTrue(este_bisect(2000))

    def test_este_divizibil_cu100_dar_nu_cu_400(self):
        self.assertFalse(este_bisect(2100))

if __name__ == "__main__":
    unittest.main()
