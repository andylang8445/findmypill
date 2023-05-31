import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget,
    QTableWidgetItem, QDockWidget, QFormLayout,
    QLineEdit, QWidget, QPushButton, QSpinBox,
    QMessageBox, QToolBar, QMessageBox, QComboBox
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QAction


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Employees')
        self.setWindowIcon(QIcon('./assets/usergroup.png'))
        self.setGeometry(100, 100, 700, 400)

        employees = [
            {'Ingredient Name': 'John', 'Amount': 25, 'Unit': 'mg'},
            {'Ingredient Name': 'Jane', 'Amount': 22, 'Unit': 'kg'},
            {'Ingredient Name': 'Alice', 'Amount': 22, 'Unit': 'ng'},
        ]

        self.table = QTableWidget(self)
        self.setCentralWidget(self.table)

        self.table.setColumnCount(3)
        self.table.setColumnWidth(0, 300)
        self.table.setColumnWidth(1, 75)
        self.table.setColumnWidth(2, 50)

        self.table.setHorizontalHeaderLabels(employees[0].keys())
        self.table.setRowCount(len(employees))

        row = 0
        for e in employees:
            self.table.setItem(row, 0, QTableWidgetItem(e['Ingredient Name']))
            self.table.setItem(row, 1, QTableWidgetItem(str(e['Amount'])))
            self.table.setItem(row, 2, QTableWidgetItem(str(e['Unit'])))
            row += 1

        dock = QDockWidget('New Employee')
        dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)

        # create form
        form = QWidget()
        layout = QFormLayout(form)
        form.setLayout(layout)

        self.ingredient_name = QLineEdit(form)
        self.amount = QLineEdit(form)
        self.unit_list = ['mg', 'g', 'ng', 'ml']
        self.unit = QComboBox(form)
        self.unit.addItems(self.unit_list)
        self.amount.clear()

        layout.addRow('Ingredient Name:', self.ingredient_name)
        layout.addRow('Amount:', self.amount)
        layout.addRow('Unit:', self.unit)

        btn_add = QPushButton('Add')
        btn_add.clicked.connect(self.add_employee)
        layout.addRow(btn_add)

        btn_remove = QPushButton('Delete Selected Row')
        btn_remove.clicked.connect(self.delete)
        layout.addRow(btn_remove)
        dock.setWidget(form)

    def delete(self):
        current_row = self.table.currentRow()
        if current_row < 0:
            return QMessageBox.warning(self, 'Warning', 'Please select a record to delete')

        button = QMessageBox.question(
            self,
            'Confirmation',
            'Are you sure that you want to delete the selected row?',
            QMessageBox.StandardButton.No |
            QMessageBox.StandardButton.Yes
        )
        if button == QMessageBox.StandardButton.Yes:
            self.table.removeRow(current_row)

    def valid(self):
        ingredient_name = self.ingredient_name.text().strip()

        if not ingredient_name:
            QMessageBox.critical(self, 'Error', 'Please enter the ingredient name')
            self.ingredient_name.setFocus()
            return False

        try:
            amount = float(self.amount.text().strip())
        except ValueError:
            QMessageBox.critical(self, 'Error', 'Please enter a valid age')
            self.amount.setFocus()
            return False

        if amount <= 0:
            QMessageBox.critical(
                self, 'Error', 'The valid amount is larger than 0')
            return False

        return True

    def reset(self):
        self.ingredient_name.clear()
        self.amount.clear()
        self.unit.setCurrentIndex(0)

    def add_employee(self):
        if not self.valid():
            return

        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(
            self.ingredient_name.text().strip())
                           )
        self.table.setItem(
            row, 1, QTableWidgetItem(self.amount.text())
        )
        self.table.setItem(
            row, 2, QTableWidgetItem(self.unit.currentText())
        )

        self.reset()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())