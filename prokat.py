import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import tksheet
import csv
import sys
import re

#Массив отвечающий за журнал проката
stat = []
#Массив отвечающий за велосипеды
velos = []
#Массив отвечающий за базу данных клиентов
client = []

#Сохранени значений массива в файл CSV
def save_array_to_csv(array, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(array)

#Чтение значение журнала проката из файла stat.csv
def read_array_from_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            stat.append(row)

#Чтение значение таблицы велосипедов из файла velos.csv
def read_array_from_csv2(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            velos.append(row)

#Вывод отладочных значений журнала проката в консоль
def return_arr():
    print(stat)

#Обновление значений из файлов
def update():
    #Очистка массивов для велосипедов и журала проката
    velos.clear()
    stat.clear()
    #Считывание данных из файлов и запись их в массивы
    read_array_from_csv('stat.csv')
    sheet.set_sheet_data(stat)
    read_array_from_csv2('velos.csv')
    sheetvelos.set_sheet_data(velos)
    #Выставление значений для выпадающих списков
    velo_adder['values'] = get_column('velos.csv', 0)
    velo['values'] = get_column('velos.csv', 0)
    #Отладочный вывод значений массивов в консоль
    print(stat)
    print(velos)

#Добавление записи в журнал проката
def add():
    update()
    stat.append([name.get(),phone.get(),velo.get()])
    sheet.set_sheet_data(stat)
    print(stat)
    save_array_to_csv(stat,'stat.csv')
    update()

#Добавление нового велосипеда
def addvelo():
    tarif = price.get()
    print(tarif.isdigit())
    if(tarif.isdigit()==True):
        velos.append([velo_adder.get(),price.get()])
        sheetvelos.set_sheet_data(velos)
        save_array_to_csv(velos,'velos.csv')
        update()
    else:
        print(velos)
        print("В цене есть что-то кроме цифр")

#Метод для получение колонки из CSV файла
def get_column(csv_file, column_index):
    column = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > column_index:
                column.append(row[column_index])
    return column

#Удаление дублирующихся записей из списка велосипедов
def remove_duplicates(csv_file):
    rows = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row not in rows:
                rows.append(row)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

#Отладочный метод для вывода массива velos в консоль
def printvelo():
    print(velo.get())

#Метод для изменения параметров велосипеда
def changevelo():
    print("PLACEHOLDER")

#Удаление велосипеда
def deletevelo():
    with open('velos.csv', 'r') as file:
        reader = csv.reader(file)
        rows_to_keep = [row for row in reader if velo_adder.get() not in row]
        with open('velos.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(rows_to_keep)
    update()

window = Tk()
window.title("Prokat")

#Вкладка проката
tab_control = ttk.Notebook(window)
tab_control.pack(anchor=NW, side=LEFT, fill="both")
prokat = Frame(tab_control)
tab_control.add(prokat, text='Прокат')

#Панель меню вкладки
main_menu = Frame(prokat, borderwidth=2)
main_menu.pack(fill="x", anchor=NW)
add = Button(main_menu, text="Добавить", command=add)
add.pack(side=LEFT)
prt = Button(main_menu, text="Prt", command=return_arr)
prt.pack(side=LEFT)
prtv = Button(main_menu, text="PrtV", command=printvelo)
prtv.pack(side=LEFT)

#Строка имени
name_menu = Frame(prokat, borderwidth=2)
name_menu.pack(fill="x", anchor=NW, ipady=2)
name_label = Label(name_menu, text="Имя:")
name_label.pack(side=LEFT)
name = Entry(name_menu, width=20)
name.pack(side=RIGHT)

#Строка телефона
phone_menu = Frame(prokat, borderwidth=2)
phone_menu.pack(fill="x", anchor=NW, ipady=2)
phone_label = Label(phone_menu, text="Телефон:")
phone_label.pack(side=LEFT)
phone = Entry(phone_menu, width=20)
phone.pack(side=RIGHT)

#Строка велосипеда
velo_stroke = Frame(prokat, borderwidth=2)
velo_stroke.pack(fill="x", anchor=NW, ipady=2)
velo_label = Label(velo_stroke, text="Велосипед:")
velo_label.pack(side=LEFT)
velo = Combobox(velo_stroke, values=get_column('velos.csv', 1), state="readonly")
velo.pack(side=RIGHT)

#Место для таблиц (журнала проката и велосипедов)
sheet_place = Frame(window)
sheet_place.pack(side=LEFT, fill="both", pady=26, ipadx=5)
#Таблица журнала проката
sheet_journal = Frame(sheet_place, borderwidth=2)
sheet_journal.pack(side=LEFT, fill="both")
sheet_journal_name = Label(sheet_journal, text="Журнал проката/продажи", anchor=NW)
sheet_journal_name.pack(side=TOP)
sheet = tksheet.Sheet(sheet_journal)
sheet.pack(side=LEFT, fill="both")
sheet.insert_column()
sheet.insert_row()
sheet.set_sheet_data(stat)

#Вкладка велосипеды
velotab = ttk.Frame(tab_control)
tab_control.add(velotab, text='Велосипеды')

#Панель меню вкладки
velo_menu = Frame(velotab, borderwidth=2)
velo_menu.pack(fill="x", anchor=NW)
addvel = Button(velo_menu, text="Добавить", command=addvelo)
addvel.pack(side=LEFT)
changevel = Button(velo_menu, text="Изменить", command=changevelo)
changevel.pack(side=LEFT)
deletevel = Button(velo_menu, text="Удалить", command=deletevelo)
deletevel.pack(side=LEFT)

#Строка имени велосипеда
velo_adder_stroke = Frame(velotab, borderwidth=2)
velo_adder_stroke.pack(fill="x", anchor=NW, ipady=2)
velo_adder_label = Label(velo_adder_stroke, text="Название велосипеда:")
velo_adder_label.pack(side=LEFT)
velo_adder = Combobox(velo_adder_stroke, values=get_column('velos.csv', 0), width=10)
velo_adder.pack(side=RIGHT)

#Строка тарифа
price_stroke = Frame(velotab, borderwidth=2)
price_stroke.pack(fill="x", anchor=NW, ipady=2)
price_label = Label(price_stroke, text="Тариф:")
price_label.pack(side=LEFT)
price = Entry(price_stroke,width=15)
price.pack(side=RIGHT)

#Таблица велосипедов
sheet_velos_frame = Frame(sheet_place, borderwidth=2)
sheet_velos_frame.pack(side=LEFT, fill="both")
sheet_velos_name = Label(sheet_velos_frame, text="Журнал проката/продажи", anchor=NW)
sheet_velos_name.pack(side=TOP)
sheetvelos = tksheet.Sheet(sheet_velos_frame)
sheetvelos.pack(side=LEFT, fill="both")
sheetvelos.insert_column()
sheetvelos.insert_row()
sheetvelos.set_sheet_data(velos)

clients = ttk.Frame(tab_control)
tab_control.add(clients, text='База клиентов')

tab_control.pack(fill='x')

update()

window.mainloop()
