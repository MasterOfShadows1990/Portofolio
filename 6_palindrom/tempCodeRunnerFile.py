cuvinte = input("Introduceti cuvintele: ").split()

for cuvant in cuvinte:
    if cuvant == cuvant[::-1]:
        print(cuvant)
    else:
        print("Cuvantul",cuvant ,"nu este un palindrom")