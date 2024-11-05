### Test driven development

def conversie_celsius_fahrenheit(temp):
    try:
        temp = float(temp)
    except:
        return None
    return (temp * 9/5) + 32

def test_temperatura():
    assert conversie_celsius_fahrenheit(100) == 212, "Formula incorecta"
    assert conversie_celsius_fahrenheit(0) == 32, "Formula incorecta"

    assert conversie_celsius_fahrenheit("100") == 212, "Formula incorecta"
    assert conversie_celsius_fahrenheit("100.0") == 212, "Formula incorecta"


if __name__ == "__main__":
    test_temperatura()