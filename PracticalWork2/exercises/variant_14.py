
def solve():

    print("========> Условие <========")
    print("Дано трехзначное число N.\n" +
        "Используя одну операцию деления нацело,\n" +
        "вывести первую цифру данного числа (сотни)")

    n = int(input("Введите N: "))

    if n // 100 == 0:
        return print("Некорректные данные")

    print("========> Ответ <========")
    print(f"Первая цифра числа {n} - { n // 100 }")
