from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
import sys


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self, parent=None)
        self.ui = uic.loadUi('main_window.ui', self)
        '''
        self.tab = self.findChild(QtWidgets.QTabWidget, "tabWidget")
        self.tab1 = self.findChild(QtWidgets.QWidget, 'tab_chamber')
        self.but1 = self.findChild(QtWidgets.QPushButton, 'high_chamber_run')
        '''
        
        # signal > slot connection parts
        self.but1.clicked.connect(self.high_chamber_run)
        
        
        self.ui.show()


    @pyqtSlot()
    def high_chamber_run(self):
        print('Hello worlds')

    @pyqtSlot()
    def high_chamber_stop(self):
        print('Hello worlds')

    @pyqtSlot()
    def room_chamber_run(self):
        print('Hello worlds')

    @pyqtSlot()
    def room_chamber_stop(self):
        print('Hello worlds')

    @pyqtSlot()
    def buzzer_stop(self):
        print('Hello worlds')

    @pyqtSlot()
    def set_mode(self):
        print('Hello worlds')

    @pyqtSlot()
    def slot1(self):
        print('Hello worlds')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Main()
    sys.exit(app.exec())
