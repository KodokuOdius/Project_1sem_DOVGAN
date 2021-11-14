from exercises import *

while True:

    var = input("Введите номер варианта (0 - выход): ")

    if var == "0":
        print("Выход из программы\n")
        break

    elif var == "1":
        variant_1.solve()

    elif var == "6":
        variant_6.solve()

    else:
        print("Нет такого варианта\n")
    