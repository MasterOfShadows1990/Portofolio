
### Dezvoltare
def adunare(x, y):
    return x + y


### Testare
def test_adunare():
    assert adunare(4, 5) == 9, "Rezultatul nu este corect"
    assert adunare(2, 3) == 5, "Rezultatul nu este corect"

test_adunare()