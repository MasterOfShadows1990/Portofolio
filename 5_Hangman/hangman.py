# Exercițiul: Jocul de Hangman
# Cerință:
# Scrie un joc de Hangman în Python în care utilizatorul trebuie să ghicească un cuvânt ascuns. Utilizatorul are un număr limitat de încercări pentru a ghici întregul cuvânt.

# Pași de rezolvare:
# Inițializarea cuvântului de ghicit:
# Alege un cuvânt aleatoriu dintr-o listă de cuvinte prestabilită sau permite utilizatorului să introducă un cuvânt.

# Afisarea cuvantului ascuns:
# Afișează cuvântul sub formă de liniuțe sau spații pentru literele neîncă descoperite și literele ghicite până acum.

# Primirea ghicirii utilizatorului:
# Permite utilizatorului să introducă o literă și verifică dacă aceasta face parte din cuvântul de ghicit.

# Verificarea ghicirii:
# Verifică dacă litera introdusă de utilizator se regăsește în cuvântul de ghicit. Actualizează cuvântul afișat în consecință.

# Numărarea încercărilor:
# Monitorizează numărul de încercări pe care le-a avut utilizatorul și oprește jocul dacă acesta a depășit un anumit număr de încercări.

# Afișarea rezultatului:
# Afișează rezultatul jocului (cuvântul de ghicit și dacă utilizatorul a ghicit sau nu).

import random

def choose_word():
    words = ["hangman","python","programming","computer","game"]
    return random.choice(words)

def display_word(word,guessed_lettters):
    display_word = ""
    for letter in word:
        if letter in guessed_lettters:
            display_word += letter
        else:
            display_word += "_"
    return display_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6


    print("Bine ati venit la jocul Hangman!")
    print("Cuvantul de ghicit:",display_word(word,guessed_letters))

    while True:
        guess = input("Introduceti o litera: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Introduceti o singura litera valida!")
            continue
        if guess in guessed_letters:
            print("Ati ghicit deja aceasta litera!")
            continue
        guessed_letters.append(guess)
        
        if guess not in word:
            attempts -= 1
            print("Litera",guess,"nu se regaseste in cuvant.Mai aveti",attempts,"incercari.")
            if attempts == 0:
                print("Ai pierdut!Cuvantul era:",word)
                break
        else:
            print("Felicitari!Litera",guess,"se regaseste in cuvantul ghicit:",display_word(word,guessed_letters))
            if "_" not in display_word(word,guessed_letters):
                print("Ai ghicit cuvantul!Cuvantul era:",word)
                break

if __name__ == "__main__":
    hangman()