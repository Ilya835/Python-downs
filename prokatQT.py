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
# Массив тарифов
tarifs = []


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
            read_array_from_csv('velos.csv', velos)
            self.velosi = MatrixTableModel(velos)
            self.stati = MatrixTableModel(stat)
            self.ui.prokat_table.setModel(self.stati)
            self.ui.velo_table.setModel(self.velosi)
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

        def addvelo():
            update()
            velos.append([self.ui.velo_name.text(),
                          self.ui.velo_count.value(),
                          self.ui.velo_tarif.currentText()])
            save_array_to_csv(velos, 'velos.csv')
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

        def select_velo():
            indexes = self.ui.velo_table.selectionModel().selectedRows()
            for index in sorted(indexes):
                row = index.row()
                print(velos[row][1])
                self.ui.velo_name.setText(velos[row][0])
                self.ui.velo_count.setValue(int(velos[row][1]))
                self.ui.velo_tarif.setCurrentText(velos[row][2])

        def find_rows_with_data():
            rows_with_data = 0
            for row_index, row in enumerate(velos):
                if any(cell_data == self.ui.velo_name.text() for cell_data in row):
                    rows_with_data = (row_index)
            return rows_with_data

        def change_velo():
            row = (find_rows_with_data())
            velos[row][0] = self.ui.velo_name.text()
            velos[row][1] = self.ui.velo_count.value()
            velos[row][2] = self.ui.velo_tarif.currentText()
            print(velos)
            save_array_to_csv(velos, 'velos.csv')

        def delete_velosi():
            row = (find_rows_with_data())
            velos.pop(row)

        # Добавляем реакцию на сигналы от кнопок
        self.ui.add_prokat.clicked.connect(add)
        self.ui.clear_prokat.clicked.connect(clear_lines)
        self.ui.add_velo.clicked.connect(addvelo)
        self.ui.velo_table.clicked.connect(select_velo)
        self.ui.edit_velo.clicked.connect(change_velo)
        self.ui.delete_velo.clicked.connect(delete_velosi)
        update()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
