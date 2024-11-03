import random
import time 

def genereaza_perechi():
    nr = random.randint(0, 36)
    culoare = random.choice(["rosie", "neagra"])
    return nr,culoare if nr else "verde"


rezultat = genereaza_perechi()
culoare = rezultat[1]
print(rezultat)
print(culoare)

def joaca_pana_dai_de_verde():
    nr, culoare =  genereaza_perechi()
    while culoare != "verde":
        nr, culoare =  genereaza_perechi()
        print(nr, culoare)
        time.sleep(0.1)

def joaca_de_10_ori_si_mergi_acasa():
    for i in range(10):
        nr, culoare =  genereaza_perechi()
        print(nr, culoare)
        if culoare == "verde":
            print("Ai castigat!")
            break
        time.sleep(0.1)
    else:
        print("Nu ai castigat")

joaca_pana_dai_de_verde()
