
"""
1. Дан символ С, изображающий цифру или букву (латинскую или русскую).
Если С изображает цифру, то вывести строку «digit»,
если латинскую букву - вывести строку «lat», если русскую -- вывести строку «rus».
2. Дана строка-предложение на русском языке.
Зашифровать всё, выполнив циклическую замену каждой буквы
на следующую за ней в алфавите и сохранив при этом регистр букв
(«А» перейдет в «Б», «а» -- в «б», «Б» - в «В», «я» - в «а» и т. д.).
Букву «ё» в алфавите не учитывать («е» должна переходить в «ж»).
Знаки препинания и пробелы не изменять.
"""

import unicodedata

def solve():
    def ex1():
        while True:
            c = input("Введите символ C: ")
            if len(c) > 1:
                print("Вы ввели больше одного символа\n")
                continue
            if c == "":
                print("Вы ничего не ввели\n")
                continue

            c = str(unicodedata.name(c)).split(" ")[0]
            if c == "DIGIT":
                return print("Ответ: digit")
            elif c == "LATIN":
                return print("Ответ: lat")
            elif c == "CYRILLIC":
                return print("Ответ: rus")
            else:
                print("Ответ: другой символ\n")

    def ex2():
        while True:
            sentence = input("Введите предложение:\n")
            big_rus = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
            lower_rus = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
            temp_sen = ""
            for letter in sentence:
                if str(unicodedata.name(letter)).split(" ")[0] == "CYRILLIC":
                    if letter.islower():
                        index = lower_rus.index(letter)
                        temp_sen += lower_rus[-len(lower_rus) + 1 + index]
                    else:
                        index = big_rus.index(letter)
                        temp_sen += big_rus[-len(big_rus) + 1 + index]
                else:
                    temp_sen += letter

            return print(str(temp_sen))

    while True:
        ex = input("Введите номер задания: ")

        if ex == "1":
            print("Условие:")
            print(
                "1. Дан символ С, изображающий цифру или букву (латинскую или русскую).\n" +
                "Если С изображает цифру, то вывести строку «digit»,\n" +
                "если латинскую букву - вывести строку «lat», если русскую -- вывести строку «rus»."
            )
            ex1()
        elif ex == "2":
            print("Условие:")
            print(
                "2. Дана строка-предложение на русском языке.\n" +
                "Зашифровать се, выполнив циклическую замену каждой буквы\n" +
                "на следующую за ней в алфавите и сохранив при этом регистр букв\n" +
                "(«А» перейдет в «Б», «а» -- в «б», «Б» - в «В», «я» - в «а» и т. д.).\n" +
                "Букву «ё» в алфавите не учитывать («е» должна переходить в «ж»).\n" +
                "Знаки препинания и пробелы не изменять."
            )
            ex2()
        else:
            print("Нет такого задания\n")