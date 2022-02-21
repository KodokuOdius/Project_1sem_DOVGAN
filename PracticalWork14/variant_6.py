from exersices import ex1


print(
    "Приветствую тебя в Практическом задании номер 6"
)
while True:
    ex = input("Ввeди номер задания (0 - выход)\n Хотя он тут один =P : ")

    if ex == "0":
        print("Выход")
        break

    if ex == "1":
        ex1.solve()
        break
        
    else:
        print("Не угадал))\n")
