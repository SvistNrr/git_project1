import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLCDNumber, QLabel, QInputDialog,
                             QTableWidgetItem)
from ПРОЕКТ import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.gorohostrel_desc = ['Горохострелы – это ваша первая линия обороны. Они стреляют в атакующих зомби',
                                 'Урон: средний', 'Цена: 100', 'Зарядка быстрая']
        self.podsolnuh_desc = ['Подсолнух - очень важен, он производит для вас дополнительное солнце.Выращивайте их как можно больше!',
                               'Производство солнца: Нормальное', 'Цена: 50', 'Зарядка: Быстрая']
        self.cherries_desc = ['Вишнёвые бомбы - могут взорвать всех зомби вокруг себя. Они быстро срабатывают, так что сажайте их рядом с зомби.',
                              'Урон: средний', 'Цена: 100', 'Зарядка быстрая']
        self.nut_desc = ['СтенаОрех - имеет прочную оболочку, которую вы сможете использовать для защиты ваших растений.',
                         'Производство солнца: Нормальное', 'Цена: 50', 'Зарядка: Быстрая']
        self.chavv_desc = ['Жевуны - могут проглотить зомби целиком, но они уязвимы, когда жуют.',
                           'Урон: средний', 'Цена: 100', 'Зарядка быстрая']
        self.frost_desc = ['Морозный Горох - стреляет замороженными горошинами, которые повреждают и замедляют зомби.',
                           'Производство солнца: Нормальное', 'Цена: 50', 'Зарядка: Быстрая']
        self.gypno_desc = ['Гипногриб - когда его съедают, обращает зомби на Вашу сторону',
                           'Урон: средний', 'Цена: 100', 'Зарядка быстрая']
        self.frost_2_desc = ['Ледогриб временно останавливает всех зомби на экране.',
                            'Производство солнца: Нормальное', 'Цена: 50', 'Зарядка: Быстрая']
        self.cabbage_desc = ['Кабачок - поражает первого зомби, который подойдёт к нему',
                           'Производство солнца: Нормальное', 'Цена: 50', 'Зарядка: Быстрая']
        self.spikes_desc = ['Гипногриб - когда его съедают, обращает зомби на Вашу сторону',
                           'Урон: средний', 'Цена: 100', 'Зарядка быстрая']
        self.high_nut_desc = ['Высокие Орехи - это укреплённые стены, которые нельзя перепрыгнуть.',
                              'Производство солнца: Нормальное', 'Цена: 50', 'Зарядка: Быстрая']
        self.hero_1.clicked.connect(self.information_func_1)
        self.hero_2.clicked.connect(self.information_func_2)
        self.hero_3.clicked.connect(self.information_func_3)
        self.hero_4.clicked.connect(self.information_func_4)
        self.hero_5.clicked.connect(self.information_func_5)
        self.hero_6.clicked.connect(self.information_func_6)
        self.hero_7.clicked.connect(self.information_func_7)
        self.hero_8.clicked.connect(self.information_func_8)
        self.hero_9.clicked.connect(self.information_func_9)
        self.hero_10.clicked.connect(self.information_func_10)
        self.hero_11.clicked.connect(self.information_func_11)


    def information_func_1(self):
        self.image_connect.setPixmap(QtGui.QPixmap('Горохострел1.png'))
        self.lineEdit.setText(self.gorohostrel_desc[0])

    def information_func_2(self):
        self.image_connect.setPixmap(QtGui.QPixmap('Патсолнух.png'))
        self.lineEdit.setText(self.podsolnuh_desc[0])

    def information_func_3(self):
        self.image_connect.setPixmap(QtGui.QPixmap('Вишнёвые бомбы.png'))
        self.lineEdit.setText(self.cherries_desc[0])

    def information_func_4(self):
        self.image_connect.setPixmap(QtGui.QPixmap('СтенаОрех.png'))
        self.lineEdit.setText(self.nut_desc[0])

    def information_func_5(self):
        self.image_connect.setPixmap(QtGui.QPixmap('Морозный Горох.png'))
        self.lineEdit.setText(self.frost_desc[0])

    def information_func_6(self):
        self.image_connect.setPixmap(QtGui.QPixmap('Жевун.png'))
        self.lineEdit.setText(self.chavv_desc[0])

    def information_func_7(self):
        self.image_connect.setPixmap(QtGui.QPixmap('Гипногриб.png'))
        self.lineEdit.setText(self.gypno_desc[0])

    def information_func_8(self):
        self.image_connect.setPixmap(QtGui.QPixmap('Ледогриб.png'))
        self.lineEdit.setText(self.frost_2_desc[0])

    def information_func_9(self):
        self.image_connect.setPixmap(QtGui.QPixmap('Кабачок.png'))
        self.lineEdit.setText(self.cabbage_desc[0])

    def information_func_10(self):
        self.image_connect.setPixmap(QtGui.QPixmap('Колючки.jpg'))
        self.lineEdit.setText(self.spikes_desc[0])

    def information_func_11(self):
        self.image_connect.setPixmap(QtGui.QPixmap('Высокие Орехи.jpg'))
        self.lineEdit.setText(self.high_nut_desc[0])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())





