import time
import random

def ask_question(question, correct_answer, options=None):
    if options:
        print("Optiuni: ", " / ".join(options))
    
    answer = input(question + " ")
    
    if answer.lower() == correct_answer.lower():
        print("Corect! ✔️\n")
        return 1
    else:
        print(f"Incorect! ❌ Raspunsul corect era: {correct_answer}\n")
        return 0

def start_game():
    print("🕹️ Jocul Programatorului! 🕹️")
    playing = input("Doresti sa incerci jocul?\n").lower()

    if playing != "da":
        quit()

    print("Perfect, sa incepem atunci! 🎉\n")
    score = 0
    total_questions = 0

    # Listele de intrebari si raspunsuri
    questions = [
        {"question": "Ce face functia `input`?", "answer": "Introduce date de la tastatura"},
        {"question": "HTML este un limbaj de programare?", "answer": "nu"},
        {"question": "Ce inseamna CSS?", "answer": "Cascading Style Sheets", "options": ["Cascading Style Sheets", "Computer Style Sheets", "Colorful Style Sheets"]},
        {"question": "Care este variabila corecta in Python?", "answer": "my_var", "options": ["my-var", "my var", "my_var"]},
        {"question": "Ce inseamna SQL?", "answer": "Structured Query Language", "options": ["Structured Query Language", "Standard Query Language", "Simple Query Language"]}
    ]


    random.shuffle(questions)


    print("Ai 30 de secunde pentru fiecare intrebare!\n")

    for q in questions:
        total_questions += 1
        start_time = time.time()  # Cronometru pentru intrebari
        if 'options' in q:
            score += ask_question(q['question'], q['answer'], q['options'])
        else:
            score += ask_question(q['question'], q['answer'])
        
        # Verificare timp
        end_time = time.time()
        if end_time - start_time > 30:
            print("Timpul a expirat! ❌\n")


    print(f"Ai raspuns corect la {score} din {total_questions} intrebari!")
    procentaj = (score / total_questions) * 100
    print(f"Ai obtinut un scor de {procentaj:.2f}%.\n")

    if procentaj == 100:
        print("Felicitari! Esti un adevarat maestru al programarii! 👨‍💻🎉")
    elif procentaj >= 70:
        print("Bravo! Ai cunostinte solide! 💪")
    elif procentaj >= 50:
        print("Bun inceput, mai ai putin de lucru. 👍")
    else:
        print("Mai trebuie sa exersezi. Nu te lasa! 🚀")

    # Optiunea de rejucare
    replay = input("\nVrei sa incerci din nou? (da/nu) ").lower()
    if replay == "da":
        start_game()
    else:
        print("Multumim ca ai jucat! La revedere! 👋")


start_game()
