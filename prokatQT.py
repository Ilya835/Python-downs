from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QAbstractTableModel
from form import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import csv
from datetime import datetime
import os

def get_current_date():
    current_date = datetime.now().strftime('%Y-%m-%d')
    print(current_date)
    return current_date

# Массив отвечающий за журнал проката
stat = []
# Массив отвечающий за велосипеды
velos = []
# Массив отвечающий за базу данных клиентов
client = []
# Дата
date = get_current_date()

class MatrixTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        self._rows = len(data)
        self._columns = len(data[0]) if self._rows > 0 else 0

    def rowCount(self, parent):
        return self._rows

    def columnCount(self, parent):
        return self._columns

    def data(self, index, role):
        if not index.isValid():
            return None
        if role != Qt.DisplayRole:
            return None
        return self._data[index.row()][index.column()]

    def setData(self, index, value, role):
        if role != Qt.EditRole:
            return False
        self._data[index.row()][index.column()] = value
        self.dataChanged.emit(index, index)
        return True

# Общий класс приложения
class mywindow(QtWidgets.QMainWindow):
    # Вывод отладочных значений журнала проката в консоль
    def return_arr():
        print(stat)

    def __init__(self):
        # Сохранение значений массива в файл CSV
        def save_array_to_csv(array, filename):
            with open(filename, 'w', newline='\n') as file:
                writer = csv.writer(file)
                writer.writerows(array)

        # Чтение значений для массивов из файлов
        def read_array_from_csv(filename, arrayname):
            if not os.path.exists(filename):
                with open(filename, 'w') as file:
                    pass

            else:
                with open(filename, 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        arrayname.append(row)

        # Обновление значений из файлов
        def update():
            # Очистка массивов для велосипедов и журала проката
            velos.clear()
            stat.clear()
            # Считывание данных из файлов и запись их в массивы
            read_array_from_csv('stat_' + date + '.csv', stat)
            read_array_from_csv('velos_' + date + '.csv', velos)
            self.velosi = MatrixTableModel(velos)
            self.stati = MatrixTableModel(stat)
            self.ui.tableView.setModel(self.stati)
            # Отладочный вывод значений массивов в консоль
            print(stat)
            print(velos)

        # Метод добавления новых записей в журнал
        def add():
            update()
            stat.append([self.ui.name_prokat.text(),
                         self.ui.phone_number_prokat.text(),
                         self.ui.velo_prokat.currentText(),

                         ])
            print(stat)
            save_array_to_csv(stat, 'stat_' + date + '.csv')
            update()

        # Очищение полей ввода
        def clear_lines():
            self.ui.name_prokat.setText('')
            self.ui.passport_prokat.setText('')
            self.ui.phone_number_prokat.setText('')
            self.ui.velo_prokat.setCurrentText('')
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Добавляем реакцию на сигналы от кнопок
        self.ui.add_prokat.clicked.connect(add)
        self.ui.clear_prokat.clicked.connect(clear_lines)
        update()

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
