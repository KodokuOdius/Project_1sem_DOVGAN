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

from pydoc import text
from tkinter import *



def encryption_rus():

    alp = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    alp_b = "абвгдежзийклмнопрстуфхцчшщъыьэюя".upper()

    cip = {s: alp[-len(alp) + alp.index(s) + 1] for s in alp}
    cip_b = {s: alp_b[-len(alp_b) + alp_b.index(s) + 1] for s in alp_b}

    text = txt_ent.get("1.0", END)
    for s in set(text):
        if s in alp:
            text = text.replace(s, cip[s])
        elif s in alp_b:
            text = text.replace(s, cip_b[s])
    ans_lbl["text"] = text
    
# Сделать Функцию
# Сделать шкалу сдвига
# Добавть фотку

row_size = 25
column_size = 75


root = Tk()
root.title("Caesar's Cipher")
root.rowconfigure(
    [i for i in range(4)],
    weight=1,
    minsize=row_size
)
root.columnconfigure(
    [0],
    weight=1,
    minsize=column_size
)
root.resizable(False, False)


Label(
    master=root,
    text=("Symple GUI for Caesar`s Cipher"),
    font="Times 20 bold"
). grid(row=0, column=0, padx=(10, 10), sticky="swen")

frm_ent = Frame(master=root)
frm_ent.rowconfigure(
    [0, 1],
    weight=1,
    minsize=row_size
)
frm_ent.columnconfigure(
    [0],
    weight=1, 
    minsize=column_size
)
frm_ent.grid(row=1, column=0, padx=(10, 10), pady=(10, 0), sticky="swen")

Label(master=frm_ent, text="Enter your text (rus)", font="Times 12 bold").grid(row=0, sticky="sw")

txt_ent = Text(
    master=frm_ent,
    height=3,
    width=5
)
txt_ent.grid(row=1, sticky="swen")




frm_btn = Frame(master=root)
frm_btn.rowconfigure(
    [0],
    weight=1,
    minsize=row_size
)
frm_btn.columnconfigure(
    [0, 1],
    weight=1,
    minsize=column_size
)
frm_btn.grid(row=2, padx=(10, 10), sticky="swen")

encr_btn = Button(
    master=frm_btn,
    text="Encrypt",
    font="Times 10 bold",
    command=encryption_rus
)
encr_btn.grid(row=0, column=0, padx=(0, 10), pady=(10, 0), sticky="swen")

Label(master=frm_btn, text="Photo change").grid(row=0, column=1, sticky="w")



frm_ans = Frame(master=root)
frm_ans.rowconfigure(
    [0, 1],
    weight=1,
    minsize=row_size
)
frm_ans.columnconfigure(
    [0],
    weight=1,
    minsize=column_size
)
frm_ans.grid(row=3, column=0, padx=(10, 10), pady=(10, 0), sticky="swen")


Label(master=frm_ans, text="Encrypted text", font="Times 12 bold").grid(row=0, sticky="sw")

ans_lbl = Label(
    master=frm_ans,
    text="Simple text for simple label",
    font="Times 14"
)
ans_lbl.grid(row=1, column=0, sticky="nw")



if __name__ == "__main__":
    root.mainloop()