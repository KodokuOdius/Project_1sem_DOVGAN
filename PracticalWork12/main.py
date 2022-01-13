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
root.rowconfigure(
    [i for i in range(9)],
    weight=10,
    minsize=25
)
root.columnconfigure(
    [i for i in range(2)],
    weight=10,
    minsize=100
)
root.resizable(
    width=False,
    height=False
)


main_lbl = Label(
    master=root,
    text="EVENT REGISTRATION FORM",
    bg="black",
    fg="white"
)
main_lbl.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="swen"
)


Label(master=root, text="Name").grid(row=1, column=0, sticky="swen")
frm_enter_name = Frame(master=root)
frm_enter_name.rowconfigure(
    [0, 1],
    weight=1,
    minsize=25
)
frm_enter_name.columnconfigure(
    [0, 1],
    weight=1,
    minsize=100
)
frm_enter_name.grid(row=1, column=1, sticky="swen")

frt_name = Entry(master=frm_enter_name)
frt_name.grid(row=0, column=0, sticky="swen")
Label(master=frm_enter_name, text="First Name").grid(row=1, column=0, sticky="nw")

snd_name = Entry(master=frm_enter_name)
snd_name.grid(row=0, column=1, sticky="swen")
Label(master=frm_enter_name, text="Second Name").grid(row=1, column=1, sticky="nw")


Label(master=root, text="Company").grid(row=2, column=0, sticky="swen")
copmany_ent = Entry(master=root)
copmany_ent.grid(row=2, column=1, sticky="swen")


Label(master=root, text="Email").grid(row=3, column=0, sticky="swen")
email_ent = Entry(master=root)
email_ent.grid(row=3, column=1, sticky="swen")


Label(master=root, text="Phone").grid(row=4, column=0, sticky="swen")
frm_enter_phone = Frame(master=root)
frm_enter_phone.rowconfigure(
    [0, 1],
    weight=1,
    minsize=25
)
frm_enter_phone.columnconfigure(
    [0, 1, 2, 3],
    weight=1,
    minsize=100
)
frm_enter_phone.grid(row=4, column=1, sticky="swen")

area_code = Entry(master=frm_enter_phone)
area_code.grid(row=0, column=0, sticky="swen")
Label(master=frm_enter_phone, text="Area Code").grid(row=1, column=0, sticky="swen")

phone_num = Entry(master=frm_enter_phone)
phone_num.grid(row=0, column=1, columnspan=3, sticky="swen")
Label(master=frm_enter_phone, text="Phone Number").grid(row=1, column=1, sticky="swen")


Label(master=root, text="Subject").grid(row=5, column=0, sticky="swen")
subj_lst = [f"Subj{i+1}" for i in range(4)]
variable = StringVar(root)
variable.set("")

opt_subj = OptionMenu(root, variable, *subj_lst)
opt_subj.grid(row=5, column=1, sticky="swen")


frm_rad = Frame(master=root)
frm_rad.rowconfigure(
    [0, 1],
    weight=1,
    minsize=25
)
frm_rad.columnconfigure(
    [0, 1],
    weight=1,
    minsize=100
)
frm_rad.grid(row=7, column=0, sticky="swen")

Label(master=frm_rad, text="Question").grid(row=0, column=0, columnspan=2, sticky="swen")

rad_y = Radiobutton(master=frm_rad, text="Yes", variable=1)
rad_y.grid(row=1, column=0, sticky="swen")

rad_n = Radiobutton(master=frm_rad, text="No", variable=1)
rad_n.grid(row=1 ,column=1, sticky="swen")

"""
reg_btn = Button(
    master=frm_rad,
    text="Registration"
)
reg_btn.grid(row=2, column=0, columnspan=2, sticky="swen")
"""

reg_btn = Button(
    master=root,
    text="Registration"
)
reg_btn.grid(row=8, column=0, sticky="swen")

if __name__ == "__main__":
    root.mainloop()