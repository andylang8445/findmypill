from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import register as reg
import sys


class DataProcessor:
    def upload(data: dict()):
        print(data)
        new_pill_dict = data.copy()
        ing_dict = dict()
        for item in data['ingredient_list']:
            ing_dict[item[0]] = item[1:]
        new_pill_dict['ingredient'] = ing_dict

        print("result: ", reg.add_new_pill(new_pill_dict))
        return True


class AdminPanel(QWidget):
    def __init__(self):
        super().__init__()
        container_all_v = QVBoxLayout()

        self.setGeometry(100, 100, 1000, 400)

        h1 = QHBoxLayout()
        label1 = QLabel(self)
        label1.setText("Pill Name")
        self.input_box1 = QLineEdit(self)
        h1.addWidget(label1)
        h1.addWidget(self.input_box1)

        h2 = QHBoxLayout()
        label2 = QLabel(self)
        label2.setText("Company Name")
        self.input_box2 = QLineEdit(self)
        h2.addWidget(label2)
        h2.addWidget(self.input_box2)

        h3 = QHBoxLayout()
        label3 = QLabel(self)
        label3.setText("Select Pill Type")
        pill_type_options = ['Tablet', 'Suspension', 'Capsule', 'Liquid', 'Cream', 'Patch']
        self.combobox3 = QComboBox(self)
        self.combobox3.addItems(pill_type_options)
        h3.addWidget(label3)
        h3.addWidget(self.combobox3)

        h4 = QHBoxLayout()
        label4 = QLabel(self)
        label4.setText("Select Consumption Method")
        # Referenced https://www.ncbi.nlm.nih.gov/books/NBK568677/ for information
        pill_consumption_method = ['Oral', 'Sublingual and Buccal Routes', 'Rectal Route', 'Intranasal Route',
                                   'Inhalational Route', 'Vaginal Route', 'Transdermal Route']
        self.combobox4 = QComboBox(self)
        self.combobox4.addItems(pill_consumption_method)
        h4.addWidget(label4)
        h4.addWidget(self.combobox4)

        h5 = QHBoxLayout()
        label5 = QLabel(self)
        label5.setText("DIN Code")
        self.input_box5 = QLineEdit(self)
        int_validator = QIntValidator()
        int_validator.setRange(0, 99999999)
        self.input_box5.setValidator(int_validator)
        h5.addWidget(label5)
        h5.addWidget(self.input_box5)

        h6 = QHBoxLayout()
        self.table = QTableWidget(self)

        self.table.setColumnCount(3)
        self.table.setColumnWidth(0, 350)
        self.table.setColumnWidth(1, 75)
        self.table.setColumnWidth(2, 50)
        self.table_labels = ['Ingredient Name', 'Amount', 'Unit']
        self.table.setHorizontalHeaderLabels(self.table_labels)
        dock = QDockWidget('New Employee')
        dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        form = QWidget()
        layout = QFormLayout(form)
        form.setLayout(layout)

        self.ingredient_name = QLineEdit(form)
        self.ingredient_name.setMinimumWidth(300)
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
        h6.addWidget(self.table, 60)
        h6.addWidget(dock, 40)

        h99 = QHBoxLayout()
        ok_button = QPushButton('Add To DB')
        ok_button.clicked.connect(self.submit)
        cancel_button = QPushButton('Cancel')
        cancel_button.clicked.connect(self.close)
        h99.addWidget(ok_button)
        h99.addWidget(cancel_button)

        container_all_v.addLayout(h1)
        container_all_v.addLayout(h2)
        container_all_v.addLayout(h3)
        container_all_v.addLayout(h4)
        container_all_v.addLayout(h5)
        container_all_v.addLayout(h6)
        container_all_v.addLayout(h99)
        self.setLayout(container_all_v)
        self.setWindowTitle('FMP Admin Panel')

    def submit(self):
        data_dict = dict()
        if len(self.input_box1.text().strip()) == 0:
            QMessageBox.critical(self, 'Error', 'Please enter the pill name')
            self.input_box1.setFocus()
            return False

        if len(self.input_box2.text().strip()) == 0:
            QMessageBox.critical(self, 'Error', 'Please enter the company name')
            self.input_box2.setFocus()
            return False

        try:
            din = int(self.input_box5.text().strip())
        except ValueError:
            QMessageBox.critical(self, 'Error', 'Please enter a valid DIN Code')
            self.input_box5.setFocus()
            return False

        if din <= 0:
            QMessageBox.critical(
                self, 'Error', 'The valid DIN is larger than 0')
            return False

        data_dict['name'] = self.input_box1.text()
        data_dict['company'] = self.input_box2.text()
        data_dict['type_info'] = self.combobox3.currentText()
        data_dict['consume_info'] = self.combobox4.currentText()
        ing_li = list()
        for row in range(self.table.rowCount()):
            sub_li = list()
            for col in range(len(self.table_labels)):
                it = self.table.item(row, col)
                text = it.text() if it is not None else ""
                sub_li.append(text)
            ing_li.append(sub_li)
        data_dict['ingredient_list'] = ing_li
        data_dict['din_code'] = self.input_box5.text()
        result_val = DataProcessor.upload(data_dict)
        if result_val:
            QMessageBox.warning(self, 'Success', 'All Data have been added to DB')
            self.ingredient_name.clear()
            self.amount.clear()
            self.unit.setCurrentIndex(0)
            for row in range(self.table.rowCount()):
                self.table.removeRow(row)
            self.input_box1.clear()
            self.input_box2.clear()
            self.input_box5.clear()
            self.combobox3.setCurrentIndex(0)
            self.combobox4.setCurrentIndex(0)
            return True
        return False




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
            QMessageBox.critical(self, 'Error', 'Please enter a valid amount')
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
    ex = AdminPanel()
    ex.show()
    sys.exit(app.exec())
