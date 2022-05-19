import tkinter as tk
from tkinter import ttk
import sqlite3 as sql
import re


class Main(tk.Frame):

    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#a0dea0', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        outer_padx = 10

        self.add_img = tk.PhotoImage(file="DB/add-user.png")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить клиента', command=self.open_dialog, bg='#5da130',
                                    compound=tk.TOP, image=self.add_img, padx=5, pady=2, border='5')
        self.btn_open_dialog.pack(side=tk.LEFT, padx=outer_padx, pady=3)

        self.update_img = tk.PhotoImage(file="DB/edit.png")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#5da130',
                                    compound=tk.TOP, image=self.update_img, padx=5, pady=2, border='5')
        btn_edit_dialog.pack(side=tk.LEFT, padx=outer_padx)

        self.delete_img = tk.PhotoImage(file="DB/trash.png")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#5da130',
                                    compound=tk.TOP, image=self.delete_img, padx=5, pady=2, border='5')
        btn_delete.pack(side=tk.LEFT, padx=outer_padx)

        self.search_img = tk.PhotoImage(file="DB/search.png")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#5da130',
                               compound=tk.TOP, image=self.search_img, padx=5, pady=2, border='5')
        btn_search.pack(side=tk.LEFT, padx=outer_padx)

        self.refresh_img = tk.PhotoImage(file="DB/refresh.png")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#5da130',
                               compound=tk.TOP, image=self.refresh_img, padx=5, pady=2, border='5')
        btn_refresh.pack(side=tk.LEFT, padx=outer_padx)

        self.tree = ttk.Treeview(self, columns=('tourist_id', 'surname', 'phone', 'country', 'region', 'duration', 'cost'), height=15, show='headings')

        self.tree.column('tourist_id', width=30, anchor=tk.CENTER)
        self.tree.column('surname', width=120, anchor=tk.CENTER)
        self.tree.column('phone', width=120, anchor=tk.CENTER)
        self.tree.column('country', width=90, anchor=tk.CENTER)
        self.tree.column('region', width=90, anchor=tk.CENTER)
        self.tree.column('duration', width=80, anchor=tk.CENTER)
        self.tree.column('cost', width=120, anchor=tk.CENTER)

        self.tree.heading('tourist_id', text='ID')
        self.tree.heading('surname', text='Фамилия клиента')
        self.tree.heading('phone', text='Номер телефона')
        self.tree.heading('country', text='Страна')
        self.tree.heading('region', text='Регион')
        self.tree.heading('duration', text='Кол-во дней')
        self.tree.heading('cost', text='Стоимоть')

        self.tree.pack()

    def records(self, surname, phone, country, region, duration, cost):
        msg = self.clean_data(surname, phone, country, region, duration, cost)
        if not msg:
            self.db.insert_data(surname, phone, country, region, duration, cost)
            self.view_records()
        else:
            self.open_error(msg)

    def update_record(self, surname, phone, country, region, duration, cost):
        try:
            self.db.update_data(
                id=self.tree.set(self.tree.selection()[0], '#1'),
                surname=surname, phone=phone,
                country=country, region=region,
                duration=duration, cost=cost

            )
            self.view_records()
        except IndexError as ex:
            self.open_error("Выберите запись для редактирования")


    def view_records(self):
        self.db.cur.execute("""SELECT * FROM tourists ORDER BY tourist_id DESC""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM tourists WHERE tourist_id=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, duration):
        duration = (duration,)
        self.db.cur.execute("""SELECT * FROM tourists WHERE duration >= ?""", duration)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def clean_data(self, surname, phone, country, region, duration, cost):
        if not surname or re.findall(r"[^a-zA-ZА-ЯёЁа-я]", surname):
            return "Неверно указана Фамилия клиента"

        if not (phone.isdigit() and len(phone) == 11):
            return "Неверно указан номер\n Пример: 7xxxxxxxxxx"

        if not country or re.findall(r"[^a-zA-ZА-ЯёЁа-я\s]", country):
            return "Неверно указана страна"

        if not region or re.findall(r"[^a-zA-ZА-ЯёЁа-я\s]", region):
            return "Неверно указан регион"
        
        if not duration.isdigit():
            return "Неверно указана\n продолжительность поездки"
        
        if not cost.isdigit():
            return "Неверно указана cтоимоть поездки"
        
    def open_dialog(self):
        Child(root, app)
    
    def open_error(self, msg):
        Error(msg)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):

    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить клиента')
        self.geometry('400x300+400+300')
        self.resizable(False, False)

        label_surname = tk.Label(self, text='Фамилия\nклиента')
        label_surname.place(x=70, y=15)
        self.entry_surname = ttk.Entry(self)
        self.entry_surname.place(x=165, y=25)

        label_phone = tk.Label(self, text='Номер\nтелефона')
        label_phone.place(x=70, y=50)
        self.entry_phone = ttk.Entry(self)
        self.entry_phone.place(x=165, y=60)

        label_country = tk.Label(self, text='Страна')
        label_country.place(x=75, y=95)
        self.entry_country = ttk.Entry(self)
        self.entry_country.place(x=165, y=95)

        label_region = tk.Label(self, text='Регион')
        label_region.place(x=75, y=130)
        self.entry_region = ttk.Entry(self)
        self.entry_region.place(x=165, y=130)

        label_duration = tk.Label(self, text='Продолжительность\nпоездки в днях')
        label_duration.place(x=35, y=155)
        self.entry_duration = ttk.Entry(self)
        self.entry_duration.place(x=165, y=165)

        label_cost = tk.Label(self, text='Стоимость поездки\n(тыс. руб)')
        label_cost.place(x=35, y=200)
        self.entry_cost = ttk.Entry(self)
        self.entry_cost.place(x=165, y=200)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=245)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=245)
        self.btn_ok.bind('<Button-1>',
            func=lambda event: 
                self.view.records(
                        self.entry_surname.get(),
                        self.entry_phone.get(),
                        self.entry_country.get(),
                        self.entry_region.get(),
                        self.entry_duration.get(),
                        self.entry_cost.get()
                    )
                )


        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=210, y=245)
        btn_edit.bind('<Button-1>', 
            func=lambda event: 
                self.view.update_record(
                        self.entry_surname.get(),
                        self.entry_phone.get(),
                        self.entry_country.get(),
                        self.entry_region.get(),
                        self.entry_duration.get(),
                        self.entry_cost.get()
                    )
                )
        self.btn_ok.destroy()

class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x120+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск производиться по длительности поздки,\n большей либо равной указаной в поле ввода")
        label_search.place(x=15, y=10)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=60, y=55, width=170)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=65, y=85)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        # btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=150, y=85)


class Error(tk.Toplevel):
    def __init__(self, msg: str) -> None:
        super().__init__()
        self.view = app
        self.init_error(msg)

    def init_error(self, msg):
        self.title('Системная ошибка!')
        self.geometry('280x100+450+350')
        self.resizable(False, False)

        label_error = tk.Label(self, text=msg)
        label_error.place(x=25, y=25)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=170, y=60)

        self.grab_set()
        self.focus_set()



class DB:
    def __init__(self):
        with sql.connect('DB/db.sqlite3') as self.con:
            self.cur = self.con.cursor()
            # duration in days
            self.cur.execute("""CREATE TABLE IF NOT EXISTS tourists (
                tourist_id INTEGER PRIMARY KEY AUTOINCREMENT,
                surname VARCHAR(255) NOT NULL,
                phone INTEGER NOT NULL,
                country VARCHAR(255) NOT NULL,
                region VARCHAR(255) NOT NULL,
                duration INTEGER NOT NULL,
                cost INTEGER NOT NULL
            )""")

    def insert_data(self, surname, phone, country, region, duration, cost):
        self.cur.execute("""INSERT INTO tourists(surname, phone, country, region, duration, cost) VALUES (?, ?, ?, ?, ?, ?)""",
                             (surname, phone, country, region, duration, cost))
        self.con.commit()

    def update_data(self, id, *args, **kwargs):
        #     """UPDATE tourists SET surname=?, phone=?, country=?, region=?, duration=?, cost=? WHERE tourist_id=?""", 
        self.cur.execute(
            "UPDATE tourists SET " + \
                (", ".join([f"{key}={kwargs[key]}" for key in kwargs.keys() if kwargs[key]])) + \
                    f" WHERE tourist_id={id}"
        )

        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("T.Y.P. - 6 вариант")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
