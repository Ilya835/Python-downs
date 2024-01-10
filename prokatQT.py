from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QAbstractTableModel
from form import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import csv
from datetime import datetime
# Массив отвечающий за журнал проката
stat = []
# Массив отвечающий за велосипеды
velos = []
# Массив отвечающий за базу данных клиентов
client = []

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
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(array)

        # Чтение значение журнала проката из файла stat.csv
        def read_array_from_csv(filename):
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    stat.append(row)

        # Чтение значение таблицы велосипедов из файла velos.csv
        def read_array_from_csv2(filename):
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    velos.append(row)

        # Обновление значений из файлов
        def update():
            # Очистка массивов для велосипедов и журала проката
            velos.clear()
            stat.clear()
            # Считывание данных из файлов и запись их в массивы
            read_array_from_csv('stat.csv')
            read_array_from_csv2('velos.csv')
            self.velosi = MatrixTableModel(velos)
            self.stati = MatrixTableModel(stat)
            self.ui.tableView.setModel(self.stati)
            # Отладочный вывод значений массивов в консоль
            print(stat)
            print(velos)

        # Метод добавления новых записей в журнал
        def add():
            now = datetime.datetime.now()
            update()
            stat.append([self.ui.name_prokat.text(),
                         self.ui.phone_number_prokat.text(),
                         self.ui.velo_prokat.currentText(),
                         datetime.strptime(now.time(), "%H:%M:%S")
                         ])
            print(stat)
            save_array_to_csv(stat, 'stat.csv')
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
