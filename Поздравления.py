import tkinter as tk
from datetime import datetime
import customtkinter

birthdays = {}# пустой список днюх


def checkbirthdays():   #функция проверки дней рождений и вывода их в окно
    currentdate = datetime.now().date()
    for name, birthday in birthdays.items():
        nextbirthday = datetime(currentdate.year, birthday.month, birthday.day).date()
        daysuntilbirthday = (nextbirthday - currentdate).days

        if daysuntilbirthday >= 0 <= 7:
            label = customtkinter.CTkLabel(root,
                                           text=f"День рождения {name} через {daysuntilbirthday} дня,{nextbirthday}")
            label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)


def addbirthday():  #функция добавления дня рождения
    name = entry_name.get()
    day = int(entry_day.get())
    month = int(entry_month.get())

    try:
        birthday = datetime(datetime.now().year, month, day).date() #создает дату
        birthdays[name] = birthday
        entry_name.delete(0, customtkinter.END)#очищает строчки ввода
        entry_day.delete(0, customtkinter.END)
        entry_month.delete(0, customtkinter.END)

    except ValueError:
        label_error = customtkinter.CTkLabel(root, text="Введите корректную дату")
        label_error.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


root = customtkinter.CTk() #Создание окна
root.geometry("420x580") #Размер окна
root.resizable(False, False) #запрещаем менять размер окна мышкой
label_name = customtkinter.CTkLabel(root, text="Введите имя:") #создание текстового поля
label_name.place(relx=0.5, rely=0.05, anchor=tk.CENTER) #размещение внутри окна
entry_name = customtkinter.CTkEntry(root, width=200, height=20) #создание поля ввода
entry_name.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
label_day = customtkinter.CTkLabel(root, text="Введите день:")
label_day.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
entry_day = customtkinter.CTkEntry(root, width=200, height=20)
entry_day.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
label_month = customtkinter.CTkLabel(root, text="Введите месяц:")
label_month.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
entry_month = customtkinter.CTkEntry(root, width=200, height=20)
entry_month.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
button_add = customtkinter.CTkButton(root, text="Добавить день рождения", command=addbirthday) #создание кнопки
button_add.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
button_check = customtkinter.CTkButton(root, text="Проверить ближайшие дни рождения", command=checkbirthdays)
button_check.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
sozdali_label = customtkinter.CTkLabel(root, text="Сделали Скупков,Корочкин,Кернер")
sozdali_label.place(relx=0.3, rely=0.95, anchor=tk.CENTER)

root.mainloop()
