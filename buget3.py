import customtkinter
from tkinter import *
from PIL import Image


def get_budget():
    cifra = int(balance_enter.get())
    ciifgra = int(rashod_enter.get())
    freebudget = int(cifra - ciifgra)  # расчет свободного бюджета
    freebudgete.configure(text=f"Ваш свободный бюджет: {freebudget}")
    self.update()  # Обновляем отображение
    invest2 = int((freebudget / 100) * 10)
    investe.configure(text=f"Инвестируйте:{invest2} в месяц")


self = customtkinter.CTk()
self.geometry("720x540")  # размер окна
self.title("Трекер бюджета")  # название окна
self.resizable(False, False)  # запрет менять размер окна вручную
self.logo = customtkinter.CTkImage(dark_image=Image.open("dengi.png"), size=(128, 128))  # добавляем фотографию
self.logo_label = customtkinter.CTkLabel(master=self, text="", image=self.logo)  # привязка фотографии к окну
self.logo_label.place(relx=0.5, rely=0.2, anchor='center')  # расположение фото внутри окна
balance_enter = customtkinter.CTkEntry(master=self, width=100, height=20)  # окно ввода доходов
balance_enter.place(relx=0.1, rely=0.5)  # расположение
rashod_enter = customtkinter.CTkEntry(master=self, width=100, height=20)  # ввод расходов
rashod_enter.place(relx=0.1, rely=0.7)  # расположение
balance = customtkinter.CTkLabel(master=self, text="Введите ваш доход")  # вывод текста
balance.place(relx=0.1, rely=0.4)
rashodi = customtkinter.CTkLabel(master=self, text="Введите ваши расходы")
rashodi.place(relx=0.1, rely=0.6)
get_budgete = customtkinter.CTkButton(master=self, text="Создать план", command=get_budget)
get_budgete.place(relx=0.1, rely=0.8)
freebudgete = customtkinter.CTkLabel(master=self, text="")
freebudgete.place(relx=0.4, rely=0.4)
investe = customtkinter.CTkLabel(master=self, text="")
investe.place(relx=0.4, rely=0.7)
self.mainloop()
