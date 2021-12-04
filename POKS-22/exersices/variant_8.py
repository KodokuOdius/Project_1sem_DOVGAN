# Вариант 6.
# Даны три словаря на три элемента каждый.
# Объединить все словари в один.
# Вывести исходные словари и результирующий.
from random import randint


def solve():
    print(
        "Вариант 6.\n" +
        "Даны три словаря на три элемента каждый.\n" +
        "Объединить все словари в один.\n" +
        "Вывести исходные словари и результирующий.\n"
    )
    temp = []
    j = 0
    for k in range(3):
        temp.append({j+i: randint(-10, 10) for i in range(3)})
        j += 3

    res_dict = {}
    for dictory in temp:
        for key in dictory:
            res_dict[key] = dictory[key]

    print("Начальные словари:")
    for i in range(3):
        print(temp[i])
    print("Результат:")
    print(res_dict, end="\n\n")

