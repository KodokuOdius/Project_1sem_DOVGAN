
def solve():

    print("========> Условие <========")
    print("Дан номер некоторого года N (целое положительное число).\n" +
            "Определить соответствующий ему номер столетия,\n" +
            "учитывая, что, к примеру, началом 20 столетия был 1901 год")

    n = int(input("Введите N: " ))

    if n % 100 != 0:
        print("========> Ответ <========")
        return print(f"Номер столетия - { ( n // 100 + 1 ) }")

    print("========> Ответ <========")
    print(f"Номер столетия - { ( n // 100 ) }")
