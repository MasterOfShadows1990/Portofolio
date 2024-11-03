# Definim o listă goală care va conține informațiile despre studenți
studenti = []

# Solicităm utilizatorului să introducă numărul de studenți
n = int(input("Introdu numărul de studenți: "))

# Colectăm informațiile despre fiecare student
for i in range(n):
    nume = input(f"Introdu numele studentului {i+1}: ")
    nota = int(input(f"Introdu nota studentului {nume}: "))
    
    # Creăm un dicționar cu informațiile studentului
    student = {
        'nume': nume,
        'nota': nota
    }
    
    # Adăugăm dicționarul în lista de studenți
    studenti.append(student)

# Afișăm lista de studenți și notele lor
print("\nLista studenților și notele lor:")
for student in studenti:
    print(f"{student['nume']} - {student['nota']}")

# Calculăm și afișăm media notelor
suma_notelor = sum(student['nota'] for student in studenti)
media_notelor = suma_notelor / n
print(f"\nMedia notelor este: {media_notelor}")

# Găsim și afișăm studentul cu nota cea mai mare
student_cu_nota_maxima = max(studenti, key=lambda student: student['nota'])
print(f"Studentul cu nota cea mai mare este: {student_cu_nota_maxima['nume']} cu nota {student_cu_nota_maxima['nota']}")
