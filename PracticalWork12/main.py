# Задание 1. 
# В соответствии с номером варианта перейти по ссылке на прототип. 
# Реализовать его в IDE PyCharm Community с применением пакета tk. 
# Получить интерфейс максимально приближенный к оригиналу (см. таблицу 1). 
# link = https://uicookies.com/wp-content/uploads/2019/05/Reg-Form-v5.jpg

# Задание 2. 
# Разработать программу с применением пакета tk, 
# взяв в качестве условия одну любую задачу из ПЗ № 3 – 8.

# ПЗ 7. Задание 2
# Дана строка-предложение на русском языке.
# Зашифровать всё, выполнив циклическую замену каждой буквы
# на следующую за ней в алфавите и сохранив при этом регистр букв
# («А» перейдет в «Б», «а» -- в «б», «Б» - в «В», «я» - в «а» и т. д.).
# Букву «ё» в алфавите не учитывать («е» должна переходить в «ж»).
# Знаки препинания и пробелы не изменять.

from tkinter import *

root = Tk()
root.title("Registration form")
root.resizable(
    width=False,
    height=False
)


root.mainloop()