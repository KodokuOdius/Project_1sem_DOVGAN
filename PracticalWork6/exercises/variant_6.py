
"""
Вариант 6
1.Даны  целые  числа  N  (>2),  A и  B.  
    Сформировать  и  вывести  целочисленный  список размера 10, 
    первый элемент которого равен A, второй равен B, 
    а каждый последующий элемент равен сумме всех предыдущих.
2.Дан список размера N. 
    Найти максимальный из его локальных минимумов 
    (локальный минимум —это элемент, который меньше любого из своих соседей).
3.Дан список размера N и целое число K (1 < K < N).
    Осуществить сдвиг элементов списка вправо на K позиций 
    (при этом A1 перейдет в AK+1, A2 — в AK+2, ..AN-K—в AN, 
    а  исходное  значение  K  последних  элементов  будет  потеряно).  
    Первые  K  элементов полученного списка положить равными 0.

"""

from random import randint

def solve():
    def GenList(length):
        return [randint(0, 100) for i in range(0, length)]

    def ex1():
        def MakeList(num1, num2):
            list = []
            for i in range(0, 10):
                list.append(num1)
                num1 = num2
                num2 = sum(list) + num1
            return list

        while True:
            try:
                a = int(input("Введите A: "))
                b = int(input("Введите B: "))
                if a < 3 or b < 3:
                    print(f"Данные не подходят по условию (N > 2)")
                    continue

                return print(f"Готовый список: {MakeList(a, b)}\n")
            except ValueError:
                print("Некорректные данные\n")

    def ex2():
        def LocalMin(list1 = []):
            temp_list = []
            for i in range(0, len(list1)):
                if list1[i] > list1[-len(list1)+i+1] and list1[-len(list1)+i+1] < list1[-len(list1)+i+2]:
                    temp_list.append(list1[-len(list1)+i+1])
            return temp_list
            
        while True:
            try:
                n = int(input("Введите N: "))

                if n < 1:
                    print("Данные не подходят по условию (N > 0)")
                    continue

                g_list = GenList(n)
                min_list = LocalMin(g_list)
                
                print(f"Сгенерированный список:\n {g_list}")
                print(f"Локальные минимумы:\n {min_list}")
                return print(f"Максимум из этого: {max(min_list)}\n")
            except ValueError:
                print("Некорректные данные\n")

    def ex3():
        def MoveList(step, temp = []):
            temp_list = [temp[-step+i] for i in range(0, len(temp))]
            for i in range(0, step):
                temp_list[i] = 0
            return temp_list

        while True:
            try:
                n = int(input("Введите N: "))
                k = int(input("Введите K: "))
                if n <= k or k <= 1:
                    print("Данные не подходят по условию (N > K > 1)")
                    continue
                list = GenList(n)

                print(f"Сгенерированный список:\n {list}")
                return print(f"Преобразованный список:\n {MoveList(k, list)}\n")
            except ValueError:
                print("Некорректные данные\n")


    while True:
        ex = input("Введите номер (0 - выход) задания: ")

        if ex == "0":
            return print("Выход из варианта\n")
        elif ex == "1":
            print("Условия:")
            print("1.Даны  целые  числа  N  (>2),  A и  B.\n" +
                "Сформировать  и  вывести  целочисленный  список размера 10,\n" +
                "первый элемент которого равен A, второй равен B,\n" +
                "а каждый последующий элемент равен сумме всех предыдущих.\n")
            ex1()
        elif ex == "2":
            print("Условие:")
            print("2.Дан список размера N.\n" +
                "Найти максимальный из его локальных минимумов\n" +
                "(локальный минимум — это элемент, который меньше любого из своих соседей).\n")
            ex2()
        elif ex == "3":
            print("Условия:")
            print("3.Дан список размера N и целое число K (1 < K < N).\n" +
                "Осуществить сдвиг элементов список вправо на K позиций\n" +
                "(при этом A1перейдет в AK+1, A2—в AK+2, ..AN-K—в AN,\n" +
                "а  исходное  значение  K  последних  элементов  будет  потеряно).\n" +
                "Первые  K  элементов полученного списка положить равными 0.\n")
            ex3()
        else:
            print("Такого задания нет\n")
        
