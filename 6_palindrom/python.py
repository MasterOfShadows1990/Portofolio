# Găsirea cuvintelor palindrome într-o listă de cuvinte

# Primirea listei de cuvinte de la utilizator:
# Folosește funcția input() pentru a permite utilizatorului să introducă cuvintele în listă.

# Verificarea cuvintelor palindrome:
# Parcurge fiecare cuvânt din listă și verifică dacă este palindrom sau nu.

# Afișarea cuvintelor palindrome:
# Afișează doar cuvintele care sunt palindrome.

cuvinte = input("Introduceti cuvintele separate prin spatiu: ").split()

print("Cuvintele palindrome din lista sunt:")

for cuvant in cuvinte:
    if cuvant == cuvant[::-1]:
        print(cuvant)
    else:
        print("Din pacate ", cuvant ,"nu se regaseste ca si palindrom")



#Alt exemplu
# while True:
#     sir = input("Introduceti un cuvant pentru al transforma: ")
#     invers = sir[::-1]
#     print(invers)



