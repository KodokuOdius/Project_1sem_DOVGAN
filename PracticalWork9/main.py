
from exersices import variant_6

while True:

    ex = input("Введите номер (0 - выход) вариант: ")

    if ex == "0":
        print("Выход из программы\n")
        break
    elif ex == "6":
        variant_6.solve()
    else:
        print("Такого варианта нет")