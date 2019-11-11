# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc
import datetime
import getpass
import webbrowser

from XIO import *
from Auth import *



class Ui_MainWindow(object):

    global hostg,portnumberg,usernameg,passg,serviceg,arrayg,issuetypeg,pass2g,user2g,start
    start = time.time()
    print(datetime.datetime.now())

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(608, 341)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.Hostname = QtWidgets.QLabel(self.centralwidget)
        self.Hostname.setObjectName("Hostname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Hostname)
        self.hostlineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.hostlineedit.setObjectName("hostlineedit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.hostlineedit)
        self.Port = QtWidgets.QLabel(self.centralwidget)
        self.Port.setObjectName("Port")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Port)
        self.portlineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.portlineedit.setObjectName("portlineedit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.portlineedit)
        self.serialnum = QtWidgets.QLabel(self.centralwidget)
        self.serialnum.setObjectName("serialnum")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.serialnum)
        self.Arrayserialnumberlineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.Arrayserialnumberlineedit.setObjectName("Arrayserialnumberlineedit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Arrayserialnumberlineedit)
        self.User = QtWidgets.QLabel(self.centralwidget)
        self.User.setObjectName("User")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.User)
        self.usernamelineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernamelineedit.setObjectName("usernamelineedit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.usernamelineedit)
        self.pwd = QtWidgets.QLabel(self.centralwidget)
        self.pwd.setObjectName("pwd")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.pwd)
        self.passwordlineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordlineedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordlineedit.setObjectName("passwordlineedit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.passwordlineedit)
        self.sr = QtWidgets.QLabel(self.centralwidget)
        self.sr.setObjectName("sr")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.sr)
        self.servicerequestlineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.servicerequestlineedit.setObjectName("servicerequestlineedit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.servicerequestlineedit)
        self.type = QtWidgets.QLabel(self.centralwidget)
        self.type.setObjectName("type")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.type)
        self.issuetypecombobox = QtWidgets.QComboBox(self.centralwidget)
        self.issuetypecombobox.setObjectName("issuetypecombobox")
        self.issuetypecombobox.addItem("")
        self.issuetypecombobox.addItem("")
        self.issuetypecombobox.addItem("")
        self.issuetypecombobox.addItem("")
        self.issuetypecombobox.addItem("")
        self.issuetypecombobox.addItem("")
        self.issuetypecombobox.addItem("")
        self.issuetypecombobox.addItem("")
        self.issuetypecombobox.addItem("")
        self.issuetypecombobox.addItem("")
        self.issuetypecombobox.addItem("")
        self.issuetypecombobox.addItem("")
        self.issuetypecombobox.addItem("")
        self.issuetypecombobox.addItem("")
        self.issuetypecombobox.addItem("")
        self.issuetypecombobox.addItem("")
        self.issuetypecombobox.addItem("")
        self.issuetypecombobox.addItem("")
        self.issuetypecombobox.addItem("")
        self.issuetypecombobox.addItem("")
        self.issuetypecombobox.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.issuetypecombobox)
        self.verticalLayout.addLayout(self.formLayout)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 608, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.onSubmit)

    def onSubmit(self):

        self.hostg = self.hostlineedit.text().strip()
        self.portnumberg = self.portlineedit.text().strip()
        self.usernameg = self.usernamelineedit.text().strip()
        self.passg = self.passwordlineedit.text()
        self.serviceg = self.servicerequestlineedit.text().strip()
        self.arrayg = self.Arrayserialnumberlineedit.text().strip()
        self.issuetypeg = self.issuetypecombobox.currentText()
        ob = GetServerConnection()
        res = ob.getcon(self.hostg, self.portnumberg,self.arrayg,self.usernameg, self.passg)
        print(res)
        if res == 'Failed':
            MainWindow.statusBar().showMessage('Login failed')
        else:
            self.auth()

    def auth(self):
        Dialog = QtWidgets.QDialog()
        uiAuth = Ui_Dialog()
        uiAuth.setupUi(Dialog)
        Dialog.show()
        var = Dialog.exec_()
        if var == QtWidgets.QDialog.Accepted:
            self.user2g = uiAuth.lineEditUserName.text()
            self.pass2g = uiAuth.lineEditPassword.text()
            ob2 = GetServerConnection()
            res, res_html = ob2.runcommands(self.arrayg, self.hostg, self.portnumberg, self.usernameg, self.passg, self.user2g, self.pass2g)
            op_file = "OUTPUT_XIO" + datetime.datetime.now().strftime('%d-%m-%Y-%H-%M-%S') + ".html"
            file = open(op_file, 'w')
            file.write(res_html)
            file.close()
            stop = time.time()
            print('Time taken is', stop - start)
            print(datetime.datetime.now())

            if res == 'Failure':
                MainWindow.statusBar().showMessage('Tech Login Failed')
            else:
                try:
                    conn = pyodbc.connect(DRIVER='{SQL Server}', SERVER='10.26.119.214',
                                          DATABASE='XIO_LOG_DOWNLOADER',
                                          UID='sa', PWD='wipro@123')
                    print(conn)
                    user = getpass.getuser()
                    Service_Request = '1'
                    arrayserialnumber = '123'
                    x = datetime.datetime.today().strftime('%Y-%m-%d')
                    y = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                    stop = time.time()
                    Manual_Effort = 1800
                    Bot_Time_Taken = (stop - start)
                    Effort_Saving = (Manual_Effort - Bot_Time_Taken)
                    print(datetime.datetime.now())
                    print('Time taken to finish is')
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO dbo.XIO_LOG_DOWNLOADER (ADID,SR_No,Array_Serial_Number,Bot_Used_Date,Manual_Efforts_Required,Bot_Time_Taken,Efforts_Saving,Team_Name,Issue_Type,Usage_Create_Date) VALUES (?,?,?,?,?,?,?,'XIO','XIO',?)",
                        (user, Service_Request, arrayserialnumber, x, Manual_Effort, Bot_Time_Taken, Effort_Saving,
                         y))
                    conn.commit()
                    cursor.close()
                    webbrowser.open(op_file)
                except:
                    webbrowser.open(op_file)
                    print('connection has been handled')



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Hostname.setText(_translate("MainWindow", "Hostname"))
        self.Port.setText(_translate("MainWindow", "Port Number"))
        self.serialnum.setText(_translate("MainWindow", "Array Serial Number"))
        self.User.setText(_translate("MainWindow", "Username"))
        self.pwd.setText(_translate("MainWindow", "Password"))
        self.sr.setText(_translate("MainWindow", "Service Request"))
        self.type.setText(_translate("MainWindow", "Issue Type"))
        self.issuetypecombobox.setItemText(0, _translate("MainWindow", "Alerts"))
        self.issuetypecombobox.setItemText(1, _translate("MainWindow", "Array"))
        self.issuetypecombobox.setItemText(2, _translate("MainWindow", "Backup"))
        self.issuetypecombobox.setItemText(3, _translate("MainWindow", "Components"))
        self.issuetypecombobox.setItemText(4, _translate("MainWindow", "Connectivity"))
        self.issuetypecombobox.setItemText(5, _translate("MainWindow", "Contract"))
        self.issuetypecombobox.setItemText(6, _translate("MainWindow", "Disk Fault"))
        self.issuetypecombobox.setItemText(7, _translate("MainWindow", "Enclosure"))
        self.issuetypecombobox.setItemText(8, _translate("MainWindow", "ESRS"))
        self.issuetypecombobox.setItemText(9, _translate("MainWindow", "Host"))
        self.issuetypecombobox.setItemText(10, _translate("MainWindow", "ISCSI-CIFS-NFS-FC"))
        self.issuetypecombobox.setItemText(11, _translate("MainWindow", "NTP"))
        self.issuetypecombobox.setItemText(12, _translate("MainWindow", "Performance"))
        self.issuetypecombobox.setItemText(13, _translate("MainWindow", "Pool"))
        self.issuetypecombobox.setItemText(14, _translate("MainWindow", "Portal"))
        self.issuetypecombobox.setItemText(15, _translate("MainWindow", "Queries"))
        self.issuetypecombobox.setItemText(16, _translate("MainWindow", "Replication"))
        self.issuetypecombobox.setItemText(17, _translate("MainWindow", "Security"))
        self.issuetypecombobox.setItemText(18, _translate("MainWindow", "Storage Processor"))
        self.issuetypecombobox.setItemText(19, _translate("MainWindow", "Unisphere"))
        self.issuetypecombobox.setItemText(20, _translate("MainWindow", "Upgrade-Code"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())