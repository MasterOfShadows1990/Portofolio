# Scrie un program care primește de la utilizator un număr întreg pozitiv și calculează factorialul acestuia.

# Pași de rezolvare:
# Primirea numărului de la utilizator:
# Folosește funcția input() pentru a permite utilizatorului să introducă numărul întreg pozitiv pentru care se va calcula factorialul.

# Verificarea numărului:
# Asigură-te că numărul introdus de utilizator este un număr întreg pozitiv.

# Calcularea factorialului:
# Folosește o buclă for pentru a calcula factorialul numărului introdus.

# Afișarea rezultatului:
# Afișează factorialul calculat.


numar = int(input("Introdu un numar intreg pozitiv: "))

factorial = 1

if numar < 0:
    print("Factorialul nu poate fi calculat pentru numere negative.")
elif numar == 0:
    print("Factorialul lui 0 este 1.")
else:
    print("Factorialurile numerelor pana la",numar,"sunt:")
    for i in range(1, numar + 1):
        factorial *= i
        print("Factorialul lui",i ,"este", factorial)

