import unittest

def este_palindrom(cuvant:str):

    if len(cuvant)<2: return False
    cuvant = cuvant.replace(" ","")


    if not cuvant.isalpha():return False
    cuvant = cuvant.lower()
    return cuvant == cuvant [::-1]
    #return cuvant == "".join(reversed(cuvant))


class TestPalindrom(unittest.TestCase):
    def test_palindrom(self):
        self.assertTrue(este_palindrom("cojoc"))
        self.assertTrue(este_palindrom("capac"))

    def test_nu_este_palindrom(self):
        self.assertFalse(este_palindrom("colac"))
        self.assertFalse(este_palindrom("copac"))

    def test_numarul_nu_este_palindrom(self):
        self.assertFalse(este_palindrom("121"))
        self.assertFalse(este_palindrom("2331"))
        self.assertFalse(este_palindrom("c0j0c"))

    def test_semnul_de_punctuatie_nu_este_palindrom(self):
        self.assertFalse(este_palindrom("ca!ac"))

    def test_capitalizarea_este_palindrom(self):
        self.assertFalse(este_palindrom("Cojoc"))

    def test_nu_ia_in_considerare_spatiile_libere(self):
        self.assertTrue(este_palindrom("ele fac cafele"))

    def test_numar_caractere_min_2(self):
        self.assertFalse( este_palindrom("a"))
        self.assertFalse( este_palindrom("  "))


if __name__ == "__main__":
    unittest.main()