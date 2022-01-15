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


def exch_lang():
    if lang_btn["text"] == "rus":
        titl["text"] = "Простой ГИ для шифра Цезаря"
        lbl_sh["text"] = "- Выбери сдвиг 👇"
        scl["to"] = 31
        lbl_inv["text"] = "Введи свой текст (🐻)"
        encr_btn["text"] = "Зашифровать"
        lbl_out["text"] = "Зашифрованный текст"
        lang_btn["text"] = "eng"
    else:
        titl["text"] = "Symple GUI for Caesar`s Cipher"
        lbl_sh["text"] = "- Select shift 👇"
        scl["to"] = 25
        lbl_inv["text"] = "Enter your text (☕)"
        encr_btn["text"] = "Encrypt"
        lbl_out["text"] = "Encrypted text"
        lang_btn["text"] = "rus"


def encryption():
    if lang_btn["text"] == "rus":
        alp = tuple("abcdefghijklmnopqrstuvwxyz")
        alp_b = tuple("abcdefghijklmnopqrstuvwxyz".upper())
    else:
        alp = tuple("абвгдежзийклмнопрстуфхцчшщъыьэюя")
        alp_b = tuple("абвгдежзийклмнопрстуфхцчшщъыьэюя".upper())
        


    shift = int(scl.get())
    text = txt_ent.get("1.0", END)

    temp = "".join(alp_b[-len(alp) + shift + alp_b.index(s)] if s in alp_b 
                    else alp[-len(alp) + shift + alp.index(s)] if s in alp 
                    else s 
                    for s in text)

    # for s in text:
    #     news = s
    #     if s in alp_b:
    #         news = alp_b[-len(alp) + shift + alp_b.index(s)]
    #     elif s in alp:
    #         news = alp[-len(alp) + shift + alp.index(s)]
    #     temp += news
    
    if text != "\n":
        ans_lbl["text"] = temp
    

# Добавть фотку

row_size = 25
column_size = 75


root = Tk()
root.title("Caesar's Cipher")
root.rowconfigure(
    [i for i in range(7)],
    weight=1,
    minsize=row_size
)
root.columnconfigure(
    [0],
    weight=1,
    minsize=column_size
)
root.resizable(False, False)


titl = Label(
    master=root,
    text="Symple GUI for Caesar`s Cipher",
    font="Times 20 bold"
)
titl.grid(row=0, column=0, padx=(10, 10), sticky="swen")


frm_slc = Frame(master=root)
frm_slc.rowconfigure(
    [0, 1],
    weight=1,
    minsize=row_size/2
)
frm_slc.columnconfigure(
    [0],
    weight=1,
    minsize=column_size
)
frm_slc.grid(row=1, column=0, sticky="swen")

lbl_sh = Label(master=frm_slc, text="- Select shift 👇", font="Times 12 bold")
lbl_sh.grid(row=0, column=0, padx=(10, 10), pady=(10, 0), sticky="sw")

scl = Scale(
    master=frm_slc,
    orient=HORIZONTAL,
    from_=1,
    to=25
)
scl.grid(row=1, column=0, padx=(20, 20), sticky="swen")


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
frm_ent.grid(row=2, column=0, padx=(10, 10), pady=(10, 0), sticky="swen")

lbl_inv = Label(master=frm_ent, text="Enter your text (☕)", font="Times 12 bold")
lbl_inv.grid(row=0, sticky="sw")

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
frm_btn.grid(row=3, padx=(10, 10), sticky="swen")

encr_btn = Button(
    master=frm_btn,
    text="Encrypt",
    font="Times 10 bold",
    command=encryption
)
encr_btn.grid(row=0, column=0, padx=(0, 10), pady=(10, 0), sticky="swen")


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
frm_ans.grid(row=4, column=0, padx=(10, 10), pady=(10, 0), sticky="swen")


lbl_out = Label(master=frm_ans, text="Encrypted text", font="Times 12 bold")
lbl_out.grid(row=0, sticky="sw")

ans_lbl = Label(
    master=frm_ans,
    text="Simple text for simple label\n",
    font="Times 14"
)
ans_lbl.grid(row=1, column=0, sticky="nw")


lang_btn = Button(
    master=root,
    text="rus",
    bg="red",
    font="Times 12 bold",
    command=exch_lang,
    height=1
)
lang_btn.grid(row=5, column=0, padx=(10, 300), sticky="swe")

if __name__ == "__main__":
    root.mainloop()