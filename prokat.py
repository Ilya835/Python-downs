import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import tksheet
import csv

stat = []
velos = []
client = []

def save_array_to_csv(array, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(array)

def read_array_from_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            stat.append(row)

def read_array_from_csv2(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            velos.append(row)

def return_arr():
    print(stat)

def update():
    read_array_from_csv('stat.csv')
    sheet.set_sheet_data(stat)
    read_array_from_csv2('velos.csv')
    sheetvelos.set_sheet_data(velos)
    print(stat)
    print(velos)

def add():
    stat.append([name.get(),phone.get(),velo.get()])
    sheet.set_sheet_data(stat)
    print(stat)
    save_array_to_csv(stat,'stat.csv')

def addvelo():
    velos.append([velo.get(),price.get()])
    sheetvelos.set_sheet_data(velos)
    print(velos)
    save_array_to_csv(velos,'velos.csv')

def get_column(csv_file, column_index):
    column = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > column_index:
                column.append(row[column_index])
    return column

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

window = Tk()
window.title("Prokat")

tab_control = ttk.Notebook(window)

prokat = ttk.Frame(tab_control)
tab_control.add(prokat, text='Прокат')

menu = Frame(prokat)
menu.pack(fill = 'x')
add = Button(menu, text="Add", command=add)
add.pack(anchor='nw')
prt = Button(menu, text="Prt", command=return_arr)
prt.pack()

name = Entry(prokat,width=10)
name.pack()

phone = Entry(prokat,width=10)
phone.pack()

velo = ttk.Combobox(prokat, values=get_column('velos.csv', 1))
velo.pack()

sheet = tksheet.Sheet(prokat)
sheet.pack()
sheet.insert_column()
sheet.insert_row()
sheet.set_sheet_data(stat)

velotab = ttk.Frame(tab_control)
tab_control.add(velotab, text='Велосипеды')

addvel = Button(velotab, text="Add", command=addvelo)
addvel.pack()

price = Entry(velotab,width=15)
price.pack()

velo = Entry(velotab,width=15)
velo.pack()

sheetvelos = tksheet.Sheet(velotab)
sheetvelos.pack()
sheetvelos.insert_column()
sheetvelos.insert_row()
sheetvelos.set_sheet_data(velos)

remove_duplicates('velos.csv')

clients = ttk.Frame(tab_control)
tab_control.add(clients, text='База клиентов')

tab_control.pack(fill='x')

update()

window.mainloop()
