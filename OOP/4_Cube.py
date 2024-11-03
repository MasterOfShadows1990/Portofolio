import threading

class Cub:
    def __init__(self, latura):
        self.latura = latura

    def calcul_lungime_totala(self):
        lungime_totala = 12 * self.latura
        print(f"Lungime totala a laturilor: {lungime_totala}")

    def calcul_volum(self):
        volum = self.latura ** 3
        print(f"Volumul cubului: {volum}")


cub1 = Cub(3)
cub2 = Cub(5)


fir_lungime_totala = threading.Thread(target=cub1.calcul_lungime_totala)

fir_lungime_totala.start()


fir_lungime_totala.join()


cub2.calcul_volum()


