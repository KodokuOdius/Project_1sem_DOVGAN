
def solve():

    print("========> Условие <========")
    print("С начала суток прошло N секунд (N — целое).\n" +
            "Найти количество секунд, прошедших с начала последней минуты")

    n = int(input("Введите N: ")) 

    print("========> Ответ <========")
    print(f"Количество секунд, прошедших с начала последней минуты - { n % 60 }")
