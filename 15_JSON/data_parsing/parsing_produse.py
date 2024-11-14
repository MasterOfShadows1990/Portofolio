import json


categorie_cautata = input("Introdu categoria de produse pe care dorești să o vezi (ex. Electronice, Mobilier, etc.): ")


with open('15_JSON/data_parsing/produse.json', 'r') as file:
    produse = json.load(file)


print(f"Produse din categoria '{categorie_cautata}' care sunt în stoc:")
for produs in produse:
    
    if produs['categorie'] == categorie_cautata and produs['in_stoc']:
        print(f"Nume: {produs['nume']}")
        print(f"Preț: {produs['pret']} RON")
        print("-" * 20)
