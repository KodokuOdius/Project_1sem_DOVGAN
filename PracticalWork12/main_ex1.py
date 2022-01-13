# Задание 1. 
# В соответствии с номером варианта перейти по ссылке на прототип. 
# Реализовать его в IDE PyCharm Community с применением пакета tk. 
# Получить интерфейс максимально приближенный к оригиналу (см. таблицу 1). 
# link = https://uicookies.com/wp-content/uploads/2019/05/Reg-Form-v5.jpg

from tkinter import *


# CONSTS
row_size = 25
column_size = 40
px = 2
py = 5

# MAIN WINDOW
root = Tk()
root.title("Registration form")
root.rowconfigure(
    [i for i in range(9)],
    weight=10,
    minsize=row_size
)
root.columnconfigure(
    [i for i in range(4)],
    weight=10,
    minsize=column_size
)
root.resizable(
    width=False,
    height=False
)


# TITLE
main_lbl = Label(
    master=root,
    text="EVENT REGISTRATION FORM",
    bg="black",
    fg="white",
    font=("Times", "14", "bold")
)
main_lbl.grid(row=0, column=0, columnspan=4, pady=(0, 10), sticky="swen")


# ENTERY FOR NAME
Label(master=root, text="Name", font=("Times", "10", "bold")).grid(row=1, column=1, padx=(px, 0), pady=py+3, sticky="nw")
frm_enter_name = Frame(master=root)
frm_enter_name.rowconfigure(
    [0, 1],
    weight=1,
    minsize=row_size
)
frm_enter_name.columnconfigure(
    [0, 1],
    weight=1,
    minsize=column_size
)
frm_enter_name.grid(row=1, column=2, padx=px, pady=py, sticky="swen")

frt_name = Entry(master=frm_enter_name)
frt_name.grid(row=0, column=0, padx=(0, 15), pady=(py, 0), sticky="swen")
Label(master=frm_enter_name, text="First Name", font=("Times", "8")).grid(row=1, column=0, sticky="nw")

snd_name = Entry(master=frm_enter_name)
snd_name.grid(row=0, column=1, pady=(py, 0), sticky="swen")
Label(master=frm_enter_name, text="Second Name", font=("Times", "8")).grid(row=1, column=1, sticky="nw")


# ENTRY FOR COMPANY
Label(master=root, text="Company", font=("Times", "10", "bold")).grid(row=2, column=1, padx=px, pady=py, sticky="w")
copmany_ent = Entry(master=root)
copmany_ent.grid(row=2, column=2, padx=px, pady=py, sticky="swen")


# ENTRY FOR EMAIL
Label(master=root, text="Email", font=("Times", "10", "bold")).grid(row=3, column=1, padx=px, pady=py, sticky="w")
email_ent = Entry(master=root)
email_ent.grid(row=3, column=2, padx=px, pady=py, sticky="swen")


# ENTRY FOR PHONE NUMBER
Label(master=root, text="Phone", font=("Times", "10", "bold")).grid(row=4, column=1, padx=(px, 0), pady=py+3, sticky="nw")
frm_enter_phone = Frame(master=root)
frm_enter_phone.rowconfigure(
    [0, 1],
    weight=1,
    minsize=row_size
)
frm_enter_phone.columnconfigure(
    [0, 1, 2, 3],
    weight=1,
    minsize=column_size
)
frm_enter_phone.grid(row=4, column=2, padx=px, pady=py, sticky="swen")

# area code num
area_code = Entry(master=frm_enter_phone, textvariable="", justify=CENTER, width=10)
area_code.grid(row=0, column=0, padx=(0, 15), pady=(py, 0), sticky="w")
Label(master=frm_enter_phone, text="Area Code", font=("Times", "8")).grid(row=1, column=0, sticky="nw")

# phone num
phone_num = Entry(master=frm_enter_phone, justify=CENTER)
phone_num.grid(row=0, column=1, columnspan=5, pady=(py, 0), sticky="swen")
Label(master=frm_enter_phone, text="Phone Number", font=("Times", "8")).grid(row=1, column=1, sticky="nw")


# ENTRY FOR SELECT SUBJECT
Label(master=root, text="Subject", font=("Times", "10", "bold")).grid(row=5, column=1, padx=px, pady=py, sticky="w")

# menu
subj_lst = [f"Select Subject {i+1}" for i in range(7)]
var_s = StringVar(root)
var_s.set("Choose option")
opt_subj = OptionMenu(root, var_s, *subj_lst)
opt_subj.grid(row=5, column=2, padx=px, pady=py, sticky="swen")


# RADIOBUTTON FRAME
frm_rad = Frame(master=root)
frm_rad.rowconfigure(
    [0, 1, 2],
    weight=1,
    minsize=row_size
)
frm_rad.columnconfigure(
    [0, 1],
    weight=1,
    minsize=column_size
)
frm_rad.grid(row=6, column=1, columnspan=2, padx=(px, 0), pady=0, sticky="w")

# question
Label(master=frm_rad, text="Are you an existing customer?", font=("Times", "10", "bold")).grid(row=0, column=0, columnspan=2, padx=px, pady=(py+10, 0), sticky="w")

var_r = IntVar()
var_r.set(" ")
rad_y = Radiobutton(master=frm_rad, text="Yes", variable=var_r, value=1)
rad_y.grid(row=1, column=0, padx=(px, 0), sticky="w")

rad_n = Radiobutton(master=frm_rad, text="No", variable=var_r, value=0)
rad_n.grid(row=1 ,column=1, padx=(0, 0), sticky="w")


# REGESTER BUTTON
reg_btn = Button(
    master=frm_rad,
    text="Register",
    background="red",
    foreground="white",
    font=("Times", "10", "bold"),
    height=2
)
reg_btn.grid(row=2, column=0, columnspan=2, padx=(0, 25), pady=(25, 0), sticky="swen")


if __name__ == "__main__":
    root.mainloop()