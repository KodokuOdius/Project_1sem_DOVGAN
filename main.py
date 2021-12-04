from exersices import variant_8


while True:

    var = input("Введите номер (0 - выход) варианта: ")

    if var == "0":
        print("Выход из программы\n")
        break
    elif var == "6":
        variant_8.solve()
    else:
        print("Нет такого варианта\n")