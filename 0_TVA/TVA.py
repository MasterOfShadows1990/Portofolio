while True:
    tasta = input("Pentru pret cu TVA apasa 1, pentru pret fara TVA apasa 2 (sau apasa 'q' pentru a iesi)\n")

    if tasta == "1":
        suma_fara_taxe = input("Introdu suma fara taxe... ")
        try:
            suma_fara_taxe = float(suma_fara_taxe)
            print("Pret cu taxe:", suma_fara_taxe * 1.2)
        except ValueError:
            print("Te rog introdu un numar valid!\n")
    elif tasta == "2":
        suma_cu_taxe = input("Introdu suma cu taxe... ")
        try:
            suma_cu_taxe = float(suma_cu_taxe)
            print("Pret fara taxe:", suma_cu_taxe / 1.2)
        except ValueError:
            print("Te rog introdu un numar valid!\n")
    elif tasta.lower() == 'q':
        print("Iesire din program. La revedere!")
        break
    else:
        print("Optiune invalida. Te rog apasa 1, 2 sau 'q' pentru a iesi.\n")
