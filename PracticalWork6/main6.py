from exercises import *

while True:
    var = input("Введите номер (0 - выход) варианта: ")

    if var == "0":
        print("Выход из программы\n")
        break
    elif var == "6":
        variant_6.solve()
    else:
        print("Нет такого вариата\n")