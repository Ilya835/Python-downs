from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex
from form import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys

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

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        velos = [[1,2,3,4],[4,3,2,1]]
        self.model = MatrixTableModel(velos)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableView.setModel(self.model)

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
