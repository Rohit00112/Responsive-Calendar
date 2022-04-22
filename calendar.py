
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QDate


class Calendar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calendar')
        self.setGeometry(300, 300, 300, 300)
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.clicked[QDate].connect(self.showDate)
        self.label = QLabel(self)
        date = self.calendar.selectedDate()
        self.label.setText(date.toString())
        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def showDate(self, date):
        self.label.setText(date.toString())

if __name__ == '__main__':
    app = QApplication([])
    cal = Calendar()
    cal.show()
    app.exec_()