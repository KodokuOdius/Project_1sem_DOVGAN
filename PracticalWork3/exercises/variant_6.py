
from types import TracebackType


def solve():


    """
        1. Даны три целых числа: A, B, C. Проверить истинность высказывания: «Справедливо
        двойное
        2. Смоделировать простейший калькулятор, умеющий выполнять 4 основные арифметические
        операции
    """

    while True:

        ex = input("Введите номер задания (0 - выход): ")

        if ex == "0":
            return print("Вызод из варианта\n")

        if ex == "1":
            print("Условие: (Вариант 7)")
            print("Даны три целых числа: A, B, C.\n" +
                "Проверить истинность высказывания:\n" +
                "«Число B находится между числами A и C»")
            while True:
                try:
                    a = float(input("Введите A: "))
                    b = float(input("Введите B: "))
                    c = float(input("Введите C: "))

                    if a < b < c or a > b > c:
                        print("Высказывание верно")
                        print(f"{a} - {b} - {c}")
                        break

                    else:
                        print("Высказывание ложно")
                        print(f"{a} - {b} - {c}")
                        break

                except ValueError:
                    print("Некорректные данные")

        if ex == "2":
            print("Условие:")
            print("Смоделировать простейший калькулятор,\n" +
            "умеющий выполнять 4 основные арифметические операции\n")

            print("Калькулятор")

            while True:
                try:
                    a = float(input("Введите первое число: "))
                    b = float(input("Введите второе число: "))

                    act = input("Выберите действие:\n" +
                                " 1 - сумма\n" +
                                " 2 - разность\n" +
                                " 3 - произведение\n" +
                                " 4 - деление")


                    if act == "1":
                        print(f"Сумма = { a + b }")
                        break

                    if act == "2":
                        print(f"Разность = { a - b }")
                        break

                    if act == "3":
                        print(f"Произведение = { a * b }")
                        break

                    if act == "4":
                        print(f"Частное = { a / b }")
                        break
                    else:
                        print("Нет такого действия")
                        break

                except ValueError:
                    print("Некорректные данные")

        else:
            print("Нет такого задания")
