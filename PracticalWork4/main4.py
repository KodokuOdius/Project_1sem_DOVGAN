from exercises import *

while True:

    var = input("Введите номер варианта (0 - выход): ")

    if var == "0":
        break

    if var == "6":
        variant_6.solve()

    else:
        print("Нет такого варианта")