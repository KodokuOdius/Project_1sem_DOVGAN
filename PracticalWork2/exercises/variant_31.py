
def solve():

    print("========> Условие <========")
    print("Дни недели пронумерованы следующим образом:\n" +
            "1 — понедельник, 2 — вторник, ..., 6 — суббота, 7 — воскресенье.\n" +
            "Дано целое число K, лежащее в диапазоне 1-365.\n" +
            "Определить номер дня недели для K-го дня года,\n" +
            "если известно, что в этом году 1 января было вторником")

    days = [ 
            "Понедельник",
            "Вторник",
            "Среда",
            "Четверг",
            "Пятница",
            "Суббота",
            "Воскречение"
            ]

    k = int(input("Введите K: "))

    if k not in range(1, 366):
        return print("Некорректные данные")

    print(f"Номер дня недели для {k}-го дня года - { k % 7 + 1 }\n" +
            f"Это { days[ k % 7 ] }")
