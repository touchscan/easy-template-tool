#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui,  QtWidgets, uic

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('interface.ui', self)
        self.tmp = ''
        self.cb = [self.checkBox,
                   self.checkBox_2,
                   self.checkBox_3,
                   self.checkBox_4,
                   self.checkBox_5,
                   self.checkBox_6,
                   self.checkBox_7]
        self.rb = [self.radioButton,
                   self.radioButton_2,
                   self.radioButton_3,
                   self.radioButton_4,
                   self.radioButton_5,
                   self.radioButton_6]
        self.names = {'down': ' пропала связь с:\n',
                      'ups': ' работает от батарей:\n',
                      'dups': ' пропала связь с:\n\nТакже от батарей работает:\n',
                      'fups': ' без перехода на ИБП пропала связь с:\n',
                      'zam': 'Замена оборудования: \nРаботает: \nСроки: 30 минут\n',
                      'sig': 'Модернизация сети: \nРаботает: \nСроки: 30 минут\n',
                      'dtek': '\nДТЕК: отключений нет',
                      'pred': '\nПредседатель: ',
                      'suv': '\nУК \"Суворовский\": ',
                      'abon': '\nАбонент: ',
                      'per': '\nПередано: ',
                      'news': '\nНовость добавлена.',
                      'sms': '\nОтправлены sms.'}
        self.radioButton.toggled.connect(self.work)
        self.radioButton_2.toggled.connect(self.work)
        self.radioButton_3.toggled.connect(self.work)
        self.radioButton_4.toggled.connect(self.work)
        self.radioButton_5.toggled.connect(self.work)
        self.radioButton_6.toggled.connect(self.work)
        self.radioButton_7.setHidden(True)
        self.checkBox.toggled.connect(self.check)
        self.checkBox_2.toggled.connect(self.check)
        self.checkBox_3.toggled.connect(self.check)
        self.checkBox_4.toggled.connect(self.check)
        self.checkBox_5.toggled.connect(self.check)
        self.checkBox_6.toggled.connect(self.check)
        self.checkBox_7.toggled.connect(self.check)
        self.pushButton_2.toggled.connect(self.mode)
        self.pushButton_3.clicked.connect(self.copy)
        self.show()
        
    def mode(self):
        if self.pushButton_2.isChecked():
            Window.setStyleSheet(self, 'background-color: rgb(175, 175, 175);')
        elif not self.pushButton_2.isChecked():
            Window.setStyleSheet(self, 'background-color: rgb(f0, f0, f0);')

    def work(self):
        for i in range (len(self.rb)):
            if self.rb[i].isChecked():
                if self.rb[i].accessibleName() == 'zam' or self.rb[i].accessibleName() == 'sig':
                    for x in range (len(self.cb) - 2):
                        self.cb[x].setChecked(False)
                        self.cb[x].setEnabled(False)
                elif self.rb[i].accessibleName() != 'zam'or self.rb[i].accessibleName() != 'sig':
                    for x in range (len(self.cb) - 2):
                        self.cb[x].setChecked(False)
                        self.cb[x].setEnabled(True)
                self.plainTextEdit.setPlainText(self.names.get(self.rb[i].accessibleName()))
    
    def check(self):       
        for j in range (len(self.cb)):
            self.tmp = self.plainTextEdit.toPlainText()
            if self.cb[j].isChecked():
                if self.names.get(self.cb[j].accessibleName()) not in self.plainTextEdit.toPlainText():
                    self.tmp = self.plainTextEdit.toPlainText()
                    self.tmp += self.names.get(self.cb[j].accessibleName())
                    self.plainTextEdit.setPlainText(self.tmp)
            elif not self.cb[j].isChecked():
                if self.names.get(self.cb[j].accessibleName()) in self.plainTextEdit.toPlainText():
                    if self.cb[j].accessibleName() == 'dtek' or self.cb[j].accessibleName() == 'news' or self.cb[j].accessibleName() == 'sms':
                        self.tmp = self.tmp.replace(self.names.get(self.cb[j].accessibleName()), '')
                        self.plainTextEdit.setPlainText(self.tmp)
                        break
                    self.tmp = self.tmp.replace(self.names.get(self.cb[j].accessibleName()), '#')
                    self.a = self.tmp.find('#')
                    self.b = self.tmp.find('\n', self.a)
                    self.tmp = self.tmp.replace(self.tmp[self.a:self.b], '')
                    self.tmp = self.tmp.replace('#', '')
                    if self.b == -1 and len(self.tmp) > 0:
                        self.tmp = self.tmp.replace(self.tmp[self.b], '')
                    self.plainTextEdit.setPlainText(self.tmp)
                    print(self.tmp)                    
       
    def copy(self):
        self.plainTextEdit.selectAll()
        self.plainTextEdit.copy()
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    instance = Window()
    instance.show()
    sys.exit(app.exec_())
