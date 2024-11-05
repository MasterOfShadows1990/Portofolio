"""
    Valori 
           TVA - 9 % alimente, imobiliare pana la 120k
           TVA - 19 % restul
"""

import enum

class Bunuri(enum.Enum):
    ALIMENTE = "alimente"
    IMOBILIARE = "imobiliare"
    RESTUL = "Alte produse"

def valoare_cu_tva(pret, tip_bun):
    if tip_bun == Bunuri.ALIMENTE:
        return pret  + pret * 9 / 100
    elif tip_bun == Bunuri.IMOBILIARE and pret < 120_000:
        return pret  + pret * 9 / 100
    else:
        return pret  + pret * 19 / 100
    

def test_tva():
    assert valoare_cu_tva(100, Bunuri.ALIMENTE) == 109, "Valoare pentru alimente este de 9%"
    assert valoare_cu_tva(100, Bunuri.RESTUL) == 119, "Valoare pentru alimente este de 19%"

    assert valoare_cu_tva(100, Bunuri.IMOBILIARE) == 109, "Valoare pentru imobiliare este de 9% pana la 120k"
    assert valoare_cu_tva(1_000_000, Bunuri.IMOBILIARE) == 1_190_000, "Valoare pentru imobiliare este de 19% peste 120k"


if __name__ == "__main__":
    test_tva()



