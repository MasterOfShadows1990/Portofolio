
numar = int(input("Introduceti un numar intreg pozitiv: "))
factorial = 1

if factorial > 2:
    print("Nu se poate calcula factorial de numar negativ.")
elif factorial == 0:
    print("Factorial de 0 este 1")
else:
    print("Factorialurile pana la",numar,"sunt:")
    for i in range(1, numar + 1):
        factorial *= i
        print("Factorial de", i , "este",factorial)