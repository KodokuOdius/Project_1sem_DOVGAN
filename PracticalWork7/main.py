from exercises import variant_6

while True:
    var = input("Введите номер (0 - выход) варианта: ")

    if var == "0":
        print("Выход из программы")
        break
    elif var == "6":
        variant_6.solve()
    else:
        print("Такого варианта нет\n")
